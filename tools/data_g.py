# -*- coding: utf-8 -*-
"""100 مهارة خارقة — 110: استوديو الأنيميشن الاحترافي (HyperFrames + KOSIF Motion)."""
G = [
dict(n="110", slug="hyperframes-animation-studio", ar="استوديو الأنيميشن الاحترافي (HyperFrames + KOSIF Motion)", en="HyperFrames Animation Studio",
 desc="أنيميشن احترافي سينمائي بمدة محددة من طلب واحد — مسطّح (SVG/GSAP) أو ثلاثي الأبعاد واقعي (Three.js على GPU الجهاز): تركيب HTML واحد (صيغة HyperFrames: data-composition-id/width/height/duration، "
      "وخطوط GSAP الزمنية في window.__timelines بالثواني) مع عدّة KOSIF Motion (نص عربي بأقنعة كلمات، قلم يرسم المسارات، مطر وبخار "
      "وبريق بعشوائية مبذورة، كاميرا واحدة تتحرك ككتلة، وميض، حبيبات فيلم وفينييت) وصوت محيط مركّب بـ numpy؛ يُصيَّر حتمياً إطاراً بإطار "
      "بـ HyperFrames (Puppeteer + FFmpeg) أو بمصيّر KOSIF Studio (Playwright/Edge) من الملف نفسه، ويمرّ ببوابة الثماني ثوانٍ (إطارات مفتاحية "
      "تُفحص بالعين)، وفحص HyperFrames (lint + تشغيل + تباين)، وقياس طاقة الحركة؛ مبني على دليل 500 أداة لإنتاج الفيديو حول HyperFrames؛ KOSIF Motion v3: نظام حركة مقيس من أفلام الصف الأول، نوابض فيزيائية، موسيقى على شبكة الإيقاع، ضبابية حركة لكل صفحة، فحوص lint/sheet/speed/study، وواقعية ماء وكاوستكس وكائنات حية.",
 trig_ar=["اعمل أنيميشن", "انيميشن احترافي", "أنيميشن 5 ثواني", "فيديو موشن", "موشن غرافيك", "فيديو تعليمي متحرك", "هايبرفريمز", "hyperframes",
          "حوّل الفكرة لفيديو", "أنيميشن بالعربي", "فيلم قصير متحرك", "شرح متحرك", 'فيديو موشن احترافي', 'موشن ديزاين', 'أنيميشن واقعي', 'فيلم إطلاق منتج', 'شوريل'],
 trig_en=["make an animation", "professional animation", "5 second animation", "motion graphics video", "explainer animation", "hyperframes",
          "html to video", "gsap timeline video", "animated explainer", "render mp4 from html", "kinetic typography arabic", 'showreel', 'launch video', 'product film', 'motion design', 'realistic 3d animation', 'opus motion'],
 pipeline=[
     "الإخراج قبل المؤثر (منهج KOSIF Motion Director في references/motion-director.md): حدّد الجمهور والشعور والمخرج والمدة، ثم 2–3 اتجاهات بصرية مختلفة حقاً "
     "لكل منها استعارة من الموضوع وتكوين وسلوك مميز ومقايضة؛ اختر واحداً واكتب: الأطروحة (جملة)، الموتيف المتكرر، التكوين، المادة (خطوط، لون، ضوء، سقف عمق)، الحركة (إيقاع، تمهيد، أين يسكن).",
     "المدة والصيغة: ثوانٍ وfps وأبعاد؛ ثم قائمة مشاهد 4–7 بجمل فعلية بأزمنتها، وجسم حامل واحد، و2–3 حركات كاميرا مسمّاة، ثم «نوتة الحركة»: لكل إيقاع "
     "الموضوع/الغرض، حالة البداية، حالة النهاية، المدة/التأخير، التمهيد، المحفّز، البديل، سلوك المقاطعة.",
     "اختر أصغر تنفيذ قادر: CSS/WAAPI للحالات البسيطة، GSAP للخطوط المنسّقة، SVG للرسوم والمسارات، Three.js لتكوين فضائي حقيقي بإضاءة وكاميرا "
     "(الواقعية السينمائية: Sky model، ماء عاكس، سحب حجمية raymarch، تضاريس PBR بظلال، DOF وbloom وحبيبات وتدرّج لوني؛ تُحزَّم بـ motion.py bundle عبر esbuild "
     "وتُصيَّر على GPU الجهاز: --use-angle=d3d11 في Edge الخفي = 30× أسرع من SwiftShader). المثال: examples/water_cycle_3d.",
     "python scripts/motion.py new NAME --seconds N --fps 30 --size 1920x1080 --title «…» (و--3d لفيلم سينمائي ثلاثي الأبعاد على عدّة scripts/kit/three-kit.js: سماء وشمس وتضاريس وغابة وبحر وسحب وجسيمات وطبقة ما بعد المعالجة وكاميرا وضبابية حركة، ثم motion.py bundle) يُنشئ projects/NAME/index.html من القالب مع "
     "assets/motion-kit.js وassets/gsap.min.js (بعد npm install hyperframes gsap في scripts/).",
     "اكتب التركيب: كل حركة على خط GSAP واحد مُوقَف (paused) بالثواني (المعامل الثالث موضع مطلق)؛ سجّل window.__timelines['root'] = tl حرفياً؛ "
     "MOTION.shim('root', N) ليعمل الملف أيضاً بمصيّر الاستوديو. الأدوات: revealWords/hideWords (أقنعة كلمات صالحة للعربية)، drawPath (مع رأس سهم "
     "يهبط عند الوصول) وflowDash، rain/vapour/sparkle ببذرة، camera (المسرح كتلة واحدة)، flash، grain، vignette. أربع تمهيدات فقط: slam/snap/drive/settle.",
     "ممنوعات يثبتها فاحص HyperFrames: dir=rtl على <html> (فيديو أسود صامت) — direction: rtl على عناصر النص فقط؛ <audio> بلا id صامت؛ "
     "أسماء خطوط بلا @font-face؛ Math.random وsetTimeout وrequestAnimationFrame للحالة؛ fromTo بحالة from مرئية لعنصر يجب أن يبقى مخفياً؛ marker-end للأسهم.",
     "الصوت (بديل حين لا تسجيل مرخّصاً): python scripts/ambience.py assets/ambience.wav --seconds N --rain t0:t1 --thunder t --whoosh t1,t2 --chords 0:A,6:F — صوت محيط حتمي "
     "(بحر، ريح، وسادة أوتار، مطر، رعد، ووش) مُفتاح إلى الثواني نفسها؛ يُدرج <audio id=… data-start data-duration data-volume>.",
     "بوابة الثماني ثوانٍ: python scripts/motion.py frames NAME --times 1,4,7,… يرسم إطارات مفتاحية؛ اصنع لوحة واحدة وافحصها بالعين: "
     "أسهم شاردة، حواف المسرح عند تحريك الكاميرا، تداخل النصوص، نص يتجاوز قناعه، تباين النص على الخلفية؛ أصلح ثم أعد.",
     "python scripts/motion.py check NAME = npx hyperframes check: صفر ✗ قبل التصيير (lint + تشغيل في Chrome الخفي + تخطيط + تباين WCAG).",
     "python scripts/motion.py render NAME --engine auto --quality looks --fps 30 --out out/NAME.mp4: HyperFrames إن كان مثبتاً (عامل واحد "
     "ووضع الذاكرة المنخفضة على 8 GB)، وإلا مصيّر الاستوديو (film.py animate). --resolution 4k لرفع DPR بلا تغيير التركيب.",
     "الحركة لها كتلة: نوابض MOTION.spring (snappy/default/heavy/playful) لا منحنيات جاهزة للحركة المكانية، MOTION.track لقيمة تتغيّر هدفها مراراً، "
     "MOTION.zoomTrack للزوم اللوغاريتمي، MOTION.beats(bpm) ليقرأ الصورة والصوت ساعة واحدة؛ جداول المدد والتدرّج والتجاوز وقواعد الثلث في references/motion-craft.md.",
     "ضبابية الحركة الحقيقية للمشاهد ثلاثية الأبعاد: --blur 4 يراكم أربعة إطارات فرعية على GPU (الحبيبات ثابتة للإطار؛ الأرقام تبقى حادة)؛ للتسليم النهائي فقط.",
     "القياس: python scripts/motion.py measure out/NAME.mp4 — حصة الإطارات شبه الساكنة، الذروة، المتوسط، أطول تجميد؛ الأرضية: سكون قليل، "
     "لا قفزة واحدة ضخمة، شيء يتحرك دائماً (أرقام المرجع في 105/motion_energy.py إن وُجد مرجع).",
     "حلقة النقد (Motion Director): انظر إلى إطاراتك (لوحة اتصال + عرض هاتف + الإطار الأول)، قيّم 1–10 على ثمانية معايير (الخطّاف، المقروئية، جودة الحركة، التنوّع، "
     "التكوين، الصدق، تزامن الصوت، الهوية)، أصلح أسوأ ثلاث مشكلات بزمنها والنتيجة المطلوبة، أعد الفحص والتصيير، ثلاث جولات على الأقل، واختم بـ «ما كنت سأغيّره بعد».",
     "التسليم بإيصال أدلة: الاتجاه المختار والتنفيذ، الإطارات المصيَّرة فعلاً، ما اختُبر، وما لم يُختبر أو ما عطّل؛ لا توحِ باختبار أو مراجعة لم تحدث. MP4 + index.html المصدر + لوحة الإطارات + تقرير القياس + المحرّك والمدة والحجم.",
     "طبقة الإنتاج كما في أفضل أفلام موجة Opus 5.5 (تحليل آلاف المنشورات في references/x-trend-2026.md): البرومبت عُشر النتيجة والباقي هو الحزام: محرّك قابل للبحث seek(t)، نوابض بدل المنحنيات، شبكة إيقاع واحدة للصورة والصوت، ضبابية حركة حقيقية، وحلقة نقد يرى فيها النموذج إطاراته. ثلاثة مسارات: GSAP/HyperFrames (الافتراضي)، القماش الواحد (motion.py new NAME --canvas: ملف واحد وwindow.seek(t))، وثلاثي الأبعاد (--3d).",
     "برومبت المواصفة (XML) للأفلام المهمة: <inputs> ما تسأل عنه + الافتراضيات، <direction> الشعور والمراجع والممنوعات، <structure> قائمة حالات/لقطات على شبكة الإيقاع (120 BPM، شيء يحدث كل نبضة)، <build> قواعد المحرّك، <gotchas>، <start> اعرض قائمة الحالات قبل الكود. من مرجع: python scripts/motion.py study REF.mp4 يقيس القطعات وطول اللقطات وأول تغيّر وطاقة الحركة واللوحة ويكتب style_guide.md — خذ القواعد لا المحتوى.",
     "نظام الحركة v3 (references/craft-numbers.md — أرقام مقيسة من أفلام الصف الأول): MOTION.E (out للدخول، exit للخروج نحو القطع، cam/rest للكاميرا، inOut/whip للنقل)، MOTION.SPR (firm/soft/heavy حرجة التخميد؛ snap/pop/land لهبوط حقيقي فقط، اثنان في الفيلم)، track بنابض لكل تغيير هدف، lmix/push للزوم اللوغاريتمي، hitPulse لكل ضربة، durFor (0.35 ث + 1.35 مللي ث/بكسل)، riseWords/maskRise/typeOn/scramble/counter للنص، iris/flood/rackFocus/roll/morphPath/polarity للانتقالات (بلا تلاشٍ متقاطع)، cursor/moveCursor/press لمؤشر بفيزياء، squash/speedBlur/shot للوزن، breathe ليبقى الثبات حيّاً. لقطات حقيقية داخل التركيب: motion.py footage CLIP --out assets/clip.mp4 ثم <video data-start ...>.",
     "الصوت على الشبكة: python scripts/score.py assets/score.wav --spec score.json --cues cues.json (كِك/تصفيق/هاي-هات/باص/وسادة/نقر/لحن، رايزر، بوم، ومؤثرات مصمَّمة على إطارات التلامس: click/pop/tick/thump/whoosh/chime/type)؛ لمقطوعة جاهزة: motion.py beats TRACK.wav يعطي bpm والنبضات والضربات لتقرأها MOTION.beats(json). المزج يُعاير على −14 LUFS. ambience.py --sea 0 --drops --brook للبرك والغرف.",
     "الواقعية ثلاثية الأبعاد v3 (examples/koi_pond): makeShallowWater (ماء ترى ما تحته، يعكس الضفة الداكنة قرب الأفق والسماء فوقها، لمعة شمس، حلقات تموج من البتلات)، addCaustics (كاوستكس على ضوء الشمس المباشر + امتصاص بالعمق)، makeKoi، makePetals، makePebbles، makeBlades + addSway، makeDappledSun (شمس عبر أوراق)، envFromGradient، cameraPath. لا تبنِ بيئة من Sky (قرص الشمس يفيض في half-float فيصير NaN ويُبلّمه الـbloom مستطيلات سوداء) — makePost يضيف الآن ممر حماية.",
     "الجودة قبل التسليم: python scripts/motion.py lint NAME (حتمية، عقد، ذوق)، ثم بعد التصيير motion.py sheet FILM.mp4 (لوحة 2 إطار/ث + اختبار عرض الهاتف 360 بكسل + شريط حول لحظة سريعة + review.md بمعايير النقد) وmotion.py speed FILM.mp4 (بكسل/إطار بالتدفق البصري: >12 ضبابية، >80 أعد التصميم). التصيير النهائي: motion.py render NAME --engine studio --blur 4 (عينات مركزية حول زمن الإطار تُجمع بفاصلة عائمة لكل صفحة؛ صفحات 3D تجمع على GPU)."],
 gates=["قائمة المشاهد بأزمنتها قبل أي كود، والمدة المطلوبة تساوي data-duration بالضبط.",
        "لا تمهيد خطي على حركة مكانية؛ الدخول أطول من الخروج؛ مجموع التدرّج < 500 مللي ثانية؛ لا شيء يتلاشى دخولاً ولا انتقال بتلاشٍ متقاطع بين المشاهد.",
        "الصوت مطبّع إلى −14 LUFS بذروة −1 dB، والتسجيل الحقيقي مقدَّم على الصوت المركّب ويُصرَّح بالبديل.",
        "فحص HyperFrames يمرّ بصفر أخطاء، أو يُذكر صراحةً أن التصيير تم بمصيّر الاستوديو مع سبب.",
        "لوحة إطارات مفتاحية فُحصت بالعين قبل التصيير الكامل.",
        "لا عشوائية غير مبذورة ولا ساعة جهاز: الإطار نفسه يُعاد إنتاجه من الزمن نفسه.",
        "النص العربي بكلمات متصلة (أقنعة كلمات لا حروف) وتباين ≥ 3:1 على خلفيته.",
        "لا أصول من CDN وقت التصيير؛ GSAP والعدّة نسختان محليتان في assets/.",
       'frame 0 مركَّب ويتحرك؛ تغيّر مرئي كل ~0.7 ث؛ ثبات مقصود واحد ≤ 1.6 ث تحت صمت موسيقي؛ أكبر ذروة طاقة عند ~80% من المدة.', 'لا تلاشٍ متقاطع ولا ارتداد إلا على هبوط حقيقي؛ نص يُقرأ ≤ 3 بكسل/إطار؛ لا عنصر أسرع من ~80 بكسل/إطار (motion.py speed).', 'motion.py lint بلا أخطاء، وsheet مفحوصة بالعين مع review.md مكتوب لثلاث جولات على الأقل، وخاتمة «ما كنت سأغيّره بعد».'],
 outputs=["projects/<name>/index.html", "projects/<name>/assets/ (motion-kit.js, gsap.min.js, ambience.wav)", "frames/ + sheet.png", "out/<name>.mp4", "measure.json"],
 kw=["hyperframes", "gsap", "three.js", "cinematic", "volumetric clouds", "html video", "motion graphics", "animation", "puppeteer", "ffmpeg", "deterministic render", "arabic typography",
     "explainer", "water cycle", "kinetic", "svg animation"], scripts=True),
]

# ── KOSIF Motion v3.1 / v3.2: the sound drives the world (kloss), real motion drives bodies (aicreataro), and the
#    montage, QA and lighting capabilities taken from KOSIF Omni (Ultra Motion & Montage, Lighting, Vision, Aesthetics) ──
G[0]["desc"] += (" v3.1: الصوت يقود العالم — قنوات لكل إطار من الموسيقى (كِك، باص، بدايات، صمت، توقف الشريط) وساعة شريط تُجمّد "
                 "المشهد حين يتوقف التسجيل، وأرض من الطيف، وغلتش مفتاحه التحليل، والتقاط حركة حقيقية من فيديو إلى جسيمات؛ "
                 "v3.2 من KOSIF Omni: مونتاج أي لقطات على الإيقاع مع زووم نبضي وتلوين وتخفيض موسيقى تحت الصوت وترجمة كاريوكي عربية، "
                 "وبوابة تسليم (أسود/تجمّد/LUFS/ذروة/تعريض)، وإضاءة بالوقفات والكلفن.")
G[0]["trig_ar"] += ["مونتاج على الإيقاع", "مونتاج ذكي", "ترجمة كاريوكي", "سبتايتل عربي متحرك", "أنيميشن على الموسيقى", "فيديو يتحرك مع الصوت"]
G[0]["trig_en"] += ["beat-synced montage", "audio reactive animation", "music visualizer", "karaoke captions", "auto edit footage", "tape stop"]
G[0]["pipeline"] += [
    "الصوت يقود الصورة (منهج kloss «استمع بالرياضيات»): python scripts/motion.py channels assets/score.wav --out src/channels.json "
    "→ قنوات لكل إطار (kicks, onsets, bass/mid/high, centroid, silence, pitch_dive/rise, speed, tape) + spectrogram.png وspectrum_height.png؛ "
    "في الصفحة const C = MOTION.channels(json) ثم C.kick(t) وC.onset(t) وC.v('bass', t) وC.tape(t). شغّل العالم على ساعة الشريط والكاميرا "
    "وحدها على ساعة الحائط: حين يتوقف الشريط يتجمّد كل شيء والكاميرا تدور حوله (زمن الرصاصة). three-kit: spectrumOnTape وmakeSpectrumGround "
    "(أرض من الطيف: نهر باص في الوسط، توافقيات على الجدران، حمم في أعلى الخلايا فقط) وmakeGlitchPass (chroma/slice/negative/mono/warp كلمسات لا كحالة دائمة) "
    "وmakeSparks؛ score.py يكتب توقف الشريط (tape_stops_s) وmotion.py loopcheck يثبت خياطة الحلقة. مثال: examples/sound_ground.",
    "حركة حقيقية (منهج aicreataro): فيديو بكاميرا ثابتة لمؤدٍّ حقيقي → python scripts/motion.py mocap clip.mp4 --out body.json → "
    "makeParticleBody(json) جسم من جسيمات يتحرك تماماً كالمؤدي؛ loadModel(url) لنموذج GLB بحركته مضبوطة على t؛ addWave للقماش والأعلام.",
    "التعليق الصوتي بلا إنترنت: python scripts/voice.py vo.wav --script lines.json --voice Naayf (أصوات Windows OneCore) → vo.wav + توقيتات؛ "
    "<audio data-role=\"voice\"> فيخفض الدمج الموسيقى تحته (sidechain) ثم −14 LUFS.",
    "مونتاج أي لقطات (من Ultra Motion & Montage في KOSIF Omni): python scripts/montage.py cut a.mp4 b.mp4 --music track.wav --seconds 15 "
    "--ratio 9:16 --grade teal_orange [--voice vo.wav --captions vo.json] --out film.mp4 — خطة لقطات سريعة (~1 ث) ومتنفّسة (~3 ث) كل قطع على نبضة "
    "والمتنفسة تنتهي على الضربة الأولى، أنشط نافذة غير مستعملة من كل لقطة، زووم نبضي يضرب ويخمد على الضربات الأولى، تلوين (7 قوالب)، قطع حادة، "
    "تخفيض الموسيقى تحت الصوت، −14 LUFS وذروة ≤ −1. الترجمة: montage.py captions VIDEO --spec caps.json (حدث لكل كلمة منطوقة، Encoding −1 ليبقى ترتيب العربية صحيحاً).",
    "بوابة التسليم: python scripts/motion.py inspect out/NAME.mp4 [--allow 6.6-7.3] — yuv420p/H.264، لا إطارات سوداء فعلاً (الإظلام عند الطرفين مسموح)، "
    "لا تجمّد غير مقصود، LUFS ضمن ±1.5 والذروة الحقيقية ≤ −1، ونسب البياض المحروق والسواد المسحوق على إطارات العينة.",
    "الإضاءة كما في موقع التصوير (KOSIF Lighting): lightRig(scene, {key, fillStops: 2, rimStops: 0.5, keyK: 5600, fillK: 6500, rimK: 4300}) — "
    "تعبئة أقل بوقفتين = نسبة إضاءة 5:1؛ kelvin(K) لون حرارة اللون؛ gel(fromK, toK) فلتر CTO/CTB؛ falloffStops(d1, d2) للتلاشي بمربع المسافة.",
    "جولة النقد بمراجعَين ومُصلح: review.md يرتّب الملاحظات P0 (يكسر الفيلم) / P1 (يبدو مولَّداً) / P2 (ذوق)، ويمرّ على العدسات الاثنتي عشرة لمجلس الجماليات "
    "(المكان، الشخصية، الفعل، الكاميرا، الضوء، اللون، المؤثرات، الجو، المواد، تصميم الإنتاج، التكوين، الجمال)؛ لا يُصلَح إلا ما يُشار إليه على إطار.",
]
G[0]["gates"] += [
    "motion.py inspect يمرّ (ok: true) قبل التسليم، وكل تجمّد مقصود مذكور في --allow.",
    "في الأفلام الموسيقية: كل قيمة تتفاعل مع الصوت تُقرأ من channels.json لا من تقدير؛ والعالم على ساعة الشريط إن وُجد توقف.",
    "الترجمة العربية تُفحص على إطار مصيَّر: ترتيب الكلمات صحيح والكلمة المنطوقة وحدها مميّزة.",
]
G[0]["outputs"] += ["src/channels.json + spectrogram.png (أفلام الصوت)", "out/NAME.montage.json (خطة المونتاج)", "inspect JSON (بوابة التسليم)"]

# ── v3.3: the owner's reference books (Gurney, Joel Grimes, Night Photography, Veo 3 guide, 360° character sheet, colour theory) ──
G[0]["desc"] += (" v3.3 من مكتبة الكتب: لغة لقطات حتمية من مفردات Veo (من أسفل، تتبّع، رافعة، دوران، دولي-زوم، يدوي، لوحة 360°)، "
                 "وإضاءة رامبرانت/كلامشيل/حواف، ومنظور جوي بثلاث قنوات ورؤية ليلية وقناع ألوان (جورني)، وتعريض طويل يرسم مسارات الضوء.")
G[0]["trig_ar"] += ["لقطة من أسفل", "دولي زوم", "إضاءة رامبرانت", "تعريض طويل", "مسارات ضوء", "الساعة الزرقاء", "منظور جوي"]
G[0]["trig_en"] += ["dolly zoom", "rembrandt lighting", "long exposure", "light trails", "blue hour", "aerial perspective", "shot list camera"]
G[0]["pipeline"] += [
    "لغة اللقطات (دليل Veo 3 + لوحة الشخصية 360°): shot('low_angle'|'tracking'|'crane_up'|'push_in'|'orbit'|'handheld'|'dolly_zoom'|'whip_pan'|'turntable'…) "
    "أو shotFromWords('low angle tracking shot') ثم sequence([{at, shot}]) بقطع حاد؛ الدولي-زوم يثبّت ارتفاع الموضوع في الكادر بالضبط؛ "
    "turntable يصوّر الشخصية أمام/جانب/خلف/جانب كلوحة استمرارية قبل التحريك.",
    "الإضاءة (Joel Grimes): lightPreset(scene, 'rembrandt'|'clamshell'|'edgy'|'ultrasoft'|'short'|'broad'|'sun')؛ النعومة = حجم المصدر الظاهر "
    "(softnessDeg) لا قوته. اللون (Gurney): aerialPerspective() بلون ضباب = لون أفق السماء، fogTowardSun() للمنظور الجوي العكسي، "
    "skyBounce() (الظلال المتجهة لأعلى باردة ولأسفل دافئة)، lightColor('sodium'|'moonlight'|'mercury_vapor'…)، makeLookPass({gamut, night, split})، "
    "harmony()/MOTION.palette()، وmakeRenderer({tone: 'agx'}) ليحفظ لون المصابيح في الإضاءات العالية.",
    "التعريض الطويل (Night Photography): motion.py render --blur 16 --shutter 30 --stack lighten — ثانية تعريض لكل إطار مكدّسة بالأفتح "
    "(مسارات السيارات وأقواس النجوم)؛ الضوء الأسرع من حجمه بين عيّنتين يرسم نقاطاً فمُدّه بـ trailLength(speed). --stack average بغالق طويل = ماء حريري. "
    "مثال: examples/blue_hour.",
]
G[0]["gates"] += ["في مشاهد الضباب: لون الضباب يساوي لون أفق السماء (وإلا تنتهي الأشكال البعيدة أغمق من السماء)؛ والتعريض الطويل بلا مسارات منقّطة."]
