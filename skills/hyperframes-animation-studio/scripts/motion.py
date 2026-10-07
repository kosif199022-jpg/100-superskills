"""KOSIF Motion — professional animations as HTML compositions (HyperFrames format + GSAP + the motion kit),
rendered by HyperFrames' CLI when it is installed here, or by KOSIF Studio's own frame renderer.

    python motion.py new NAME [--seconds 8] [--fps 30] [--size 1920x1080] [--title "..."]   a project in projects/NAME
    python motion.py frames PROJECT [--times 0.5,2,4,8] [--out DIR]                           key frames (the 8-second gate)
    python motion.py check PROJECT                                                             HyperFrames lint + runtime validation
    python motion.py render PROJECT [--engine auto|hyperframes|studio] [--quality looks] [--fps 30] [--out X.mp4]
    python motion.py measure FILM.mp4 [--fps 15]                                               motion energy: still share, peak, mean
    python motion.py doctor                                                                     what is available on this machine

A composition is index.html with a root <div data-composition-id data-width data-height data-duration>, GSAP
timelines registered in window.__timelines (seconds), assets/motion-kit.js for text masks, pen strokes, rain,
vapour, camera moves, grain and vignette, and the kit's shim so the same file renders through either engine.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECTS = HERE / "projects"
KIT = HERE / "kit" / "motion-kit.js"
TEMPLATE = next((p for p in (HERE / "templates" / "composition.html", HERE.parent / "templates" / "composition.html") if p.exists()),
                HERE / "templates" / "composition.html")
GSAP = HERE / "node_modules" / "gsap" / "dist" / "gsap.min.js"
# KOSIF Studio's renderer (html_render.py, film.py): next to motion/ in the studio, or in skill 109 next to this skill
STUDIO = next((p for p in (HERE.parent, HERE.parent.parent / "pixel-studio-painter" / "scripts") if (p / "html_render.py").exists()), HERE.parent)
sys.path.insert(0, str(STUDIO))


def hf_cmd() -> list[str] | None:
    """How to run HyperFrames' CLI here: node + its bin script (the .cmd wrapper breaks on non-ASCII paths)."""
    pkg = HERE / "node_modules" / "hyperframes" / "package.json"
    if not pkg.exists():
        return None
    meta = json.loads(pkg.read_text(encoding="utf-8"))
    b = meta.get("bin")
    rel = b if isinstance(b, str) else (b or {}).get("hyperframes") or next(iter((b or {}).values()), None)
    if not rel:
        return None
    node = shutil.which("node")
    return [node, str(pkg.parent / rel)] if node else None


def _env() -> dict:
    env = dict(os.environ)
    env.setdefault("HYPERFRAMES_SKIP_SKILLS", "1")
    env.setdefault("PRODUCER_LOW_MEMORY_MODE", "1")
    return env


def project_dir(name: str) -> Path:
    p = Path(name)
    return p if p.is_dir() else PROJECTS / name


def duration_of(index: Path) -> float:
    import re
    m = re.search(r'data-composition-id="[^"]+"[^>]*data-duration="([\d.]+)"', index.read_text(encoding="utf-8"))
    return float(m.group(1)) if m else 10.0


def new(name: str, seconds: float, fps: int, size: str, title: str) -> Path:
    d = PROJECTS / name
    (d / "assets").mkdir(parents=True, exist_ok=True)
    w, h = (int(v) for v in size.lower().split("x"))
    html = TEMPLATE.read_text(encoding="utf-8")
    html = html.replace("{{TITLE}}", title or name).replace("{{W}}", str(w)).replace("{{H}}", str(h)) \
               .replace("{{SECONDS}}", str(seconds)).replace("{{FPS}}", str(fps))
    (d / "index.html").write_text(html, encoding="utf-8")
    sync_assets(d)
    print(d)
    return d


def sync_assets(d: Path):
    (d / "assets").mkdir(exist_ok=True)
    shutil.copy2(KIT, d / "assets" / "motion-kit.js")
    if GSAP.exists():
        shutil.copy2(GSAP, d / "assets" / "gsap.min.js")


def frames(name: str, times: list[float], out: Path | None) -> list[Path]:
    """Key frames through the studio's own renderer (headless Edge; window.render(t) from the kit's shim)."""
    import html_render
    d = project_dir(name)
    out = out or d / "frames"
    out.mkdir(parents=True, exist_ok=True)
    import re
    html = (d / "index.html").read_text(encoding="utf-8")
    m = re.search(r'data-width="(\d+)"[^>]*data-height="(\d+)"', html)
    w, h = (int(m.group(1)), int(m.group(2))) if m else (1920, 1080)
    files = []
    for t in times:
        f = out / f"t{t:05.2f}.png"
        html_render.render_html(d / "index.html", f, w, h, t)
        files.append(f)
        print(f)
    return files


def check(name: str) -> int:
    cmd = hf_cmd()
    if not cmd:
        print("HyperFrames is not installed here: npm install hyperframes gsap  (in motion/)")
        return 2
    r = subprocess.run([*cmd, "check", str(project_dir(name))], env=_env(), cwd=HERE)
    return r.returncode


def render(name: str, engine: str, quality: str, fps: int | None, out: Path | None) -> Path:
    d = project_dir(name)
    index = d / "index.html"
    out = out or STUDIO / "out" / f"{d.name}.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = hf_cmd()
    use_hf = engine == "hyperframes" or (engine == "auto" and cmd is not None)
    t0 = time.perf_counter()
    if use_hf:
        if not cmd:
            raise SystemExit("HyperFrames is not installed here")
        args = [*cmd, "render", str(d), "-o", str(out), "-q", quality, "--quiet"]
        if fps:
            args += ["-f", str(fps)]
        r = subprocess.run(args, env=_env(), cwd=HERE)
        if r.returncode != 0 or not out.exists():
            raise SystemExit(f"hyperframes render failed ({r.returncode})")
    else:
        import film
        film.film_animate(str(index), out, fps=fps or 30, seconds=duration_of(index), size=_size(index))
    print(json.dumps({"file": str(out), "engine": "hyperframes" if use_hf else "studio", "seconds": round(time.perf_counter() - t0, 1),
                      "mb": round(out.stat().st_size / 1e6, 2)}, ensure_ascii=False))
    return out


def _size(index: Path) -> tuple[int, int]:
    import re
    m = re.search(r'data-width="(\d+)"[^>]*data-height="(\d+)"', index.read_text(encoding="utf-8"))
    return (int(m.group(1)), int(m.group(2))) if m else (1920, 1080)


def measure(film_path: Path, fps: int = 15) -> dict:
    """Motion energy frame by frame (mean |difference| between consecutive frames at 320 px): the share of
    near-still frames, the peak, the mean, and the longest freeze. The motion-director floor: little stillness,
    no single huge jump, something always moving."""
    import numpy as np
    from PIL import Image
    tmp = Path(tempfile.mkdtemp(prefix="kosif_me_"))
    subprocess.run(["ffmpeg", "-v", "error", "-i", str(film_path), "-vf", f"fps={fps},scale=320:-2", str(tmp / "f_%05d.png")], check=True)
    files = sorted(tmp.glob("f_*.png"))
    prev, energy = None, []
    for f in files:
        a = np.asarray(Image.open(f).convert("L")).astype(np.float32)
        if prev is not None:
            energy.append(float(np.abs(a - prev).mean()))
        prev = a
    shutil.rmtree(tmp, ignore_errors=True)
    e = np.array(energy)
    still = e < 0.6
    longest, run = 0, 0
    for s in still:
        run = run + 1 if s else 0
        longest = max(longest, run)
    rep = {"frames": len(files), "fps": fps, "mean": round(float(e.mean()), 2), "peak": round(float(e.max()), 2),
           "near_still_share": round(float(still.mean()), 3), "longest_freeze_s": round(longest / fps, 2),
           "above_2_share": round(float((e > 2).mean()), 3)}
    print(json.dumps(rep, ensure_ascii=False))
    return rep


def doctor():
    cmd = hf_cmd()
    print("hyperframes:", " ".join(cmd) if cmd else "not installed (npm install hyperframes gsap in motion/)")
    print("gsap:", GSAP if GSAP.exists() else "missing")
    print("ffmpeg:", shutil.which("ffmpeg") or "missing")
    try:
        import html_render
        print("browser:", html_render.browser_path())
    except Exception as e:
        print("browser:", e)
    if cmd:
        subprocess.run([*cmd, "doctor"], env=_env(), cwd=HERE)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new"); p.add_argument("name"); p.add_argument("--seconds", type=float, default=8); p.add_argument("--fps", type=int, default=30)
    p.add_argument("--size", default="1920x1080"); p.add_argument("--title", default="")
    p = sub.add_parser("frames"); p.add_argument("project"); p.add_argument("--times", default="0.5,2,4,6,8"); p.add_argument("--out")
    p = sub.add_parser("check"); p.add_argument("project")
    p = sub.add_parser("render"); p.add_argument("project"); p.add_argument("--engine", default="auto", choices=["auto", "hyperframes", "studio"])
    p.add_argument("--quality", default="looks"); p.add_argument("--fps", type=int); p.add_argument("--out")
    p = sub.add_parser("measure"); p.add_argument("film"); p.add_argument("--fps", type=int, default=15)
    sub.add_parser("doctor")
    p = sub.add_parser("sync"); p.add_argument("project")
    a = ap.parse_args()
    if a.cmd == "new":
        new(a.name, a.seconds, a.fps, a.size, a.title)
    elif a.cmd == "frames":
        frames(a.project, [float(v) for v in a.times.split(",")], Path(a.out) if a.out else None)
    elif a.cmd == "check":
        sys.exit(check(a.project))
    elif a.cmd == "render":
        render(a.project, a.engine, a.quality, a.fps, Path(a.out) if a.out else None)
    elif a.cmd == "measure":
        measure(Path(a.film), a.fps)
    elif a.cmd == "doctor":
        doctor()
    elif a.cmd == "sync":
        sync_assets(project_dir(a.project))


if __name__ == "__main__":
    main()
