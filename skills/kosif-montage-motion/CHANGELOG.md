# KOSIF Montage & Motion — changelog

## v5.0 — 2026-10-08 — one skill: v4 + Pro 1.3 + direct + verse

Two branches had grown from v3.4/v1.1 side by side; v5 joins them and adds two automatic directors.

### Merged
- **Rendering:** v4's parallel studio renderer (frame ranges on N browsers, lossless concat, CDP `optimizeForSpeed`,
  drafts, fingerprint cache, GPU process off for DOM pages) with Pro's worker policy (≥ 20 frames per page, ≤ 6 pages,
  one page per 2 cores on software WebGL, `KOSIF_WORKERS`) and Pro's undecoded PNG pipe to FFmpeg.
- **Kits:** v4 `motion-kit` (shake, parallax, glitch, stagger, lowerThird, the self-playing preview) · v4 `lab-kit`
  (`new --lab`) · Pro `shape-kit` (`window.K3S`, SDF characters) copied into every 3D project · Pro `three-kit` with
  `K3.POST`, bundle rebuilt (`kmotion kit-bundle`) · Cairo / Space Grotesk / JetBrains Mono (OFL) in `kit/fonts`.
- **Tools:** v4 `tools.py` (silence, aspect, export, thumb, trim, concat, loop, stabilize, probe, batch, fonts) ·
  Structural Twin v0.2 (2D + 3D) · `proplan` · `twinview` · two-pass loudness in the mux · Playwright-cache and
  `KOSIF_BROWSER` discovery · esbuild's native Linux binary.
- `kmotion sync` restores every kit a page names (examples ship without kit copies).
- `frames` retries a stalled grab (seek again, back off) instead of failing a long review.

### New: `direct` — the auto-directed edit of a talking clip
Subject per shot → camera pushes and punches on it; face → keyword → caption stack (type never on the mouth); one
keyword per sentence by end-focus + stress + theme words (fillers and refrains never); a number → a clock ring on its
repetition; a cut → the word at the cut becomes the transition plane; the payoff by rhetoric (the first full sentence
after a refrain's last repetition); the clip's own music bed kept when the quiet floor shows one. Everything in
`edit.json`; `--fix` corrects the transcript and keeps the timing.

### New: `verse` — a film of words from sound alone
Song, poem, dua or voice-over → aligned true text (diacritics/hamza/ASR misspellings) or Whisper times or an honest
*estimated* timing; lines by dynamic programming over phrase breaks; sections at pauses or by time; keywords that earn
it; the refrain's last return (or the closing argument) as the payoff; light driven by the track (kicks, onsets,
loudness); optional pictures with the type kept off faces. Measured on a 24.8 s dua: 743 frames, 6 browsers, 308 s,
gate ok at −14.0 LUFS / −1.0 dBTP.

### Fixed in the merge
- `reel.has_music_bed`: pauses that are digitally silent mean *no bed* (the merged floor fallback had ignored them
  and heard a bed in a dry voice).
- Filler list (`direct.STOP`) extended with colloquial Egyptian fillers (بالنسبة، عبارة، حوالي، قال لي، حاجة …).

## v4.0 (2026-10-08) — faster, wider

Measured on a 2-core Linux sandbox, the flat demo composition, 1280×720, 6 s (180 frames):

| render | v3.4 | v4.0 |
|---|---|---|
| master, 1 browser | 96 s | 34 s (CDP `optimizeForSpeed` capture, OpenCV decode, GPU process off for DOM pages) |
| master, 2 browsers | — | 22 s (`--workers`, frame ranges rendered side by side, lossless concat) |
| draft (`preview`) | — | 11 s (half size, 15 fps, ultrafast, JPEG grab) |
| unchanged re-render | 96 s | 0.05 s (fingerprint cache; `--force` to redo) |

Frames of the 1- and 2-worker masters differ by < 0.3/255 mean (codec noise): parallel rendering is deterministic.

### Rendering
- `film.film_animate`: `workers` (0 = one per core, ≤ 4), `capture` png|jpeg, `preset`, `crf`; segments concatenated with `-c copy`.
- Screenshots through Chrome DevTools `Page.captureScreenshot` with `optimizeForSpeed` (lossless PNG at ~half the time).
- `html_render.page_flags`: `--disable-gpu` for pages that never mention WebGL/three (2× faster capture); `KOSIF_GPU=0|1` overrides.
- `motion.render`: `--draft`, `--workers`, `--force`, `--capture`, `--preset`, `--crf`; `motion.preview`.
- A page that throws before `window.__ready` fails in seconds with the error instead of waiting out the 600 s budget.
- `project_dir` accepts a path, `projects/NAME` or a bare name wherever projects live.
- `measure` streams frames (no temp PNGs).

### New tools (`scripts/tools.py`, all behind `kmotion`)
`silence` (jump-cut pauses, picture+sound in one pass) · `aspect` (smart face/motion-centred crop, centre crop, blurred pad) ·
`trim` · `concat` (sizes/rates unified, silent clips padded) · `loop` (tail dissolves into head) · `stabilize` (vidstab or deshake) ·
`export` (all aspects + poster + GIF/WebP, in parallel) · `thumb` (poster with shaped, ordered Arabic title) · `probe` · `batch` · `fonts`.

### Footage pipeline
- `reel`: transcription and decaption run concurrently; the intermediate plate is fast/near-lossless; captions and the credit line
  burn in a single encode (one generation fewer, minutes faster); cross-platform credit font.
- `transcribe`: `--model auto` (best cached model), batched decoding on faster-whisper ≥ 1.1 (3-4× on CPU), `cpu_threads` = cores,
  VAD filter, openai-whisper fallback.

### Motion kit v4 (`scripts/kit/motion-kit.js`)
`shake`, `parallax`, `glitch`, `stagger`, `lowerThird` — seeded, deterministic, Arabic-safe. Run `kmotion sync PROJECT` on old projects.

### Lab kit (`scripts/kit/lab-kit.js`, `kmotion new NAME --lab`, template `templates/lab/`)
Shell fur, glossy eyes, procedural rabbit and lion with named joints, schematic modes (wire ↔ plush, exploded, joint
rings), `orbitWalk` with holds, a cream studio with a three-light rig and contact shadow, an instrument-panel HUD with
callouts projected from 3D and t-driven charts, `labPost`, `idle`. Drafts: `window.__draftScale` shrinks the GL buffers.
Example film: `scripts/projects/lab_rabbit_lion` (أرنب وأسد, 20 s).

### Merged from the v1.2 Structural edition
`structural_twin.py` (2D pin-jointed truss: SHAPE/JOINT/LOAD/BREAK/SWAP/RANK), `twin_dashboard.py`, `proplan.py`,
`references/STRUCTURAL_TWIN.md`, `references/KOSIF_SEE_INTEGRATION.md`, `examples/`, `tests/` (18 offline tests),
`reel --transcript` (a reel from a pre-timed words.json without Whisper), the credit line via a text file.

### Drafts
`render --draft` / `preview` now keep the composition's own layout (CSS zoom) and shrink the GL buffers; frames are
the composition at half the pixels, never a crop.

### Environment
`env_check` reports CPU count, parallel workers, vidstab, the Arabic font found, openai-whisper and reshaper/bidi availability.

---
## The Pro branch (merged into v5)

### 1.3.0 — 2026-10-08 — faster, 3D shapes, 3D structural twin
- Parallel studio renderer: contiguous chunks on N browser pages → per-chunk H.264 segments → lossless concat;
  CDP optimizeForSpeed capture piped to FFmpeg without decoding; `--workers`, `--capture`, `--preset`.
- New `kit/shape-kit.js` (window.K3S): SDF sculpting (smooth union / carve / intersect / paint), coarse-to-fine
  surface-nets mesher with surface projection, plush/gloss materials, eyes, tubes, stage disc, lite post stack,
  3D truss overlay, rigged `bunny()`. `references/shape-kit.md` documents the API and the cute-character recipe.
- `three-kit` exports `POST` (EffectComposer and passes); `kmotion kit-bundle` rebuilds the bundle; esbuild's
  native Linux binary is now run directly (bundling failed on Linux before).
- Structural Twin v0.2: 3D space trusses (x/y/z), NumPy solve with eigenvalue singularity gate, 400 nodes / 1600
  members; 2D behaviour and all earlier tests unchanged.
- Fixes: browser discovery in Playwright caches (route C → A on cloud sandboxes); two-pass loudness in the mux
  (−12.1 → −14.5 LUFS on a 5 s film); `kmotion` now prints a command's error message instead of exiting silently.
- Fonts: Cairo (Arabic), Space Grotesk, JetBrains Mono (OFL) in `kit/fonts/` for offline Arabic HUDs.
- Example film `projects/bunny_twin` (5 s, 1080×1920) and tests: space truss (5), shape kit (4), fast render (2).

### 1.1.0 — 2026-10-08
- Added ProPlan preflight, deterministic 5-shot beat timeline, Arabic typography and mobile-safe-area gates.
- Added honest/locked Full Pro transport boundary and bounded nine-pack Atlas method selection.
- Added `reel --transcript` timing-validated fallback independent of Whisper installation.
- Fixed credit-overlay Windows font-only path and unsafe FFmpeg inline user text.
- Added unit regression tests, environment capability extension and integration documentation.
- Preserved the source scripts, kits, examples and original project layout.

### Structural Twin v0.1 (2026-10-08)
- Inspired by user-provided schematic-motion clip (concept; vendor attribution not validated).
- Implemented deterministic 2D linear elastic pin-jointed truss solver, reactions, axial stress and utilization ranking.
- Added hypothetical break/removal sequence, swap-and-recompute, strict JSON validation and offline HUD viewer.
- Added physics-specific six-beat shotplan routing without replacing general animation or image prompts.
- Added regression tests for equilibrium, hand calculation, singularity, NaN, parameter allowlist, swapping, browser behavior and output contract.
