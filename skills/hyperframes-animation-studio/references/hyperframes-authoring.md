# HyperFrames authoring, as the renderer actually checks it (v0.8.139, measured here)

HyperFrames (heygen-com/hyperframes, Apache-2.0) turns one HTML file into a deterministic MP4: Puppeteer seeks the
page frame by frame, FFmpeg encodes. KOSIF Motion writes that HTML and renders it through HyperFrames' CLI when it
is installed in `motion/` (`npm install hyperframes gsap`), or through KOSIF Studio's own renderer (Playwright/Edge,
`window.render(t)`) — the kit's `shim` makes the same file work for both.

## The contract

```html
<html lang="ar">                                  <!-- never dir="rtl" on <html>: HyperFrames renders that blank -->
<script src="assets/gsap.min.js"></script>        <!-- local copy from node_modules/gsap; no CDN at render time -->
<script src="assets/motion-kit.js"></script>
<div id="root" data-composition-id="root" data-width="1920" data-height="1080" data-start="0" data-duration="17" data-fps="30">
  <audio id="ambience" src="assets/ambience.wav" data-start="0" data-duration="17" data-volume="0.9" data-fade-out="1"></audio>
  ...
  <script>
    const tl = gsap.timeline({ paused: true });    // paused: the runtime seeks it
    tl.to("#x", { x: 100, duration: 1 }, 2.5);      // the 3rd argument is the absolute time in seconds
    window.__timelines = window.__timelines || {};  // written literally: the linter looks for these two lines
    window.__timelines["root"] = tl;
    MOTION.shim("root", 17);                         // KOSIF Studio's renderer: window.render(t) + window.__ready
  </script>
</div>
```

- `data-start` / `data-duration` are **seconds**; `data-track-index` is only a Studio lane.
- Timed elements get `class="clip"` (the runtime keys visibility off `data-start`).
- Media needs an **`id`** (`<audio id=…>`), or it is silent in renders; `data-volume`, `data-fade-in/out`,
  `data-media-start` trim.
- Nested compositions: `<div data-composition-id="intro" data-composition-src="compositions/intro.html" data-start data-duration>`.
- Variables: `data-composition-variables` (schema on `<html>`), `--variables '{...}'` at render time,
  `window.__hyperframes.getVariables()` inside.
- Fonts: system fonts that the renderer auto-resolves (Segoe UI, Tahoma, Arial…) or an explicit `@font-face`
  (`src: local('…')` is enough for an OS font). Unknown family names fail lint.
- Seekable only: GSAP tweens, CSS animations (the runtime seeks `document.getAnimations()`), Lottie, Three.js via
  adapters. No `setTimeout`, no `requestAnimationFrame` state, no `Math.random` (use `MOTION.rng(seed)`).
- GSAP `fromTo` renders its *from* state immediately: never put `opacity: 1` in a from-state of something that must
  stay hidden until later (the kit's `drawPath` uses `set` + `immediateRender: false`).
- `marker-end` arrowheads show as soon as the path is visible; draw heads as separate shapes that land when the
  stroke arrives (`drawPath(..., { head })`).

## CLI (run from `motion/`; `motion.py` wraps these)

```bash
npx hyperframes check projects/x        # lint + runtime validation + layout/motion/contrast samples; fix every ✗
npx hyperframes snapshot projects/x     # key frames as PNG
npx hyperframes render projects/x -o out/x.mp4 -q looks -f 30      # draft | looks (CRF 16) | delivery
npx hyperframes render projects/x --resolution 4k                   # integer DPR upscale of the same composition
npx hyperframes doctor                  # Chrome headless shell (cached under ~/.cache/puppeteer), FFmpeg, memory
```

Environment: `HYPERFRAMES_SKIP_SKILLS=1` (no GitHub check at init), `PRODUCER_LOW_MEMORY_MODE=1` on an 8 GB machine
(one worker, screenshot capture), `PUPPETEER_EXECUTABLE_PATH` to use another Chrome. The npm `.cmd` wrappers break
on non-ASCII user paths: `motion.py` calls `node node_modules/hyperframes/bin/...` directly.

## What the checker enforced on the first real composition

| Finding | Fix |
|---|---|
| `missing_timeline_registry` although `MOTION.register` registered it | write the two `window.__timelines` lines literally |
| `media_missing_id` | `<audio id="ambience">` |
| `html_dir_attribute_breaks_render` | remove `dir="rtl"` from `<html>`, set `direction: rtl; unicode-bidi: isolate` on the text elements |
| `font_family_without_font_face` for Noto names | keep Segoe UI / Tahoma, or add `@font-face { src: local(...) }` |

## KOSIF Motion kit (assets/motion-kit.js)

`MOTION.ease` (slam / snap / drive / settle), `rng(seed)`, `svgEl`, `revealWords` / `hideWords` (word masks,
Arabic-safe), `drawPath` (pen stroke, optional arrowhead) / `flowDash` (moving current), `rain`, `vapour`,
`sparkle` (seeded), `camera` (the stage as one object), `flash`, `grain` (stepped, seekable), `vignette`,
`register`, `shim`. `motion.py new` scaffolds a project with the kit and GSAP copied in; `frames` renders key
frames for the 8-second gate; `check` runs HyperFrames' gate; `render` picks the engine; `measure` reports motion
energy (near-still share, peak, mean, longest freeze); `ambience.py` synthesises a deterministic soundtrack.

## Cinematic 3D compositions (Three.js) — the realism path

- Write the scene as an ES module (`src/main.js`) importing `three` and its `examples/jsm` addons; `motion.py bundle`
  turns it into one classic script (`assets/main.bundle.js`) that loads from file:// in any renderer.
- Everything is a function of `t`: sun elevation/azimuth, sea `time`, cloud cover, particle phases, camera keys.
  `composer.render(0)` with `FilmPass.uniforms.time = t`; no `Clock`, no `Math.random` (seeded Perlin / mulberry32).
- Building blocks that read as real: `Sky` (Preetham) + `ACESFilmicToneMapping` exposure; `Water` with a generated
  normal map (reflects the sky, sun glitter); terrain from seeded ridged FBM with slope/height vertex colours, shadows
  from the sun light; a raymarched cloud slab (36 steps, 3 light taps) on a box mesh; `Points` with seeded phases for
  vapour and rain (size capped, faded near the lens); `EffectComposer`: bloom (0.22 / 0.6 / 0.9), `BokehPass`
  (aperture 4e-5, maxblur 0.0035), grade + vignette ShaderPass, `FilmPass(0.16)`, `OutputPass`.
- Lighting lessons: a sun in front of the lens only at sunrise, then swing it to a side key; a camera-side fill light
  (no shadows) for valleys; keep exposure ≈ 0.5–0.62 and bloom threshold ≥ 0.9 or the frame whites out; lightning as
  a 2-frame spike of light + exposure, not a full-frame flash.
- GPU: `html_render.GPU_FLAGS` uses `--use-angle=d3d11`; `HTML_RENDER_SOFTWARE=1` forces SwiftShader. This machine:
  ~1.0–1.5 s per 1080p frame including the screenshot (≈ 10 min for 17 s at 30 fps).
- HyperFrames' own runtime drives GSAP/CSS, not a custom WebGL render loop; render 3D compositions with the studio
  engine (`motion.py render --engine studio`), which also muxes the `<audio>` clips.
