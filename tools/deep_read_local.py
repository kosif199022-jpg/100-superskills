#!/usr/bin/env python3
"""القراءة المحلية الكاملة لأطلس KOSIF: استخراج بطاقات بدون API من النص الخام بـ heuristics.
بدل استدعاء نموذج، نستخرج المعلومات من الهيكل والكلمات الدالة لكل مهارة.

usage:
  python tools/deep_read_local.py [--limit 100] [--tags video-editing,animation]

النتيجة: tools/deep-read/cards.jsonl + tools/atlas-deep-read.json + DEEP-READ.md
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
STATE = TOOLS / "deep-read"
ATLAS = ROOT.parent / "kosif-atlas" / "skills"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOMAINS = [
    "video-editing", "animation", "video-generation", "image-generation", "captions-subtitles", "audio-music",
    "photography-lighting", "social-content", "storytelling", "copywriting-marketing", "prompt-engineering",
    "agents-orchestration", "llm-evals", "ai-safety-security", "rag-knowledge", "excel-spreadsheets",
    "financial-modeling", "accounting-audit", "business-strategy", "data-analysis", "dataviz-dashboards",
    "database", "backend-api", "web-frontend", "design-ui", "mobile", "game-dev", "3d-webgl", "devops-ci",
    "cloud-edge", "security", "testing-qa", "debugging", "code-review-refactor", "architecture", "git-github",
    "claude-code-meta", "docs-writing", "pdf", "word-docs", "powerpoint-slides", "productivity-email",
    "research", "education-learning", "translation-i18n", "legal-contracts", "hr-recruiting", "healthcare",
    "real-estate", "ecommerce", "landing-marketing", "math-science", "decision-reasoning", "other",
]

PATTERNS = {
    "input": r"(?:input|requires?|needs?|takes?|accept|given|provided|pass|supply|data sources?)\b",
    "output": r"(?:output|returns?|produces?|generates?|yields?|gives?|resulting?|deliverables?)\b",
    "procedure": r"(?:step|phase|stage|process|workflow|pipeline|method|procedure|follows?)\b",
    "scripts": r"(?:script|tool|command|cli|python|node|bash|shell)\b",
    "quality": r"(?:validation|check|verify|test|assert|assert|guard|ensure|guarantee|robust|reliable|safe)\b",
}

DOMAIN_KEYWORDS = {
    "video-editing": r"\b(video|edit|montage|cut|timeline|scene|shot|clip|transition|xfade|trim|sequence|footage)\b",
    "animation": r"\b(animat|motion|keyframe|tween|frame|gsap|remotion|lottie|sprite|sprite sheet|easing)\b",
    "audio-music": r"\b(audio|sound|music|voice|speech|mp3|wav|loudness|lufs|equalize|reverb|fx|effects?)\b",
    "excel-spreadsheets": r"\b(excel|spreadsheet|xlsx|formula|cell|pivot|vlookup|sumif|xlookup|named range)\b",
    "financial-modeling": r"\b(dcf|wacc|valuation|forecast|budget|variance|cash flow|roi|npv|irr)\b",
    "prompt-engineering": r"\b(prompt|system prompt|instruction|jailbreak|injection|guard|constraint|few-shot)\b",
    "database": r"\b(sql|postgres|mysql|database|schema|query|index|table|relation|join)\b",
    "testing-qa": r"\b(test|suite|unit|integration|e2e|qa|assert|mock|stub|fixture|benchmark)\b",
}

# ----------------------------------------------------------------

def extract_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}, text
    fm_text = m.group(1)
    body = text[m.end():]
    fm = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip("'\"")
    return fm, body


def guess_domain(name: str, desc: str, body: str) -> str:
    combined = f"{name} {desc} {body[:2000]}".lower()
    scores = {}
    for dom, pat in DOMAIN_KEYWORDS.items():
        hits = len(re.findall(pat, combined, re.I))
        if hits:
            scores[dom] = hits
    if scores:
        return max(scores, key=scores.get)
    return "other"


def extract_sections(body: str) -> dict[str, str]:
    sections = {}
    current = None
    current_text = []
    for line in body.split("\n"):
        if line.startswith("#"):
            if current and current_text:
                sections[current] = "\n".join(current_text)
            current = line.lstrip("#").strip().lower()
            current_text = []
        elif current:
            current_text.append(line)
    if current:
        sections[current] = "\n".join(current_text)
    return sections


def extract_capabilities(body: str) -> list[str]:
    caps = []
    # تابع عن أي "يفعل"، "يتيح"، "يحسب"
    pattern = r"(?:يفعل|يتيح|يحسب|يبني|يولّد|يكتشف|يحوّل|يقطع|يرسم|ينشئ|يستخرج|يطبّق|يدير|يراقب)\s+([^.،\n]{20,200})"
    matches = re.findall(pattern, body)
    for m in matches[:10]:
        m = m.strip()
        if len(m) > 10:
            caps.append(m)
    if not caps:
        # بحث إنجليزي
        pattern = r"(?:does|enables|calculates|builds|generates|detects|transforms|cuts|renders|creates|extracts|applies|manages|monitors)\s+([^.،\n]{20,200})"
        matches = re.findall(pattern, body, re.I)
        for m in matches[:10]:
            m = m.strip()
            if len(m) > 10:
                caps.append(m[:150])
    return list(dict.fromkeys(caps))[:5]


def grade_quality(name: str, desc: str, body: str, fm: dict) -> dict:
    words = len(body.split())
    sections = extract_sections(body)

    # specificity: هل فيه أمثلة وأوامر فعلية؟
    spec = 1
    if re.search(r"(example|usage|command|python|bash|node|```)", body, re.I):
        spec += 1
    if re.search(r"(step|phase|procedure|workflow)", body, re.I):
        spec += 1
    if words > 1000:
        spec += 1
    spec = min(5, spec)

    # actionability: هل يمكن تنفيذه؟
    action = 1
    if re.search(r"(script|tool|command|cli)", body, re.I):
        action += 2
    if re.search(r"(json|yaml|config|input|output)", body, re.I):
        action += 1
    if re.search(r"(error|troubleshoot|debug|fix)", body, re.I):
        action += 1
    action = min(5, action)

    # completeness: يغطي الدورة كاملة؟
    compl = 1
    if "input" in sections or re.search(PATTERNS["input"], body, re.I):
        compl += 1
    if "output" in sections or re.search(PATTERNS["output"], body, re.I):
        compl += 1
    if re.search(r"(edge case|error|exception|warning)", body, re.I):
        compl += 1
    if words > 1500:
        compl += 1
    compl = min(5, compl)

    # safety: هل يحذّر من المخاطر؟
    safe = 2  # عام
    if re.search(r"(dangerous|risk|warning|caution|deprecated|security|auth|secret)", body, re.I):
        safe = 4
    if re.search(r"(destructive|delete|remove|unrecoverable)", body, re.I):
        safe = 3

    overall = (spec + action + compl) // 3
    reason = f"specificity:{spec} actionability:{action} completeness:{compl} (words:{words})"

    return {"specificity": spec, "actionability": action, "completeness": compl, "safety": safe,
            "overall": overall, "reasons": reason}


def process_skill(path: Path, plugin: str) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return None

    fm, body = extract_frontmatter(text)
    name = fm.get("name") or path.parent.name
    desc = fm.get("description", "")[:300]

    domain = guess_domain(name, desc, body)
    caps = extract_capabilities(body)
    quality = grade_quality(name, desc, body, fm)

    card = {
        "path": str(path.relative_to(ATLAS)).replace("\\", "/"),
        "plugin": plugin,
        "name": name,
        "summary_ar": desc[:200],
        "summary_en": desc[:200],
        "what_it_does": "\n".join(caps[:2]) if caps else desc,
        "domain": domain,
        "subdomain": fm.get("tag", ""),
        "secondary_domains": [],
        "capabilities": caps,
        "procedure_steps": len(extract_sections(body)),
        "inputs": [],
        "outputs": [],
        "requires": {"tools": [], "apis_keys": [], "platforms": []},
        "has_concrete_examples": bool(re.search(r"example|usage", body, re.I)),
        "has_quality_gates": bool(re.search(r"test|check|assert|verify", body, re.I)),
        "has_scripts": bool(re.search(r"script|command|bash|python|node", body, re.I)),
        "quality": quality,
        "unique_value": "",
        "risks_flags": [],
        "superskills": [],
        "keywords": [name] + re.findall(r"\b[a-z0-9_-]{4,15}\b", desc.lower())[:12],
        "truncated": False,
        "model": "local heuristic",
    }
    return card


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--tags", default="")
    a = ap.parse_args()

    if not ATLAS.exists():
        sys.exit(f"{ATLAS} لا يوجد")

    STATE.mkdir(parents=True, exist_ok=True)
    cards_file = STATE / "cards.jsonl"
    out = open(cards_file, "w", encoding="utf-8")

    done = set()
    if cards_file.exists():
        for line in cards_file.read_text(encoding="utf-8").splitlines():
            try:
                done.add(json.loads(line)["path"])
            except:
                pass

    n = 0
    for plugin_dir in sorted(ATLAS.iterdir()):
        if not plugin_dir.is_dir():
            continue
        for skill_dir in sorted(plugin_dir.iterdir()):
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.exists():
                continue
            path_str = str(skill_file.relative_to(ATLAS)).replace("\\", "/")
            if path_str in done:
                continue

            card = process_skill(skill_file, plugin_dir.name)
            if card:
                out.write(json.dumps(card, ensure_ascii=False) + "\n")
                n += 1
                if n % 100 == 0:
                    print(f"{n} cards…", flush=True)
                if a.limit and n >= a.limit:
                    break
        if a.limit and n >= a.limit:
            break

    out.close()
    print(f"done: {n} cards → {cards_file}")


if __name__ == "__main__":
    main()
