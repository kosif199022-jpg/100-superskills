"""What can this machine do? Run first, then pick the route the report names.

    python scripts/env_check.py            JSON + a short Arabic summary

Checks: Python libraries, FFmpeg (or the imageio-ffmpeg wheel), a Chromium-family browser or Playwright's own Chromium
(frame capture), Node/npm (bundling, HyperFrames), faster-whisper and cached models (transcription), the OS (Windows
voices, Direct3D GPU). Routes:
  A  full studio   — browser capture + FFmpeg: render MP4 films (2D, 3D, canvas), montage, reel, decaption, QA.
  B  footage only  — FFmpeg but no browser: montage, grade, captions, decaption, reel (if whisper), QA; films as HTML.
  C  preview only  — no FFmpeg: write the composition HTML (it plays itself with a play bar), score/WAV, references.
"""
from __future__ import annotations

import importlib
import json
import os
import platform
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def _mod(name: str) -> bool:
    try:
        importlib.import_module(name)
        return True
    except Exception:
        return False


def ffmpeg_path() -> str | None:
    p = shutil.which("ffmpeg")
    if p:
        return p
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def browser() -> str | None:
    try:
        import html_render
        b = html_render.browser_path()
        return b or ("playwright-chromium" if _mod("playwright") else None)
    except Exception:
        return None


def whisper_models() -> list[str]:
    hub = Path.home() / ".cache" / "huggingface" / "hub"
    return sorted(p.name.replace("models--Systran--faster-whisper-", "") for p in hub.glob("models--Systran--faster-whisper-*")) if hub.exists() else []


def check() -> dict:
    libs = {m: _mod(m) for m in ("numpy", "PIL", "cv2", "scipy", "playwright", "faster_whisper")}
    ff = ffmpeg_path()
    br = browser() if libs["playwright"] or os.name == "nt" else browser()
    node = shutil.which("node")
    rep = {
        "os": platform.system(), "python": platform.python_version(), "libs": libs, "ffmpeg": ff, "browser": br,
        "node": node, "npm_kit": (HERE / "node_modules" / "three").exists(), "k3_bundle": (HERE / "kit" / "three-kit.bundle.js").exists(),
        "whisper_models": whisper_models(), "windows_voices": platform.system() == "Windows",
    }
    can_render = bool(ff and br and libs["playwright"] and libs["numpy"] and libs["PIL"])
    rep["route"] = "A" if can_render else ("B" if ff and libs["numpy"] and libs["cv2"] else "C")
    rep["can"] = {
        "render_films": can_render,
        "montage_grade_captions": bool(ff),
        "decaption": bool(ff and libs["cv2"] and libs["numpy"]),
        "transcribe": libs["faster_whisper"],
        "reel": bool(ff and libs["cv2"] and libs["faster_whisper"]),
        "score_wav": libs["numpy"],
        "voice_arabic_offline": rep["windows_voices"],
        "preview_html": True,
    }
    return rep


def main():
    r = check()
    print(json.dumps(r, ensure_ascii=False, indent=1))
    names = {"A": "A — استوديو كامل: تصيير أفلام MP4 ومونتاج وفحص", "B": "B — فيديو حقيقي فقط: مونتاج وتلوين وترجمة وإزالة ترجمة؛ الأفلام كـ HTML",
             "C": "C — معاينة فقط: تركيب HTML يشتغل بزر تشغيل + موسيقى WAV"}
    print("\nالمسار المتاح هنا:", names[r["route"]])
    missing = [k for k, v in r["can"].items() if not v]
    if missing:
        print("غير متاح:", "، ".join(missing))


if __name__ == "__main__":
    main()
