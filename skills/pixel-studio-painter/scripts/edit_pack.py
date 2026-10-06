"""The edit loop with any AI: 🧩 copies ONE package (instructions + what the picture contains + an edit program);
the user asks the AI for a change ("make the shirt red"), pastes the program the AI returns, and the studio draws
the edited picture.

The edit program is small: the original image is NOT inside it (only a reference key), so an AI can read and
change it. It edits with named tools (recolor, adjust, tint, paint, write, erase) between two markers; everything
else stays. When it comes back, the studio puts the original's bytes back in place of the key and runs it.
"""
from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
ORIGINALS = HERE / "code" / "originals"
KEY = "<<KOSIF:ORIGINAL:{sha}>>"

TOOLS = '''
# ── أدوات التعديل (Pillow فقط). كلها تعمل على img في مكانه. region = (x0, y0, x1, y1) بالبيكسل أو None للصورة كلها ──
def _box(region, size):
    if region is None:
        return (0, 0, size[0], size[1])
    x0, y0, x1, y1 = region
    return (max(0, int(x0)), max(0, int(y0)), min(size[0], int(x1)), min(size[1], int(y1)))


def _hsv(hexcolor):
    return Image.new("RGB", (1, 1), hexcolor).convert("HSV").getpixel((0, 0))


def color_mask(img, hexcolor, tolerance=40, region=None, soft=1.5):
    """Where the picture is close to a colour (average channel distance <= tolerance), inside region."""
    rgb = img.convert("RGB")
    diff = ImageChops.difference(rgb, Image.new("RGB", rgb.size, hexcolor))
    r, g, b = diff.split()
    avg = ImageChops.add(ImageChops.add(r, g, scale=2.0), b, scale=1.5)
    mask = avg.point(lambda v: 255 if v <= tolerance else 0)
    if region is not None:
        keep = Image.new("L", rgb.size, 0)
        keep.paste(255, _box(region, rgb.size))
        mask = ImageChops.multiply(mask, keep)
    return mask.filter(ImageFilter.GaussianBlur(soft)) if soft else mask


def recolor(img, src_hex, dst_hex, tolerance=40, region=None, keep_shading=True):
    """Change one colour into another. Pixels that are exactly src_hex become exactly dst_hex; darker and lighter
    pixels of it (folds, shadows, highlights) keep their relative shading when keep_shading is True, or become
    flat when it is False. Example: recolor(img, "#8a8a8a", "#c0392b", 42, (380, 420, 620, 760))  # the shirt"""
    mask = color_mask(img, src_hex, tolerance, region)
    h, s, v = img.convert("RGB").convert("HSV").split()
    sh, ss, sv = _hsv(src_hex)
    dh, ds, dv = _hsv(dst_hex)
    nh = Image.new("L", img.size, dh)
    ns = s.point(lambda x: max(0, min(255, int(x * ds / max(ss, 8) + .5) if ss > 8 else ds)))
    nv = v.point(lambda x: max(0, min(255, int(x * dv / max(sv, 1) + .5)))) if keep_shading else Image.new("L", img.size, dv)
    out = Image.merge("HSV", (nh, ns, nv)).convert("RGB")
    img.paste(out, (0, 0), mask)


def adjust(img, region=None, brightness=1.0, contrast=1.0, saturation=1.0, sharpness=1.0):
    """Brightness / contrast / saturation / sharpness of a region (1.0 = unchanged)."""
    box = _box(region, img.size)
    part = img.crop(box).convert("RGB")
    for cls, k in ((ImageEnhance.Brightness, brightness), (ImageEnhance.Contrast, contrast),
                   (ImageEnhance.Color, saturation), (ImageEnhance.Sharpness, sharpness)):
        if k != 1.0:
            part = cls(part).enhance(k)
    img.paste(part, box)


def tint(img, hexcolor, amount=0.3, region=None):
    """Wash a region with a colour (amount 0..1)."""
    box = _box(region, img.size)
    part = img.crop(box).convert("RGB")
    img.paste(Image.blend(part, Image.new("RGB", part.size, hexcolor), amount), box)


def paint(img, points, hexcolor, outline=None, width=1):
    """Draw a filled polygon: points = [(x, y), ...] in pixels."""
    ImageDraw.Draw(img).polygon(points, fill=hexcolor, outline=outline, width=width)


def write(img, text, xy, size=32, hexcolor="#ffffff", font_file=None):
    """Write text at xy (top-left). Latin text only renders reliably with the default font; give font_file for
    others."""
    try:
        font = ImageFont.truetype(font_file or "arial.ttf", size)
    except OSError:
        font = ImageFont.load_default(size)
    ImageDraw.Draw(img).text(xy, text, fill=hexcolor, font=font)


def erase(img, region, softness=14):
    """Remove something small: the region is filled with its blurred surroundings."""
    x0, y0, x1, y1 = _box(region, img.size)
    pad = softness * 3
    big = (max(0, x0 - pad), max(0, y0 - pad), min(img.size[0], x1 + pad), min(img.size[1], y1 + pad))
    patch = img.crop(big).convert("RGB").filter(ImageFilter.GaussianBlur(softness))
    mask = Image.new("L", patch.size, 0)
    ImageDraw.Draw(mask).rectangle([x0 - big[0], y0 - big[1], x1 - big[0], y1 - big[1]], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(softness / 2))
    img.paste(patch, big, mask)


def flip(img, horizontal=True):
    """Mirror the whole picture."""
    src = img.transpose(Image.FLIP_LEFT_RIGHT if horizontal else Image.FLIP_TOP_BOTTOM)
    img.paste(src, (0, 0))
'''

PROGRAM = '''# -*- coding: utf-8 -*-
"""KOSIF Studio edit program (Pillow only).

Picture: {title} ({w}x{h}). The original image is restored by the studio from the key below.
Edit ONLY between the markers "# EDITS START" and "# EDITS END". Keep everything else, including the IMAGE_B64 line.
"""
import base64
import io

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont

TITLE = {title!r}
SIZE = ({w}, {h})
IMAGE_B64 = "{key}"
{tools}

def load_original():
    if IMAGE_B64.startswith("<<KOSIF:ORIGINAL:"):
        raise SystemExit("open this program in KOSIF Studio: it puts the original image back in place of the key")
    im = Image.open(io.BytesIO(base64.b64decode("".join(IMAGE_B64.split()))))
    im.load()
    return im.convert("RGB")


img = load_original()
draw = ImageDraw.Draw(img)       # in the studio the picture appears first, then the edits are painted over it

# EDITS START
# مثال (احذفه وضع تعديلاتك):
# recolor(img, "#8a8a8a", "#c0392b", tolerance=42, region=(380, 420, 620, 760))   # change the shirt from grey to red
# EDITS END

if __name__ == "__main__":
    img.save(TITLE + "_edited.png")
    print(TITLE + "_edited.png", SIZE)
'''

INSTRUCTIONS = '''أنت تساعد في تعديل صورة داخل برنامج KOSIF Studio. تحتك: (1) وصف لما تحتويه الصورة بالألوان والمواضع،
(2) برنامج بايثون صغير يحمّل الصورة الأصلية ويطبّق تعديلات عليها بأدوات جاهزة.

المطلوب منك: نفّذ طلب المستخدم بكتابة التعديلات بين السطرين "# EDITS START" و"# EDITS END" فقط، ثم أعد
**البرنامج كاملاً** كما هو (لا تغيّر سطر IMAGE_B64 ولا الأدوات ولا الاستيرادات). لا شرح خارج الكود.

الأدوات: recolor(img, "#src", "#dst", tolerance, region, keep_shading=True) يغيّر لوناً مع الحفاظ على الظلال؛
adjust(img, region, brightness, contrast, saturation, sharpness)؛ tint(img, "#hex", amount, region)؛
paint(img, [(x,y),...], "#hex")؛ write(img, "text", (x,y), size, "#hex")؛ erase(img, region)؛ flip(img)؛
وللرسم الحر draw (ImageDraw جاهز): draw.rectangle / ellipse / polygon / line / text.
region = (x0, y0, x1, y1) بالبيكسل. الإحداثيات تبدأ من أعلى اليسار. استعمل مواضع الطبقات في الوصف لتحديد المنطقة
واللون المصدر. للقميص مثلاً: خذ لون طبقته ومربّعها من الوصف ثم recolor بلون جديد.
'''


def describe(path: str | Path, max_layers: int = 14) -> str:
    """What the picture contains, in words an AI can act on: size, then the colour layers with their colour, share,
    bounding box and centre (from the studio's own vectoriser)."""
    import vectorize as V
    with Image.open(path) as im:
        w, h = im.size
    data = V.trace(path, max_side=300)
    tw, th = data["size"]
    sx, sy = w / tw, h / th
    lines = [f"الصورة: {Path(path).name}، {w}×{h} بيكسل، {'صورة فوتوغرافية' if data['photo'] else 'رسم أو شعار'}.",
             "الطبقات اللونية (الاسم، اللون، النسبة، المربع المحيط x0,y0,x1,y1، المركز):"]
    total = max(1.0, sum(L["area"] for L in data["layers"]))
    for L in data["layers"][:max_layers]:
        xs = [p[0] for q in L["polys"] for p in q["pts"]]
        ys = [p[1] for q in L["polys"] for p in q["pts"]]
        if not xs:
            continue
        box = (int(min(xs) * sx), int(min(ys) * sy), int(max(xs) * sx), int(max(ys) * sy))
        cx, cy = int(L["centre"][0] * sx), int(L["centre"][1] * sy)
        lines.append(f"- {L['name']}: {L['color']}، {L['area'] / total:.0%}، المربع {box}، المركز ({cx}, {cy})")
    return "\n".join(lines)


def edit_program(path: str | Path, title: str | None = None) -> tuple[str, str]:
    """(program, sha): the small edit program with a key instead of the image; the original's bytes are stored
    under code/originals/<sha>.b64 so the studio can restore them."""
    path = Path(path)
    data = path.read_bytes()
    sha = hashlib.sha1(data).hexdigest()[:16]
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    (ORIGINALS / f"{sha}.b64").write_text(base64.b64encode(data).decode("ascii"), encoding="ascii")
    with Image.open(path) as im:
        w, h = im.size
    title = title or path.stem
    return PROGRAM.format(title=title, w=w, h=h, key=KEY.format(sha=sha), tools=TOOLS), sha


def package(path: str | Path, title: str | None = None, request: str = "") -> str:
    """Instructions + description + program: one text to paste into any AI."""
    program, _ = edit_program(path, title)
    parts = [INSTRUCTIONS.strip(), "", "## وصف الصورة", describe(path), "",
             "## طلب المستخدم", request.strip() or "[اكتب التعديل المطلوب هنا، مثلاً: غيّر لون القميص إلى الأحمر]", "",
             "## البرنامج", "```python", program.rstrip(), "```"]
    return "\n".join(parts)


def restore(code: str) -> tuple[str, bool]:
    """Put the original image back in place of the key. (code, restored?)"""
    import re
    m = re.search(r"""^IMAGE_B64\s*=\s*\(?\s*['"]<<KOSIF:ORIGINAL:([0-9a-f]{16})>>['"]\s*\)?[ \t]*(#[^\n]*)?$""", code, re.M)
    if not m:
        return code, False
    f = ORIGINALS / f"{m.group(1)}.b64"
    if not f.exists():
        raise FileNotFoundError(f"the original image for key {m.group(1)} is not stored on this computer")
    b64 = f.read_text(encoding="ascii")
    body = "\n".join(f'    "{b64[i:i + 100]}"' for i in range(0, len(b64), 100))
    return code[:m.start()] + f"IMAGE_B64 = (\n{body}\n)" + code[m.end():], True


if __name__ == "__main__":
    import sys
    print(package(sys.argv[1], request=" ".join(sys.argv[2:])))
