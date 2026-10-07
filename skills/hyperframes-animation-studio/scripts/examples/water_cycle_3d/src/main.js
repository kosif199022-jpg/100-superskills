/* The water cycle as a cinematic 3D film. Everything is a function of the time t (seconds): the sun, the sea,
   the clouds, the rain, the river, the camera. Nothing reads a clock; all noise is seeded. window.__three.render(t)
   draws one frame; the composition's index.html calls it from window.render(t). */
import * as THREE from "three";
import { Sky } from "three/examples/jsm/objects/Sky.js";
import { Water } from "three/examples/jsm/objects/Water.js";
import { EffectComposer } from "three/examples/jsm/postprocessing/EffectComposer.js";
import { RenderPass } from "three/examples/jsm/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/examples/jsm/postprocessing/UnrealBloomPass.js";
import { BokehPass } from "three/examples/jsm/postprocessing/BokehPass.js";
import { FilmPass } from "three/examples/jsm/postprocessing/FilmPass.js";
import { ShaderPass } from "three/examples/jsm/postprocessing/ShaderPass.js";
import { OutputPass } from "three/examples/jsm/postprocessing/OutputPass.js";

/* ───────── seeded noise (CPU) ───────── */
function rng(seed) { let a = seed >>> 0 || 1; return () => { a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
const PERM = (() => { const r = rng(1337), p = []; for (let i = 0; i < 256; i++) p[i] = i; for (let i = 255; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [p[i], p[j]] = [p[j], p[i]]; } return p.concat(p); })();
const fade = (t) => t * t * t * (t * (t * 6 - 15) + 10);
const lerp = (a, b, t) => a + (b - a) * t;
function grad(h, x, y) { switch (h & 3) { case 0: return x + y; case 1: return -x + y; case 2: return x - y; default: return -x - y; } }
function perlin(x, y) {                                   // 2D Perlin, [-1, 1]
  const X = Math.floor(x) & 255, Y = Math.floor(y) & 255; x -= Math.floor(x); y -= Math.floor(y);
  const u = fade(x), v = fade(y), A = PERM[X] + Y, B = PERM[X + 1] + Y;
  return lerp(lerp(grad(PERM[A], x, y), grad(PERM[B], x - 1, y), u), lerp(grad(PERM[A + 1], x, y - 1), grad(PERM[B + 1], x - 1, y - 1), u), v);
}
function fbm(x, y, oct = 5, lac = 2.0, gain = 0.5) { let a = 0, w = 1, s = 0; for (let i = 0; i < oct; i++) { a += w * perlin(x, y); s += w; x *= lac; y *= lac; w *= gain; } return a / s; }
function ridged(x, y, oct = 5) { let a = 0, w = 1, s = 0; for (let i = 0; i < oct; i++) { a += w * (1 - Math.abs(perlin(x, y))); s += w; x *= 2.1; y *= 2.1; w *= 0.5; } return a / s; }
const smooth = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
const clamp01 = (x) => Math.min(1, Math.max(0, x));

/* ───────── the land: a mountain range behind a bay, a valley carved by the river ───────── */
const RIVER = (z) => 140 * Math.sin(z / 420) - 220;      // the river's x for a given z (from the peak, z=-900, to the bay, z=700)
function height(x, z) {
  const ridge = 820 * Math.exp(-Math.pow((z + 1250) / 820, 2)) * (0.55 + 0.45 * ridged(x * 0.0006 + 3.1, z * 0.0006));
  const hills = 260 * ridged(x * 0.0011 + 7.7, z * 0.0011 + 1.2) * Math.exp(-Math.pow((z + 500) / 1100, 2));
  const detail = 55 * fbm(x * 0.004, z * 0.004, 4);
  const land = smooth(900, 150, z);                         // the land sinks under the sea toward the camera
  let h = (ridge + hills + detail + 60) * land - 45 * (1 - land);
  const d = Math.abs(x - RIVER(z));
  if (z > -950 && z < 800) h -= 150 * Math.exp(-(d * d) / (2 * 55 * 55)) * smooth(-950, -700, z) * land;   // the channel
  return h;
}

export function build(canvas, W, H) {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: "high-performance", preserveDrawingBuffer: true });
  renderer.setPixelRatio(1);
  renderer.setSize(W, H, false);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 0.6;

  const scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0xc9d6e2, 0.00022);
  const camera = new THREE.PerspectiveCamera(38, W / H, 2, 60000);

  /* sky and sun */
  const sky = new Sky();
  sky.scale.setScalar(45000);
  scene.add(sky);
  const skyU = sky.material.uniforms;
  skyU.turbidity.value = 5; skyU.rayleigh.value = 2.2; skyU.mieCoefficient.value = 0.006; skyU.mieDirectionalG.value = 0.85;
  const sun = new THREE.Vector3();
  const sunLight = new THREE.DirectionalLight(0xffffff, 3.2);
  sunLight.castShadow = true;
  sunLight.shadow.mapSize.set(2048, 2048);
  const sc = sunLight.shadow.camera; sc.left = -2200; sc.right = 2200; sc.top = 2200; sc.bottom = -2200; sc.near = 100; sc.far = 9000;
  sunLight.shadow.bias = -0.0006;
  scene.add(sunLight, sunLight.target);
  const hemi = new THREE.HemisphereLight(0xbfd8ff, 0x3a4a2a, 0.55);
  scene.add(hemi);
  const flashLight = new THREE.PointLight(0xdfe9ff, 0, 5000, 1.2);
  flashLight.position.set(-300, 1100, -900);
  scene.add(flashLight);
  const fill = new THREE.DirectionalLight(0xcfe0ff, 0.0);   // a soft fill from the camera side (no shadows): the cinematographer's bounce
  scene.add(fill, fill.target);

  /* terrain */
  const SEG = 420, SIZE = 4600;
  const geo = new THREE.PlaneGeometry(SIZE, SIZE, SEG, SEG);
  geo.rotateX(-Math.PI / 2);
  const pos = geo.attributes.position, col = new Float32Array(pos.count * 3);
  const c = new THREE.Color(), snow = new THREE.Color(0xf4f7fb), rock = new THREE.Color(0x5d5a58), rock2 = new THREE.Color(0x7a6f66),
        grass = new THREE.Color(0x4e6e34), grass2 = new THREE.Color(0x6b8a3c), sand = new THREE.Color(0xb9a77a), deep = new THREE.Color(0x2f4a3a);
  for (let i = 0; i < pos.count; i++) {
    const x = pos.getX(i), z = pos.getZ(i), h = height(x, z);
    pos.setY(i, h);
  }
  geo.computeVertexNormals();
  const nrm = geo.attributes.normal;
  for (let i = 0; i < pos.count; i++) {
    const x = pos.getX(i), z = pos.getZ(i), h = pos.getY(i), slope = 1 - nrm.getY(i);
    const v = 0.5 + 0.5 * fbm(x * 0.01 + 11, z * 0.01 + 5, 3);
    if (h < -5) c.copy(deep);
    else if (h < 25) c.copy(sand).lerp(grass, smooth(5, 25, h));
    else c.copy(grass).lerp(grass2, v);
    if (h > 120) c.lerp(rock.clone().lerp(rock2, v), smooth(120, 420, h) * 0.8);
    c.lerp(rock, smooth(0.28, 0.6, slope));
    if (h > 520) c.lerp(snow, smooth(520, 700, h) * (1 - smooth(0.35, 0.7, slope)));
    col[i * 3] = c.r; col[i * 3 + 1] = c.g; col[i * 3 + 2] = c.b;
  }
  geo.setAttribute("color", new THREE.BufferAttribute(col, 3));
  const terrain = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.96, metalness: 0 }));
  terrain.castShadow = true; terrain.receiveShadow = true;
  scene.add(terrain);

  /* sea: reflects the sky, lit by the sun; normals are a generated map (no downloads) */
  const normalTex = (() => {
    const N = 512, cv = document.createElement("canvas"); cv.width = cv.height = N;
    const ctx = cv.getContext("2d"), img = ctx.createImageData(N, N), d = img.data;
    const hmap = new Float32Array(N * N);
    for (let y = 0; y < N; y++) for (let x = 0; x < N; x++) hmap[y * N + x] = fbm(x / 36, y / 36, 4) * 0.6 + fbm(x / 9 + 50, y / 9, 2) * 0.25;
    for (let y = 0; y < N; y++) for (let x = 0; x < N; x++) {
      const l = hmap[y * N + ((x - 1 + N) % N)], r = hmap[y * N + ((x + 1) % N)], u = hmap[((y - 1 + N) % N) * N + x], dn = hmap[((y + 1) % N) * N + x];
      const nx = (l - r) * 2.2, ny = (u - dn) * 2.2, len = Math.hypot(nx, ny, 1);
      const o = (y * N + x) * 4;
      d[o] = 128 + 127 * nx / len; d[o + 1] = 128 + 127 * ny / len; d[o + 2] = 128 + 127 / len; d[o + 3] = 255;
    }
    ctx.putImageData(img, 0, 0);
    const tex = new THREE.CanvasTexture(cv); tex.wrapS = tex.wrapT = THREE.RepeatWrapping; return tex;
  })();
  const water = new Water(new THREE.PlaneGeometry(30000, 30000), {
    textureWidth: 768, textureHeight: 768, waterNormals: normalTex, sunDirection: new THREE.Vector3(), sunColor: 0xffffff,
    waterColor: 0x0e4a63, distortionScale: 2.4, fog: true, size: 3.0 });
  water.rotation.x = -Math.PI / 2;
  water.position.y = 0;
  scene.add(water);

  /* a soft sprite for vapour and glow, and a streak for rain */
  function spriteTex(kind) {
    const S = 128, cv = document.createElement("canvas"); cv.width = cv.height = S; const ctx = cv.getContext("2d");
    if (kind === "soft") {
      const g = ctx.createRadialGradient(S / 2, S / 2, 0, S / 2, S / 2, S / 2);
      g.addColorStop(0, "rgba(255,255,255,1)"); g.addColorStop(0.35, "rgba(255,255,255,.55)"); g.addColorStop(1, "rgba(255,255,255,0)");
      ctx.fillStyle = g; ctx.fillRect(0, 0, S, S);
    } else {
      const g = ctx.createLinearGradient(0, 0, 0, S);
      g.addColorStop(0, "rgba(255,255,255,0)"); g.addColorStop(0.5, "rgba(255,255,255,.9)"); g.addColorStop(1, "rgba(255,255,255,0)");
      ctx.fillStyle = g; ctx.fillRect(S / 2 - 3, 0, 6, S);
    }
    return new THREE.CanvasTexture(cv);
  }
  const softTex = spriteTex("soft"), streakTex = spriteTex("streak");

  /* vapour: puffs lifting from the bay, thinning as they rise */
  const VAP = 1400, vr = rng(5), vSeed = new Float32Array(VAP), vBase = new Float32Array(VAP * 3);
  for (let i = 0; i < VAP; i++) { vSeed[i] = vr(); vBase[i * 3] = -900 + vr() * 1500; vBase[i * 3 + 1] = 0; vBase[i * 3 + 2] = -50 + vr() * 950; }
  const vGeo = new THREE.BufferGeometry();
  vGeo.setAttribute("position", new THREE.BufferAttribute(vBase, 3));
  vGeo.setAttribute("seed", new THREE.BufferAttribute(vSeed, 1));
  const vMat = new THREE.ShaderMaterial({
    uniforms: { uT: { value: 0 }, uOn: { value: 0 }, uTex: { value: softTex }, uSun: { value: new THREE.Color(0xfff1d6) } },
    vertexShader: `attribute float seed; uniform float uT, uOn; varying float vA;
      void main(){ float life = 6.0 + seed * 4.0; float ph = mod(uT * 0.9 + seed * 37.0, life) / life;
        vec3 p = position; p.y += ph * (520.0 + seed * 420.0); p.x += sin(uT * 0.4 + seed * 20.0) * 40.0 * ph; p.z -= ph * 260.0;
        vec4 mv = modelViewMatrix * vec4(p, 1.0); gl_Position = projectionMatrix * mv;
        vA = uOn * (1.0 - ph) * smoothstep(0.0, 0.15, ph) * (0.35 + 0.65 * seed) * smoothstep(250.0, 700.0, -mv.z);
        gl_PointSize = min(170.0, (90.0 + 160.0 * seed) * (1.0 + ph * 1.6) * 900.0 / max(40.0, -mv.z)); }`,
    fragmentShader: `uniform sampler2D uTex; uniform vec3 uSun; varying float vA;
      void main(){ vec4 s = texture2D(uTex, gl_PointCoord); gl_FragColor = vec4(uSun * 1.1, s.a * vA * 0.16); }`,
    transparent: true, depthWrite: false, blending: THREE.AdditiveBlending });
  const vapour = new THREE.Points(vGeo, vMat);
  scene.add(vapour);

  /* rain: streaks in a volume over the range, visible while it pours */
  const RAIN = 9000, rr = rng(11), rSeed = new Float32Array(RAIN), rBase = new Float32Array(RAIN * 3);
  for (let i = 0; i < RAIN; i++) { rSeed[i] = rr(); rBase[i * 3] = -1500 + rr() * 2200; rBase[i * 3 + 1] = 0; rBase[i * 3 + 2] = -1700 + rr() * 2000; }
  const rGeo = new THREE.BufferGeometry();
  rGeo.setAttribute("position", new THREE.BufferAttribute(rBase, 3));
  rGeo.setAttribute("seed", new THREE.BufferAttribute(rSeed, 1));
  const rMat = new THREE.ShaderMaterial({
    uniforms: { uT: { value: 0 }, uOn: { value: 0 }, uTex: { value: streakTex } },
    vertexShader: `attribute float seed; uniform float uT, uOn; varying float vA;
      void main(){ float h = 1500.0; float y = h - mod(uT * (900.0 + seed * 500.0) + seed * 4000.0, h);
        vec3 p = position; p.y = y + 80.0; p.x += (y / h) * 120.0;
        vec4 mv = modelViewMatrix * vec4(p, 1.0); gl_Position = projectionMatrix * mv;
        vA = uOn * (0.35 + 0.65 * seed) * smoothstep(40.0, 160.0, -mv.z); gl_PointSize = min(64.0, (26.0 + 30.0 * seed) * 900.0 / max(60.0, -mv.z)); }`,
    fragmentShader: `uniform sampler2D uTex; varying float vA; void main(){ vec4 s = texture2D(uTex, gl_PointCoord); gl_FragColor = vec4(vec3(0.85, 0.92, 1.0), s.a * vA * 0.55); }`,
    transparent: true, depthWrite: false, blending: THREE.NormalBlending });
  const rain = new THREE.Points(rGeo, rMat);
  scene.add(rain);

  /* clouds: a raymarched slab of seeded 3D noise, lit toward the sun, covering the range as the film asks */
  const cloudBox = new THREE.Mesh(new THREE.BoxGeometry(7000, 520, 4200), new THREE.ShaderMaterial({
    uniforms: { uT: { value: 0 }, uCover: { value: 0 }, uDark: { value: 0 }, uSun: { value: new THREE.Vector3(0, 1, 0) }, uCam: { value: new THREE.Vector3() },
                uMin: { value: new THREE.Vector3(-3500, 980, -3000) }, uMax: { value: new THREE.Vector3(3500, 1500, 1200) },
                uSkyCol: { value: new THREE.Color(0x9fb6cc) }, uSunCol: { value: new THREE.Color(0xfff2d9) } },
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
  cloudBox.position.set(0, 1240, -900);
  cloudBox.frustumCulled = false;
  scene.add(cloudBox);

  /* the river: a tube along the channel, revealed from the peak to the bay */
  const pts = [];
  for (let z = -880; z <= 840; z += 40) { const x = RIVER(z); pts.push(new THREE.Vector3(x, Math.max(height(x, z), -3) + 3.5, z)); }
  const riverCurve = new THREE.CatmullRomCurve3(pts);
  const riverGeo = new THREE.TubeGeometry(riverCurve, 220, 11, 10, false);
  {                                                         // flatten the tube into a ribbon lying in the channel
    const rp = riverGeo.attributes.position, ring = 11;
    for (let i = 0; i <= 220; i++) {
      const c = riverCurve.getPointAt(i / 220);
      for (let j = 0; j < ring; j++) { const k = i * ring + j; rp.setY(k, c.y + (rp.getY(k) - c.y) * 0.3); }
    }
    rp.needsUpdate = true;
    riverGeo.computeVertexNormals();
  }
  const riverTex = normalTex.clone(); riverTex.needsUpdate = true; riverTex.repeat.set(1, 14);
  const riverMat = new THREE.MeshPhysicalMaterial({ color: 0x6fb4d6, roughness: 0.08, metalness: 0.0, clearcoat: 1, clearcoatRoughness: 0.05,
    normalMap: riverTex, normalScale: new THREE.Vector2(0.5, 0.5), emissive: 0x1a5f85, emissiveIntensity: 0.55, transparent: true, opacity: 0.94,
    envMapIntensity: 1.0 });
  const river = new THREE.Mesh(riverGeo, riverMat);
  river.position.y = 0.5;
  river.receiveShadow = true;
  riverGeo.setDrawRange(0, 0);
  scene.add(river);
  const riverIndexCount = riverGeo.index.count;

  /* post: bloom, depth of field, grain, a teal–orange grade with a vignette, ACES output */
  const composer = new EffectComposer(renderer);
  composer.addPass(new RenderPass(scene, camera));
  const bloom = new UnrealBloomPass(new THREE.Vector2(W, H), 0.22, 0.6, 0.9);
  composer.addPass(bloom);
  const bokeh = new BokehPass(scene, camera, { focus: 900, aperture: 0.00004, maxblur: 0.0035 });
  composer.addPass(bokeh);
  const grade = new ShaderPass({
    uniforms: { tDiffuse: { value: null }, uWarm: { value: 0.5 }, uVig: { value: 0.42 }, uLift: { value: 0.0 } },
    vertexShader: `varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`,
    fragmentShader: `uniform sampler2D tDiffuse; uniform float uWarm, uVig, uLift; varying vec2 vUv;
      void main(){ vec3 c = texture2D(tDiffuse, vUv).rgb; float l = dot(c, vec3(0.299, 0.587, 0.114));
        vec3 shadows = vec3(0.92, 0.98, 1.08), highs = vec3(1.08, 1.0, 0.92);
        c *= mix(shadows, highs, smoothstep(0.15, 0.85, l)) * mix(vec3(1.0), vec3(1.05, 0.98, 0.9), uWarm);
        c = c * (1.0 - uLift) + uLift * 0.06;
        vec2 d = vUv - 0.5; c *= 1.0 - uVig * smoothstep(0.35, 0.95, length(d) * 1.4);
        gl_FragColor = vec4(c, 1.0); }` });
  composer.addPass(grade);
  const film = new FilmPass(0.16, false);
  composer.addPass(film);
  composer.addPass(new OutputPass());

  /* ───────── the film's timing: what each second does ───────── */
  const keyPos = [                                        // t, camera xyz, look-at xyz — three slow moves, stillness between
    [0.0, 1300, 90, 2600, -200, 350, -700],
    [3.0, 900, 170, 2000, -250, 380, -650],
    [6.5, 300, 400, 1250, -350, 620, -600],
    [9.5, -100, 660, 500, -400, 980, -1000],
    [12.8, -520, 640, 560, -300, 300, -600],
    [15.2, 380, 560, 1350, -150, 20, 420],
    [17.0, 1300, 540, 2700, 0, 320, -500],
  ];
  function camAt(t) {
    let i = 0; while (i < keyPos.length - 2 && t > keyPos[i + 1][0]) i++;
    const a = keyPos[i], b = keyPos[i + 1], u = smooth(a[0], b[0], t);
    const p = new THREE.Vector3(lerp(a[1], b[1], u), lerp(a[2], b[2], u), lerp(a[3], b[3], u));
    const l = new THREE.Vector3(lerp(a[4], b[4], u), lerp(a[5], b[5], u), lerp(a[6], b[6], u));
    return [p, l];
  }
  const ramp = (t, a, b) => clamp01((t - a) / Math.max(1e-3, b - a));
  const state = {};
  function update(t) {
    // sun: dawn → day → overcast → clearing
    const elev = 2.5 + 24 * smooth(0, 6.5, t) - 8 * smooth(8, 10, t) + 12 * smooth(12.5, 15.5, t);
    // the sun rises in front of the lens (behind the range), then swings to a side key light that models the land
    const azim = 195 - 80 * smooth(1.5, 7.5, t) + 12 * smooth(12, 17, t);
    const phi = THREE.MathUtils.degToRad(90 - elev), theta = THREE.MathUtils.degToRad(azim);
    sun.setFromSphericalCoords(1, phi, theta);
    skyU.sunPosition.value.copy(sun);
    const overcast = smooth(8, 10, t) * (1 - smooth(12.6, 15.5, t));
    skyU.turbidity.value = 3 + 7 * overcast;
    skyU.rayleigh.value = 1.6 - 0.9 * overcast;
    skyU.mieCoefficient.value = 0.004 + 0.02 * overcast;
    sunLight.position.copy(sun).multiplyScalar(6000).add(new THREE.Vector3(0, 0, -600));
    sunLight.target.position.set(0, 300, -700);
    const flash = Math.max(0, 1 - Math.abs(t - 10.6) / 0.09) + 0.55 * Math.max(0, 1 - Math.abs(t - 10.82) / 0.07);
    sunLight.intensity = (3.0 - 2.1 * overcast) * (0.35 + 0.65 * smooth(0, 4, t)) + flash * 0.5;
    sunLight.color.setHSL(0.08, 0.6, 0.5 + 0.5 * smooth(0, 5, t)).lerp(new THREE.Color(0xffffff), smooth(2, 6, t));
    hemi.intensity = 0.45 + 0.35 * smooth(0, 5, t) - 0.1 * overcast;
    flashLight.intensity = flash * 9000;
    renderer.toneMappingExposure = 0.5 + 0.12 * smooth(0, 5, t) - 0.08 * overcast + flash * 0.05;
    scene.fog.color.setHex(0xc9d6e2).lerp(new THREE.Color(0x9aa6b2), overcast).lerp(new THREE.Color(0xd9a57a), 1 - smooth(0, 4, t));
    scene.fog.density = 0.00011 + 0.00012 * overcast;
    // sea
    water.material.uniforms.time.value = t * 0.55;
    water.material.uniforms.sunDirection.value.copy(sun).normalize();
    water.material.uniforms.sunColor.value.copy(sunLight.color);
    water.material.uniforms.waterColor.value.setHex(0x0e4a63).lerp(new THREE.Color(0x24414f), overcast);
    // vapour, clouds, rain, river
    vMat.uniforms.uT.value = t; vMat.uniforms.uOn.value = ramp(t, 2.6, 3.6) * (1 - ramp(t, 6.2, 7.2));
    const cover = 0.42 * ramp(t, 5.8, 7.6) + 0.5 * ramp(t, 7.4, 9.4) - 0.55 * ramp(t, 12.8, 15.2) - 0.22 * ramp(t, 15.2, 17);
    const cu = cloudBox.material.uniforms;
    cu.uT.value = t; cu.uCover.value = clamp01(cover); cu.uDark.value = overcast; cu.uSun.value.copy(sun);
    cu.uSunCol.value.copy(sunLight.color).multiplyScalar(1.0 + flash * 1.6);
    cu.uSkyCol.value.setHex(0x9fb6cc).lerp(new THREE.Color(0x56616d), overcast);
    rMat.uniforms.uT.value = t; rMat.uniforms.uOn.value = ramp(t, 9.5, 10.3) * (1 - ramp(t, 12.6, 13.4));
    const rp = ramp(t, 12.6, 14.4);
    riverGeo.setDrawRange(0, Math.floor(riverIndexCount * (rp * rp * (3 - 2 * rp))));
    riverTex.offset.y = -t * 0.9;
    // camera and focus
    const [p, l] = camAt(t);
    camera.position.copy(p); camera.lookAt(l);
    fill.position.copy(p).add(new THREE.Vector3(0, 400, 0)); fill.target.position.copy(l);
    const valley = smooth(12.4, 13.4, t) * (1 - smooth(15.0, 16.0, t));
    fill.intensity = 0.35 + 2.0 * valley;
    hemi.intensity += 0.5 * valley;
    renderer.toneMappingExposure += 0.16 * valley;
    camera.fov = 38 - 4 * smooth(9.5, 12.8, t) + 4 * smooth(12.8, 15.2, t); camera.updateProjectionMatrix();
    bokeh.uniforms.focus.value = p.distanceTo(l) * 0.9;
    cu.uCam.value.copy(camera.position);
    grade.uniforms.uWarm.value = 0.75 * (1 - smooth(0, 5, t)) + 0.2;
    grade.uniforms.uLift.value = 0.08 * overcast;
    film.uniforms.time.value = t;
    state.t = t;
  }
  function render(t) {
    update(t);
    composer.render(0);
  }
  return { render, scene, camera, renderer, state };
}

window.__three = { build };
