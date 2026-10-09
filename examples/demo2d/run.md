# تشغيل «demo2d»

```bash
python "../../skills/claude-animation-studio/scripts/capture.py" --html index.html
python "../../skills/claude-animation-studio/scripts/encode.py" --frames frames --fps 30 --out demo2d.mp4 --gif preview.gif
python "../../skills/claude-animation-studio/scripts/qa.py" --frames frames --fps 30 --out qa.json
```
افتح index.html في المتصفح للمعاينة الحية (يعيد التشغيل تلقائياً؛ النقر يوقف). راجع contact-sheet.png قبل التسليم.
