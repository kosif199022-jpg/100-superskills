# -*- coding: utf-8 -*-
"""100 مهارة خارقة — 110: استوديو الأنيميشن الاحترافي (HyperFrames + KOSIF Motion)."""
G = [
dict(n="110", slug="hyperframes-animation-studio", ar="استوديو الأنيميشن الاحترافي (HyperFrames + KOSIF Motion)", en="HyperFrames Animation Studio",
 desc="أنيميشن احترافي سينمائي بمدة محددة من طلب واحد — مسطّح (SVG/GSAP) أو ثلاثي الأبعاد واقعي (Three.js على GPU الجهاز): تركيب HTML واحد (صيغة HyperFrames: data-composition-id/width/height/duration، "
      "وخطوط GSAP الزمنية في window.__timelines بالثواني) مع عدّة KOSIF Motion (نص عربي بأقنعة كلمات، قلم يرسم المسارات، مطر وبخار "
      "وبريق بعشوائية مبذورة، كاميرا واحدة تتحرك ككتلة، وميض، حبيبات فيلم وفينييت) وصوت محيط مركّب بـ numpy؛ يُصيَّر حتمياً إطاراً بإطار "
      "بـ HyperFrames (Puppeteer + FFmpeg) أو بمصيّر KOSIF Studio (Playwright/Edge) من الملف نفسه، ويمرّ ببوابة الثماني ثوانٍ (إطارات مفتاحية "
      "تُفحص بالعين)، وفحص HyperFrames (lint + تشغيل + تباين)، وقياس طاقة الحركة؛ مبني على دليل 500 أداة لإنتاج الفيديو حول HyperFrames.",
 trig_ar=["اعمل أنيميشن", "انيميشن احترافي", "أنيميشن 5 ثواني", "فيديو موشن", "موشن غرافيك", "فيديو تعليمي متحرك", "هايبرفريمز", "hyperframes",
          "حوّل الفكرة لفيديو", "أنيميشن بالعربي", "فيلم قصير متحرك", "شرح متحرك"],
 trig_en=["make an animation", "professional animation", "5 second animation", "motion graphics video", "explainer animation", "hyperframes",
          "html to video", "gsap timeline video", "animated explainer", "render mp4 from html", "kinetic typography arabic"],
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
     "التسليم بإيصال أدلة: الاتجاه المختار والتنفيذ، الإطارات المصيَّرة فعلاً، ما اختُبر، وما لم يُختبر أو ما عطّل؛ لا توحِ باختبار أو مراجعة لم تحدث. MP4 + index.html المصدر + لوحة الإطارات + تقرير القياس + المحرّك والمدة والحجم."],
 gates=["قائمة المشاهد بأزمنتها قبل أي كود، والمدة المطلوبة تساوي data-duration بالضبط.",
        "لا تمهيد خطي على حركة مكانية؛ الدخول أطول من الخروج؛ مجموع التدرّج < 500 مللي ثانية؛ لا شيء يتلاشى دخولاً ولا انتقال بتلاشٍ متقاطع بين المشاهد.",
        "الصوت مطبّع إلى −14 LUFS بذروة −1 dB، والتسجيل الحقيقي مقدَّم على الصوت المركّب ويُصرَّح بالبديل.",
        "فحص HyperFrames يمرّ بصفر أخطاء، أو يُذكر صراحةً أن التصيير تم بمصيّر الاستوديو مع سبب.",
        "لوحة إطارات مفتاحية فُحصت بالعين قبل التصيير الكامل.",
        "لا عشوائية غير مبذورة ولا ساعة جهاز: الإطار نفسه يُعاد إنتاجه من الزمن نفسه.",
        "النص العربي بكلمات متصلة (أقنعة كلمات لا حروف) وتباين ≥ 3:1 على خلفيته.",
        "لا أصول من CDN وقت التصيير؛ GSAP والعدّة نسختان محليتان في assets/."],
 outputs=["projects/<name>/index.html", "projects/<name>/assets/ (motion-kit.js, gsap.min.js, ambience.wav)", "frames/ + sheet.png", "out/<name>.mp4", "measure.json"],
 kw=["hyperframes", "gsap", "three.js", "cinematic", "volumetric clouds", "html video", "motion graphics", "animation", "puppeteer", "ffmpeg", "deterministic render", "arabic typography",
     "explainer", "water cycle", "kinetic", "svg animation"], scripts=True),
]
