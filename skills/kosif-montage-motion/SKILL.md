---
name: kosif-montage-motion
description: "KOSIF Montage & Motion — مونتاج وموشن احترافي من طلب واحد: أنيميشن مسطّح أو ثلاثي الأبعاد واقعي (Three.js)، موشن غرافيك ونص عربي حركي، مونتاج أي فيديو (قص على الإيقاع، زووم نبضي، تلوين، ترجمة كاريوكي عربية، تخفيض الموسيقى تحت الصوت، −14 LUFS)، مونتاج تلقائي كامل لمقطع متكلم (reel)، تفريغ الكلام، إزالة الترجمة المحروقة، موسيقى أصلية وتعليق صوتي، وبوابة جودة قبل التسليم. Use for: animation, motion graphics, 3D animation, video montage, reel, short, TikTok, edit this video, captions, subtitles, color grade, remove burned subtitles, transcribe, beat sync, showreel, explainer, kinetic typography. Arabic: انميشن، أنيميشن، موشن، موشن غرافيك، مونتاج، فيديو، ريلز، قص على الإيقاع، ترجمة فيديو، سبتايتل، تلوين فيديو، إزالة الترجمة، تفريغ فيديو، فيلم قصير، شوريل، شرح متحرك."
---

# KOSIF Montage & Motion — استوديو المونتاج والموشن

One skill for every moving-picture job: films made from code (2D, 3D, canvas), edits of real footage, sound, and the
quality gate. Everything is deterministic (each frame is a function of time), measured (beats, loudness, speed,
exposure) and rendered locally. Built from KOSIF Motion v3.4, the Ultra Motion & Montage skill and KOSIF Omni's
cinema, video, audio, lighting and vision skills.

## 0. First: what can this machine do?
```bash
python scripts/env_check.py
```
- **Route A** (browser + FFmpeg): render MP4 films, edit footage, everything below.
- **Route B** (FFmpeg, no browser): edit footage (montage, grade, captions, decaption, reel); films are delivered as a
  self-playing HTML composition.
- **Route C** (no FFmpeg — e.g. a locked-down sandbox): write the composition HTML (it plays itself with a play bar,
  audio in sync), synthesise the music WAV, and give the exact commands to render on a full machine.
- The skill folder may be read-only (claude.ai): `export KOSIF_MOTION_HOME=$PWD` (or a writable folder) before creating
  projects; put deliverables where the environment lets the user download them (on claude.ai: `/mnt/user-data/outputs`).
- Never claim a render you did not run. If a step is unavailable, say which and deliver the strongest artifact possible.

All tools sit behind one entry: `python scripts/kmotion.py help` (or run with no arguments for the Arabic menu).

## 1. Classify the request
| The user wants | Do |
|---|---|
| An animation / motion piece / explainer / showreel from an idea | §2 Film from code |
| Their own video edited ("مونتاج", "ريلز", captions, colour) | §3 Footage |
| Burned-in subtitles removed / a transcript / an SRT | `decaption` / `transcribe` (§3) |
| Music, ambience, narration | §4 Sound |
| Prompts for Veo / Sora / Kling / Runway | `references/ai_video_models.md` + `references/seven-layer-anatomy.md` (write prompts; generate only if asked and a tool exists) |

## 2. Film from code
**Direction before effects** (`references/motion-craft.md`, `craft-numbers.md`): audience, feeling, duration, aspect →
2–3 genuinely different directions → pick one → a shot list with times (4–7 beats, one carried device, named camera
moves) → a motion score (what moves, from where, how long, which ease). Story arc for short pieces: hook (frame 0
composed and moving) → development → pressure → lift → payoff → deliberate end.

```bash
python scripts/kmotion.py new NAME --seconds 10                 # flat: HTML + GSAP + motion-kit
python scripts/kmotion.py new NAME --3d --seconds 10            # 3D: src/main.js on the three-kit (runs on window.K3 without npm)
python scripts/kmotion.py new NAME --canvas --seconds 10        # canvas: one page, window.seek(t)
python scripts/kmotion.py frames projects/NAME --times 1,4,7    # the 8-second gate: look at keyframes before rendering
python scripts/kmotion.py render projects/NAME --engine studio --blur 4
python scripts/kmotion.py inspect out/NAME.mp4                  # delivery gate
```
- **Flat kit** (`scripts/kit/motion-kit.js`, `window.MOTION`): eases `E`, physical springs `SPR`/`track`, Arabic word
  masks `revealWords`/`riseWords`/`maskRise` (whole words move, letters stay joined), `typeOn`, `counter`, `drawPath`,
  `morphPath`, camera `push`/`rackFocus`, `shim(root, seconds)`; footage via `<video data-start>`; audio via
  `<audio id data-start data-volume data-role="voice|music">` (voice ducks music in the mux, master −14 LUFS).
- **3D kit** (`scripts/kit/three-kit.js`; global `window.K3` from `three-kit.bundle.js`): renderer (tone `aces|agx|neutral`),
  sky, terrain, forest, sea, shallow water + caustics, koi, petals, pebbles, clouds, flocks, post (bloom, rays, DOF,
  grade, grain, NaN guard), GPU motion blur, `shot()`/`shotFromWords()`/`sequence()` (Veo shot vocabulary as cameras),
  `lightPreset()` (Rembrandt, clamshell, edge…), `aerialPerspective()`, `makeLookPass()` (gamut, night, split tone),
  `makeSpectrumGround()`/`makeGlitchPass()`/`MOTION.channels()` (the sound drives the picture), `makeParticleBody()`
  (real motion from `mocap`), long exposure `render --shutter 30 --stack lighten`.
- Contract and traps: `references/hyperframes-authoring.md` (no `dir=rtl` on `<html>`, literal
  `window.__timelines["root"] = tl`, `<audio>` needs an id, fonts need @font-face, seeded randomness only).
- Any composition opened in a normal browser **plays itself** (play/pause, scrub, audio in sync, fitted to the window) —
  the preview deliverable for Route C; renderers never see the player.

## 3. Footage (real video)
**Edit the meaning, not just the words.** Transcribe first; for every sentence find its meaning, emphasis and the
1–4 key words, then choose: nothing · caption · keyword typography · camera move · symbol · transition · sound accent.
The speaker stays the hero; every graphic has a reason (`references/montage_grammar.md`, `animation_craft.md`).

```bash
python scripts/kmotion.py reel CLIP.mp4 --out FINAL.mp4                     # automatic: words → decaption → restore 1080×1920 → voice → music only if none → karaoke → −14 LUFS → gate
python scripts/kmotion.py transcribe CLIP.mp4 --model large-v3              # words.json, .srt, captions.json (word times drive animation)
python scripts/kmotion.py decaption CLIP.mp4 --out CLEAN.mp4                # erase burned-in captions + a fixed credit line
python scripts/kmotion.py montage a.mp4 b.mp4 --music track.wav --out M.mp4 # beat-planned cuts, punches, grade, ducking
python scripts/kmotion.py grade CLIP.mp4 --preset restore                   # restore · teal_orange · golden_hour · blue_hour · sodium_night · cyberpunk · vintage_film …
python scripts/kmotion.py captions CLIP.mp4 --spec captions.json            # Arabic karaoke (one ASS event per word)
```
**Directed premium edit** (the strongest result; example `scripts/projects/premium_edit/index.html`):
1. Transcribe (large-v3) and cross-check against any burned captions (OCR) — the audio is the source of truth.
2. `decaption` → restore/upscale the plate (`grade restore`, Lanczos to 1080×1920) → an all-intra plate
   (`kmotion footage`) the composition seeks frame-exactly.
3. A composition over the plate: camera (push 100→108 %, punches on stressed words, a pull-back before the payoff),
   three text levels (speech caption · phrase · keyword), micro-graphics ≤ 1.5 s for examples, the cut treated as a
   chapter, the payoff alone on screen, a deliberate end (hold → dip to black).
4. Sound: clean the voice; if the clip already has a music bed keep it and add only accents; else an original
   underscore; SFX on stressed words, always under the voice.
5. Render, then the gate and a contact sheet; review with two reviewers (P0/P1/P2), fix, re-render.

## 4. Sound
`kmotion score out.wav --spec score.json` (original music on the beat grid; tape stops; risers; booms; designed SFX
from cues) · `kmotion ambience` (rain, sea, birds, brook, chords, whoosh) · `kmotion voice out.wav --text "…"`
(Arabic narration offline — Windows voices only) · `kmotion beats` / `channels` (any track → beat grid / per-frame
channels: kick, bass, onsets, silence, tape-stop). Analysis: `scripts/omni/audio_analyze.py` (LUFS, peaks, BPM).

## 5. Gates (all must pass before delivery)
1. `kmotion inspect FILM` → ok (yuv420p H.264, no unintended black/frozen stretches, −14 ± 1.5 LUFS, true peak ≤ −1,
   no blown/crushed frames); intended holds listed with `--allow a-b`.
2. Keyframes / contact sheet looked at (`kmotion sheet FILM`) — including the phone-width view; a review written.
3. Arabic: correct spelling, joined letters, RTL on text elements, words in the right order (ASS `Encoding -1`),
   descender dots visible (`background-clip:text` needs padding), max 2 lines, inside mobile safe areas
   (9:16: keep text between ~15 % and ~80 % of the height, off the right-edge UI), never over eyes or mouth.
4. Motion: no linear eases on spatial moves, no crossfades, a visible change every ~0.7–2.5 s, nothing faster than
   ~80 px/frame (`kmotion speed`), the strongest moment near the end.
5. Sound: the voice is always on top; SFX below dialogue; 48 kHz AAC.
6. Honesty: report what was measured and what was not; credit the source of footage you did not make (re-set the
   creator's handle in your typography if a watermark was removed); never fabricate or replace a real person's face.

## 6. References
`references/craft-numbers.md` (measured motion norms) · `motion-craft.md` · `motion-director.md` ·
`hyperframes-authoring.md` (contract, kit, lessons v1→v3.4) · `book-lessons.md` (Gurney colour, Grimes lighting, night
photography, Veo shot language) · `montage_grammar.md` · `animation_craft.md` · `ai_video_models.md` ·
`seven-layer-anatomy.md` + `continuity-protocols.md` (cinema prompts) · `story-conflict.md` (+ `scripts/omni/story_lint.py`)
· `lighting-presets.md` (+ `scripts/omni/light_calc.py`) · `x-trend-2026.md` (what made the Opus 5.5 motion wave work).
Examples (sources only; renders are rebuilt): `scripts/projects/` — koi_pond, sound_ground, blue_hour, showreel,
premium_edit, water_cycle_3d.
