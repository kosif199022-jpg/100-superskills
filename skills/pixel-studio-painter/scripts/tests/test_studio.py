"""KOSIF Studio tests:  python -m unittest discover -s tests   (from the kosif-studio folder)."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(HERE), str(HERE / "scenes")]
import render as R  # noqa: E402
import studio  # noqa: E402
import svg_import  # noqa: E402
import vector_scene  # noqa: E402
import vectorize  # noqa: E402


def sample_logo() -> np.ndarray:
    """A badge like a real logo: two rings, a white field, small antialiased text, a see-through outside."""
    im = Image.new("RGBA", (160, 190), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([4, 4, 155, 185], radius=60, fill=(170, 200, 55, 255))
    d.rounded_rectangle([9, 9, 150, 180], radius=56, fill=(255, 255, 255, 255))
    d.rounded_rectangle([13, 13, 146, 176], radius=52, fill=(240, 5, 12, 255))
    d.rounded_rectangle([24, 24, 135, 165], radius=44, fill=(255, 255, 255, 255))
    d.ellipse([55, 45, 105, 95], outline=(10, 10, 6, 255), width=4)
    d.rectangle([30, 120, 130, 145], fill=(240, 5, 12, 255))
    d.text((48, 125), "KOSIF 2026", fill=(255, 255, 255, 255))
    d.text((40, 100), "since", fill=(150, 150, 150, 255))
    return np.asarray(im).copy()


def px(img: Image.Image, x: float, y: float, scale: float):
    return img.getpixel((round(x * scale), round(y * scale)))


class Renderer(unittest.TestCase):
    def test_holes_cut_out(self):
        ring = [list(R.ellipse(600, 400, 200)[0]), R.Hole(R.ellipse(600, 400, 100)[0])]
        im = R.render_image([R.Step("bg", [R.fill(R.rect(0, 0, 1200, 800), "#ffffff")]),
                             R.Step("ring", [R.fill(ring, "#ff0000")])], .25, rolloff=1)
        self.assertEqual(px(im, 600, 400, .25), (255, 255, 255))
        self.assertEqual(px(im, 600, 250, .25), (255, 0, 0))

    def test_even_odd_compound(self):
        shape = R.compound(R.path("M0 0 H1200 V800 H0 Z M500 300 H700 V500 H500 Z"))
        im = R.render_image([R.Step("s", [R.fill(shape, "#0000ff")])], .25, rolloff=1)
        self.assertEqual(px(im, 600, 400, .25), (0, 0, 0))          # the hole shows the black sheet
        self.assertEqual(px(im, 100, 100, .25), (0, 0, 255))

    def test_path_arcs_and_smooth_curves_end_where_they_should(self):
        pts = R.path("M10 50 A40 40 0 0 1 90 50 S 50 100 10 50 Q30 20 50 50 T 90 50 a10 10 0 01 5 5")[0]
        self.assertAlmostEqual(pts[-1][0], 95, 3)
        self.assertAlmostEqual(pts[-1][1], 55, 3)

    def test_transparent_gradient_and_text(self):
        im = R.render_image([R.Step("bg", [R.fill(R.rect(0, 0, 1200, 800), "#000000")]),
                             R.Step("g", [R.fill(R.ellipse(600, 400, 300), R.rad((600, 400), 300,
                                                                                [(0, "#ffffffff"), (1, "#ffffff00")]))]),
                             R.Step("t", [R.text("سلام", 200, 200, 80, "#ff0000", anchor="mm")])], .5, rolloff=1)
        centre, edge = px(im, 600, 400, .5)[0], px(im, 600, 690, .5)[0]
        self.assertGreater(centre, 240)
        self.assertLess(edge, 40)
        reds = np.asarray(im)[50:150, 50:150]
        self.assertTrue(((reds[..., 0] > 200) & (reds[..., 1] < 60)).any(), "Arabic text was not drawn")

    def test_realism_primitives_change_a_flat_fill(self):
        base = [R.Step("b", [R.fill(R.ellipse(600, 400, 300, 200), "#808080")])]
        plain = np.asarray(R.render_image(base, .25, rolloff=1)).astype(int)
        for op in (R.shade(R.ellipse(600, 400, 300, 200), (200, 100), "#c0c0c0", "#202020"),
                   R.noise(R.ellipse(600, 400, 300, 200), .4, 20, 3),
                   R.scales(R.ellipse(600, 400, 300, 200), 16, "#000000", .5)):
            im = np.asarray(R.render_image(base + [R.Step("x", [op])], .25, rolloff=1)).astype(int)
            self.assertGreater(np.abs(im - plain).mean(), 1.0)
            self.assertGreater(len(np.unique(im[70:130, 100:200].reshape(-1, 3), axis=0)), 4)

    def test_reveal_order_is_a_permutation_for_every_order(self):
        idx = np.arange(0, 12000, 7, dtype=np.int32)
        for order in ("sweep", "grow", "rise", "down", "left", "right", "sparkle"):
            out = R.reveal_order(idx, 300, R.Step("x", [], order, (100, 100)), .25)
            self.assertEqual(sorted(out.tolist()), idx.tolist(), order)

    def test_highlight_rolloff_is_per_picture(self):
        steps = [R.Step("w", [R.fill(R.rect(0, 0, 1200, 800), "#ffffff")])]
        self.assertEqual(px(R.render_image(steps, .1, rolloff=1.0), 10, 10, .1), (255, 255, 255))
        self.assertLess(px(R.render_image(steps, .1), 10, 10, .1)[0], 255)


class Svg(unittest.TestCase):
    def test_basic_shapes_styles_and_transforms(self):
        svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 80">
          <style>.r{fill:#ff0000}</style>
          <rect width="120" height="80" fill="#0000ff"/>
          <g transform="translate(60 40)"><circle class="r" r="10"/></g>
          <rect x="5" y="5" width="20" height="10" rx="3" fill="rgb(0,255,0)" stroke="black" stroke-width="2"/>
        </svg>"""
        title, steps = svg_import.load_svg(svg)
        im = R.render_image(steps, .25, rolloff=1)
        self.assertEqual(px(im, 600, 400, .25), (255, 0, 0))        # the circle, moved to the centre
        self.assertEqual(px(im, 1100, 700, .25), (0, 0, 255))
        self.assertGreaterEqual(len(steps), 4)

    def test_the_example_rocket(self):
        title, steps = svg_import.load_svg((HERE / "examples" / "svg_rocket.svg").read_text(encoding="utf-8"))
        self.assertEqual(title, "صاروخ")
        R.render_image(steps, .25, rolloff=1)


class Vectorize(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_flat_logo_keeps_its_colours_and_its_hole(self):
        im = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.ellipse([10, 10, 110, 110], fill=(230, 20, 30, 255))
        d.ellipse([40, 40, 80, 80], fill=(255, 255, 255, 255))
        im.save(self.tmp / "logo.png")
        data = vectorize.trace(self.tmp / "logo.png")
        self.assertFalse(data["photo"])
        cols = {L["color"] for L in data["layers"]}
        self.assertTrue(any(c.startswith("#e6") for c in cols), cols)
        self.assertIn("#ffffff", cols)
        out = R.render_image(vector_scene.build(data), .5, rolloff=1)
        s = min(1080 / 120, 730 / 120)
        ox, oy = (1200 - 120 * s) / 2, (800 - 120 * s) / 2
        self.assertEqual(px(out, ox + 60 * s, oy + 60 * s, .5), (255, 255, 255))
        self.assertEqual(px(out, ox + 25 * s, oy + 60 * s, .5), (230, 20, 30))

    def test_noise_is_seen_as_a_photo(self):
        rng = np.random.default_rng(1)
        Image.fromarray(rng.integers(0, 255, (160, 160, 3), dtype=np.uint8)).save(self.tmp / "p.png")
        self.assertTrue(vectorize.looks_like_photo(np.asarray(Image.open(self.tmp / "p.png").convert("RGBA"))))
        data = vectorize.trace(self.tmp / "p.png", colors=6)
        self.assertEqual(len(data["layers"]) <= 6, True)


class Exact(unittest.TestCase):
    """An image redrawn from nothing must end identical to the original: every pixel, colour and transparency."""

    def check(self, rgba):
        import exact
        canvas = np.zeros_like(rgba).reshape(-1, 4)
        steps = 0
        for label, kind, origin, weight, order, cols in exact.plan(rgba):
            canvas[order] = cols
            steps += 1
        self.assertGreater(steps, 1)
        self.assertEqual(exact.mismatches(canvas.reshape(rgba.shape), rgba), 0)

    def test_a_logo_ends_identical(self):
        self.check(sample_logo())

    def test_a_photo_like_image_ends_identical(self):
        rng = np.random.default_rng(3)
        base = np.zeros((90, 120, 4), np.uint8)
        base[..., :3] = rng.integers(0, 255, (90, 120, 3), dtype=np.uint8)
        base[..., 3] = 255
        base[:10, :10, 3] = 0                                   # a see-through corner must stay see-through
        self.check(base)


class ImageToPython(unittest.TestCase):
    """📤: a standalone Pillow program that makes the image again, pixel for pixel, outside the studio."""

    def test_program_reproduces_the_image_with_plain_python(self):
        import to_python
        tmp = Path(tempfile.mkdtemp())
        Image.fromarray(sample_logo(), "RGBA").save(tmp / "logo.png")
        code = to_python.image_to_python(tmp / "logo.png", "logo")
        self.assertIn("draw.polygon(", code)
        (tmp / "logo.py").write_text(code, encoding="utf-8")
        r = subprocess.run([sys.executable, "logo.py"], cwd=tmp, capture_output=True, timeout=120)
        self.assertEqual(r.returncode, 0, r.stderr.decode("utf-8", "replace"))
        out = np.asarray(Image.open(tmp / "logo.png").convert("RGBA"))
        self.assertEqual(int(np.any(out != sample_logo(), axis=2).sum()), 0)
        import runner
        self.assertEqual(runner.kind_of(code), "python")        # a real program: it runs and is recorded
        shutil.rmtree(tmp, ignore_errors=True)


class Judge(unittest.TestCase):
    """The realism gate tells a flat cartoon from a shaded picture, measured, not guessed."""

    def test_flat_cartoon_is_revised_and_shaded_scene_passes(self):
        import judge
        tmp = Path(tempfile.mkdtemp())
        flat = Image.new("RGB", (400, 300), "#ffffff")
        d = ImageDraw.Draw(flat)
        d.rectangle([0, 150, 400, 300], fill="#4caf50")
        d.ellipse([150, 40, 250, 140], fill="#ffd54f", outline="#000000", width=4)
        d.rectangle([100, 120, 300, 220], fill="#d7a86e", outline="#000000", width=4)
        flat.save(tmp / "flat.png")
        steps = [R.Step("bg", [R.fill(R.rect(0, 0, 1200, 800), R.lin((0, 0), (0, 800), [(0, "#102030"), (1, "#405060")])),
                               R.noise(R.rect(0, 0, 1200, 800), .3, 40, 1)]),
                 R.Step("ball", [R.shade(R.ellipse(600, 400, 250, 250), (300, 200), "#d0b090", "#301808", .4),
                                 R.noise(R.ellipse(600, 400, 250, 250), .3, 12, 2), R.grain(.02)])]
        R.render_image(steps, .5).save(tmp / "shaded.png")
        mf, ms = judge.measure(tmp / "flat.png"), judge.measure(tmp / "shaded.png")
        vf, rf = judge.verdict(mf)
        shutil.rmtree(tmp, ignore_errors=True)
        self.assertEqual(vf, "REVISE", rf)
        self.assertGreater(mf["flat_share"], judge.THRESH["flat_share"])          # the cartoon is caught by its flat fills
        self.assertLess(ms["flat_share"], judge.THRESH["flat_share"])             # shading leaves no flat fill
        self.assertLess(ms["hard_edge_share"], judge.THRESH["hard_edge_share"])   # and no outline look
        self.assertLess(ms["flat_share"], mf["flat_share"] / 5)

    def test_the_whale_scene_passes_the_gate(self):
        import judge
        _, steps, rolloff = studio.load("whale_dragon")
        tmp = Path(tempfile.mkdtemp())
        R.render_image(steps, 1.0, rolloff=rolloff).save(tmp / "whale.png")
        v, reasons = judge.verdict(judge.measure(tmp / "whale.png"))
        shutil.rmtree(tmp, ignore_errors=True)
        self.assertEqual(v, "PASS", reasons)


class JevPlan(unittest.TestCase):
    """Photos: the painting plan is chosen among measured candidates (by Jev, or by the rule when Jev is off)."""

    def photo(self):
        rng = np.random.default_rng(5)
        y, x = np.mgrid[:140, :180]
        img = np.zeros((140, 180, 4), np.uint8)
        img[..., 0] = (x * 1.3 + rng.integers(0, 40, x.shape)).clip(0, 255)
        img[..., 1] = (y * 1.6 + rng.integers(0, 40, x.shape)).clip(0, 255)
        img[..., 2] = ((x + y) * .6 + rng.integers(0, 40, x.shape)).clip(0, 255)
        img[..., 3] = 255
        return img

    def test_without_jev_the_rule_chooses_and_the_result_is_still_exact(self):
        import os
        import exact
        old = os.environ.get("KOSIF_JEV_URL")
        os.environ["KOSIF_JEV_URL"] = "off"
        try:
            rgba = self.photo()
            bk, fk, info = exact.choose_plan(rgba)
        finally:
            if old is None:
                os.environ.pop("KOSIF_JEV_URL", None)
            else:
                os.environ["KOSIF_JEV_URL"] = old
        self.assertEqual(info["by"], "rule")
        self.assertIn(info["choice"], exact.PLANS)
        self.assertEqual(set(info["candidates"]), set(exact.PLANS))
        canvas = np.zeros_like(rgba).reshape(-1, 4)
        for *_, order, cols in exact.plan(rgba, bk, fk):
            canvas[order] = cols
        self.assertEqual(exact.mismatches(canvas.reshape(rgba.shape), rgba), 0)

    def test_final_touches_go_from_visible_to_invisible(self):
        import exact
        labels = [(lb, w) for lb, kind, origin, w, o, c in exact.plan(self.photo(), 6, 32) if "اللمسات" in lb]
        weights = [w for _, w in labels]
        self.assertGreaterEqual(len(labels), 2)
        self.assertEqual(weights, sorted(weights, reverse=True), labels)


class Runner(unittest.TestCase):
    """Code from any AI runs in its own process and comes back as paint jobs."""

    def run_code(self, name):
        out = Path(tempfile.mkdtemp())
        r = subprocess.run([sys.executable, str(HERE / "runner.py"), str(HERE / "examples" / name), str(out)],
                           capture_output=True, timeout=240)
        info = json.loads((out / "done.json").read_text(encoding="utf-8")) if (out / "done.json").exists() else None
        err = (out / "error.txt").read_text(encoding="utf-8") if (out / "error.txt").exists() else None
        jobs = len(list(out.glob("job_*.npz")))
        shutil.rmtree(out, ignore_errors=True)
        return r.returncode, info, err, jobs

    def test_pil_code_is_drawn_in_the_codes_own_order(self):
        rc, info, err, jobs = self.run_code("pil_house.py")
        self.assertEqual(rc, 0, err)
        self.assertEqual(info["kind"], "pil")
        self.assertGreater(jobs, 5)

    def test_raster_code_is_painted_at_its_own_size_and_matches_it(self):
        out = Path(tempfile.mkdtemp())
        subprocess.run([sys.executable, str(HERE / "runner.py"), str(HERE / "examples" / "pil_house.py"), str(out)],
                       capture_output=True, timeout=240)
        c = json.loads((out / "canvas.json").read_text(encoding="utf-8"))
        canvas = np.zeros((c["w"] * c["h"], 4), np.uint8)
        for f in sorted(out.glob("job_*.npz")):
            with np.load(f) as z:
                canvas[z["order"]] = z["cols"]
        final = np.asarray(Image.open(out / "final.png").convert("RGBA")).reshape(-1, 4)
        shutil.rmtree(out, ignore_errors=True)
        self.assertEqual((c["w"], c["h"]), (800, 600))
        self.assertEqual(int(np.any(canvas != final, axis=1).sum()), 0)

    def test_image_code_is_drawn_identical_to_the_original(self):
        tmp = Path(tempfile.mkdtemp())
        Image.fromarray(sample_logo(), "RGBA").save(tmp / "logo.png")
        (tmp / "logo_code.py").write_text(studio.image_code(tmp / "logo.png", "logo"), encoding="utf-8")
        out = tmp / "run"
        subprocess.run([sys.executable, str(HERE / "runner.py"), str(tmp / "logo_code.py"), str(out)],
                       capture_output=True, timeout=240)
        c = json.loads((out / "canvas.json").read_text(encoding="utf-8"))
        info = json.loads((out / "done.json").read_text(encoding="utf-8"))
        canvas = np.zeros((c["w"] * c["h"], 4), np.uint8)
        for f in sorted(out.glob("job_*.npz")):
            with np.load(f) as z:
                canvas[z["order"]] = z["cols"]
        original = np.asarray(Image.open(tmp / "logo.png").convert("RGBA")).reshape(-1, 4)
        shutil.rmtree(tmp, ignore_errors=True)
        self.assertEqual(info["kind"], "image")
        self.assertGreater(info["jobs"], 1)
        self.assertEqual(int(np.any(canvas != original, axis=1).sum()), 0)

    def test_image_code_is_read_as_data_and_never_executed(self):
        import base64
        import io
        import runner
        buf = io.BytesIO()
        Image.new("RGB", (4, 3), "red").save(buf, "PNG")
        b64 = base64.b64encode(buf.getvalue()).decode()
        code = "\n".join(['import os', 'os.remove("nothing-here")', 'TITLE = "t"', f'IMAGE_B64 = "{b64}"', ''])
        self.assertEqual(runner.kind_of(code), "image")
        title, data = runner.read_image_code(code)              # would raise if os.remove had run
        self.assertEqual((title, Image.open(io.BytesIO(data)).size), ("t", (4, 3)))
        with self.assertRaises(ValueError):
            runner.read_image_code('IMAGE_B64 = open("x").read()')

    def test_broken_code_reports_the_real_error(self):
        rc, info, err, _ = self.run_code("broken_code.py")
        self.assertNotEqual(rc, 0)
        self.assertIn("bluee", err)


class Studio(unittest.TestCase):
    def test_scenes_and_loading(self):
        self.assertIn("dragon_girl", studio.scenes())
        title, steps, rolloff = studio.load("dragon_girl")
        self.assertEqual(len(steps), 22)
        self.assertEqual(rolloff, 0.82)

    def test_a_traced_logo_loads_as_an_exact_colour_scene(self):
        tmp = Path(tempfile.mkdtemp())
        Image.fromarray(sample_logo(), "RGBA").save(tmp / "logo.png")
        data = vectorize.trace(tmp / "logo.png")
        shutil.rmtree(tmp, ignore_errors=True)
        self.assertFalse(data["photo"])
        self.assertGreaterEqual(len(data["layers"]), 4)
        R.render_image(vector_scene.build(data), .25, rolloff=1.0)

    def test_code_kinds_and_risk_check(self):
        import runner
        self.assertEqual(runner.kind_of("<svg viewBox='0 0 1 1'></svg>"), "svg")
        self.assertEqual(runner.kind_of("def build():\n    return []"), "scene")
        self.assertEqual(runner.kind_of("from PIL import Image"), "python")
        self.assertEqual(studio.risky("from PIL import Image, ImageDraw\nimg.save('a.png')"), [])
        self.assertTrue(studio.risky("import os\nos.remove('x')"))
        self.assertTrue(studio.risky("import requests"))
        self.assertEqual(studio.risky("<svg><text>os.remove</text></svg>"), [])


if __name__ == "__main__":
    unittest.main()
