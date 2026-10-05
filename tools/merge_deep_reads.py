#!/usr/bin/env python3
"""دمج نتائج القراءة المحلية مع الفهرس الآلي وبناء DEEP-READ.md والجداول."""
from __future__ import annotations

import json
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
STATE = TOOLS / "deep-read"
DEEP_DB = TOOLS / "atlas-deep.sqlite"

def merge_deep_reads():
    cards_file = STATE / "cards.jsonl"
    if not cards_file.exists():
        print("لا توجد بطاقات.")
        return

    rows = []
    for line in cards_file.read_text(encoding="utf-8").splitlines():
        try:
            c = json.loads(line)
            rows.append(c)
        except Exception as e:
            print(f"خطأ: {e}")
            continue

    (TOOLS / "atlas-deep-read.json").write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")

    # SQLite
    if DEEP_DB.exists():
        db = sqlite3.connect(DEEP_DB)
        db.executescript("""
        DROP TABLE IF EXISTS card; DROP TABLE IF EXISTS card_fts;
        CREATE TABLE card(path TEXT PRIMARY KEY, plugin, name, summary_ar, summary_en, what_it_does, domain, subdomain,
            secondary_domains, capabilities, inputs, outputs, requires, quality_overall REAL, specificity, actionability,
            completeness, safety, reasons, unique_value, risks_flags, superskills, keywords, truncated, model);
        CREATE VIRTUAL TABLE card_fts USING fts5(path, summary_ar, summary_en, what_it_does, capabilities, keywords, unique_value, tokenize='unicode61');
        """)
        for c in rows:
            q = c.get("quality") or {}
            db.execute("INSERT OR REPLACE INTO card VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                c["path"], c.get("plugin"), c.get("name"), c.get("summary_ar"), c.get("summary_en"), c.get("what_it_does"),
                c.get("domain"), c.get("subdomain"), json.dumps(c.get("secondary_domains"), ensure_ascii=False),
                json.dumps(c.get("capabilities"), ensure_ascii=False), json.dumps(c.get("inputs"), ensure_ascii=False),
                json.dumps(c.get("outputs"), ensure_ascii=False), json.dumps(c.get("requires"), ensure_ascii=False),
                float(q.get("overall") or 0), q.get("specificity"), q.get("actionability"), q.get("completeness"), q.get("safety"),
                q.get("reasons"), c.get("unique_value"), json.dumps(c.get("risks_flags"), ensure_ascii=False),
                json.dumps(c.get("superskills"), ensure_ascii=False), json.dumps(c.get("keywords"), ensure_ascii=False),
                int(bool(c.get("truncated"))), c.get("model")))
            db.execute("INSERT INTO card_fts VALUES (?,?,?,?,?,?,?)", (
                c["path"], c.get("summary_ar") or "", c.get("summary_en") or "", c.get("what_it_does") or "",
                " ".join(c.get("capabilities") or []), " ".join(c.get("keywords") or []), c.get("unique_value") or ""))
        db.commit(); db.close()

    # Markdown
    by_dom = defaultdict(list)
    for c in rows:
        by_dom[c.get("domain") or "other"].append(c)

    flags = Counter(fl for c in rows for fl in (c.get("risks_flags") or []) if fl != "none")
    L = ["# القراءة المحلية لأطلس KOSIF (بطاقة لكل مهارة بـ heuristics وعدّ الكلمات)", "",
         f"- بطاقات: **{len(rows):,}** مهارة.",
         f"- متوسط الجودة الكلية: {sum(float((c.get('quality') or {}).get('overall') or 0) for c in rows)/max(1,len(rows)):.2f}/5.",
         f"- أعلام الخطر الأكثر: " + "، ".join(f"{k} ({v:,})" for k, v in flags.most_common(8)) if flags else "none", "",
         "## المجالات (كشفتها heuristics) وأفضل 10 مهارات جودةً في كل مجال", ""]

    for dom, lst in sorted(by_dom.items(), key=lambda kv: -len(kv[1])):
        lst.sort(key=lambda c: -float((c.get("quality") or {}).get("overall") or 0))
        L.append(f"### {dom} — {len(lst):,} مهارة")
        L.append("| المهارة | الجودة | ماذا تفعل | النموذج |")
        L.append("|---|---|---|---|")
        for c in lst[:10]:
            L.append(f"| `{c['path'].replace('/SKILL.md','')}` | {(c.get('quality') or {}).get('overall')} | {(c.get('summary_ar') or '')[:100]} | {c.get('model','?')} |")
        L.append("")

    L += ["## البحث في البطاقات", "",
          "```python", "import sqlite3; db = sqlite3.connect('tools/atlas-deep.sqlite')",
          "for r in db.execute(\"SELECT c.path, c.quality_overall, c.summary_ar FROM card_fts f JOIN card c ON c.path=f.path WHERE card_fts MATCH 'excel AND formula' ORDER BY c.quality_overall DESC LIMIT 10\"): print(r)",
          "```", ""]

    (ROOT / "DEEP-READ.md").write_text("\n".join(L), encoding="utf-8")
    print(f"done: {len(rows):,} بطاقة → DEEP-READ.md, tools/atlas-deep-read.json, card in {DEEP_DB.name}")


if __name__ == "__main__":
    merge_deep_reads()
