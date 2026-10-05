# سجل الاختبارات (2026-10-05، Windows 11، Python 3.13، ffmpeg 9.0، Edge headless عبر Playwright)

| # | ما اختُبر | الأمر | النتيجة |
|---|---|---|---|
| 1 | فهرسة الأطلس | `python tools/catalog.py` | 15,122 مهارة من 3,691 إضافة؛ 12,914 MIT و2,064 Apache |
| 2 | بناء المئة مهارة | `python tools/build.py` | 100 مجلد SKILL.md + references/sources.md، كل مهارة بـ 8 مصادر مطابقة |
| 3 | أنيميشن 2D كامل | `new_scene.py --ratio 9:16 --dur 6` ثم `capture.py` ثم `encode.py` ثم `qa.py` | 180 إطاراً في 1080×1920، MP4 h264 yuv420p، لوحة تحقق، QA = PASS (المثال في `examples/demo2d/`) |
| 4 | أنيميشن 3D (Three.js) | نفس المسار بـ `--kind 3d --ratio 16:9 --dur 4` | 120 إطاراً في 1920×1080 عبر Edge headless (WebGL + Bloom)، MP4، QA = PASS بعد جعل الإيقاعات نسبية وإضاءة الافتتاح أعلى |
| 5 | باني البرومبت | `prompt_build.py brief.json` | ولّد البرومبت + 3 حالات اختبار + نسختي A/B + أسئلة النقاط العمياء (148 كلمة) |
| 6 | فاحص البرومبت | `prompt_lint.py p1.md --kind task --untrusted` | PASS بدرجة 100/100 |
| 7 | فاحص البرومبت على برومبت رديء | `prompt_lint.py bad.md` | BLOCK بدرجة 20/100: مدخل غير مسوّر، لغة غير محددة، لا صيغة إخراج (كما هو متوقع) |
| 8 | مصنع برومبتات الصور | `image_prompt_forge.py spec.json` | 6 صيغ (Midjourney، Flux، SDXL، ChatGPT، Ideogram، NanoBanana) + تنبيه النص العربي؛ خروج 0 |
| 9 | مخرج برومبتات الفيديو | `video_prompt_forge.py shots.json --platforms veo,sora` | لقطتان × منصتان، قصّ المدة الزائدة إلى حد المنصة؛ خروج 0 |
| 10 | فاحص الإكسل | `xlsx_check.py t.xlsx` على ملف مولّد بـ openpyxl | كشف رقماً كنص (F3)، وقيمة ثابتة وسط عمود صيغ (F5)، وVLOOKUP قديمة؛ REVISE كما هو متوقع |

## ما لم يُختبر هنا (قل «not-executed» حتى يُشغَّل)
- السكربتات داخل claude.ai أو ChatGPT (المهارات هناك منهجيات؛ السكربتات تحتاج بيئة تنفيذ).
- `capture.py` على Linux/macOS بلا Edge (المسار البديل: `python -m playwright install chromium`).
- دقة البرومبتات على المولّدات نفسها (Midjourney وVeo…) تحتاج توليداً فعلياً ومراجعة بصرية.

## إعادة التشغيل
```text
python tools/build.py
cd examples/demo2d && python ../../skills/claude-animation-studio/scripts/capture.py --html index.html
```
