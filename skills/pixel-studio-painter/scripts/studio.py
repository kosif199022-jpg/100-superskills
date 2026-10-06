"""KOSIF Studio: a drawing program that paints a picture pixel by pixel.

Three ways to give it a picture:
  * a scene from scenes/ (hand-written picture programs, traced images, SVG files)
  * 📝 code from any AI: SVG, Python that draws with PIL / matplotlib / turtle, or a KOSIF scene (build() -> Steps)
  * 🖼 an image (file, or Ctrl+V of a copied picture): it is traced into vector shapes and redrawn

Whatever it is, the studio lays the changed pixels down one at a time in a painter's order (strokes for skies,
growing shapes, rising figures, sparkling details). Vector pictures (scenes, SVG, traced images) also export at
3840x2560 or any size without losing quality.

    python studio.py                      # open the studio
    python studio.py dragon_girl --speed fast
    python studio.py --code drawing.py    # draw a code file (SVG / PIL / matplotlib / turtle / KOSIF scene)
    python studio.py --image photo.jpg    # trace an image and draw it
    python studio.py dragon_girl --render out.png --scale 3.2   # no window: render a 3840x2560 PNG
"""
from __future__ import annotations

import argparse
import ctypes
import json
import queue
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE / "scenes")]
import render as R  # noqa: E402

OUT, SCENES, SOURCES, CODE = HERE / "out", HERE / "scenes", HERE / "sources", HERE / "code"
PAPER = "#f3eee4"
BACKDROP = (27, 24, 34)
EXACT, VECTOR = "مطابق تماماً", "متجه قابل للتكبير"
# seconds a full-sheet step takes; smaller steps take less (time grows with the square root of their area)
SPEEDS = {"بطيء": 5.0, "عادي": 1.8, "سريع": 0.55, "فوري": 0.0}
CODE_TIMEOUT = 120
IMAGE_TYPES = (".png", ".jpg", ".jpeg", ".bmp", ".webp", ".gif", ".tif", ".tiff")
RISKY = [(r"\bos\.(remove|unlink|rmdir|removedirs|rename|replace|system|popen|kill|startfile)\b", "حذف ملفات أو تشغيل برامج"),
         (r"\bshutil\.", "نقل أو حذف ملفات"), (r"\bsubprocess\b", "تشغيل برامج"),
         (r"\b(socket|requests|urllib|http\.client|ftplib|smtplib|webbrowser)\b", "اتصال بالإنترنت"),
         (r"\b(ctypes|winreg|_winapi)\b", "وصول مباشر للنظام"), (r"\b(eval|exec|__import__|compile)\s*\(", "تنفيذ كود مخفي"),
         (r"open\([^)]*,\s*['\"](w|a|x)", "كتابة ملفات"), (r"\bpip\b|\bsys\.exit\b", "تثبيت حزم أو إنهاء البرنامج")]

AI_PROMPT = """أريد كود صورة لبرنامج رسم اسمه KOSIF Studio. أعطني كوداً واحداً كاملاً فقط، بدون أي شرح، بإحدى الصيغ:

1) الأفضل: ملف SVG كامل، viewBox="0 0 1200 800"، يبدأ بخلفية تغطي اللوحة، ثم العناصر من الخلف إلى الأمام
   (الأبعد ثم الأقرب ثم التفاصيل). استعمل path وcircle وellipse وrect وpolygon وlinearGradient وradialGradient
   والشفافية بحرية. لا تستعمل filter أو mask أو clipPath أو صوراً خارجية.

2) أو كود بايثون بمكتبة PIL فقط: img = Image.new("RGB", (1200, 800)) ثم draw = ImageDraw.Draw(img)، وارسم من
   الخلفية إلى التفاصيل بـ rectangle وellipse وpolygon وline وarc وtext، ثم img.save("out.png").

3) أو للمؤثرات السينمائية (توهج، إضاءة حواف، تدرجات ناعمة) كود KOSIF: دالة build() ترجع قائمة Step:
   Step("اسم الخطوة", [عمليات], "ترتيب", origin=(x, y))   الترتيب: "sweep" أو "grow" أو "rise" أو "down" أو "sparkle"
   أشكال: rect(x,y,w,h) ellipse(cx,cy,rx,ry) path("M .. C .. Z") poly([(x,y),...]) tube([(x,y),...],[r,...]) dots([(x,y,r),...])
   ألوان: "#rrggbb" أو "#rrggbbaa" أو lin((x1,y1),(x2,y2),[(0,"#..."),(1,"#...")]) أو rad((cx,cy),r,[(0,"#..."),(1,"#...")])
   عمليات: fill(shape, paint, alpha=1, blur=0, mode="normal"|"add"|"screen"|"multiply")  glow(shape, colour, radius, alpha)
           rim(shape, (dx,dy), width, colour, alpha)  text("نص", x, y, size, colour, anchor="mm", bold=False)
           grade(shadows, highlights, amount)  vignette(0.5)  grain(0.02)
   اللوحة 1200×800، والأسماء كلها جاهزة بدون import.

الصورة المطلوبة: [اكتب وصف الصورة هنا]"""


# ── scenes: picture programs on disk ─────────────────────────────────────────────────────────────────────────
def scenes() -> list[str]:
    return sorted({p.stem for p in [*SCENES.glob("*.py"), *SCENES.glob("*.json"), *SCENES.glob("*.svg")]
                   if not p.stem.startswith("_")})


def scene_file(name: str) -> Path | None:
    for ext in (".py", ".svg", ".json"):
        p = SCENES / f"{name}{ext}"
        if p.exists():
            return p
    return None


def load(name: str):
    """(title, steps, rolloff) for a scene drawn inside the studio, or None when it is Python that must run in
    its own process (any AI's PIL / matplotlib / turtle code)."""
    p = scene_file(name)
    if p is None:
        raise FileNotFoundError(name)
    if p.suffix == ".json":
        import vector_scene
        data = json.loads(p.read_text(encoding="utf-8"))
        return data.get("title", name), vector_scene.build(data), 1.0
    if p.suffix == ".svg":
        import svg_import
        title, steps = svg_import.load_svg(p.read_text(encoding="utf-8"))
        return title if title != "SVG" else name, steps, 1.0
    src = p.read_text(encoding="utf-8-sig")
    if not re.search(r"^\s*def\s+build\s*\(", src, re.M):
        return None
    ns = {"__name__": f"scene_{name}", "__file__": str(p)}
    exec("from render import *\nimport math, random\n", ns)
    exec(compile(src, str(p), "exec"), ns)                 # read fresh every time, so edits show at once
    return ns.get("TITLE", name), ns["build"](), ns.get("ROLLOFF", 0.82)


def image_code(path: Path, title: str) -> str:
    """Code for an image: the original file's own bytes, embedded. The studio paints it from nothing and ends
    identical to the original; the code needs nothing else, so it works the same on any machine."""
    import base64
    data = Path(path).read_bytes()
    with Image.open(path) as im:
        w, h = im.size
    b64 = base64.b64encode(data).decode("ascii")
    body = "\n".join(f'    "{b64[i:i + 100]}"' for i in range(0, len(b64), 100))
    return (f"# KOSIF Studio: كود الصورة «{title}».\n"
            "# يرسمها البرنامج من ورقة فارغة بيكسلاً ببيكسل (الكتل ثم التدقيق ثم اللمسات الدقيقة)،\n"
            "# وتنتهي مطابقة للأصل تماماً. الصورة الأصلية محفوظة داخل الكود، فهو يعمل وحده على أي جهاز.\n"
            f"TITLE = {title!r}\nSIZE = ({w}, {h})\nIMAGE_B64 = (\n{body}\n)\n")


def enlarge(im: Image.Image, target: int = 3840) -> tuple[Image.Image, int]:
    """A high-resolution copy of a raster picture with its own colours: a whole-number Lanczos enlargement (the
    pixel grid stays regular) and a gentle unsharp mask to keep edges crisp. Colours are not simplified."""
    import cv2
    rgba = np.ascontiguousarray(np.asarray(im.convert("RGBA")))
    h, w = rgba.shape[:2]
    k = max(1, round(target / max(w, h)))
    if k == 1:
        return Image.fromarray(rgba, "RGBA"), 1
    big = cv2.resize(rgba, (w * k, h * k), interpolation=cv2.INTER_LANCZOS4)
    rgb = big[..., :3]
    big[..., :3] = cv2.addWeighted(rgb, 1.35, cv2.GaussianBlur(rgb, (0, 0), .6 * k), -.35, 0)
    return Image.fromarray(big, "RGBA"), k


def risky(code: str) -> list[str]:
    if code.lstrip().startswith("<"):
        return []                                         # SVG is data, not code
    return sorted({why for pat, why in RISKY if re.search(pat, code)})


# ── paint jobs: one per step, the changed pixels in painting order ───────────────────────────────────────────
class Job:
    __slots__ = ("i", "step", "order", "cols", "pos", "t0", "dur")

    def __init__(self, i, step, order, cols):
        self.i, self.step, self.order, self.cols = i, step, order, cols
        self.pos, self.t0, self.dur = 0, 0.0, 0.0


def produce(steps, scale: float, out: queue.Queue, stop: threading.Event, rolloff: float = 0.82):
    """Render a picture program inside the studio and turn each step into the pixels to lay down."""
    prev = None
    try:
        for i, st, img in R.render(steps, scale, ss=3, paper=PAPER, rolloff=rolloff):
            if stop.is_set():
                return
            flat = img.reshape(-1, 3)
            if prev is None:
                prev = np.empty_like(flat)
                prev[:] = (R.rgb(PAPER) * 255 + .5).astype(np.uint8)
            idx = np.flatnonzero(np.any(flat != prev, axis=1)).astype(np.int32)
            order = R.reveal_order(idx, img.shape[1], st, scale, seed=i)
            out.put(Job(i, st, order, flat[order].copy()))
            prev = flat.copy()
    except Exception as e:
        out.put(("error", f"{type(e).__name__}: {e}"))
    finally:
        out.put(None)


def produce_exact(rgba: np.ndarray, out: queue.Queue, stop: threading.Event):
    """Paint an image from nothing at its own resolution; the last job leaves it identical to the original."""
    import exact
    i = -1
    try:
        out.put(("status", "🧠 يقيس خطط الرسم الممكنة ويسأل Jev عن أفضلها..."))
        block_k, fine_k, info = exact.choose_plan(rgba)          # photos: Jev chooses; logos keep their colours
        if info:
            out.put(("plan", info))
        for i, (label, kind, origin, weight, order, cols) in enumerate(exact.plan(rgba, block_k, fine_k)):
            if stop.is_set():
                return
            out.put(Job(i, R.Step(label, [], kind, origin, weight), order, cols))
        out.put(("done", {"jobs": i + 1}))
    except Exception as e:
        out.put(("error", f"{type(e).__name__}: {e}"))
    finally:
        out.put(None)


def produce_code(code_file: Path, scale: float, out: queue.Queue, stop: threading.Event):
    """Run code in its own process (runner.py) and stream its paint jobs as they are written."""
    work = Path(tempfile.mkdtemp(prefix="kosif_run_"))
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    proc = subprocess.Popen([sys.executable, str(HERE / "runner.py"), str(code_file), str(work), "--scale", str(scale)],
                            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, creationflags=flags)
    n, t0, canvas_sent = 0, time.time(), False
    try:
        while not stop.is_set():
            if not canvas_sent and (work / "canvas.json").exists():
                c = json.loads((work / "canvas.json").read_text(encoding="utf-8"))
                out.put(("canvas", (c["w"], c["h"])))
                canvas_sent = True
            job = work / f"job_{n:04d}.npz"
            if job.exists():
                meta = json.loads((work / f"job_{n:04d}.json").read_text(encoding="utf-8"))
                with np.load(job) as z:
                    order, cols = z["order"], z["cols"]
                st = R.Step(meta["label"], [], meta["order"], tuple(meta["origin"]) if meta["origin"] else None,
                            meta["weight"])
                out.put(Job(n, st, order, cols))
                n += 1
                continue
            if (work / "error.txt").exists():
                out.put(("error", (work / "error.txt").read_text(encoding="utf-8")))
                return
            if (work / "done.json").exists():
                if not (work / f"job_{n:04d}.npz").exists():
                    if (work / "final.png").exists():
                        out.put(("reference", np.asarray(Image.open(work / "final.png").convert("RGBA")).copy()))
                    out.put(("done", json.loads((work / "done.json").read_text(encoding="utf-8"))))
                    return
                continue
            if proc.poll() is not None:
                time.sleep(.1)
                if not any((work / f).exists() for f in ("done.json", "error.txt")) and \
                        not (work / f"job_{n:04d}.npz").exists():
                    err = proc.stderr.read().decode("utf-8", "replace") if proc.stderr else ""
                    out.put(("error", err or f"the code process ended (exit code {proc.returncode})"))
                    return
            if time.time() - t0 > CODE_TIMEOUT:
                proc.kill()
                out.put(("error", f"الكود تجاوز {CODE_TIMEOUT} ثانية فأُوقف."))
                return
            time.sleep(.03)
    finally:
        if proc.poll() is None:
            proc.kill()
        out.put(None)
        shutil.rmtree(work, ignore_errors=True)


# ── the window ─────────────────────────────────────────────────────────────────────────────────────────────
class Studio:
    def __init__(self, scene: str, speed: str, scale: float = 1.0):
        import tkinter as tk
        from tkinter import ttk
        from PIL import ImageTk
        self.tk, self.ttk = tk, ttk
        self.scale = scale
        self.W, self.H = round(R.W0 * scale), round(R.H0 * scale)
        self.root = tk.Tk()
        self.root.title("KOSIF Studio — رسم بالبيكسل")
        self.root.configure(bg="#16141c")
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TButton", padding=(10, 4))

        bar = tk.Frame(self.root, bg="#16141c")
        bar.pack(fill="x", padx=8, pady=6)
        self.scene = tk.StringVar(value=scene)
        self.speed = tk.StringVar(value=speed)
        self.scene_box = ttk.Combobox(bar, textvariable=self.scene, values=scenes(), width=18, state="readonly")
        self.scene_box.pack(side="left")
        self.scene_box.bind("<<ComboboxSelected>>", lambda e: self.start())
        ttk.Button(bar, text="▶  ارسم", command=self.redraw).pack(side="left", padx=(8, 2))
        self.pause_btn = ttk.Button(bar, text="⏸  إيقاف", command=self.toggle_pause)
        self.pause_btn.pack(side="left", padx=2)
        tk.Label(bar, text="السرعة", fg="#cfc8dc", bg="#16141c").pack(side="left", padx=(14, 4))
        ttk.Combobox(bar, textvariable=self.speed, values=list(SPEEDS), width=7, state="readonly").pack(side="left")
        ttk.Button(bar, text="📝  كود", command=self.open_code).pack(side="left", padx=(14, 2))
        ttk.Button(bar, text="🖼  صورة", command=self.open_image).pack(side="left", padx=2)
        ttk.Button(bar, text="📤  كود الصورة", command=self.export_image_code).pack(side="left", padx=2)
        self.image_mode = tk.StringVar(value=EXACT)
        ttk.Combobox(bar, textvariable=self.image_mode, values=[EXACT, VECTOR], width=16,
                     state="readonly").pack(side="left", padx=2)
        ttk.Button(bar, text="⤢  تصدير عالي الدقة", command=self.export_big).pack(side="right", padx=2)
        ttk.Button(bar, text="💾  حفظ PNG", command=self.save_png).pack(side="right", padx=2)

        self.cv = tk.Canvas(self.root, width=self.W, height=self.H, bg=PAPER, highlightthickness=0)
        self.cv.pack(padx=8)
        self.disp = np.empty((self.H, self.W, 3), np.uint8)
        self.photo = ImageTk.PhotoImage(Image.new("RGB", (self.W, self.H), PAPER))
        self.cv.create_image(0, 0, image=self.photo, anchor="nw")
        self.brush = self.cv.create_oval(-20, -20, -10, -10, outline="#ffffff", width=2)
        self.brush_in = self.cv.create_oval(-20, -20, -10, -10, outline="#1a1420", width=1)

        self.info = tk.StringVar(value="")
        tk.Label(self.root, textvariable=self.info, fg="#9fe0b5", bg="#16141c", anchor="e",
                 font=("Segoe UI", 11, "bold")).pack(fill="x", padx=10, pady=(4, 0))
        self.status = tk.StringVar(value="")
        tk.Label(self.root, textvariable=self.status, fg="#e9e2f5", bg="#16141c", anchor="e",
                 font=("Segoe UI", 11)).pack(fill="x", padx=10, pady=(2, 8))
        self.root.bind("<Control-v>", lambda e: self.paste_any())
        self.root.bind("<Control-V>", lambda e: self.paste_any())
        self.root.bind("<Control-o>", lambda e: self.open_image())

        self.q: queue.Queue = queue.Queue(maxsize=6)
        self.stop = threading.Event()
        self.job = None
        self.paused = False
        self.drawn, self.t_start, self.steps_total = 0, 0.0, 0
        self.source = ("scene", scene)                     # what is being drawn: a scene, a code file, an image
        self.native = None                                 # an image painted at its own resolution
        self.reference = None                              # what that image must end up identical to
        self.code_win = None
        self.last_info: dict = {}
        if scene:
            self.root.after(300, self.start)

    # ── drawing ──────────────────────────────────────────────────────────────────────────────────────────────
    def redraw(self):
        if self.source[0] == "code":
            self.start_code(self.source[1])
        elif self.source[0] == "image":
            self.start_exact(*self.source[1:])
        else:
            self.start()

    def _reset(self, title: str, total: int, canvas: tuple[int, int] | None = None):
        self.stop.set()
        self.stop = threading.Event()
        self.q = queue.Queue(maxsize=6)
        self.title, self.steps_total = title, total
        self.disp[:] = (R.rgb(PAPER) * 255 + .5).astype(np.uint8)
        self.flat = self.disp.reshape(-1, 3)
        self.photo.paste(Image.fromarray(self.disp))
        self.job, self.paused, self.drawn = None, False, 0
        self.pause_btn.configure(text="⏸  إيقاف")
        self.t_start = time.perf_counter()
        self.last_info = {}
        self.native, self.reference = None, None
        self.info.set("")
        if canvas:
            self.set_native(*canvas)

    def set_native(self, w: int, h: int):
        """Paint on a w x h canvas at its own resolution (nothing resampled), shown fitted into the window."""
        f = min(self.W / w, self.H / h)
        f = float(int(f)) if f >= 2 else f                 # small images: a whole-number zoom keeps pixels square
        dw, dh = max(1, round(w * f)), max(1, round(h * f))
        ox, oy = (self.W - dw) // 2, (self.H - dh) // 2
        xs = np.minimum((np.arange(dw) / f).astype(np.int64), w - 1)
        ys = np.minimum((np.arange(dh) / f).astype(np.int64), h - 1)
        self.native = {"w": w, "h": h, "f": f, "ox": ox, "oy": oy, "dw": dw, "dh": dh,
                       "map": (ys[:, None] * w + xs[None, :]).reshape(-1), "canvas": np.zeros((w * h, 4), np.uint8)}
        self.disp[:] = BACKDROP
        self.refresh_native()

    def refresh_native(self, final: bool = False):
        """Show the native canvas fitted to the window the way image viewers do: shrinking averages the pixels
        (no jagged edges), small pictures zoom by whole numbers (crisp pixels). Very large pictures use the fast
        nearest-pixel view while drawing and the smooth one at the end."""
        import cv2
        nv = self.native
        if nv["w"] * nv["h"] <= 4_000_000 or final:
            can = nv["canvas"].reshape(nv["h"], nv["w"], 4).astype(np.float32)
            a = can[..., 3:4] / 255
            rgb = can[..., :3] * a + R.rgb(PAPER) * 255 * (1 - a)       # see-through pixels show the paper
            if (nv["dw"], nv["dh"]) != (nv["w"], nv["h"]):
                interp = cv2.INTER_AREA if nv["f"] < 1 else cv2.INTER_NEAREST if nv["f"] >= 2 else cv2.INTER_CUBIC
                rgb = cv2.resize(rgb, (nv["dw"], nv["dh"]), interpolation=interp)
            view = np.clip(rgb + .5, 0, 255).astype(np.uint8)
        else:
            sub = nv["canvas"][nv["map"]].astype(np.float32)
            a = sub[:, 3:4] / 255
            view = (sub[:, :3] * a + R.rgb(PAPER) * 255 * (1 - a) + .5).astype(np.uint8).reshape(nv["dh"], nv["dw"], 3)
        self.disp[nv["oy"]:nv["oy"] + nv["dh"], nv["ox"]:nv["ox"] + nv["dw"]] = view
        self.photo.paste(Image.fromarray(self.disp))

    def start_exact(self, src: Path, name: str):
        import exact
        self.source = ("image", src, name)
        rgba = exact.load_rgba(src)
        h, w = rgba.shape[:2]
        self._reset(f"{name} ({w}×{h})", 0, canvas=(w, h))
        self.reference = rgba
        self.status.set("يرسم الصورة من الصفر ليطابق الأصل تماماً...")
        threading.Thread(target=produce_exact, args=(rgba, self.q, self.stop), daemon=True).start()
        self.root.after(1, self.tick)

    def start(self):
        name = self.scene.get()
        self.source = ("scene", name)
        try:
            loaded = load(name)
        except Exception as e:
            self.status.set(f"تعذّر فتح المشهد {name}: {e}")
            return
        if loaded is None:                                  # plain Python from an AI: run it in its own process
            self.start_code(scene_file(name), keep_source=False)
            self.source = ("scene", name)
            return
        title, steps, rolloff = loaded
        self._reset(title, len(steps))
        threading.Thread(target=produce, args=(steps, self.scale, self.q, self.stop, rolloff), daemon=True).start()
        self.root.after(1, self.tick)

    def start_code(self, code_file: Path, keep_source: bool = True):
        if keep_source:
            self.source = ("code", code_file)
        self._reset("كود", 0)
        self.status.set("يشغّل الكود...")
        threading.Thread(target=produce_code, args=(Path(code_file), self.scale, self.q, self.stop),
                         daemon=True).start()
        self.root.after(1, self.tick)

    def toggle_pause(self):
        self.paused = not self.paused
        self.pause_btn.configure(text="▶  متابعة" if self.paused else "⏸  إيقاف")
        if not self.paused and self.job:
            self.job.t0 = time.perf_counter() - self.job.dur * self.job.pos / max(1, len(self.job.order))

    def tick(self):
        if self.paused:
            self.root.after(50, self.tick)
            return
        now = time.perf_counter()
        if self.job is None:
            try:
                item = self.q.get_nowait()
            except queue.Empty:
                self.root.after(10, self.tick)
                return
            if item is None:                                # the picture is finished
                self.finish()
                return
            if isinstance(item, tuple):
                kind, val = item
                if kind == "done":
                    self.last_info = val
                    p = val.get("plan")
                    if p and p.get("candidate"):
                        c = p["candidate"]
                        who = (f"ثقة Jev {round(p['probabilities'][p['choice']] * 100)}٪"
                               if p["by"] == "jev" else "بالقاعدة: Jev غير متاح")
                        self.info.set(f"🧠 الخطة: {c['block_colours']} لوناً ثم {c['refine_tones']} درجة ({who})")
                    self.title, self.steps_total = val.get("title", self.title), val.get("jobs", self.steps_total)
                elif kind == "canvas":
                    self.set_native(*val)
                elif kind == "reference":
                    self.reference = val
                elif kind == "status":
                    self.status.set(val)
                elif kind == "plan":
                    c = val["candidates"][val["choice"]]
                    who = (f"ثقة Jev {round(val['probabilities'][val['choice']] * 100)}٪"
                           if val["by"] == "jev" else "بالقاعدة: Jev غير متاح")
                    self.info.set(f"🧠 الخطة: {c['block_colours']} لوناً ثم {c['refine_tones']} درجة ({who})")
                else:
                    self.show_error(val)
                self.root.after(1, self.tick)
                return
            self.job = item
            n = len(self.job.order)
            k = SPEEDS.get(self.speed.get(), 1.8)
            area = self.native["w"] * self.native["h"] if self.native else self.W * self.H
            self.job.dur = k * self.job.step.weight * (n / area) ** .5
            self.job.t0 = now
        j = self.job
        n = len(j.order)
        target = n if j.dur <= 0 else min(n, int(n * (now - j.t0) / j.dur))
        if target > j.pos:
            sel = j.order[j.pos:target]
            last = int(sel[-1])
            if self.native is None:
                self.flat[sel] = j.cols[j.pos:target]
                x, y = last % self.W, last // self.W
                self.photo.paste(Image.fromarray(self.disp))
            else:
                nv = self.native
                cols = j.cols[j.pos:target]
                nv["canvas"][sel] = cols if cols.shape[1] == 4 else np.column_stack([cols, np.full(len(cols), 255,
                                                                                                    np.uint8)])
                x = nv["ox"] + (last % nv["w"] + .5) * nv["f"]
                y = nv["oy"] + (last // nv["w"] + .5) * nv["f"]
                self.refresh_native()
            self.drawn += target - j.pos
            j.pos = target
            self.cv.coords(self.brush, x - 7, y - 7, x + 7, y + 7)
            self.cv.coords(self.brush_in, x - 5, y - 5, x + 5, y + 5)
        total = f"/{self.steps_total}" if self.steps_total else ""
        self.status.set(f"{self.title}   ·   الخطوة {j.i + 1}{total}: {j.step.label}   ·   "
                        f"{self.drawn:,} بيكسل مرسوم   ·   {now - self.t_start:.1f} ث")
        if j.pos >= n:
            self.job = None
            self.root.after(1, self.tick)
        else:
            self.root.after(12, self.tick)

    def finish(self):
        self.cv.coords(self.brush, -20, -20, -10, -10)
        self.cv.coords(self.brush_in, -20, -20, -10, -10)
        self.photo.paste(Image.fromarray(self.disp))
        if getattr(self, "error_shown", False):
            self.error_shown = False
            return
        secs = time.perf_counter() - self.t_start
        steps = self.steps_total or (self.job.i + 1 if self.job else 0)
        msg = (f"{self.title}   ·   اكتملت الرسمة: {self.drawn:,} بيكسل في {secs:.1f} ثانية"
               + (f"   ·   {steps} خطوة" if steps else ""))
        OUT.mkdir(exist_ok=True)
        if self.native is None:
            Image.fromarray(self.disp).save(OUT / f"{self.out_name()}_{self.W}x{self.H}.png")
        else:
            nv = self.native
            self.refresh_native(final=True)
            img = nv["canvas"].reshape(nv["h"], nv["w"], 4)
            Image.fromarray(img, "RGBA").save(OUT / f"{self.out_name()}_exact.png")
            if self.reference is not None and self.reference.shape == img.shape:
                import exact
                bad = exact.mismatches(img, self.reference)
                total = nv["w"] * nv["h"]
                plan = self.info.get()
                self.info.set((f"✅ مطابقة للأصل تماماً ({total:,} بيكسل)" if bad == 0 else
                               f"⚠ {bad:,} بيكسل يختلف عن الأصل") + (f"   ·   {plan[2:]}" if plan else ""))
        self.status.set(msg)

    def out_name(self) -> str:
        return {"code": "code", "image": self.source[-1]}.get(self.source[0], self.scene.get())

    def show_error(self, msg: str):
        self.error_shown = True
        last = [ln for ln in msg.strip().splitlines() if ln.strip()][-1:] or [msg]
        self.status.set(f"⚠ الكود فيه خطأ: {last[0][:150]}")
        if self.code_win is not None and self.code_win.winfo_exists():
            self.err_box.configure(state="normal")
            self.err_box.delete("1.0", "end")
            self.err_box.insert("1.0", msg)
            self.err_box.configure(state="disabled")

    # ── code from any AI ───────────────────────────────────────────────────────────────────────────────────
    def open_code(self, text: str | None = None, run: bool = False):
        tk, ttk = self.tk, self.ttk
        if self.code_win is None or not self.code_win.winfo_exists():
            w = self.code_win = tk.Toplevel(self.root)
            w.title("📝 كود الصورة — الصق كود أي ذكاء اصطناعي")
            w.configure(bg="#16141c")
            tk.Label(w, text="الصق كود الصورة من أي ذكاء اصطناعي، ثم اضغط «ارسم الكود»", fg="#e9e2f5",
                     bg="#16141c", font=("Segoe UI", 11), anchor="e").pack(fill="x", padx=10, pady=(8, 0))
            tk.Label(w, text="SVG   ·   Python: PIL / matplotlib / turtle   ·   KOSIF scene: build()   ·   Ctrl+Enter",
                     fg="#9f97b3", bg="#16141c", font=("Segoe UI", 9), anchor="e").pack(fill="x", padx=10, pady=(0, 4))
            row = tk.Frame(w, bg="#16141c")
            row.pack(fill="x", padx=8, pady=4)
            ttk.Button(row, text="▶  ارسم الكود", command=self.run_code).pack(side="right", padx=2)
            ttk.Button(row, text="📋  لصق", command=self.paste_code).pack(side="right", padx=2)
            ttk.Button(row, text="📂  فتح ملف", command=self.open_code_file).pack(side="right", padx=2)
            ttk.Button(row, text="💾  حفظ كمشهد", command=self.save_code_as_scene).pack(side="right", padx=2)
            ttk.Button(row, text="🧹  مسح", command=lambda: self.code_text.delete("1.0", "end")).pack(side="right", padx=2)
            ttk.Button(row, text="🤖  انسخ تعليمات للذكاء الاصطناعي", command=self.copy_ai_prompt).pack(side="left", padx=2)
            ex = sorted(p.name for p in (HERE / "examples").glob("*") if p.suffix in (".py", ".svg"))
            if ex:
                self.example = tk.StringVar(value="أمثلة…")
                cb = ttk.Combobox(row, textvariable=self.example, values=ex, width=22, state="readonly")
                cb.pack(side="left", padx=6)
                cb.bind("<<ComboboxSelected>>", lambda e: self.load_code_text(
                    (HERE / "examples" / self.example.get()).read_text(encoding="utf-8")))
            body = tk.Frame(w, bg="#16141c")
            body.pack(fill="both", expand=True, padx=8)
            self.code_text = tk.Text(body, width=100, height=30, wrap="none", undo=True, font=("Consolas", 11),
                                     bg="#100e15", fg="#e8e3f2", insertbackground="#ffffff", relief="flat")
            ys = ttk.Scrollbar(body, orient="vertical", command=self.code_text.yview)
            xs = ttk.Scrollbar(body, orient="horizontal", command=self.code_text.xview)
            self.code_text.configure(yscrollcommand=ys.set, xscrollcommand=xs.set)
            ys.pack(side="right", fill="y")
            xs.pack(side="bottom", fill="x")
            self.code_text.pack(side="left", fill="both", expand=True)
            self.err_box = tk.Text(w, height=6, wrap="word", font=("Consolas", 10), bg="#1d1218", fg="#ff9a9a",
                                   relief="flat", state="disabled")
            self.err_box.pack(fill="x", padx=8, pady=(4, 8))
            self.code_text.bind("<Control-Return>", lambda e: (self.run_code(), "break")[1])
            w.geometry("+%d+%d" % (self.root.winfo_rootx() + 60, self.root.winfo_rooty() + 80))
        self.code_win.deiconify()
        self.code_win.lift()
        if text is not None:
            self.load_code_text(text)
        if run:
            self.run_code()

    def load_code_text(self, text: str):
        self.code_text.delete("1.0", "end")
        self.code_text.insert("1.0", text)

    def paste_code(self):
        try:
            self.load_code_text(self.root.clipboard_get())
        except self.tk.TclError:
            self.status.set("الحافظة لا تحتوي نصاً.")

    def open_code_file(self):
        from tkinter import filedialog
        p = filedialog.askopenfilename(filetypes=[("كود صورة", "*.py *.svg *.txt"), ("الكل", "*.*")])
        if p:
            self.load_code_text(Path(p).read_text(encoding="utf-8-sig", errors="replace"))

    def copy_ai_prompt(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(AI_PROMPT)
        self.status.set("نُسخت التعليمات: الصقها في أي ذكاء اصطناعي، واكتب وصف صورتك مكان [اكتب وصف الصورة هنا]، "
                        "ثم الصق الكود الذي يعطيك إياه هنا.")

    def run_code(self):
        from tkinter import messagebox
        code = self.code_text.get("1.0", "end").strip()
        code = re.sub(r"^```[\w-]*\s*\n|\n```\s*$", "", code)        # AIs often wrap code in ``` fences
        if not code:
            self.status.set("الصق كوداً أولاً.")
            return
        why = risky(code)
        if why and not messagebox.askyesno("تنبيه قبل التشغيل",
                                           "هذا الكود يحتوي أوامر تتجاوز الرسم:\n• " + "\n• ".join(why) +
                                           "\n\nسيعمل على جهازك بصلاحياتك. هل تثق بمصدره وتريد تشغيله؟",
                                           icon="warning", default="no", parent=self.code_win):
            return
        CODE.mkdir(exist_ok=True)
        f = CODE / ("last.svg" if code.lstrip().startswith("<") else "last.py")
        f.write_text(code, encoding="utf-8")
        self.err_box.configure(state="normal")
        self.err_box.delete("1.0", "end")
        self.err_box.configure(state="disabled")
        self.start_code(f)

    def save_code_as_scene(self):
        from tkinter import simpledialog
        code = self.code_text.get("1.0", "end").strip()
        if not code:
            return
        name = simpledialog.askstring("حفظ كمشهد", "اسم المشهد (بالإنجليزية، بدون مسافات):", parent=self.code_win)
        if not name:
            return
        name = re.sub(r"[^\w-]+", "_", name.strip())
        (SCENES / f"{name}{'.svg' if code.lstrip().startswith('<') else '.py'}").write_text(code, encoding="utf-8")
        self.scene_box.configure(values=scenes())
        self.status.set(f"حُفظ المشهد {name}، وصار في قائمة المشاهد.")

    # ── pictures: trace and redraw ─────────────────────────────────────────────────────────────────────────
    def open_image(self, path: str | None = None, image: Image.Image | None = None):
        from tkinter import filedialog
        if path is None and image is None:
            path = filedialog.askopenfilename(filetypes=[("صور", " ".join("*" + e for e in IMAGE_TYPES)),
                                                         ("الكل", "*.*")])
            if not path:
                return
        SOURCES.mkdir(exist_ok=True)
        self.original = None
        if image is not None:
            name = time.strftime("clip_%Y%m%d_%H%M%S")
            src = SOURCES / f"{name}.png"
            image.save(src)
            self.original = src
        else:
            name = re.sub(r"[^\w-]+", "_", Path(path).stem) or "image"
            src = SOURCES / f"{name}.png"
            Image.open(path).save(src)                  # decoded pixels kept losslessly: the reference to match
            self.original = Path(path)                  # the file itself, for 📤 image code
        if self.image_mode.get() == EXACT:
            self.start_exact(src, name)
            return
        self.status.set("يُعيد رسم الصورة: يتعرّف على ألوانها ويحوّلها إلى أشكال متجهة...")

        def work():
            import vectorize as V
            t = time.perf_counter()
            try:
                data = V.trace(src)
            except Exception as e:
                self.root.after(0, lambda: self.status.set(f"تعذّر تحليل الصورة: {e}"))
                return
            data["title"] = name
            V.save(data, SCENES / f"{name}.json")
            OUT.mkdir(exist_ok=True)
            V.to_svg(data, OUT / f"{name}.svg", scale=2)
            secs = time.perf_counter() - t

            def go():
                self.scene_box.configure(values=scenes())
                self.scene.set(name)
                self.start()
                self.title = f"{name} ({len(data['layers'])} لون، حُلّلت في {secs:.1f} ث)"
            self.root.after(0, go)
        threading.Thread(target=work, daemon=True).start()

    def paste_any(self):
        """Ctrl+V: a copied picture is traced and redrawn; copied code or SVG goes to the code panel and runs."""
        from PIL import ImageGrab
        try:
            clip = ImageGrab.grabclipboard()
        except Exception:
            clip = None
        if isinstance(clip, Image.Image):
            self.open_image(image=clip.convert("RGBA"))
            return
        if isinstance(clip, list) and clip:
            p = Path(clip[0])
            if p.suffix.lower() in IMAGE_TYPES:
                self.open_image(path=str(p))
            elif p.suffix.lower() in (".py", ".svg", ".txt"):
                self.open_code(p.read_text(encoding="utf-8-sig", errors="replace"), run=True)
            return
        try:
            text = self.root.clipboard_get()
        except self.tk.TclError:
            return
        if "<svg" in text or re.search(r"\b(import|from|def|ImageDraw|turtle|plt)\b", text):
            self.open_code(text, run=True)

    def export_image_code(self, path: str | None = None):
        """📤: the code of an image (the open one, or one you pick). Pasted into any KOSIF Studio it paints the
        picture from nothing and ends identical to the original."""
        from tkinter import filedialog
        src = Path(path) if path else getattr(self, "original", None) if self.source[0] == "image" else None
        if src is None or not src.exists():
            p = filedialog.askopenfilename(title="اختر الصورة التي تريد كودها",
                                           filetypes=[("صور", " ".join("*" + e for e in IMAGE_TYPES)), ("الكل", "*.*")])
            if not p:
                return
            src = Path(p)
        name = re.sub(r"[^\w-]+", "_", src.stem) or "image"
        OUT.mkdir(exist_ok=True)
        code = image_code(src, name)
        f = OUT / f"{name}_code.py"
        f.write_text(code, encoding="utf-8")
        self.open_code(code)
        self.status.set(f"📤 كود الصورة جاهز ({len(code) // 1024:,} ك.ب): {f}. اضغط «ارسم الكود» ليرسمها مطابقة للأصل.")

    # ── files ────────────────────────────────────────────────────────────────────────────────────────────
    def save_png(self):
        from tkinter import filedialog
        p = filedialog.asksaveasfilename(defaultextension=".png", initialdir=OUT,
                                         initialfile=f"{self.out_name()}.png", filetypes=[("PNG", "*.png")])
        if p:
            if self.native is not None:
                nv = self.native
                Image.fromarray(nv["canvas"].reshape(nv["h"], nv["w"], 4), "RGBA").save(p)
            else:
                Image.fromarray(self.disp).save(p)
            self.status.set(f"حُفظت: {p}")

    def export_big(self):
        name = self.out_name()
        OUT.mkdir(exist_ok=True)
        p = OUT / f"{name}_3840x2560.png"
        self.status.set("يُصدَّر بدقة 3840×2560 من نفس البرنامج...")

        def work():
            t = time.perf_counter()
            try:
                if self.source[0] == "image":
                    import vectorize as V
                    src = self.source[1]
                    im = Image.open(src)
                    im.load()
                    if V.looks_like_photo(np.asarray(im.convert("RGBA"))):
                        big, k = enlarge(im)                 # photos: the exact image itself, enlarged, true colours
                        pk = OUT / f"{name}_x{k}.png"
                        big.save(pk)
                        msg = (f"✅ تكبير ×{k} من الصورة المطابقة نفسها بألوانها الأصلية ({big.width}×{big.height}): "
                               f"out/{pk.name}   ·   والأصل المطابق: out/{name}_exact.png")
                    else:                                    # logos and flat art: vector stays sharp at any size
                        import vector_scene
                        data = V.trace(src)
                        V.to_svg(data, OUT / f"{name}.svg", scale=2)
                        R.render_image(vector_scene.build(data), scale=3.2, ss=2, rolloff=1.0).save(p)
                        msg = (f"✅ نسخة متجهة حادة بأي حجم: out/{name}.svg و {p.name}   ·   "
                               f"والأصل المطابق: out/{name}_exact.png")
                elif self.source[0] == "code" or load(name) is None:
                    code = self.source[1] if self.source[0] == "code" else scene_file(name)
                    tmp = Path(tempfile.mkdtemp(prefix="kosif_exp_"))
                    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
                    subprocess.run([sys.executable, str(HERE / "runner.py"), str(code), str(tmp), "--scale", "3.2",
                                    "--export", str(p)], timeout=CODE_TIMEOUT * 2, creationflags=flags,
                                   capture_output=True)
                    info = json.loads((tmp / "done.json").read_text(encoding="utf-8"))
                    shutil.rmtree(tmp, ignore_errors=True)
                    if info.get("raster"):                  # raster result: keep it exact, and enlarge it faithfully
                        exact_p = OUT / f"{name}_original.png"
                        Path(p).replace(exact_p)
                        big, k = enlarge(Image.open(exact_p))
                        pk = OUT / f"{name}_x{k}.png"
                        big.save(pk)
                        msg = (f"✅ ناتج الكود بدقته الأصلية: out/{exact_p.name}   ·   وتكبير ×{k} بألوانه الأصلية "
                               f"({big.width}×{big.height}): out/{pk.name}")
                    else:
                        msg = f"تم التصدير 3840×2560 بلا فقد في الجودة في {time.perf_counter() - t:.0f} ث: {p}"
                else:
                    _, steps, rolloff = load(name)
                    R.render_image(steps, scale=3.2, ss=2, rolloff=rolloff).save(p)
                    msg = f"تم التصدير 3840×2560 بلا فقد في الجودة في {time.perf_counter() - t:.0f} ث: {p}"
            except Exception as e:
                msg = f"تعذّر التصدير: {e}"
            self.root.after(0, lambda: self.status.set(msg))
        threading.Thread(target=work, daemon=True).start()

    def run(self):
        self.root.mainloop()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scene", nargs="?", default="dragon_girl" if scene_file("dragon_girl") else (scenes() or [""])[0])
    ap.add_argument("--speed", default="عادي", help="بطيء / عادي / سريع / فوري  (or slow/normal/fast/instant)")
    ap.add_argument("--render", metavar="PNG", help="no window: render the picture program to this file")
    ap.add_argument("--scale", type=float, default=1.0, help="1.0 = 1200x800, 3.2 = 3840x2560")
    ap.add_argument("--trace", metavar="IMAGE", help="vectorize an image into scenes/<name>.json (+ out/<name>.svg)")
    ap.add_argument("--image", metavar="IMAGE", help="open the studio and redraw this image")
    ap.add_argument("--image-code", metavar="IMAGE", help="no window: write the code of this image to out/<name>_code.py")
    ap.add_argument("--code", metavar="FILE", help="open the studio and draw this code file (SVG/PIL/matplotlib/turtle/scene)")
    ap.add_argument("--name", help="scene name for --trace (default: the image's file name)")
    ap.add_argument("--title", help="title shown while drawing a traced scene")
    a = ap.parse_args()
    if a.trace:
        import vectorize as V
        name = a.name or Path(a.trace).stem
        t = time.perf_counter()
        data = V.trace(a.trace)
        data["title"] = a.title or name
        V.save(data, SCENES / f"{name}.json")
        OUT.mkdir(exist_ok=True)
        V.to_svg(data, OUT / f"{name}.svg", scale=4)
        pts = sum(len(p["pts"]) for L in data["layers"] for p in L["polys"])
        print(f"traced {a.trace} -> scenes/{name}.json + out/{name}.svg: {len(data['layers'])} colours, "
              f"{pts} points, {time.perf_counter() - t:.1f}s")
        a.scene = name
    if a.image_code:
        name = re.sub(r"[^\w-]+", "_", Path(a.image_code).stem) or "image"
        OUT.mkdir(exist_ok=True)
        f = OUT / f"{name}_code.py"
        f.write_text(image_code(Path(a.image_code), name), encoding="utf-8")
        print(f"{f}: {f.stat().st_size // 1024:,} KB")
        return
    speed = {"slow": "بطيء", "normal": "عادي", "fast": "سريع", "instant": "فوري"}.get(a.speed, a.speed)
    if a.render:
        t = time.perf_counter()
        loaded = load(a.scene)
        if loaded is None:
            raise SystemExit("this scene is plain Python: draw it in the studio, or run runner.py with --export")
        _, steps, rolloff = loaded
        R.render_image(steps, scale=a.scale, ss=2 if a.scale > 2 else 3, rolloff=rolloff).save(a.render)
        print(f"{a.render}: {round(R.W0 * a.scale)}x{round(R.H0 * a.scale)} in {time.perf_counter() - t:.1f}s")
        return
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)      # real pixels, not Windows' blurry upscaling
    except Exception:
        pass
    st = Studio("" if (a.code or a.image) else a.scene, speed, a.scale)
    if a.code:
        st.root.after(300, lambda: st.open_code(Path(a.code).read_text(encoding="utf-8-sig"), run=True))
    elif a.image:
        st.root.after(300, lambda: st.open_image(path=a.image))
    st.run()


if __name__ == "__main__":
    main()
