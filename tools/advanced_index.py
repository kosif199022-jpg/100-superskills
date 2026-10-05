#!/usr/bin/env python3
"""الفهرس المتقدم: دمج الفهارس الثلاثة في طبقة واحدة متسقة.

1. الفهرس الآلي (tools/atlas-deep.json): الوسوم بكثافة الذكر لكل ألف كلمة، والسكربتات والمراجع والأدوات وكتل الكود.
2. القراءة المحلية (هذا الملف يعيد تدريجها بمُدرِّج أدلة v2): خصوصية/إجرائية/اكتمال/أمان 1–5 مع أعلام خطر.
3. فهرس المهارات الخارقة (skills/*/references/sources.md): أي مصادر أطلس تغذّي كل مهارة من الـ108.

المخرجات:
- ADVANCED-INDEX.md  التقرير الموحّد (درجة مركبة لكل مهارة ولكل وسم، أفضل 10 لكل وسم بعد إزالة التكرار، أفضل 50 عموماً، خريطة المهارات الخارقة ← مصادرها).
- tools/deep-read/cards.jsonl  بطاقات v2 لكل مهارة (المخطط نفسه).
- DEEP-READ.md  أعيد بناؤه من بطاقات v2.
- tools/atlas-deep.sqlite  جدولا grade وskill_tag وview باسم advanced_skill.

usage: python tools/advanced_index.py [--atlas PATH]
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
STATE = TOOLS / "deep-read"
DEEP_JSON = TOOLS / "atlas-deep.json"
DEEP_DB = TOOLS / "atlas-deep.sqlite"
DEFAULT_ATLAS = ROOT.parent / "kosif-atlas" / "skills"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ------------------------------------------------------------------ أنماط الأدلة
RX = {
    "code_block": re.compile(r"^```", re.M),
    "cmd": re.compile(r"^\s*(?:\$\s*)?(?:python3?|node|npx|npm|pnpm|yarn|bash|sh|ffmpeg|ffprobe|curl|git|docker|kubectl|pip|uv|cargo|go|make|gh|wrangler|soffice|magick|convert)\s+\S", re.M),
    "path": re.compile(r"(?<![\w/])[\w.-]+/[\w./-]+\.(?:py|js|ts|tsx|mjs|sh|json|yaml|yml|md|csv|xlsx|html|css|sql|toml)\b"),
    "number_unit": re.compile(r"\b\d+(?:\.\d+)?\s?(?:%|ms|s\b|sec|px|fps|LUFS|dB|dBTP|MB|KB|GB|kHz|Hz|mm|tokens?)"),
    "table": re.compile(r"^\|\s*-{3,}", re.M),
    "marketing": re.compile(r"\b(world-class|best-in-class|cutting-edge|state-of-the-art|seamless(?:ly)?|powerful|revolutionary|effortless(?:ly)?|game-changing|ultimate|comprehensive solution|production-ready)\b", re.I),
    "destructive": re.compile(r"(rm\s+-rf|git\s+push\s+--force|--force-with-lease|DROP\s+(?:TABLE|DATABASE)|DELETE\s+FROM\s+\w+\s*;|del\s+/[sq]|Remove-Item\s+-Recurse|kubectl\s+delete|terraform\s+destroy|:\(\)\s*\{)", re.I),
    "guard": re.compile(r"\b(confirm(?:ation)?|dry[- ]run|backup|rollback|ask (?:the )?user|before (?:deleting|removing)|irreversible|never (?:delete|remove|force)|--yes|approval)\b", re.I),
    "paid": re.compile(r"\b(API[_ ]KEY|api key|access token|paid|credits|billing|subscription|pricing|\$\d+)\b", re.I),
    "secret_leak": re.compile(r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,})"),
    "outdated": re.compile(r"\b(gpt-3(?:\.5)?(?:-turbo)?|text-davinci|claude[- ]2(?:\.\d)?|claude-instant|gpt-4-0613|palm\s?2|bard)\b", re.I),
    "md_links": re.compile(r"\]\((?:\.{0,2}/)?[\w./-]+\.md\)"),
    "heading": re.compile(r"^#{1,4}\s+(.+?)\s*$", re.M),
}
SECTION_GROUPS = {
    "overview": r"overview|purpose|what (?:it|this) does|summary|نظرة|الغرض",
    "prereq": r"prereq|requirements?|setup|install|dependenc|متطلب|تثبيت",
    "steps": r"steps?|workflow|process|procedure|instructions?|how to|usage|pipeline|خطوات|طريقة|الاستخدام",
    "output": r"outputs?|deliverables?|results?|returns?|المخرج|النتيج",
    "errors": r"error|troubleshoot|pitfall|gotcha|common (?:issues|mistakes)|limitations?|caveats?|أخطاء|مشاكل",
    "examples": r"examples?|sample|demo|أمثلة|مثال",
    "quality": r"checklist|validation|verify|quality|testing|acceptance|بوابة|تحقق|فحص",
}
MARKETING_WORDS = RX["marketing"]


def frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip("'\"")
    return fm, text[m.end():]


def clamp(v: float, lo=1, hi=5) -> int:
    return int(max(lo, min(hi, round(v))))


def grade(body: str, e: dict) -> dict:
    """مُدرِّج أدلة v2: كل درجة تُشتق من عدّ أدلة ملموسة في النص وهيكل المجلد."""
    words = max(1, len(body.split()))
    code_blocks = len(RX["code_block"].findall(body)) // 2
    cmds = len(RX["cmd"].findall(body))
    paths = len(set(RX["path"].findall(body)))
    nums = len(RX["number_unit"].findall(body))
    tables = len(RX["table"].findall(body))
    marketing = len(MARKETING_WORDS.findall(body))
    scripts = len(e.get("scripts") or [])
    refs = int(e.get("refs") or 0)
    evals = int(e.get("has_evals") or 0)
    heads = [h.lower() for h in RX["heading"].findall(body)]
    sections = {g: any(re.search(p, h) for h in heads) for g, p in SECTION_GROUPS.items()}
    md_links = len(RX["md_links"].findall(body))

    # الخصوصية: أدلة ملموسة لكل ألف كلمة + مطلقة
    spec_pts = min(code_blocks, 8) * 0.35 + min(cmds, 10) * 0.25 + min(paths, 10) * 0.15 + min(nums, 12) * 0.15 + min(tables, 4) * 0.3
    spec = 1 + spec_pts
    spec -= min(marketing, 4) * 0.4
    if words < 120:
        spec = min(spec, 2)
    specificity = clamp(spec)

    # الإجرائية: هل يستطيع وكيل تنفيذه مباشرة؟
    act = 1 + min(scripts, 4) * 0.7 + min(cmds, 6) * 0.35 + (0.6 if sections["steps"] else 0) + (0.5 if sections["errors"] else 0) + (0.3 if sections["prereq"] else 0)
    if words < 120:
        act = min(act, 2)
    actionability = clamp(act)

    # الاكتمال: تغطية دورة الحياة + العمق
    cov = sum(sections.values())
    compl = 1 + cov * 0.55 + min(math.log1p(words) / 2.2, 2.2) * 0.5 + min(refs, 8) * 0.1 + evals * 0.5
    if md_links >= 8 and words < 900:
        compl -= 0.6  # ملف محوري يحيل أكثر مما يشرح
    completeness = clamp(compl)

    # الأمان
    destructive = RX["destructive"].findall(body)
    guards = RX["guard"].findall(body)
    safe = 4
    if destructive and not guards:
        safe = 2
    elif destructive and guards:
        safe = 4
    elif guards:
        safe = 5
    if RX["secret_leak"].search(body):
        safe = 1
    safety = clamp(safe)

    overall = clamp(0.35 * specificity + 0.30 * actionability + 0.25 * completeness + 0.10 * safety)

    flags = []
    if specificity <= 2:
        flags.append("vague")
    if marketing >= 3:
        flags.append("marketing-fluff")
    if destructive and not guards:
        flags.append("destructive-actions")
    if RX["paid"].search(body):
        flags.append("needs-paid-api")
    if RX["outdated"].search(body):
        flags.append("outdated")
    if RX["secret_leak"].search(body):
        flags.append("security-risk")
    if words < 80:
        flags.append("stub")
    if md_links >= 8 and words < 900:
        flags.append("hub-doc")
    if not flags:
        flags.append("none")

    evidence = {"code_blocks": code_blocks, "commands": cmds, "paths": paths, "numbers": nums, "tables": tables,
                "marketing": marketing, "scripts": scripts, "refs": refs, "evals": evals, "sections": [k for k, v in sections.items() if v], "md_links": md_links}
    reasons = (f"أدلة: {code_blocks} كتلة كود، {cmds} أمر، {paths} مسار، {nums} قيمة بوحدة، {tables} جدول، {scripts} سكربت، {refs} مرجع"
               + (f"، {marketing} كلمة تسويقية" if marketing else "") + f"؛ أقسام: {', '.join(evidence['sections']) or 'لا شيء'}؛ {words} كلمة.")
    return {"specificity": specificity, "actionability": actionability, "completeness": completeness, "safety": safety,
            "overall": overall, "reasons": reasons, "flags": flags, "evidence": evidence}


def extract_lists(body: str) -> dict:
    """قدرات ومدخلات ومخرجات من العناوين والقوائم (استخراج هيكلي لا توليدي)."""
    out = {"capabilities": [], "inputs": [], "outputs": []}
    heads = RX["heading"].findall(body)
    out["capabilities"] = [h.strip("# ").strip()[:80] for h in heads[1:13] if 3 <= len(h) <= 90]
    for key, pat in (("inputs", SECTION_GROUPS["prereq"]), ("outputs", SECTION_GROUPS["output"])):
        m = re.search(r"^#{1,4}\s+(?:" + pat + r")[^\n]*\n(.*?)(?=^#{1,4}\s|\Z)", body, re.S | re.M | re.I)
        if m:
            items = re.findall(r"^\s*(?:[-*]|\d+\.)\s+(.+)$", m.group(1), re.M)
            out[key] = [re.sub(r"[*`]", "", i).strip()[:100] for i in items[:8]]
    return out


def load_manual_cards() -> dict:
    f = STATE / "cards.sample-human.jsonl"
    cards = {}
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            try:
                c = json.loads(line)
                cards[c["path"]] = c
            except Exception:
                pass
    return cards


def superskill_sources() -> dict[str, list[tuple[str, str]]]:
    """slug → [(atlas skill name, plugin)] من references/sources.md لكل مهارة خارقة."""
    out = {}
    for sdir in sorted((ROOT / "skills").iterdir()):
        f = sdir / "references" / "sources.md"
        if not f.exists():
            continue
        names = re.findall(r"^## ([\w.-]+) \(([\w.-]+)\)", f.read_text(encoding="utf-8"), re.M)
        out[sdir.name] = names
    return out


def composite(overall: int, density: float, ev: dict) -> float:
    rel = min(1.0, density / 25.0)
    evidence = overall / 5.0
    struct = min(1.0, ev["scripts"] * 0.25 + min(ev["refs"], 8) * 0.05 + ev["evals"] * 0.2 + min(ev["code_blocks"], 10) * 0.03)
    return round(100 * (0.40 * evidence + 0.40 * rel + 0.20 * struct), 1)


def evidence_from_json(e: dict) -> dict:
    cl = e.get("code_langs") or {}
    if isinstance(cl, str):
        try:
            cl = json.loads(cl.replace("'", '"'))
        except Exception:
            cl = {}
    return {"scripts": len(e.get("scripts") or []), "refs": int(e.get("refs") or 0), "evals": int(e.get("has_evals") or 0),
            "code_blocks": int(sum(cl.values())) if isinstance(cl, dict) else 0}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--atlas", default=str(DEFAULT_ATLAS))
    ap.add_argument("--from-cache", action="store_true", help="أعد الترتيب والتقارير من cards.jsonl بلا إعادة قراءة الأطلس")
    a = ap.parse_args()
    atlas = Path(a.atlas)
    data = json.loads(DEEP_JSON.read_text(encoding="utf-8"))
    by_path = {e["path"]: e for e in data}
    manual = load_manual_cards()
    STATE.mkdir(parents=True, exist_ok=True)

    cards, grades, skill_tags = [], {}, []
    titles = {}
    cached = {}
    if a.from_cache and (STATE / "cards.jsonl").exists():
        for line in (STATE / "cards.jsonl").read_text(encoding="utf-8").splitlines():
            try:
                c = json.loads(line); cached[c["path"]] = c
            except Exception:
                pass
        print(f"cache: {len(cached):,} cards", flush=True)
    for i, e in enumerate(data):
        c0 = cached.get(e["path"])
        if c0 is not None:
            q = c0["quality"]
            g = {"specificity": q["specificity"], "actionability": q["actionability"], "completeness": q["completeness"], "safety": q["safety"],
                 "overall": q["overall"], "reasons": q["reasons"], "flags": c0.get("risks_flags") or ["none"],
                 "evidence": c0.get("evidence") or {**evidence_from_json(e), "sections": [], "md_links": 0}}
            lists = {"capabilities": c0.get("capabilities") or [], "inputs": c0.get("inputs") or [], "outputs": c0.get("outputs") or []}
            fm = {}
        else:
            p = atlas / e["path"]
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            fm, body = frontmatter(text)
            g = grade(body, e)
            lists = extract_lists(body)
        td = e.get("tag_density") or {}
        if isinstance(td, str):
            try:
                td = json.loads(td.replace("'", '"'))
            except Exception:
                td = {}
        m = manual.get(e["path"])
        if m and m.get("domain"):  # القراءة اليدوية تثبّت المجال الأساسي بصلة لا تقل عن 10/k
            td = dict(td); td[m["domain"]] = max(float(td.get(m["domain"], 0)), 10.0)
        tags = sorted(td.items(), key=lambda kv: -kv[1])
        domain = tags[0][0] if tags else "other"
        secondary = [t for t, d in tags[1:] if d >= 3][:4]
        max_density = tags[0][1] if tags else 0.0
        if m:  # القراءة اليدوية تتقدّم على المُدرِّج
            g["overall"] = int(m["quality"]["overall"]); g["specificity"] = int(m["quality"]["specificity"])
            g["actionability"] = int(m["quality"]["actionability"]); g["completeness"] = int(m["quality"]["completeness"])
            g["safety"] = int(m["quality"]["safety"]); g["reasons"] = m["quality"]["reasons"]; g["flags"] = m.get("risks_flags") or g["flags"]
            domain = m.get("domain") or domain
        comp = composite(g["overall"], max_density, g["evidence"])
        desc = (fm.get("description") or e.get("description") or "").strip().replace("\n", " ")
        titles[e["path"]] = desc
        card = {
            "path": e["path"], "plugin": e["plugin"], "name": e["name"],
            "summary_ar": m["summary_ar"] if m else "", "summary_en": m["summary_en"] if m else desc[:220],
            "what_it_does": m["what_it_does"] if m else desc[:400],
            "domain": domain, "subdomain": m.get("subdomain", "") if m else "", "secondary_domains": secondary,
            "capabilities": m["capabilities"] if m else lists["capabilities"], "procedure_steps": len(g["evidence"]["sections"]),
            "inputs": m["inputs"] if m else lists["inputs"], "outputs": m["outputs"] if m else lists["outputs"],
            "requires": m["requires"] if m else {"tools": e.get("tools") or [], "apis_keys": ["(يذكر مفاتيح/دفع)"] if "needs-paid-api" in g["flags"] else [], "platforms": []},
            "has_concrete_examples": "examples" in g["evidence"]["sections"] or g["evidence"]["code_blocks"] >= 2,
            "has_quality_gates": "quality" in g["evidence"]["sections"] or bool(g["evidence"]["evals"]),
            "has_scripts": g["evidence"]["scripts"] > 0,
            "quality": {k: g[k] for k in ("specificity", "actionability", "completeness", "safety", "overall", "reasons")},
            "unique_value": m["unique_value"] if m else "", "risks_flags": g["flags"],
            "superskills": m.get("superskills", []) if m else [], "keywords": m["keywords"] if m else [e["name"]] + (e.get("tools") or [])[:10],
            "composite": comp, "max_tag_density": max_density, "words": int(e.get("words") or 0), "richness": float(e.get("richness") or 0),
            "scripts": e.get("scripts") or [], "refs": int(e.get("refs") or 0), "evals": int(e.get("has_evals") or 0), "license": e.get("license"),
            "evidence": g["evidence"],
            "truncated": False, "model": "manual read (Claude)" if m else "evidence grader v2",
        }
        cards.append(card)
        grades[e["path"]] = card
        for t, d in td.items():
            skill_tags.append((e["path"], t, float(d), composite(g["overall"], float(d), g["evidence"])))
        if (i + 1) % 2000 == 0:
            print(f"  {i+1} graded…", flush=True)

    # ---------------------------------------------------------------- cards.jsonl v2 + JSON
    with open(STATE / "cards.jsonl", "w", encoding="utf-8") as f:
        for c in cards:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    (TOOLS / "atlas-deep-read.json").write_text(json.dumps(cards, ensure_ascii=False), encoding="utf-8")

    # ---------------------------------------------------------------- SQLite
    db = sqlite3.connect(str(DEEP_DB))
    db.executescript("""
    DROP TABLE IF EXISTS grade; DROP TABLE IF EXISTS skill_tag; DROP VIEW IF EXISTS advanced_skill;
    DROP TABLE IF EXISTS card; DROP TABLE IF EXISTS card_fts;
    CREATE TABLE grade(path TEXT PRIMARY KEY, specificity INT, actionability INT, completeness INT, safety INT, overall INT,
        composite REAL, domain TEXT, secondary TEXT, flags TEXT, reasons TEXT, model TEXT);
    CREATE TABLE skill_tag(path TEXT, tag TEXT, density REAL, composite REAL);
    CREATE INDEX skill_tag_tag ON skill_tag(tag, composite DESC);
    CREATE INDEX skill_tag_path ON skill_tag(path);
    CREATE TABLE card(path TEXT PRIMARY KEY, plugin, name, summary_ar, summary_en, what_it_does, domain, subdomain, secondary_domains,
        capabilities, inputs, outputs, requires, quality_overall REAL, specificity, actionability, completeness, safety, reasons,
        unique_value, risks_flags, superskills, keywords, truncated, model);
    CREATE VIRTUAL TABLE card_fts USING fts5(path, summary_ar, summary_en, what_it_does, capabilities, keywords, unique_value, tokenize='unicode61');
    """)
    db.executemany("INSERT INTO grade VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", [
        (c["path"], c["quality"]["specificity"], c["quality"]["actionability"], c["quality"]["completeness"], c["quality"]["safety"],
         c["quality"]["overall"], c["composite"], c["domain"], json.dumps(c["secondary_domains"]), json.dumps(c["risks_flags"]),
         c["quality"]["reasons"], c["model"]) for c in cards])
    db.executemany("INSERT INTO skill_tag VALUES (?,?,?,?)", skill_tags)
    db.executemany("INSERT INTO card VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [
        (c["path"], c["plugin"], c["name"], c["summary_ar"], c["summary_en"], c["what_it_does"], c["domain"], c["subdomain"],
         json.dumps(c["secondary_domains"], ensure_ascii=False), json.dumps(c["capabilities"], ensure_ascii=False),
         json.dumps(c["inputs"], ensure_ascii=False), json.dumps(c["outputs"], ensure_ascii=False), json.dumps(c["requires"], ensure_ascii=False),
         float(c["quality"]["overall"]), c["quality"]["specificity"], c["quality"]["actionability"], c["quality"]["completeness"], c["quality"]["safety"],
         c["quality"]["reasons"], c["unique_value"], json.dumps(c["risks_flags"], ensure_ascii=False), json.dumps(c["superskills"], ensure_ascii=False),
         json.dumps(c["keywords"], ensure_ascii=False), 0, c["model"]) for c in cards])
    db.executemany("INSERT INTO card_fts VALUES (?,?,?,?,?,?,?)", [
        (c["path"], c["summary_ar"], c["summary_en"], c["what_it_does"], " ".join(c["capabilities"]), " ".join(c["keywords"]), c["unique_value"]) for c in cards])
    db.execute("""CREATE VIEW advanced_skill AS
        SELECT s.id, s.path, s.plugin, s.name, s.description, s.license, s.words, s.scripts, s.refs, s.has_evals, s.tools, s.tags, s.richness,
               g.specificity, g.actionability, g.completeness, g.safety, g.overall AS quality, g.composite, g.domain, g.secondary, g.flags, g.reasons, g.model
        FROM skill s JOIN grade g ON g.path = s.path""")
    db.commit()
    db.close()

    # ---------------------------------------------------------------- التقرير
    by_tag = defaultdict(list)
    for path, t, d, comp in skill_tags:
        by_tag[t].append((comp, d, path))
    ss = superskill_sources()
    try:
        catalog = {e["slug"]: e for e in json.loads((ROOT / "CATALOG.json").read_text(encoding="utf-8"))}
    except Exception:
        catalog = {}
    by_name = defaultdict(list)
    for c in cards:
        by_name[(c["name"], c["plugin"])].append(c)

    def dedupe(rows, limit, per_plugin=2, min_density=0.0):
        seen_plugin, seen_name, out = Counter(), set(), []
        if min_density:
            gated = [r for r in rows if r[1] >= min_density]
            if len(gated) >= min(limit, 5):
                rows = gated
        for comp, d, path in sorted(rows, key=lambda r: -r[0]):
            c = grades[path]
            key = c["name"]
            if seen_plugin[c["plugin"]] >= per_plugin or key in seen_name:
                continue
            seen_plugin[c["plugin"]] += 1; seen_name.add(key); out.append((comp, d, c))
            if len(out) >= limit:
                break
        return out

    qdist = Counter(c["quality"]["overall"] for c in cards)
    flags = Counter(f for c in cards for f in c["risks_flags"] if f != "none")
    with_scripts = sum(1 for c in cards if c["has_scripts"])
    L = ["# الفهرس المتقدم لأطلس KOSIF (دمج الفهارس الثلاثة)", "",
         "طبقة واحدة متسقة فوق: (1) الفهرس الآلي بكثافة الوسوم، (2) تدريج الأدلة لكل مهارة من نصها الكامل، (3) خريطة المهارات الخارقة الـ108 إلى مصادرها. "
         "كل رقم هنا مشتق من عدّ أدلة ملموسة في النص (كتل كود، أوامر، مسارات، قيم بوحدات، جداول، سكربتات في المجلد، مراجع، أقسام)، لا من تقدير حر.", "",
         "## المنهج", "",
         "- **الجودة (1–5)** = 0.35 خصوصية + 0.30 إجرائية + 0.25 اكتمال + 0.10 أمان. الخصوصية من كثافة الأدلة الملموسة مع خصم للكلمات التسويقية؛ الإجرائية من السكربتات والأوامر وأقسام الخطوات والأخطاء؛ الاكتمال من تغطية دورة الحياة (نظرة، متطلبات، خطوات، مخرجات، أخطاء، أمثلة، فحص) والعمق والمراجع؛ الأمان ينخفض مع أوامر مدمّرة بلا حراسة ويهبط إلى 1 عند تسرّب مفتاح.",
         "- **الصلة بالوسم** = كثافة ذكر الوسم لكل ألف كلمة (تتشبّع عند 30).",
         "- **البنية** = سكربتات ×0.25 + مراجع ×0.05 (حتى 8) + تقييمات ×0.2 + كتل كود ×0.03 (حتى 10).",
         "- **الدرجة المركبة (0–100)** = 45% جودة + 35% صلة بالوسم + 20% بنية. تُحسب لكل (مهارة، وسم) فتختلف المهارة نفسها بين وسومها.",
         "- الست مهارات المقروءة يدوياً (`tools/deep-read/cards.sample-human.jsonl`) تتقدّم درجاتها على المُدرِّج.",
         "- إزالة التكرار في القوائم: مهارتان كحد أقصى لكل إضافة، ولا تكرار للاسم نفسه.", "",
         "## أرقام عامة", "",
         f"- مهارات مدرَّجة: **{len(cards):,}** · تحمل سكربتات فعلية في مجلدها: {with_scripts:,} ({100*with_scripts/len(cards):.0f}%).",
         "- توزيع الجودة: " + " · ".join(f"{q}/5: {qdist.get(q,0):,}" for q in (5, 4, 3, 2, 1)) + ".",
         "- أعلام الخطر: " + "، ".join(f"{k} {v:,}" for k, v in flags.most_common(9)) + ".", "",
         "## الوسوم: الحجم والجودة وأفضل 10 (بالدرجة المركبة بعد إزالة التكرار)", "",
         "| الوسم | المهارات | متوسط الجودة | 5/5 | بسكربتات | أفضل 10 (الاسم · الجودة · المركبة) |", "|---|---|---|---|---|---|"]
    tag_order = sorted(by_tag.items(), key=lambda kv: -len(kv[1]))
    for t, rows in tag_order:
        cs = [grades[p] for _, _, p in rows]
        avg = sum(c["quality"]["overall"] for c in cs) / len(cs)
        five = sum(1 for c in cs if c["quality"]["overall"] == 5)
        scr = sum(1 for c in cs if c["has_scripts"])
        top = dedupe(rows, 10, min_density=3.0)
        cell = " · ".join(f"`{c['name']}` {c['quality']['overall']}/{comp:.0f}" for comp, d, c in top)
        L.append(f"| {t} | {len(rows):,} | {avg:.2f} | {five:,} | {scr:,} | {cell} |")
    L += ["", "## أفضل 10 بالتفصيل في وسوم الوسائط والبرومبت والإكسل", ""]
    for t in ("video-editing", "animation", "captions-subtitles", "audio-music", "video-generation", "image-generation", "social-content",
              "prompt-engineering", "agents-orchestration", "llm-evals", "ai-safety-security", "excel-spreadsheets", "financial-modeling", "accounting-audit", "3d-webgl", "game-dev"):
        if t not in by_tag:
            continue
        L += [f"### {t} — {len(by_tag[t]):,} مهارة", "", "| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |", "|---|---|---|---|---|---|---|---|"]
        for i, (comp, d, c) in enumerate(dedupe(by_tag[t], 10, min_density=3.0), 1):
            L.append(f"| {i} | `{c['name']}` ({c['plugin']}) | {c['quality']['overall']} | {d:.0f}/k | {comp:.0f} | {len(c['scripts'])} | {', '.join(f for f in c['risks_flags'] if f!='none') or '—'} | {titles.get(c['path'],'')[:110]} |")
        L.append("")
    L += ["## أفضل 50 مهارة في الأطلس كله (جودة ثم بنية، بإزالة التكرار)", "", "| # | المهارة (الإضافة) | المجال | جودة | سكربتات | مراجع | كلمات | الوصف |", "|---|---|---|---|---|---|---|---|"]
    overall_rows = [(c["quality"]["overall"] * 20 + min(len(c["scripts"]), 4) * 5 + min(c["richness"] / 50, 10), c["max_tag_density"], c["path"]) for c in cards]
    for i, (sc, d, c) in enumerate(dedupe(overall_rows, 50, per_plugin=1), 1):
        L.append(f"| {i} | `{c['name']}` ({c['plugin']}) | {c['domain']} | {c['quality']['overall']} | {len(c['scripts'])} | {c['refs']} | {c['words']:,} | {titles.get(c['path'],'')[:100]} |")
    L += ["", "## جدول متقاطع: الوسم × الجودة", "", "| الوسم | 5 | 4 | 3 | 2 | 1 |", "|---|---|---|---|---|---|"]
    for t, rows in tag_order:
        qc = Counter(grades[p]["quality"]["overall"] for _, _, p in rows)
        L.append(f"| {t} | {qc.get(5,0):,} | {qc.get(4,0):,} | {qc.get(3,0):,} | {qc.get(2,0):,} | {qc.get(1,0):,} |")
    L += ["", "## خريطة المهارات الخارقة الـ108 ← مصادرها في الأطلس (مع جودة كل مصدر)", "",
          "| # | المهارة الخارقة | المصادر الثمانية (الاسم · جودة/5) | متوسط جودة المصادر |", "|---|---|---|---|"]
    for slug, srcs in sorted(ss.items(), key=lambda kv: int(catalog.get(kv[0], {}).get("n", 999)) if catalog else kv[0]):
        qs = []
        cells = []
        for name, plugin in srcs:
            cands = by_name.get((name, plugin)) or [c for c in cards if c["name"] == name and c["plugin"].endswith(plugin)]
            q = cands[0]["quality"]["overall"] if cands else None
            if q:
                qs.append(q)
            cells.append(f"{name} · {q if q else '?'}")
        n = catalog.get(slug, {}).get("n", "")
        L.append(f"| {n} | `{slug}` | {' · '.join(cells)} | {sum(qs)/len(qs):.1f} |" if qs else f"| {n} | `{slug}` | {' · '.join(cells)} | — |")
    L += ["", "## كيف تستعلم", "", "```python", "import sqlite3; db = sqlite3.connect('tools/atlas-deep.sqlite')",
          "# أفضل 10 في وسم، بالدرجة المركبة لذلك الوسم:",
          "for r in db.execute(\"SELECT a.name, a.plugin, a.quality, t.density, t.composite FROM skill_tag t JOIN advanced_skill a ON a.path=t.path WHERE t.tag='video-editing' ORDER BY t.composite DESC LIMIT 10\"): print(r)",
          "# بحث نصي كامل ثم ترتيب بالجودة:",
          "for r in db.execute(\"SELECT a.name, a.quality, a.composite FROM skill_fts f JOIN advanced_skill a ON a.id=f.rowid WHERE skill_fts MATCH 'ffmpeg AND loudnorm' ORDER BY a.quality DESC, a.composite DESC LIMIT 10\"): print(r)",
          "# مهارات بسكربتات وجودة 5 في مجال الإكسل:",
          "for r in db.execute(\"SELECT name, plugin, scripts FROM advanced_skill WHERE domain='excel-spreadsheets' AND quality=5 ORDER BY composite DESC\"): print(r)",
          "```", ""]
    (ROOT / "ADVANCED-INDEX.md").write_text("\n".join(L), encoding="utf-8")

    # ---------------------------------------------------------------- DEEP-READ.md (v2)
    by_dom = defaultdict(list)
    for c in cards:
        by_dom[c["domain"]].append(c)
    D = ["# القراءة الكاملة لأطلس KOSIF — بطاقات v2 (تدريج أدلة من النص الكامل لكل مهارة)", "",
         f"- بطاقات: **{len(cards):,}**؛ منها 6 مقروءة يدوياً بالكامل. متوسط الجودة {sum(c['quality']['overall'] for c in cards)/len(cards):.2f}/5.",
         "- كل بطاقة: ملخص، مجال أساسي وثانوي (من كثافة الوسوم)، قدرات (من العناوين)، مدخلات/مخرجات (من أقسام المتطلبات/المخرجات)، جودة بأربع درجات وسبب مُعدَّد، أعلام خطر، سكربتات، درجة مركبة.",
         "- التفصيل الكامل في `tools/deep-read/cards.jsonl` و`tools/atlas-deep-read.json` وجدول `card` في SQLite. التقرير الموحّد: `ADVANCED-INDEX.md`.", "",
         "## المجالات وأفضل 10 في كل مجال (بالجودة ثم المركبة)", ""]
    for dom, lst in sorted(by_dom.items(), key=lambda kv: -len(kv[1])):
        rows = [(c["quality"]["overall"] * 100 + c["composite"], c["max_tag_density"], c["path"]) for c in lst]
        D += [f"### {dom} — {len(lst):,}", "", "| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |", "|---|---|---|---|---|---|"]
        for sc, d, c in dedupe(rows, 10):
            D.append(f"| `{c['name']}` ({c['plugin']}) | {c['quality']['overall']} | {c['composite']:.0f} | {len(c['scripts'])} | {', '.join(f for f in c['risks_flags'] if f!='none') or '—'} | {titles.get(c['path'],'')[:100]} |")
        D.append("")
    (ROOT / "DEEP-READ.md").write_text("\n".join(D), encoding="utf-8")
    print(f"done: {len(cards):,} cards, {len(skill_tags):,} skill-tag rows → ADVANCED-INDEX.md, DEEP-READ.md, cards.jsonl, atlas-deep-read.json, sqlite(grade, skill_tag, advanced_skill)")


if __name__ == "__main__":
    main()
