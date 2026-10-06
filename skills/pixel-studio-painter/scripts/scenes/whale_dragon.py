"""الحوت والتنين — a humpback whale breaches out of a storm sea as a dragon dives on it, fire against water.

PROMPT (what this program paints):
  Photorealistic cinematic dark-fantasy still, 16:9. Night storm over open ocean. A colossal humpback whale
  breaches diagonally out of the sea in the right foreground, belly and throat pleats toward the camera, long
  white pectoral fin raised, knobbed head, mouth line running back to a small eye; water sheets off its flanks
  and explodes into spray. From the upper left an ancient dragon dives at it with wings spread, scaled hide,
  and unleashes a torrent of fire that meets the spray between them in a burst of steam. Lightning behind the
  clouds is the cold key light (steel blue); the fire is the warm key (amber-orange); the sea mirrors both.
  Heavy rain, airborne spray, deep blacks, volumetric mist, high dynamic range, physically believable water and
  fire, no cartoon look, no text.

Every element is vector code with form shading, surface texture and three light sources, so it renders at any size.
"""
from __future__ import annotations

import math
import random

from dragon_girl import belly_plates, cloud, flame, spikes, tongue, wing
from render import (Step, dots, ellipse, fill, glow, grade, grain, lin, noise, path, poly, rad, rect, rim, scales,
                    shade, stroke, translate, tube, union, vignette)

TITLE = "الحوت والتنين"
TOP, BOTTOM = 62, 738
HORIZON = 468
BOLT = (1010, 120)                    # lightning: the cold key light
MOUTH = (628, 396)                    # the dragon's open jaws
IMPACT = (712, 338)                   # fire meets spray here, just ahead of the whale's head
FIRE_LIGHT = (680, 360)


def rain(seed, n, x0, x1, y0, y1, length, width, slant=-0.25):
    r = random.Random(seed)
    out = []
    for _ in range(n):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        ln = length * r.uniform(.6, 1.3)
        out.append([(x, y), (x + slant * ln, y + ln)])
    return stroke(out, width)


def spray(seed, cx, cy, n, sx, sy, up=1.0, sizes=(1, 1.4, 2, 2.8)):
    r = random.Random(seed)
    return [(cx + r.gauss(0, sx), cy - abs(r.gauss(0, sy)) * up + r.gauss(0, 6), r.choice(sizes)) for _ in range(n)]


def along(a, b, t, off=0.0):
    """A point a fraction t along a->b, pushed `off` to the left of the direction."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy) or 1
    return (a[0] + dx * t - dy / L * off, a[1] + dy * t + dx / L * off)


def foam(seed, y, amp, n=26, x0=-40, x1=1240):
    """A wave crest as soft foam: a gentle line of blurred dots, not a drawn outline."""
    r = random.Random(seed)
    pts = [(x0 + (x1 - x0) * k / n, y + math.sin(k * 1.7 + seed) * amp + r.uniform(-amp * .3, amp * .3)) for k in range(n + 1)]
    out = []
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        for k in range(6):
            t = k / 6
            out.append((ax + (bx - ax) * t + r.uniform(-3, 3), ay + (by - ay) * t + r.uniform(-2, 2), r.choice([1.2, 1.8, 2.6])))
    return out


def build() -> list[Step]:
    S: list[Step] = []

    # 1. storm sky
    S.append(Step("السماء العاصفة", [
        fill(rect(0, 0, 1200, 800), lin((0, TOP), (0, HORIZON), [(0, "#070a10"), (.4, "#121a26"), (.8, "#273243"), (1, "#3a4556")])),
        noise(rect(0, TOP, 1200, HORIZON - TOP), .35, 160, 11, "multiply", octaves=3),
        glow(ellipse(*BOLT, 420, 260), "#5f7fb3", 120, .55)],
        "sweep", weight=1.2))

    # 2. cloud deck: cold from behind (lightning), warm underneath (fire)
    big = union(cloud(300, 150, 700, 120, 20, 41), cloud(820, 110, 760, 110, 20, 42), cloud(560, 250, 1000, 70, 18, 43))
    S.append(Step("الغيوم الركامية", [
        fill(big, "#0b0f17", .92, blur=18),
        noise(big, .5, 60, 12, "multiply", octaves=4),
        fill(translate(big, -14, -16), rad(BOLT, 520, [(0, "#a9c4ea"), (1, "#a9c4ea00")]), .55, blur=14, mode="screen"),
        fill(translate(big, 6, 22), rad(FIRE_LIGHT, 420, [(0, "#ff7a2a"), (1, "#ff7a2a00")]), .32, blur=22, mode="add"),
        fill(rect(-50, 380, 1300, 110), "#54637a", .22, blur=34, mode="screen")],
        "sweep", weight=1.0))

    # 3. lightning
    r = random.Random(7)
    bolt = [(BOLT[0], TOP + 10)]
    while bolt[-1][1] < 430:
        bolt.append((bolt[-1][0] + r.uniform(-30, 18), bolt[-1][1] + r.uniform(18, 34)))
    br = [bolt[5]] + [(bolt[5][0] + 30 + 24 * k, bolt[5][1] + 22 * k + r.uniform(-6, 6)) for k in range(1, 5)]
    S.append(Step("البرق", [
        glow(stroke([bolt, br], 10), "#8fb4ff", 30, .7),
        fill(stroke([bolt], 2.6), "#f6f9ff"), fill(stroke([br], 1.5), "#dde9ff", .9),
        fill(rect(0, TOP, 1200, HORIZON - TOP), rad(BOLT, 700, [(0, "#9fbcf0"), (1, "#9fbcf000")]), .18, mode="screen")],
        "down", origin=BOLT, weight=.5))

    # 4. the sea: dark swell with streaked texture, both lights mirrored, soft foam on the crests
    sea = rect(-50, HORIZON, 1300, BOTTOM + 50 - HORIZON)
    S.append(Step("البحر الهائج", [
        fill(sea, lin((0, HORIZON), (0, BOTTOM), [(0, "#2a3a4c"), (.25, "#15202c"), (.7, "#0a1118"), (1, "#05080c")])),
        noise(sea, .55, 22, 21, "multiply", octaves=4, stretch=(6.0, 1.0)),
        noise(sea, .3, 9, 22, "screen", "#c9d8ea", octaves=2, stretch=(4.0, 1.0)),
        fill(sea, rad(BOLT, 900, [(0, "#8eaad8"), (1, "#8eaad800")]), .22, mode="screen"),
        fill(sea, rad(IMPACT, 560, [(0, "#ff8a3a"), (1, "#ff8a3a00")]), .38, mode="add"),
        *[fill(dots(foam(s, y, a)), "#dfe9f5", al, blur=2.6) for s, y, a, al in
          ((1, 496, 3, .18), (2, 532, 5, .22), (3, 584, 8, .3), (4, 648, 11, .38), (5, 712, 14, .42))],
        *[fill(dots(foam(s + 10, y, a, 40)), "#ffffff", .22, blur=1.0) for s, y, a in ((3, 584, 8), (4, 648, 11), (5, 712, 14))],
        *[fill(cloud(x, y, w, 10, 6, 70 + k), "#e8f0f8", .45, blur=4, mode="screen") for k, (x, y, w) in
          enumerate(((180, 660, 120), (420, 700, 150), (300, 590, 90), (560, 730, 110)))]],
        "sweep", weight=1.1))

    # 5. the far swell behind the whale, its foot fading into mist
    wall = path("M 560 470 C 700 430 900 380 1100 400 C 1180 410 1240 430 1250 470 L 1250 620 L 560 620 Z")
    S.append(Step("جدار الموج والضباب", [
        fill(wall, lin((0, 380), (0, 620), [(0, "#4a5d74"), (.5, "#1e2a38"), (.85, "#0c141c"), (1, "#0c141c00")]), .95, blur=2),
        noise(wall, .45, 26, 23, "multiply", octaves=3, stretch=(3.0, 1.0)),
        fill(dots(foam(9, 418, 10, 22, 600, 1250)), "#dfe9f5", .5, blur=1.5),
        fill(dots(spray(31, 900, 420, 160, 230, 30, 1.2, (1, 1.5, 2))), "#e9f1fb", .55, blur=.6),
        fill(rect(-50, 440, 1300, 60), "#7f93ad", .28, blur=26, mode="screen")],
        "right", weight=.7))

    # 6. the dragon: bigger, neck arched down at the whale; far wing, body with scales, head, near wing
    fw_mem, fw_bones, fw_veins = wing((300, 240), (390, 90), (470, -20), [(680, -40), (760, 70), (700, 180), (580, 250)], (400, 300), sag=.3)
    S.append(Step("جناح التنين البعيد", [
        fill(fw_mem, lin((400, -20), (560, 260), [(0, "#2a2f3c"), (1, "#121620")]), .96, blur=.5),
        noise(fw_mem, .4, 18, 51, "multiply"),
        fill(fw_mem, rad(BOLT, 700, [(0, "#8fa8d0"), (1, "#8fa8d000")]), .35, mode="screen"),
        fill(fw_veins, "#0a0d14", .8), fill(fw_bones, "#0c0f16"),
        rim(union(fw_mem, fw_bones), (.6, -1), 2.6, "#c6d8f5", .6)],
        "grow", origin=(300, 240), weight=.7))

    spine = [(40, 120), (120, 160), (210, 214), (310, 272), (410, 318), (500, 348), (570, 372)]
    radii = [28, 42, 56, 66, 64, 54, 40]
    body = tube(spine, radii)
    neck_head = path("M 552 330 C 576 318 606 322 630 338 C 646 348 658 352 672 364 C 690 380 702 396 708 412 L 680 420 "
                     "C 666 410 652 404 640 402 L 610 406 L 650 436 C 660 446 652 454 640 450 C 612 442 586 424 570 402 "
                     "C 556 386 548 356 552 330 Z")
    horns = union(tube([(560, 332), (530, 296), (496, 270), (460, 258)], [11, 8.5, 5, 1.2]),
                  tube([(574, 326), (552, 288), (522, 258), (492, 242)], [8.5, 6.5, 3.8, 1]),
                  tube([(566, 352), (540, 356), (520, 372)], [6, 4, 1]), tube([(572, 372), (552, 384), (538, 402)], [5, 3.5, 1]))
    brow = path("M 596 340 C 612 334 628 338 640 350 C 630 348 616 348 600 352 Z")
    teeth = union(*[poly([(x, y), (x + 6, y - 1), (x + 3, y + 10)]) for x, y in [(646, 404), (660, 408), (674, 414)]],
                  *[poly([(x, y), (x + 6, y + 1), (x + 2.5, y - 8)]) for x, y in [(646, 430), (662, 436)]])
    legs = union(tube([(440, 340), (470, 410), (448, 470)], [28, 18, 12]),
                 *[tube([(448, 470), (448 + ex, 470 + ey)], [6, 1.2], n=4) for ex, ey in [(-28, 12), (-10, 24), (12, 22)]],
                 tube([(230, 236), (214, 312), (180, 360)], [22, 14, 9]))
    back = spikes(spine, radii, every=4, size=1.7)
    belly, plates = belly_plates(spine[1:], radii[1:])
    dragon = union(body, legs, back, neck_head, horns)
    S.append(Step("جسد التنين", [
        fill(dragon, "#0e1118"),
        shade(union(body, neck_head, legs), BOLT, "#2f3848", "#0c0f16", core=.3),
        fill(union(body, neck_head), rad(MOUTH, 420, [(0, "#7a3418"), (.45, "#30160f"), (1, "#30160f00")]), .8),
        fill(belly, rad(MOUTH, 360, [(0, "#c0683a"), (.5, "#5a2c1e"), (1, "#1a1210")]), .85),
        fill(plates, "#07070a", .5),
        scales(union(body, neck_head), 9, "#000000", .22, .8),
        fill(brow, "#1a1016", .9),
        noise(union(body, neck_head, legs), .4, 10, 52, "multiply"),
        rim(dragon, (.5, -1), 3.2, "#b9cff2", .65),
        rim(union(neck_head, body[:60], legs), (.9, .7), 4.5, "#ff7a32", .9)],
        "grow", origin=(400, 300), weight=1.4))
    S.append(Step("رأس التنين", [
        fill(teeth, "#f0e4cc", .95),
        fill(ellipse(606, 358, 7, 4, rot=20), "#ffcf4a"), glow(ellipse(606, 358, 8, 6), "#ff9a2a", 10, .9),
        fill(ellipse(607, 358, 1.8, 3.8, rot=20), "#2a0a00")],
        "grow", origin=(606, 358), weight=.4))

    nw_mem, nw_bones, nw_veins = wing((330, 270), (250, 120), (150, 0), [(-10, 0), (-40, 120), (40, 250), (190, 330)], (340, 330), sag=.3)
    S.append(Step("جناح التنين الأمامي", [
        fill(nw_mem, lin((40, 20), (280, 330), [(0, "#3a4258"), (.5, "#1c2230"), (1, "#0d1118")]), .96, blur=.5),
        noise(nw_mem, .45, 16, 53, "multiply"),
        fill(nw_mem, rad(BOLT, 1100, [(0, "#8fa8d0"), (1, "#8fa8d000")]), .3, mode="screen"),
        fill(nw_mem, rad(FIRE_LIGHT, 460, [(0, "#ff8a3a"), (1, "#ff8a3a00")]), .45, mode="add"),
        fill(nw_veins, "#0a0d14", .85), fill(nw_bones, "#0c0f16"),
        rim(union(nw_mem, nw_bones), (.5, -1), 3, "#c6d8f5", .7)],
        "grow", origin=(330, 270), weight=.9))

    # 7. the whale: a humpback breaching, belly toward the camera
    A, B = (700, 290), (1200, 760)                                   # head tip -> tail root, the body axis
    wspine = [along(A, B, t) for t in (0.0, .12, .3, .5, .7, .88, 1.0)]
    wradii = [58, 92, 120, 128, 118, 92, 56]
    wbody = tube(wspine, wradii)
    dorsal = poly([along(A, B, .62, 118), along(A, B, .66, 150), along(A, B, .72, 112)])
    ventral = tube([along(A, B, t, -r * .48) for t, r in zip((.06, .2, .4, .6, .8), (70, 110, 126, 122, 100))],
                   [34, 62, 72, 66, 48])
    rostrum = path("M 700 290 C 660 262 626 262 616 286 C 612 304 630 326 660 338 C 690 346 722 342 740 328 Z")
    mouth = [along((618, 300), (820, 440), t, -6 * math.sin(math.pi * t)) for t in [k / 12 for k in range(13)]]
    pleats = [[along(A, B, t, -r) for t, r in zip((.05, .22, .42, .62, .8), (26 + k * 11, 48 + k * 13, 60 + k * 14, 58 + k * 13, 42 + k * 11))]
              for k in range(6)]
    fin_root, fin_tip = along(A, B, .40, -92), (668, 664)
    fin_mid = along(fin_root, fin_tip, .5, 34)
    fin = tube([fin_root, along(fin_root, fin_tip, .25, 22), fin_mid, along(fin_root, fin_tip, .78, 24), fin_tip],
               [40, 38, 32, 20, 6])
    fin_knobs = [(*along(fin_root, fin_tip, t, 30 + 10 * math.sin(math.pi * t)), 2.6 + (t < .6)) for t in (.15, .28, .42, .56, .7, .84, .95)]
    fin_shadow = tube([fin_root, along(fin_root, fin_tip, .3, 10)], [48, 30])
    fluke = path("M 1150 700 C 1190 660 1240 636 1270 646 L 1262 706 C 1230 712 1196 724 1176 748 Z")
    tubercles = [(x, y, r) for x, y, r in [(640, 276, 3.2), (662, 268, 3), (686, 266, 3.4), (710, 272, 3), (650, 292, 2.6), (676, 286, 2.8),
                                           (702, 290, 2.6), (730, 300, 3), (754, 312, 2.8), (780, 330, 2.6)]]
    whale = union(wbody, dorsal, ventral, rostrum, fin, fluke)
    S.append(Step("جسد الحوت", [
        fill(whale, "#161b22"),
        shade(union(wbody, rostrum, dorsal), BOLT, "#4f5d6d", "#121820", core=.45),
        fill(ventral, lin(along(A, B, .5, -150), along(A, B, .5, 0), [(0, "#cfd8df"), (.6, "#8b98a4"), (1, "#8b98a400")]), .95),
        noise(union(wbody, rostrum, dorsal), .5, 16, 61, "multiply", octaves=4),
        noise(ventral, .35, 12, 63, "multiply", octaves=3),
        noise(union(wbody, ventral), .22, 4, 62, "screen", "#aebccb", octaves=2),
        fill(stroke(pleats, 2.2), "#2b343d", .6, blur=.8),
        fill(stroke(pleats, .7), "#e6edf3", .45),
        fill(stroke([mouth], 3.2), "#0d1116", .9, blur=.6),
        fill(stroke([[(x, y + 3) for x, y in mouth]], 1.0), "#9aa8b4", .5),
        fill(fin_shadow, "#0d1218", .55, blur=8),
        fill(fin, lin(fin_root, fin_tip, [(0, "#4a5864"), (.25, "#b9c6cf"), (.6, "#e9eff3"), (1, "#f6f9fb")])),
        shade(fin, BOLT, "#ffffff", "#9aa8b4", core=.5),
        noise(fin, .3, 10, 64, "multiply", octaves=3),
        fill(stroke([[along(fin_root, fin_tip, t, -8) for t in (.1, .4, .7, .95)]], 2), "#7f8d99", .5, blur=1.2),
        fill(dots(fin_knobs), "#aeb9c2", .8), fill(dots([(x, y, r * .5) for x, y, r in fin_knobs]), "#5a6873", .8),
        fill(dots(tubercles), "#3a4652", .9), fill(dots([(x - .8, y - .8, r * .45) for x, y, r in tubercles]), "#c2ccd6", .9),
        fill(ellipse(788, 392, 5, 3.6, rot=30), "#070a0e"), fill(ellipse(789.5, 391, 1.3, 1.3), "#dde8f3"),
        fill(wbody, rad(IMPACT, 560, [(0, "#ff8a3a"), (1, "#ff8a3a00")]), .4, mode="add"),
        rim(whale, (.4, -1), 3.6, "#dbe8fb", .9),
        rim(whale, (-.8, .3), 5, "#ffa04a", .7, soft=1.6),
        rim(whale, (.4, -1), 10, "#9fb6d8", .25, soft=3)],
        "rise", origin=(1000, 740), weight=1.6))

    # 8. water sheeting off the whale, exploding where it leaves the sea
    sheets = union(*[tube([(x, y), (x - 10, y + 70), (x - 30, y + 140)], [6, 4, 1.5]) for x, y in
                     [(1000, 500), (1040, 560), (1090, 610), (960, 470), (930, 440), (1120, 660)]])
    S.append(Step("الماء ينهمر عن جسد الحوت", [
        fill(stroke([[(x, y), (x - 8, y + 60), (x - 24, y + 130)] for x, y in
                     [(1000, 500), (1040, 560), (1090, 610), (960, 470), (932, 440), (1120, 660), (1070, 600)]], 1.6),
             "#e6eff8", .55, blur=1.0, mode="screen"),
        fill(stroke([[(x, y), (x - 14, y + 120)] for x, y in [(1010, 520), (1060, 580), (1100, 630)]], .8), "#ffffff", .6),
        fill(dots([(x - 26 + k * 2, y + 130 + k * 4, 1.6) for x, y in [(1000, 500), (1040, 560), (1090, 610)] for k in range(5)]),
             "#f2f7fc", .7),
        glow(ellipse(1140, 710, 220, 70), "#cfe0f2", 40, .4),
        fill(dots(spray(71, 1130, 710, 460, 160, 70, 1.4)), "#eef4fb", .8),
        fill(dots(spray(72, 1130, 710, 180, 190, 100, 1.6, (2.4, 3.2, 4))), "#ffffff", .35, blur=2),
        fill(dots(spray(73, 1130, 710, 120, 120, 40, 1.0)), "#ffb066", .3, blur=1.5, mode="add")],
        "rise", origin=(1140, 730), weight=.7))

    # 9. the fire
    a, b = (MOUTH[0] + 24, MOUTH[1] + 4), IMPACT
    S.append(Step("نار التنين", [
        glow(tube([a, b], [16, 60]), "#ff4a12", 44, .7),
        *[fill(flame(900 + k, a, b, 5, 34, 16, bend=(k - 3) * .5), "#ff3d0a", .5, blur=3, mode="add") for k in range(7)],
        *[fill(flame(920 + k, a, b, 3.5, 22, 9, bend=(k - 2) * .35), "#ff9326", .65, blur=2.4, mode="add") for k in range(5)],
        *[fill(flame(940 + k, a, b, 2.2, 12, 5), "#ffe7a2", .85, blur=1.8, mode="add") for k in range(3)],
        fill(flame(960, a, b, 1.4, 6, 3), "#ffffff", .75, blur=1.2, mode="add")],
        "grow", origin=MOUTH, weight=1.0))

    # 10. steam at the collision
    steam = union(cloud(IMPACT[0], IMPACT[1] - 20, 200, 90, 12, 81), cloud(IMPACT[0] - 30, IMPACT[1] - 70, 150, 60, 8, 82))
    S.append(Step("البخار عند التصادم", [
        fill(steam, "#d6dde6", .5, blur=12, mode="screen"),
        noise(steam, .5, 20, 83, "multiply", octaves=3),
        fill(translate(steam, 0, 14), "#ff8a3a", .32, blur=16, mode="add"),
        glow(ellipse(*IMPACT, 56, 40), "#fff0c0", 26, .7),
        *[fill(tongue(980 + k, [IMPACT, (IMPACT[0] + 36 * math.cos(t0), IMPACT[1] - 30 * math.sin(t0)),
                                (IMPACT[0] + 64 * math.cos(t0), IMPACT[1] - 50 * math.sin(t0))], 9, 1),
               "#ff6a1a", .5, blur=2.5, mode="add") for k, t0 in enumerate((.4, 1.2, 2.0, 2.8, 3.5, -.3))],
        fill(dots(spray(84, IMPACT[0], IMPACT[1], 140, 70, 60, 1.0, (1, 1.4, 2))), "#fff3d8", .7, blur=.6, mode="add")],
        "grow", origin=IMPACT, weight=.6))

    # 11. rain (lighter than before, so the picture reads through it), spray in the air, embers
    S.append(Step("المطر والرذاذ", [
        fill(rain(91, 520, -40, 1240, TOP - 40, BOTTOM, 24, 1.0), "#a8bbd4", .16, blur=.4),
        fill(rain(92, 150, -40, 1240, TOP - 60, BOTTOM, 60, 1.8), "#cddcef", .22, blur=1.2),
        fill(rain(93, 160, 480, 900, 240, 560, 36, 1.3), "#ffb066", .45, blur=.6, mode="add"),
        fill(dots(spray(94, 600, 600, 220, 600, 120, .5, (.8, 1, 1.4))), "#e4edf8", .3, blur=.5)],
        "down", weight=.8))
    r = random.Random(95)
    emb = []
    for _ in range(220):
        t = r.random()
        emb.append((a[0] + (b[0] - a[0]) * t + r.gauss(0, 50), a[1] + (b[1] - a[1]) * t + r.gauss(0, 40) - r.random() * 70,
                    r.choice([.6, .8, 1.1, 1.5])))
    S.append(Step("الشرر", [fill(dots(emb), "#ffd27a", .9, mode="add"),
                            fill(dots([(x, y, s * 3) for x, y, s in emb if s > 1]), "#ff7a2a", .45, blur=2.4, mode="add")],
                  "sparkle", weight=.4))

    # 12. atmosphere, grade, grain, letterbox
    S.append(Step("الجو واللمسات السينمائية", [
        fill(rect(-50, 380, 1300, 200), "#3f4d63", .14, blur=40, mode="screen"),
        grade(shadows="#071022", highlights="#ffe4c8", amount=.5, contrast=1.1),
        vignette(.62), grain(.022, 9)], "sweep", weight=.6))
    S.append(Step("إطار 16:9", [fill(rect(0, 0, 1200, TOP), "#000000"), fill(rect(0, BOTTOM, 1200, 800 - BOTTOM), "#000000")],
                  "sweep", weight=.3))
    return S
