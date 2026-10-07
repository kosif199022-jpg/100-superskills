"""Film: the studio's drawing as a video, and time-based pictures as video. Frames go straight to FFmpeg.

    python film.py drawing <scene|code file> --out out/x.mp4 [--fps 30] [--speed normal]   the picture forming pixel by pixel
    python film.py animate <page.html|scene.py> --out out/x.mp4 [--fps 30] [--seconds 6]    render(t) / build(t) frames

Idea from HyperFrames (heygen-com/hyperframes): deterministic frames from a seekable source, encoded by FFmpeg.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE / "scenes")]
import render as R  # noqa: E402

PAPER = "#f3eee4"
SPEEDS = {"slow": 5.0, "normal": 1.8, "fast": 0.55}


def ffmpeg() -> str:
    f = shutil.which("ffmpeg")
    if not f:
        raise RuntimeError("ffmpeg is not on PATH")
    return f


class Encoder:
    def __init__(self, out: Path, w: int, h: int, fps: int):
        out.parent.mkdir(parents=True, exist_ok=True)
        self.p = subprocess.Popen([ffmpeg(), "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                                   "-r", str(fps), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
                                   "-movflags", "+faststart", str(out)], stdin=subprocess.PIPE)
        self.n = 0

    def frame(self, rgb: np.ndarray):
        self.p.stdin.write(np.ascontiguousarray(rgb).tobytes())
        self.n += 1

    def close(self):
        self.p.stdin.close()
        self.p.wait()


def drawing_jobs(source: str):
    """Paint jobs for a scene name or a code file, exactly as the studio plays them."""
    import studio
    src = Path(source)
    if src.suffix.lower() in studio.IMAGE_TYPES and src.exists():         # an image: its own code, drawn exactly
        work = Path(tempfile.mkdtemp(prefix="kosif_film_img_"))
        src = work / f"{src.stem}_code.py"
        src.write_text(studio.image_code(Path(source), Path(source).stem), encoding="utf-8")
    if src.suffix.lower() in (".py", ".svg", ".html", ".htm", ".txt") and src.exists():
        work = Path(tempfile.mkdtemp(prefix="kosif_film_"))
        subprocess.run([sys.executable, str(HERE / "runner.py"), str(src), str(work)], capture_output=True, timeout=900)
        if (work / "error.txt").exists():
            raise RuntimeError((work / "error.txt").read_text(encoding="utf-8")[-800:])
        canvas = json.loads((work / "canvas.json").read_text(encoding="utf-8")) if (work / "canvas.json").exists() else None
        jobs = []
        for i in range(10000):
            f = work / f"job_{i:04d}.npz"
            if not f.exists():
                break
            meta = json.loads((work / f"job_{i:04d}.json").read_text(encoding="utf-8"))
            with np.load(f) as z:
                jobs.append((meta, z["order"], z["cols"]))
        shutil.rmtree(work, ignore_errors=True)
        return canvas, jobs
    title, steps, rolloff = studio.load(source)
    jobs, prev = [], None
    for i, st, img in R.render(steps, 1.0, ss=3, paper=PAPER, rolloff=rolloff):
        flat = img.reshape(-1, 3)
        if prev is None:
            prev = np.empty_like(flat)
            prev[:] = (R.rgb(PAPER) * 255 + .5).astype(np.uint8)
        idx = np.flatnonzero(np.any(flat != prev, axis=1)).astype(np.int32)
        order = R.reveal_order(idx, img.shape[1], st, 1.0, seed=i)
        jobs.append(({"label": st.label, "weight": st.weight}, order, flat[order].copy()))
        prev = flat.copy()
    return None, jobs


def film_drawing(source: str, out: Path, fps: int = 30, speed: str = "normal", hold: float = 1.5) -> dict:
    canvas, jobs = drawing_jobs(source)
    if canvas:
        w, h = canvas["w"], canvas["h"]
        # fit the native canvas into a 16:9 frame the way the studio shows it
        fw, fh = 1280, 720
        f = min(fw / w, fh / h)
        dw, dh = max(2, round(w * f) // 2 * 2), max(2, round(h * f) // 2 * 2)
        native = np.zeros((w * h, 4), np.uint8)
    else:
        w, h = R.W0, R.H0
        fw, fh, dw, dh = 1200, 800, 1200, 800
        flat = np.empty((w * h, 3), np.uint8)
        flat[:] = (R.rgb(PAPER) * 255 + .5).astype(np.uint8)
    enc = Encoder(out, fw, fh, fps)
    k = SPEEDS.get(speed, 1.8)
    t = time.perf_counter()
    import cv2

    def frame():
        if canvas:
            a = native[:, 3:4].astype(np.float32) / 255
            rgb = (native[:, :3] * a + (R.rgb(PAPER) * 255) * (1 - a) + .5).astype(np.uint8).reshape(h, w, 3)
            view = cv2.resize(rgb, (dw, dh), interpolation=cv2.INTER_AREA if f < 1 else cv2.INTER_NEAREST)
            fr = np.full((fh, fw, 3), 27, np.uint8)
            fr[(fh - dh) // 2:(fh - dh) // 2 + dh, (fw - dw) // 2:(fw - dw) // 2 + dw] = view
            return fr
        return flat.reshape(h, w, 3)
    for meta, order, cols in jobs:
        n = len(order)
        dur = k * float(meta.get("weight", .5)) * (n / (w * h)) ** .5
        frames = max(1, int(round(dur * fps)))
        for j in range(1, frames + 1):
            a, b = int(n * (j - 1) / frames), int(n * j / frames)
            sel = order[a:b]
            if canvas:
                c = cols[a:b]
                native[sel] = c if c.shape[1] == 4 else np.column_stack([c, np.full(len(c), 255, np.uint8)])
            else:
                flat[sel] = cols[a:b]
            enc.frame(frame())
    last = frame()
    for _ in range(int(hold * fps)):
        enc.frame(last)
    enc.close()
    return {"file": str(out), "frames": enc.n, "fps": fps, "seconds": round(enc.n / fps, 1), "encode_s": round(time.perf_counter() - t, 1)}


def film_animate(source: str, out: Path, fps: int = 30, seconds: float | None = None, size=(1280, 720), blur: int = 1,
                 shutter: float = 0.5) -> dict:
    """blur = sub-frames per output frame for pages that implement it (window.__blur / __shutter / __fps): a real
    shutter smear, k times the render cost."""
    src = Path(source)
    t0 = time.perf_counter()
    if src.suffix.lower() in (".html", ".htm"):
        import html_render
        from playwright.sync_api import sync_playwright
        w, h = size
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=html_render.browser_path(), headless=True, args=html_render.GPU_FLAGS[2:])
            pg = browser.new_context(viewport={"width": w, "height": h}).new_page()
            pg.goto(src.resolve().as_uri(), wait_until="load", timeout=120000)
            pg.wait_for_function("window.__ready === true", timeout=120000)
            pg.evaluate("([k, s, f]) => { window.__blur = k; window.__shutter = s; window.__fps = f; }", [int(blur), float(shutter), int(fps)])
            dur = seconds or pg.evaluate("window.__duration || 4")
            enc = Encoder(out, w, h, fps)
            n = int(dur * fps)
            for i in range(n):
                pg.evaluate("t => { window.__ready = false; window.render(t); }", i / fps)
                pg.wait_for_function("window.__ready === true", timeout=60000)
                png = pg.screenshot(type="png")
                import io
                enc.frame(np.asarray(Image.open(io.BytesIO(png)).convert("RGB")))
            enc.close()
            browser.close()
        return {"file": str(out), "frames": n, "fps": fps, "seconds": dur, "encode_s": round(time.perf_counter() - t0, 1)}
    import importlib
    mod = importlib.import_module(src.stem)
    if not hasattr(mod, "build_t"):
        raise RuntimeError("a scene animates when it defines build_t(t) -> steps")
    dur = seconds or getattr(mod, "DURATION", 4.0)
    w, h = R.W0, R.H0
    enc = Encoder(out, w, h, fps)
    n = int(dur * fps)
    for i in range(n):
        enc.frame(np.asarray(R.render_image(mod.build_t(i / fps), 1.0, rolloff=getattr(mod, "ROLLOFF", .82))))
    enc.close()
    return {"file": str(out), "frames": n, "fps": fps, "seconds": dur, "encode_s": round(time.perf_counter() - t0, 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["drawing", "animate"])
    ap.add_argument("source")
    ap.add_argument("--out", required=True)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--speed", default="normal")
    ap.add_argument("--seconds", type=float)
    a = ap.parse_args()
    if a.mode == "drawing":
        print(json.dumps(film_drawing(a.source, Path(a.out), a.fps, a.speed), ensure_ascii=False))
    else:
        print(json.dumps(film_animate(a.source, Path(a.out), a.fps, a.seconds), ensure_ascii=False))


if __name__ == "__main__":
    main()
