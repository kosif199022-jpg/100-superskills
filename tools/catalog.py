import os, re, json, sys
ROOT = r"C:\Users\اغنام الوادي\Desktop\الاداة\kosif-atlas\skills"
out = []
lic_re = re.compile(r"License:\s*\*\*([^*]+)\*\*")
src_re = re.compile(r"^- Source:\s*(\S+)", re.M)
insp_re = re.compile(r"KOSIF static inspection:\s*\*\*([A-Z_]+)\*\*")
def fm(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    d = {}
    if not m: return d, text
    for line in m.group(1).splitlines():
        mm = re.match(r"^(name|description|argument-hint|license):\s*(.*)$", line)
        if mm: d[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
    body = text[m.end():]
    # multi-line description (>- or |)
    if d.get("description","") in (">", ">-", "|", "|-", ""):
        mm = re.search(r"description:\s*[>|]-?\s*\n((?:[ \t]+.*\n?)+)", m.group(1))
        if mm: d["description"] = " ".join(l.strip() for l in mm.group(1).splitlines())
    return d, body
for plugin in sorted(os.listdir(ROOT)):
    pdir = os.path.join(ROOT, plugin)
    if not os.path.isdir(pdir): continue
    lic = src = insp = ""
    sp = os.path.join(pdir, "SOURCE.md")
    if os.path.exists(sp):
        s = open(sp, encoding="utf-8", errors="ignore").read()
        m = lic_re.search(s); lic = m.group(1).strip() if m else ""
        m = src_re.search(s); src = m.group(1) if m else ""
        m = insp_re.search(s); insp = m.group(1) if m else ""
    for dp, dn, fn in os.walk(pdir):
        for f in fn:
            if f.lower() == "skill.md":
                p = os.path.join(dp, f)
                try: t = open(p, encoding="utf-8", errors="ignore").read()
                except Exception: continue
                d, body = fm(t)
                rel = os.path.relpath(p, ROOT).replace("\\", "/")
                words = len(body.split())
                scripts = sum(1 for x in os.listdir(dp) if x in ("scripts","references","reference","assets","templates","examples"))
                out.append({"plugin": plugin, "path": rel, "name": d.get("name") or os.path.basename(dp),
                            "description": (d.get("description") or "")[:600], "license": lic, "source": src,
                            "inspection": insp, "words": words, "hasdirs": scripts})
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False)
print(len(out), "skills;", sum(1 for o in out if o["license"]), "with license")
from collections import Counter
print(Counter(o["license"].split(" ")[0] for o in out).most_common(12))
print(Counter(o["inspection"] for o in out).most_common())
