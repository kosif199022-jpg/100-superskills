/* KOSIF three-kit — the cinematic building blocks behind the 3D films, as an ES module bundled by esbuild
   (motion.py bundle). Everything is deterministic: seeded noise, no clocks; every block is driven by a time t.
   Blocks: noise & textures · renderer · sky + sun · terrain (ridged FBM, detail maps, vertex colours) · forest
   (instanced two-tier conifers) · sea (reflective Water) · cloud slab (raymarched) · vapour / rain points · lens
   flare · post stack (bloom, god rays, DOF, grade + vignette + CA, film grain, ACES) · camera keys · GPU motion blur. */
import * as THREE from "three";
import { Sky } from "three/examples/jsm/objects/Sky.js";
import { Water } from "three/examples/jsm/objects/Water.js";
import { Lensflare, LensflareElement } from "three/examples/jsm/objects/Lensflare.js";
import { EffectComposer } from "three/examples/jsm/postprocessing/EffectComposer.js";
import { RenderPass } from "three/examples/jsm/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/examples/jsm/postprocessing/UnrealBloomPass.js";
import { BokehPass } from "three/examples/jsm/postprocessing/BokehPass.js";
import { FilmPass } from "three/examples/jsm/postprocessing/FilmPass.js";
import { ShaderPass } from "three/examples/jsm/postprocessing/ShaderPass.js";
import { OutputPass } from "three/examples/jsm/postprocessing/OutputPass.js";
import { mergeGeometries } from "three/examples/jsm/utils/BufferGeometryUtils.js";

export { THREE };

/* ───────── seeded noise (CPU) ───────── */
export function rng(seed) { let a = seed >>> 0 || 1; return () => { a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
const PERM = (() => { const r = rng(1337), p = []; for (let i = 0; i < 256; i++) p[i] = i; for (let i = 255; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [p[i], p[j]] = [p[j], p[i]]; } return p.concat(p); })();
const fade = (t) => t * t * t * (t * (t * 6 - 15) + 10);
export const lerp = (a, b, t) => a + (b - a) * t;
function grad(h, x, y) { switch (h & 3) { case 0: return x + y; case 1: return -x + y; case 2: return x - y; default: return -x - y; } }
export function perlin(x, y) {                            // 2D Perlin, [-1, 1]
  const X = Math.floor(x) & 255, Y = Math.floor(y) & 255; x -= Math.floor(x); y -= Math.floor(y);
  const u = fade(x), v = fade(y), A = PERM[X] + Y, B = PERM[X + 1] + Y;
  return lerp(lerp(grad(PERM[A], x, y), grad(PERM[B], x - 1, y), u), lerp(grad(PERM[A + 1], x, y - 1), grad(PERM[B + 1], x - 1, y - 1), u), v);
}
export function fbm(x, y, oct = 5, lac = 2.0, gain = 0.5) { let a = 0, w = 1, s = 0; for (let i = 0; i < oct; i++) { a += w * perlin(x, y); s += w; x *= lac; y *= lac; w *= gain; } return a / s; }
export function ridged(x, y, oct = 5) { let a = 0, w = 1, s = 0; for (let i = 0; i < oct; i++) { a += w * (1 - Math.abs(perlin(x, y))); s += w; x *= 2.1; y *= 2.1; w *= 0.5; } return a / s; }
export const smooth = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
export const clamp01 = (x) => Math.min(1, Math.max(0, x));
export const ramp = (t, a, b) => clamp01((t - a) / Math.max(1e-3, b - a));

/* ───────── generated textures (no downloads) ───────── */
export function noiseCanvas(N, fn) {
  const cv = document.createElement("canvas"); cv.width = cv.height = N;
  const ctx = cv.getContext("2d"), img = ctx.createImageData(N, N), d = img.data;
  for (let y = 0; y < N; y++) for (let x = 0; x < N; x++) { const o = (y * N + x) * 4; const [r, g, b, a] = fn(x, y); d[o] = r; d[o + 1] = g; d[o + 2] = b; d[o + 3] = a == null ? 255 : a; }
  ctx.putImageData(img, 0, 0);
  const tex = new THREE.CanvasTexture(cv); tex.wrapS = tex.wrapT = THREE.RepeatWrapping; return tex;
}
export function normalFromHeight(N, hfn, strength) {
  const h = new Float32Array(N * N);
  for (let y = 0; y < N; y++) for (let x = 0; x < N; x++) h[y * N + x] = hfn(x, y);
  return noiseCanvas(N, (x, y) => {
    const l = h[y * N + ((x - 1 + N) % N)], r = h[y * N + ((x + 1) % N)], u = h[((y - 1 + N) % N) * N + x], dn = h[((y + 1) % N) * N + x];
    const nx = (l - r) * strength, ny = (u - dn) * strength, len = Math.hypot(nx, ny, 1);
    return [128 + 127 * nx / len, 128 + 127 * ny / len, 128 + 127 / len];
  });
}
export function spriteTex(kind) {                          // "soft" disc, "ring", or a vertical "streak"
  const S = 128, cv = document.createElement("canvas"); cv.width = cv.height = S; const ctx = cv.getContext("2d");
  if (kind === "soft") {
    const g = ctx.createRadialGradient(S / 2, S / 2, 0, S / 2, S / 2, S / 2);
    g.addColorStop(0, "rgba(255,255,255,1)"); g.addColorStop(0.35, "rgba(255,255,255,.55)"); g.addColorStop(1, "rgba(255,255,255,0)");
    ctx.fillStyle = g; ctx.fillRect(0, 0, S, S);
  } else if (kind === "ring") {
    const g = ctx.createRadialGradient(S / 2, S / 2, S * 0.3, S / 2, S / 2, S / 2);
    g.addColorStop(0, "rgba(255,255,255,0)"); g.addColorStop(0.7, "rgba(255,220,180,.35)"); g.addColorStop(0.85, "rgba(255,255,255,.5)"); g.addColorStop(1, "rgba(255,255,255,0)");
    ctx.fillStyle = g; ctx.fillRect(0, 0, S, S);
  } else {
    const g = ctx.createLinearGradient(0, 0, 0, S);
    g.addColorStop(0, "rgba(255,255,255,0)"); g.addColorStop(0.5, "rgba(255,255,255,.9)"); g.addColorStop(1, "rgba(255,255,255,0)");
    ctx.fillStyle = g; ctx.fillRect(S / 2 - 3, 0, 6, S);
  }
  return new THREE.CanvasTexture(cv);
}

/* ───────── renderer, sky, lights ───────── */
export function makeRenderer(canvas, W, H, o = {}) {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: "high-performance", preserveDrawingBuffer: true });
  renderer.setPixelRatio(1); renderer.setSize(W, H, false);
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = o.exposure == null ? 0.6 : o.exposure;
  return renderer;
}
export function makeSky(scene, o = {}) {
  const sky = new Sky(); sky.scale.setScalar(o.scale || 45000); scene.add(sky);
  const u = sky.material.uniforms;
  u.turbidity.value = o.turbidity == null ? 3 : o.turbidity; u.rayleigh.value = o.rayleigh == null ? 1.6 : o.rayleigh;
  u.mieCoefficient.value = o.mie == null ? 0.004 : o.mie; u.mieDirectionalG.value = o.mieG == null ? 0.85 : o.mieG;
  const sun = new THREE.Vector3();
  const setSun = (elevDeg, azimDeg) => {
    sun.setFromSphericalCoords(1, THREE.MathUtils.degToRad(90 - elevDeg), THREE.MathUtils.degToRad(azimDeg));
    u.sunPosition.value.copy(sun); return sun;
  };
  return { sky, uniforms: u, sun, setSun };
}
export function makeSunLight(scene, o = {}) {
  const light = new THREE.DirectionalLight(0xffffff, o.intensity == null ? 3.0 : o.intensity);
  light.castShadow = true; light.shadow.mapSize.set(o.shadowSize || 4096, o.shadowSize || 4096);
  const b = o.bounds || 2300, sc = light.shadow.camera; sc.left = -b; sc.right = b; sc.top = b; sc.bottom = -b; sc.near = 100; sc.far = o.far || 9000;
  light.shadow.bias = -0.0005; light.shadow.normalBias = 2.0;
  scene.add(light, light.target);
  return light;
}
export function makeFill(scene, color = 0xcfe0ff) {        // a camera-side fill without shadows: the cinematographer's bounce
  const fill = new THREE.DirectionalLight(color, 0); scene.add(fill, fill.target); return fill;
}

/* ───────── land ───────── */
/* height(x, z) → y; colour(h, slope, x, z, Color) fills the Color; detail = tiled albedo + normal maps */
export function makeTerrain(o) {
  const SEG = o.seg || 560, SIZE = o.size || 4600;
  const geo = new THREE.PlaneGeometry(SIZE, SIZE, SEG, SEG); geo.rotateX(-Math.PI / 2);
  const pos = geo.attributes.position, col = new Float32Array(pos.count * 3), c = new THREE.Color();
  for (let i = 0; i < pos.count; i++) pos.setY(i, o.height(pos.getX(i), pos.getZ(i)));
  geo.computeVertexNormals();
  const nrm = geo.attributes.normal;
  for (let i = 0; i < pos.count; i++) {
    o.colour(pos.getY(i), 1 - nrm.getY(i), pos.getX(i), pos.getZ(i), c);
    col[i * 3] = c.r; col[i * 3 + 1] = c.g; col[i * 3 + 2] = c.b;
  }
  geo.setAttribute("color", new THREE.BufferAttribute(col, 3));
  const albedo = noiseCanvas(1024, (x, y) => { const m = 0.78 + 0.22 * (0.5 + 0.5 * fbm(x / 40, y / 40, 4)) + 0.12 * fbm(x / 7 + 3, y / 7, 2); const v = Math.round(255 * Math.min(1, m)); return [v, v, v]; });
  albedo.repeat.set(o.albedoRepeat || 60, o.albedoRepeat || 60);
  const detail = normalFromHeight(1024, (x, y) => fbm(x / 30, y / 30, 4) * 0.5 + fbm(x / 6 + 9, y / 6 + 2, 3) * 0.22, 3.0);
  detail.repeat.set(o.normalRepeat || 90, o.normalRepeat || 90);
  const mesh = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ vertexColors: true, map: albedo, normalMap: detail,
    normalScale: new THREE.Vector2(o.normalScale || 0.55, o.normalScale || 0.55), roughness: o.roughness == null ? 0.95 : o.roughness, metalness: 0 }));
  mesh.castShadow = true; mesh.receiveShadow = true;
  return mesh;
}
/* the standard alpine palette: sand → grass → rock by height and slope, snow on the tops */
export function alpineColour(h, slope, x, z, c) {
  const snow = alpineColour.snow || (alpineColour.snow = new THREE.Color(0xf4f7fb)), rock = new THREE.Color(0x5d5a58), rock2 = new THREE.Color(0x7a6f66),
        grass = new THREE.Color(0x4e6e34), grass2 = new THREE.Color(0x6b8a3c), sand = new THREE.Color(0xb9a77a), deep = new THREE.Color(0x2f4a3a);
  const v = 0.5 + 0.5 * fbm(x * 0.01 + 11, z * 0.01 + 5, 3);
  if (h < -5) c.copy(deep);
  else if (h < 25) c.copy(sand).lerp(grass, smooth(5, 25, h));
  else c.copy(grass).lerp(grass2, v);
  if (h > 120) c.lerp(rock.clone().lerp(rock2, v), smooth(120, 420, h) * 0.8);
  c.lerp(rock, smooth(0.28, 0.6, slope));
  if (h > 520) c.lerp(snow, smooth(520, 700, h) * (1 - smooth(0.35, 0.7, slope)));
}
export function slopeOf(height, x, z) { const e = 6; const dx = height(x + e, z) - height(x - e, z), dz = height(x, z + e) - height(x, z - e); return Math.hypot(dx, dz) / (2 * e); }

/* instanced two-tier conifers; accept(x, z, h) decides where they grow */
export function makeForest(o) {
  const r = rng(o.seed || 42), MAX = o.max || 22000, [x0, x1, z0, z1] = o.region;
  const mats = [], cols = [], tmp = new THREE.Object3D(), cc = new THREE.Color();
  let tries = 0;
  while (mats.length < MAX && tries < MAX * 12) {
    tries++;
    const x = x0 + r() * (x1 - x0), z = z0 + r() * (z1 - z0), h = o.height(x, z);
    if (!o.accept(x, z, h)) continue;
    const clump = 0.5 + 0.5 * fbm(x * 0.0025 + 31, z * 0.0025 + 17, 3);
    if (r() > clump * clump * 1.4) continue;
    const s = (o.scale || 1) * (0.65 + r() * 0.75 - 0.35 * smooth(o.thinFrom || 300, o.thinTo || 430, h));
    tmp.position.set(x, h - 1, z); tmp.rotation.y = r() * Math.PI * 2; tmp.scale.set(s * (0.85 + 0.3 * r()), s * (0.8 + 0.5 * r()), s * (0.85 + 0.3 * r())); tmp.updateMatrix();
    mats.push(tmp.matrix.clone());
    cc.setHSL((o.hue == null ? 0.25 : o.hue) + 0.07 * (r() - 0.5), 0.3 + 0.25 * r(), 0.1 + 0.1 * r());
    cols.push(cc.clone());
  }
  const tierA = new THREE.ConeGeometry(8.0, 20, 7, 1, false); tierA.translate(0, 16, 0);
  const tierB = new THREE.ConeGeometry(5.2, 18, 7, 1, false); tierB.translate(0, 29, 0);
  const crown = mergeGeometries([tierA, tierB]);
  const trunk = new THREE.CylinderGeometry(1.1, 1.6, 10, 5); trunk.translate(0, 5, 0);
  const crowns = new THREE.InstancedMesh(crown, new THREE.MeshStandardMaterial({ roughness: 0.9, metalness: 0 }), mats.length);
  const trunks = new THREE.InstancedMesh(trunk, new THREE.MeshStandardMaterial({ color: 0x4a3524, roughness: 0.95 }), mats.length);
  for (let i = 0; i < mats.length; i++) { crowns.setMatrixAt(i, mats[i]); trunks.setMatrixAt(i, mats[i]); crowns.setColorAt(i, cols[i]); }
  crowns.instanceMatrix.needsUpdate = true; trunks.instanceMatrix.needsUpdate = true; crowns.instanceColor.needsUpdate = true;
  crowns.castShadow = true; crowns.receiveShadow = true; trunks.castShadow = true;
  const g = new THREE.Group(); g.add(crowns, trunks); g.userData.count = mats.length;
  return g;
}

/* ───────── water ───────── */
export function makeSea(o = {}) {
  const normals = o.normals || normalFromHeight(512, (x, y) => fbm(x / 36, y / 36, 4) * 0.6 + fbm(x / 9 + 50, y / 9, 2) * 0.25, 2.2);
  const water = new Water(new THREE.PlaneGeometry(o.size || 30000, o.size || 30000), {
    textureWidth: o.res || 768, textureHeight: o.res || 768, waterNormals: normals, sunDirection: new THREE.Vector3(), sunColor: 0xffffff,
    waterColor: o.color == null ? 0x0e4a63 : o.color, distortionScale: o.distortion == null ? 2.4 : o.distortion, fog: true, size: o.waveSize || 3.0 });
  water.rotation.x = -Math.PI / 2; water.position.y = o.level || 0;
  water.userData.normals = normals;
  return water;
}
/* a flat ribbon of water along a curve (a river): a tube flattened per segment, revealed with setDrawRange */
export function makeRibbon(curve, o = {}) {
  const segs = o.segments || 220, ring = (o.radial || 10) + 1;
  const geo = new THREE.TubeGeometry(curve, segs, o.radius || 11, o.radial || 10, false);
  const rp = geo.attributes.position;
  for (let i = 0; i <= segs; i++) { const cpt = curve.getPointAt(i / segs); for (let j = 0; j < ring; j++) { const k = i * ring + j; rp.setY(k, cpt.y + (rp.getY(k) - cpt.y) * (o.flatten || 0.3)); } }
  rp.needsUpdate = true; geo.computeVertexNormals();
  const tex = (o.normals || normalFromHeight(512, (x, y) => fbm(x / 36, y / 36, 4) * 0.6 + fbm(x / 9 + 50, y / 9, 2) * 0.25, 2.2)).clone();
  tex.needsUpdate = true; tex.repeat.set(1, o.repeat || 14);
  const mat = new THREE.MeshPhysicalMaterial({ color: o.color == null ? 0x6fb4d6 : o.color, roughness: 0.08, metalness: 0, clearcoat: 1, clearcoatRoughness: 0.05,
    normalMap: tex, normalScale: new THREE.Vector2(0.5, 0.5), emissive: o.emissive == null ? 0x1a5f85 : o.emissive, emissiveIntensity: 0.55, transparent: true, opacity: 0.94 });
  const mesh = new THREE.Mesh(geo, mat); mesh.position.y = 0.5; mesh.receiveShadow = true;
  geo.setDrawRange(0, 0);
  mesh.userData.reveal = (p) => geo.setDrawRange(0, Math.floor(geo.index.count * (p * p * (3 - 2 * p))));
  mesh.userData.flow = (t, speed = 0.9) => { tex.offset.y = -t * speed; };
  return mesh;
}

/* ───────── sky things ───────── */
export function makeCloudSlab(o = {}) {
  const size = o.size || [7000, 520, 4200], center = o.center || [0, 1240, -900];
  const min = new THREE.Vector3(center[0] - size[0] / 2, center[1] - size[1] / 2, center[2] - size[2] / 2), max = new THREE.Vector3(center[0] + size[0] / 2, center[1] + size[1] / 2, center[2] + size[2] / 2);
  const mesh = new THREE.Mesh(new THREE.BoxGeometry(...size), new THREE.ShaderMaterial({
    uniforms: { uT: { value: 0 }, uCover: { value: 0 }, uDark: { value: 0 }, uSun: { value: new THREE.Vector3(0, 1, 0) }, uCam: { value: new THREE.Vector3() },
                uMin: { value: min }, uMax: { value: max }, uSkyCol: { value: new THREE.Color(0x9fb6cc) }, uSunCol: { value: new THREE.Color(0xfff2d9) } },
    vertexShader: `varying vec3 vW; void main(){ vec4 w = modelMatrix * vec4(position, 1.0); vW = w.xyz; gl_Position = projectionMatrix * viewMatrix * w; }`,
    fragmentShader: `precision highp float; varying vec3 vW; uniform float uT, uCover, uDark; uniform vec3 uSun, uCam, uMin, uMax, uSkyCol, uSunCol;
      float hsh(vec3 p){ return fract(sin(dot(p, vec3(127.1, 311.7, 74.7))) * 43758.5453); }
      float vn(vec3 p){ vec3 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f);
        return mix(mix(mix(hsh(i), hsh(i+vec3(1,0,0)), f.x), mix(hsh(i+vec3(0,1,0)), hsh(i+vec3(1,1,0)), f.x), f.y),
                   mix(mix(hsh(i+vec3(0,0,1)), hsh(i+vec3(1,0,1)), f.x), mix(hsh(i+vec3(0,1,1)), hsh(i+vec3(1,1,1)), f.x), f.y), f.z); }
      float fbm3(vec3 p){ float a = 0.0, w = 0.5; for (int i = 0; i < 4; i++) { a += w * vn(p); p = p * 2.03 + vec3(11.0); w *= 0.5; } return a; }
      float dens(vec3 p){ float hgt = (p.y - uMin.y) / (uMax.y - uMin.y);
        float prof = smoothstep(0.0, 0.25, hgt) * (1.0 - smoothstep(0.55, 1.0, hgt));
        vec3 q = p * 0.0011 + vec3(uT * 0.025, 0.0, uT * 0.012);
        float base = fbm3(q) * 0.75 + fbm3(q * 3.1 + vec3(5.0)) * 0.25;
        float cov = mix(0.72, 0.36, uCover);
        return clamp((base - cov) * 3.2, 0.0, 1.0) * prof * smoothstep(0.0, 0.08, uCover); }
      vec2 boxHit(vec3 ro, vec3 rd){ vec3 t0 = (uMin - ro) / rd, t1 = (uMax - ro) / rd; vec3 a = min(t0, t1), b = max(t0, t1);
        return vec2(max(max(a.x, a.y), a.z), min(min(b.x, b.y), b.z)); }
      void main(){ vec3 rd = normalize(vW - uCam); vec2 h = boxHit(uCam, rd); if (h.y <= max(h.x, 0.0)) discard;
        float tn = max(h.x, 0.0), len = h.y - tn; const int N = 36; float dt = len / float(N);
        float jit = hsh(vec3(gl_FragCoord.xy, 1.0)) * dt;
        vec3 col = vec3(0.0); float T = 1.0; vec3 L = normalize(uSun);
        for (int i = 0; i < N; i++) { vec3 p = uCam + rd * (tn + jit + dt * float(i)); float d = dens(p); if (d < 0.003) continue;
          float lt = 1.0; for (int j = 1; j <= 3; j++) { lt *= exp(-dens(p + L * 70.0 * float(j)) * 70.0 * 0.028); }
          float powder = 1.0 - exp(-d * 2.0);
          vec3 lit = mix(uSkyCol * 0.55, uSunCol, lt * powder) * mix(1.0, 0.42, uDark);
          float a = 1.0 - exp(-d * dt * 0.032); col += T * a * lit; T *= (1.0 - a); if (T < 0.02) break; }
        gl_FragColor = vec4(col, 1.0 - T); }`,
    transparent: true, depthWrite: false, side: THREE.BackSide }));
  mesh.position.set(...center); mesh.frustumCulled = false;
  mesh.userData.set = (t, cover, dark, sun, camPos, sunCol, skyCol) => {
    const u = mesh.material.uniforms; u.uT.value = t; u.uCover.value = clamp01(cover); u.uDark.value = dark; u.uSun.value.copy(sun); u.uCam.value.copy(camPos);
    if (sunCol) u.uSunCol.value.copy(sunCol); if (skyCol) u.uSkyCol.value.copy(skyCol);
  };
  return mesh;
}
export function makeLensflare(o = {}) {
  const soft = spriteTex("soft"), ring = spriteTex("ring");
  const holder = new THREE.Object3D(), flare = new Lensflare();
  flare.addElement(new LensflareElement(soft, 420, 0, new THREE.Color(o.color || 0xffe2b0)));
  flare.addElement(new LensflareElement(ring, 90, 0.35, new THREE.Color(0xffd0a0)));
  flare.addElement(new LensflareElement(soft, 60, 0.55, new THREE.Color(0xaad4ff)));
  flare.addElement(new LensflareElement(ring, 140, 0.75, new THREE.Color(0xffc8a0)));
  flare.addElement(new LensflareElement(soft, 40, 0.95, new THREE.Color(0xffffff)));
  holder.add(flare); holder.userData.flare = flare;
  return holder;
}

/* ───────── particles (Points with seeded phases; uniforms uT, uOn) ───────── */
export function makeVapour(o) {
  const N = o.n || 1400, r = rng(o.seed || 5), seed = new Float32Array(N), base = new Float32Array(N * 3), [x0, x1, z0, z1] = o.region;
  for (let i = 0; i < N; i++) { seed[i] = r(); base[i * 3] = x0 + r() * (x1 - x0); base[i * 3 + 1] = o.y || 0; base[i * 3 + 2] = z0 + r() * (z1 - z0); }
  const geo = new THREE.BufferGeometry(); geo.setAttribute("position", new THREE.BufferAttribute(base, 3)); geo.setAttribute("seed", new THREE.BufferAttribute(seed, 1));
  const mat = new THREE.ShaderMaterial({
    uniforms: { uT: { value: 0 }, uOn: { value: 0 }, uTex: { value: spriteTex("soft") }, uSun: { value: new THREE.Color(0xfff1d6) } },
    vertexShader: `attribute float seed; uniform float uT, uOn; varying float vA;
      void main(){ float life = 6.0 + seed * 4.0; float ph = mod(uT * 0.9 + seed * 37.0, life) / life;
        vec3 p = position; p.y += ph * (520.0 + seed * 420.0); p.x += sin(uT * 0.4 + seed * 20.0) * 40.0 * ph; p.z -= ph * 260.0;
        vec4 mv = modelViewMatrix * vec4(p, 1.0); gl_Position = projectionMatrix * mv;
        vA = uOn * (1.0 - ph) * smoothstep(0.0, 0.15, ph) * (0.35 + 0.65 * seed) * smoothstep(250.0, 700.0, -mv.z);
        gl_PointSize = min(170.0, (90.0 + 160.0 * seed) * (1.0 + ph * 1.6) * 900.0 / max(40.0, -mv.z)); }`,
    fragmentShader: `uniform sampler2D uTex; uniform vec3 uSun; varying float vA;
      void main(){ vec4 s = texture2D(uTex, gl_PointCoord); gl_FragColor = vec4(uSun * 1.1, s.a * vA * 0.16); }`,
    transparent: true, depthWrite: false, blending: THREE.AdditiveBlending });
  const pts = new THREE.Points(geo, mat); pts.userData.set = (t, on) => { mat.uniforms.uT.value = t; mat.uniforms.uOn.value = on; };
  return pts;
}
export function makeRain(o) {
  const N = o.n || 9000, r = rng(o.seed || 11), seed = new Float32Array(N), base = new Float32Array(N * 3), [x0, x1, z0, z1] = o.region;
  for (let i = 0; i < N; i++) { seed[i] = r(); base[i * 3] = x0 + r() * (x1 - x0); base[i * 3 + 1] = 0; base[i * 3 + 2] = z0 + r() * (z1 - z0); }
  const geo = new THREE.BufferGeometry(); geo.setAttribute("position", new THREE.BufferAttribute(base, 3)); geo.setAttribute("seed", new THREE.BufferAttribute(seed, 1));
  const mat = new THREE.ShaderMaterial({
    uniforms: { uT: { value: 0 }, uOn: { value: 0 }, uTex: { value: spriteTex("streak") }, uTop: { value: o.top || 1500 } },
    vertexShader: `attribute float seed; uniform float uT, uOn, uTop; varying float vA;
      void main(){ float h = uTop; float y = h - mod(uT * (900.0 + seed * 500.0) + seed * 4000.0, h);
        vec3 p = position; p.y = y + 80.0; p.x += (y / h) * 120.0;
        vec4 mv = modelViewMatrix * vec4(p, 1.0); gl_Position = projectionMatrix * mv;
        vA = uOn * (0.35 + 0.65 * seed) * smoothstep(40.0, 160.0, -mv.z); gl_PointSize = min(64.0, (26.0 + 30.0 * seed) * 900.0 / max(60.0, -mv.z)); }`,
    fragmentShader: `uniform sampler2D uTex; varying float vA; void main(){ vec4 s = texture2D(uTex, gl_PointCoord); gl_FragColor = vec4(vec3(0.85, 0.92, 1.0), s.a * vA * 0.55); }`,
    transparent: true, depthWrite: false, blending: THREE.NormalBlending });
  const pts = new THREE.Points(geo, mat); pts.userData.set = (t, on) => { mat.uniforms.uT.value = t; mat.uniforms.uOn.value = on; };
  return pts;
}

/* ───────── post stack ───────── */
export function makePost(renderer, scene, camera, W, H, o = {}) {
  const composer = new EffectComposer(renderer);
  composer.addPass(new RenderPass(scene, camera));
  const bloom = new UnrealBloomPass(new THREE.Vector2(W, H), o.bloom == null ? 0.22 : o.bloom, 0.6, o.bloomThreshold == null ? 0.9 : o.bloomThreshold);
  composer.addPass(bloom);
  const rays = new ShaderPass({
    uniforms: { tDiffuse: { value: null }, uSun: { value: new THREE.Vector2(0.5, 0.5) }, uAmount: { value: 0.0 } },
    vertexShader: `varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`,
    fragmentShader: `uniform sampler2D tDiffuse; uniform vec2 uSun; uniform float uAmount; varying vec2 vUv;
      float dither(vec2 p){ return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453); }
      void main(){ vec3 base = texture2D(tDiffuse, vUv).rgb; if (uAmount <= 0.001) { gl_FragColor = vec4(base, 1.0); return; }
        const int N = 64; vec2 d = (vUv - uSun) / float(N) * 0.55;
        vec2 p = vUv - d * dither(gl_FragCoord.xy); float illum = 1.0; vec3 acc = vec3(0.0);
        for (int i = 0; i < N; i++) { p -= d; vec3 s = texture2D(tDiffuse, p).rgb; float l = max(0.0, dot(s, vec3(0.3, 0.59, 0.11)) - 0.7);
          acc += s * l * illum; illum *= 0.972; }
        acc /= float(N) * 0.25;
        float edge = 1.0 - smoothstep(0.6, 1.4, length(uSun - 0.5) * 2.0);
        float sky = smoothstep(uSun.y - 0.04, uSun.y + 0.12, vUv.y);
        gl_FragColor = vec4(base + min(acc, vec3(1.2)) * (uAmount * 0.55) * edge * sky, 1.0); }` });
  composer.addPass(rays);
  const bokeh = new BokehPass(scene, camera, { focus: 900, aperture: o.aperture == null ? 0.00004 : o.aperture, maxblur: o.maxblur == null ? 0.0035 : o.maxblur });
  composer.addPass(bokeh);
  const grade = new ShaderPass({
    uniforms: { tDiffuse: { value: null }, uWarm: { value: 0.5 }, uVig: { value: o.vignette == null ? 0.42 : o.vignette }, uLift: { value: 0.0 }, uCA: { value: o.ca == null ? 1.2 : o.ca } },
    vertexShader: `varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`,
    fragmentShader: `uniform sampler2D tDiffuse; uniform float uWarm, uVig, uLift, uCA; varying vec2 vUv;
      void main(){ vec2 d = vUv - 0.5; vec2 off = d * (uCA / 1920.0) * length(d) * 4.0;
        vec3 c = vec3(texture2D(tDiffuse, vUv + off).r, texture2D(tDiffuse, vUv).g, texture2D(tDiffuse, vUv - off).b);
        float l = dot(c, vec3(0.299, 0.587, 0.114));
        vec3 shadows = vec3(0.92, 0.98, 1.08), highs = vec3(1.08, 1.0, 0.92);
        c *= mix(shadows, highs, smoothstep(0.15, 0.85, l)) * mix(vec3(1.0), vec3(1.05, 0.98, 0.9), uWarm);
        c = c * (1.0 - uLift) + uLift * 0.06;
        c *= 1.0 - uVig * smoothstep(0.35, 0.95, length(d) * 1.4);
        gl_FragColor = vec4(c, 1.0); }` });
  composer.addPass(grade);
  const film = new FilmPass(o.grain == null ? 0.16 : o.grain, false);
  composer.addPass(film);
  composer.addPass(new OutputPass());
  /* the sun on screen, for the rays and a lens flare */
  const ndc = new THREE.Vector3();
  const sunOnScreen = (sun) => { camera.updateMatrixWorld(); ndc.copy(sun).multiplyScalar(20000).add(camera.position).project(camera);
    rays.uniforms.uSun.value.set(ndc.x * 0.5 + 0.5, ndc.y * 0.5 + 0.5); return ndc.z < 1; };
  return { composer, bloom, rays, bokeh, grade, film, sunOnScreen };
}

/* ───────── camera keys and the frame loop with optional GPU motion blur ───────── */
/* keys: [t, camX, camY, camZ, lookX, lookY, lookZ] — smoothstep between keys (still between events) */
export function cameraKeys(keys) {
  return (t) => {
    let i = 0; while (i < keys.length - 2 && t > keys[i + 1][0]) i++;
    const a = keys[i], b = keys[i + 1], u = smooth(a[0], b[0], t);
    return [new THREE.Vector3(lerp(a[1], b[1], u), lerp(a[2], b[2], u), lerp(a[3], b[3], u)),
            new THREE.Vector3(lerp(a[4], b[4], u), lerp(a[5], b[5], u), lerp(a[6], b[6], u))];
  };
}
/* render(t) with window.__blur sub-frames accumulated on the GPU (grain fixed per output frame) */
export function makeFrameLoop(renderer, post, W, H, update) {
  const accRT = new THREE.WebGLRenderTarget(W, H, { type: THREE.HalfFloatType, depthBuffer: false, stencilBuffer: false });
  const quadScene = new THREE.Scene(), quadCam = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
  const accMat = new THREE.ShaderMaterial({
    uniforms: { tex: { value: null }, w: { value: 1 } }, depthTest: false, depthWrite: false, transparent: true, blending: THREE.CustomBlending,
    blendSrc: THREE.OneFactor, blendDst: THREE.OneFactor, blendEquation: THREE.AddEquation,
    vertexShader: `varying vec2 vUv; void main(){ vUv = uv; gl_Position = vec4(position.xy, 0.0, 1.0); }`,
    fragmentShader: `uniform sampler2D tex; uniform float w; varying vec2 vUv; void main(){ gl_FragColor = vec4(texture2D(tex, vUv).rgb * w, 1.0); }` });
  const copyMat = new THREE.ShaderMaterial({
    uniforms: { tex: { value: null } }, depthTest: false, depthWrite: false,
    vertexShader: `varying vec2 vUv; void main(){ vUv = uv; gl_Position = vec4(position.xy, 0.0, 1.0); }`,
    fragmentShader: `uniform sampler2D tex; varying vec2 vUv; void main(){ gl_FragColor = vec4(texture2D(tex, vUv).rgb, 1.0); }` });
  const quad = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), accMat); quadScene.add(quad);
  const { composer, film } = post;
  return function render(t) {
    const k = Math.max(1, Math.floor(window.__blur || 1));
    if (k === 1) { update(t); film.uniforms.time.value = t; composer.renderToScreen = true; composer.render(0); return; }
    const fps = window.__fps || 30, shutter = window.__shutter == null ? 0.5 : window.__shutter;
    composer.renderToScreen = false;
    const oldClear = renderer.autoClear;
    renderer.setRenderTarget(accRT); renderer.setClearColor(0x000000, 1); renderer.clear(); renderer.setRenderTarget(null);
    for (let i = 0; i < k; i++) {
      update(Math.max(0, t - (shutter / fps) * (i / k)));
      film.uniforms.time.value = t;
      composer.render(0);
      quad.material = accMat; accMat.uniforms.tex.value = composer.readBuffer.texture; accMat.uniforms.w.value = 1 / k;
      renderer.setRenderTarget(accRT); renderer.autoClear = false; renderer.render(quadScene, quadCam); renderer.autoClear = oldClear;
      renderer.setRenderTarget(null);
    }
    quad.material = copyMat; copyMat.uniforms.tex.value = accRT.texture;
    renderer.setRenderTarget(null); renderer.render(quadScene, quadCam);
  };
}
