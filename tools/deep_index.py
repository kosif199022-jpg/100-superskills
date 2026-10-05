#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""فهرس عميق لكل مهارات الأطلس: يقرأ نص كل SKILL.md كاملاً (لا الوصف فقط) ويستخرج البنية والأدوات والوسوم ويخزّنها في SQLite FTS5.

usage: python deep_index.py [--atlas DIR] [--db tools/atlas-deep.sqlite] [--json tools/atlas-deep.json] [--md DEEP-INDEX.md]

لكل مهارة: الاسم، والوصف، والمحفّزات المقتبسة، والعناوين (##)، وعدد الكلمات، وكتل الكود ولغاتها، والملفات المرافقة
(سكربتات بلغاتها، ومراجع، وقوالب، وتقييمات)، والأدوات/المكتبات المذكورة في النص (قاموس 200 أداة)، ووسوم المجال
(تصنيف 70 وسماً بتعابير منتظمة على النص الكامل)، ودرجة «ثراء» (كلمات × بنية × سكربتات × تقنيات)، والترخيص والمصدر.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_ATLAS = ROOT.parent / "kosif-atlas" / "skills"

TOOLS = {
    # video / audio / animation
    "ffmpeg": r"\bffmpeg\b", "ffprobe": r"\bffprobe\b", "remotion": r"\bremotion\b", "gsap": r"\bgsap\b", "three.js": r"\bthree(\.js|js)\b",
    "framer-motion": r"\bframer[- ]motion\b", "lottie": r"\blottie\b", "rive": r"\brive\b", "manim": r"\bmanim\b", "blender": r"\bblender\b",
    "after-effects": r"\bafter effects\b", "premiere": r"\bpremiere\b", "davinci-resolve": r"\bdavinci|resolve studio\b", "capcut": r"\bcapcut\b",
    "playwright": r"\bplaywright\b", "puppeteer": r"\bpuppeteer\b", "whisper": r"\bwhisper\b", "elevenlabs": r"\belevenlabs\b",
    "sox": r"\bsox\b", "librosa": r"\blibrosa\b", "pydub": r"\bpydub\b", "webgl": r"\bwebgl\b", "glsl": r"\bglsl\b", "shader": r"\bshaders?\b",
    "canvas": r"\bcanvas\b", "svg": r"\bsvg\b", "css-animation": r"@keyframes|\bcss animation", "spring": r"\bspring (physics|animation)\b",
    "motion-canvas": r"\bmotion canvas\b", "p5.js": r"\bp5\.js\b", "pixi": r"\bpixi(\.js)?\b", "phaser": r"\bphaser\b", "godot": r"\bgodot\b", "unity": r"\bunity\b",
    "veo": r"\bveo\b", "sora": r"\bsora\b", "kling": r"\bkling\b", "runway": r"\brunway\b", "luma": r"\bluma\b", "pika": r"\bpika\b",
    "midjourney": r"\bmidjourney\b", "stable-diffusion": r"\bstable diffusion|sdxl\b", "flux": r"\bflux\b", "comfyui": r"\bcomfyui\b", "dall-e": r"\bdall[- ]?e\b",
    "ideogram": r"\bideogram\b", "suno": r"\bsuno\b", "imagemagick": r"\bimagemagick|\bmagick\b", "pillow": r"\bpillow\b|\bPIL\b", "opencv": r"\bopencv|cv2\b",
    "srt": r"\b\.?srt\b", "webvtt": r"\bvtt\b", "loudnorm": r"\bloudnorm|\blufs\b", "x264": r"\blibx264|h\.?264\b", "hevc": r"\bhevc|h\.?265\b",
    # office / data
    "excel": r"\bexcel\b", "openpyxl": r"\bopenpyxl\b", "xlsxwriter": r"\bxlsxwriter\b", "power-query": r"\bpower query\b|\blet\s+source\b", "dax": r"\bdax\b",
    "power-bi": r"\bpower ?bi\b", "vba": r"\bvba\b", "pivot": r"\bpivot ?table", "xlookup": r"\bxlookup\b", "lambda": r"\bLAMBDA\(", "let-fn": r"\bLET\(",
    "python-in-excel": r"\bpy\(|python in excel", "google-sheets": r"\bgoogle sheets\b", "apps-script": r"\bapps script\b", "pandas": r"\bpandas\b",
    "numpy": r"\bnumpy\b", "polars": r"\bpolars\b", "duckdb": r"\bduckdb\b", "sql": r"\bsql\b", "postgres": r"\bpostgres", "sqlite": r"\bsqlite\b",
    "docx": r"\bdocx\b", "python-docx": r"\bpython-docx\b", "pptx": r"\bpptx\b", "python-pptx": r"\bpython-pptx\b", "pdf": r"\bpdf\b", "pypdf": r"\bpypdf\b",
    "pdfplumber": r"\bpdfplumber\b", "tesseract": r"\btesseract\b", "libreoffice": r"\blibreoffice|soffice\b", "csv": r"\bcsv\b", "jupyter": r"\bjupyter\b",
    "matplotlib": r"\bmatplotlib\b", "plotly": r"\bplotly\b", "d3": r"\bd3(\.js)?\b", "chart.js": r"\bchart\.js\b", "streamlit": r"\bstreamlit\b",
    # prompts / llm
    "json-schema": r"\bjson schema\b", "few-shot": r"\bfew[- ]shot\b", "chain-of-thought": r"\bchain[- ]of[- ]thought\b|\bcot\b", "system-prompt": r"\bsystem prompt\b",
    "function-calling": r"\bfunction calling|tool (use|calling)\b", "rag": r"\brag\b|retrieval[- ]augmented", "embeddings": r"\bembeddings?\b", "eval": r"\bevals?\b|\bevaluation\b",
    "llm-judge": r"llm[- ]as[- ]a?[- ]?judge|\bjudge\b", "prompt-injection": r"prompt injection", "xml-tags": r"<\w+>.*</\w+>", "structured-output": r"structured output",
    "anthropic": r"\banthropic\b|\bclaude\b", "openai": r"\bopenai\b|\bgpt-?[45]", "gemini": r"\bgemini\b", "langchain": r"\blangchain\b", "dspy": r"\bdspy\b",
    "mcp": r"\bmcp\b", "agent": r"\bagents?\b", "subagent": r"\bsub-?agents?\b", "hooks": r"\bhooks?\b",
    # web / code
    "react": r"\breact\b", "next.js": r"\bnext(\.js|js)\b", "vue": r"\bvue\b", "svelte": r"\bsvelte\b", "tailwind": r"\btailwind\b", "typescript": r"\btypescript\b",
    "node": r"\bnode(\.js|js)?\b", "python": r"\bpython\b", "fastapi": r"\bfastapi\b", "django": r"\bdjango\b", "flask": r"\bflask\b", "express": r"\bexpress(\.js)?\b",
    "docker": r"\bdocker\b", "kubernetes": r"\bkubernetes|k8s\b", "terraform": r"\bterraform\b", "github-actions": r"github actions", "cloudflare": r"\bcloudflare\b",
    "workers": r"\bworkers?\b", "vercel": r"\bvercel\b", "aws": r"\baws\b", "gcp": r"\bgcp\b|google cloud", "azure": r"\bazure\b", "supabase": r"\bsupabase\b",
    "prisma": r"\bprisma\b", "drizzle": r"\bdrizzle\b", "graphql": r"\bgraphql\b", "openapi": r"\bopenapi|swagger\b", "pytest": r"\bpytest\b", "jest": r"\bjest\b",
    "vitest": r"\bvitest\b", "cypress": r"\bcypress\b", "eslint": r"\beslint\b", "ruff": r"\bruff\b", "git": r"\bgit\b", "wcag": r"\bwcag\b", "aria": r"\baria\b",
    "lighthouse": r"\blighthouse\b", "seo": r"\bseo\b", "json-ld": r"json-ld", "mermaid": r"\bmermaid\b", "plantuml": r"\bplantuml\b", "figma": r"\bfigma\b",
    "stripe": r"\bstripe\b", "webhook": r"\bwebhooks?\b", "oauth": r"\boauth\b", "jwt": r"\bjwt\b", "redis": r"\bredis\b", "kafka": r"\bkafka\b",
    "rust": r"\brust\b", "go": r"\bgolang\b|\bgo (code|module|package)\b", "swift": r"\bswift\b", "kotlin": r"\bkotlin\b", "flutter": r"\bflutter\b", "react-native": r"react native",
}
TAGS = {
    "animation": r"\banimat(e|ion|ed|ing)\b|\bmotion (design|graphics)\b|\bkeyframes?\b|\btween|\bgsap\b|\blottie\b|\bframer motion\b|\banime\.js|\bremotion\b|\beasing\b|\bspring (animation|physics)|\brequestAnimationFrame",
    "video-editing": r"\bvideo edit|\bmontage\b|\bcut(s|ting)? on (the )?beat|\btimeline\b.*\bclip|\b(video|clip|shot|scene|cross) transitions?\b|\btransitions? between (clips|shots|scenes)|\bb-?roll\b|\bcolor grad|\bffmpeg\b|\bpremiere pro\b|\bdavinci\b|\bfinal cut\b|\bcapcut\b|\b[jl]-cut\b|\bjump cut|\brough cut|\bfine cut|\bxfade\b|\btrim(med|ming)? (the )?clips?\b",
    "video-generation": r"text[- ]to[- ]video|image[- ]to[- ]video|\bveo\b|\bsora\b|\bkling\b|\brunway\b",
    "captions-subtitles": r"\bsubtitles?\b|\bsrt\b|\bvtt\b|\bclosed captions?\b|\bcaptions? (track|file|timing|style|overlay|burn)|\b(video|burn(ed|t)[- ]in|karaoke|word[- ]level|auto|animated|tiktok) captions?\b|\bwhisper(\.cpp|x| model| transcri)|\bword[- ]level timestamps?|\btranscri(be|ption) (the )?(audio|video|speech)",
    "audio-music": r"\baudio\b|\bmusic\b|\bpodcast\b|\bloudness\b|\bmastering\b|\bvoice[- ]?over\b|\btts\b",
    "image-generation": r"\bmidjourney\b|stable diffusion|\bsdxl\b|\bflux\b|\bcomfyui\b|\bdall[- ]?e\b|image prompt",
    "photography-lighting": r"\b(studio|natural|cinematic|product|portrait|three-?point|soft|hard|dramatic|rembrandt|butterfly|split|loop|volumetric) light(ing)?\b|\bkey light|\bfill light|\brim light|\bback ?light|\bsoftbox|\bgolden hour|\bblue hour|\bexposure (triangle|compensation|value|time)|\b(over|under)-?exposed|\bISO \d|\bshutter speed|\bf-?stop|\baperture\b|\bf/\d|\bkelvin\b|\bbokeh\b|\bdepth of field|\bfocal length|\bwhite balance|\b\d{2,3}mm lens|\bcamera lens\b",
    "3d-webgl": r"\bthree(\.js)?\b|\bwebgl\b|\bshader|\bglsl\b|\bblender\b|\b3d\b",
    "design-ui": r"\bui\b|\bux\b|\bdesign system\b|\bdesign tokens?\b|\btypography\b|\bcolor palette\b",
    "web-frontend": r"\breact\b|\bnext\.?js\b|\bvue\b|\bsvelte\b|\btailwind\b|\bcss\b|\bhtml\b",
    "landing-marketing": r"\blanding page\b|\bconversion\b|\bcopywriting\b|\bheadline\b|\bcta\b|\bfunnel\b",
    "social-content": r"\breels?\b|\bshorts\b|\btiktok\b|\binstagram\b|\byoutube\b|\b(video|youtube) thumbnails?\b|\bthumbnail (design|text|ctr|click)|\bvideo hook|\bhook (line|in the first)|\bsocial (media|post)\b",
    "prompt-engineering": r"\bprompt (engineering|design|template|pattern)|\bsystem prompt\b|\bfew[- ]shot\b|\bmeta[- ]prompt",
    "agents-orchestration": r"\bagents?\b|\borchestrat|\bsub-?agent|\bworkflow\b|\bmcp\b",
    "llm-evals": r"\bevals?\b|\bbenchmark|\bllm[- ]as[- ]judge|\brubric\b|\bregression (test|suite)",
    "rag-knowledge": r"\brag\b|\bretrieval\b|\bembeddings?\b|\bvector (db|database|store)\b|\bknowledge base\b",
    "ai-safety-security": r"prompt injection|\bjailbreak|\bred[- ]team|\b(llm|ai|model|prompt|output|input|agent) guardrails?\b|\bguardrails? (for|against|on|around) (llms?|prompts?|models?|agents?)|\bcanary (token|string)|\bindirect (prompt )?injection|\bsystem prompt (leak|extraction)|\bdata exfiltration|\bllm security",
    "excel-spreadsheets": r"\bexcel\b|\bspreadsheet|\bxlsx\b|\bxlookup\b|\bsumifs?\b|\bpivot\b|\bopenpyxl\b|\bgoogle sheets\b",
    "financial-modeling": r"\bdcf\b|\bvaluation\b|\bfinancial model|\bcash ?flow\b|\bbudget(ing)?\b|\bforecast",
    "accounting-audit": r"\baccounting\b|\bjournal entr|\bifrs\b|\bgaap\b|\bledger\b|\breconcil|\bvat\b|\binvoice",
    "word-docs": r"\bdocx\b|\bword document|\bpython-docx\b|\btrack(ed)? changes\b",
    "powerpoint-slides": r"\bpptx\b|\bpowerpoint\b|\bslide deck\b|\bpresentation\b|\breveal\.js\b",
    "pdf": r"\bpdf\b",
    "data-analysis": r"\bpandas\b|\bdataframe\b|\bsql\b|\bquery\b|\banalytics?\b|\bstatistic",
    "dataviz-dashboards": r"\bdashboard\b|\bchart\b|\bvisuali[sz]ation\b|\bplotly\b|\bd3\b",
    "database": r"\bdatabase\b|\bschema\b|\bmigration\b|\bpostgres|\bsqlite\b|\bmysql\b|\bmongo",
    "backend-api": r"\bapi\b|\brest\b|\bgraphql\b|\bendpoint\b|\bfastapi\b|\bexpress\b|\bbackend\b",
    "devops-ci": r"\bdocker\b|\bci/?cd\b|\bgithub actions\b|\bpipeline\b|\bkubernetes|\bdeploy",
    "cloud-edge": r"\bcloudflare\b|\bworkers?\b|\bvercel\b|\baws\b|\bserverless\b|\blambda\b",
    "testing-qa": r"\btests?\b|\btesting\b|\bpytest\b|\bjest\b|\bvitest\b|\bplaywright\b|\bcoverage\b",
    "debugging": r"\bdebug|\bstack trace\b|\broot cause\b|\btroubleshoot",
    "code-review-refactor": r"\bcode review\b|\brefactor|\bclean code\b|\btechnical debt\b",
    "security": r"\bsecurity\b|\bvulnerab|\bowasp\b|\bsecrets?\b|\bthreat model",
    "git-github": r"\bgit\b|\bgithub\b|\bpull request\b|\bcommit\b|\bbranch\b|\brebase\b",
    "architecture": r"\barchitecture\b|\bsystem design\b|\badr\b|\bmicroservices?\b|\bddd\b",
    "mobile": r"\bmobile\b|\bflutter\b|\breact native\b|\bandroid\b|\bios\b|\bswift\b|\bkotlin\b",
    "game-dev": r"\bgame\b|\bphaser\b|\bgodot\b|\bunity\b|\bsprite|\bpixel art\b",
    "scraping-automation": r"\bscrap(e|ing)\b|\bcrawl|\bautomation\b|\bbrowser automation\b|\bselenium\b",
    "docs-writing": r"\breadme\b|\bdocumentation\b|\btechnical writing\b|\bchangelog\b|\bmarkdown\b",
    "copywriting-marketing": r"\bcopy(writing)?\b|\bmarketing\b|\bbrand\b|\bcampaign\b|\bnewsletter\b|\bemail marketing\b",
    "storytelling": r"\bstory(telling)?\b|\bnarrative\b|\bscreenplay\b|\bcharacter arc\b|\bplot (structure|twist|beats?|points?)\b|\bworldbuilding\b|\bprotagonist\b",
    "translation-i18n": r"\btranslat|\blocali[sz]|\bi18n\b|\barabic\b|\brtl\b",
    "education-learning": r"\bcurriculum\b|\blearning\b|\bteach|\bflashcard|\bquiz\b|\bexam\b|\bstudy\b",
    "math-science": r"\bmath(ematic(s|al))?\b|\bmathematical proof\b|\bphysics\b|\bchemistry\b|\bequations?\b|\btheorem\b|\bcalculus\b|\balgebra\b",
    "business-strategy": r"\bstrategy\b|\bbusiness plan\b|\bprd\b|\broadmap\b|\bokr\b|\bpitch\b|\bmarket research\b",
    "legal-contracts": r"\blegal\b|\bcontract\b|\bcompliance\b|\bgdpr\b|\bterms\b|\bpolicy\b",
    "productivity-email": r"\bemail\b|\binbox\b|\bcalendar\b|\bmeetings?\b|\bto-?do list\b|\btask (list|management|tracker)\b|\breminders?\b",
    "decision-reasoning": r"\bdecision\b|\btrade-?offs?\b|\bpre-?mortem\b|\bred team\b|\bcouncil\b|\bdebate\b|\bfact[- ]check",
    "research": r"\bresearch\b|\bcitations?\b|\bprimary sources?\b|\bliterature review\b|\bevidence\b|\bfact[- ]check",
    "healthcare": r"\bhealthcare\b|\bmedical\b|\bclinical\b|\bpatients?\b|\bhipaa\b|\bdiagnos(is|tic)\b",
    "real-estate": r"\breal estate\b|\bproperty\b|\bmortgage\b|\blease\b",
    "ecommerce": r"\be-?commerce\b|\bshopify\b|\bamazon\b|\bproduct (listing|description)\b|\bstore\b",
    "hr-recruiting": r"\bresume\b|\bcv\b|\bhiring\b|\brecruit|\bjob description\b|\binterview\b",
    "claude-code-meta": r"\bclaude code\b|\bskill\.md\b|\bclaude\.md\b|\bslash command|\bplugin\b",
}
_TOOLS = {k: re.compile(v, re.I) for k, v in TOOLS.items()}
_TAGS = {k: re.compile(v, re.I) for k, v in TAGS.items()}
LANG = {".py": "python", ".js": "javascript", ".mjs": "javascript", ".ts": "typescript", ".sh": "bash", ".ps1": "powershell", ".rb": "ruby",
        ".go": "go", ".rs": "rust", ".sql": "sql", ".html": "html", ".css": "css", ".json": "json", ".yaml": "yaml", ".yml": "yaml", ".md": "markdown"}


def frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not m:
        return {}, text
    fm, body = m.group(1), text[m.end():]
    d = {}
    for key in ("name", "description", "argument-hint", "license", "version"):
        mm = re.search(rf"^{key}:\s*(.*)$", fm, re.M)
        if mm:
            v = mm.group(1).strip()
            if v in (">", ">-", "|", "|-", ""):
                mm2 = re.search(rf"^{key}:\s*[>|]-?\s*\n((?:[ \t]+.*\n?)+)", fm, re.M)
                v = " ".join(l.strip() for l in mm2.group(1).splitlines()) if mm2 else ""
            d[key] = v.strip().strip('"').strip("'")
    return d, body


def richness(words: int, headings: int, code_blocks: int, scripts: int, tools: int, refs: int) -> float:
    import math
    return round(math.log1p(words) * 10 + headings * 1.5 + code_blocks * 2 + scripts * 3 + tools * 1.2 + refs * 1.5, 1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--atlas", default=str(DEFAULT_ATLAS))
    ap.add_argument("--db", default=str(HERE / "atlas-deep.sqlite"))
    ap.add_argument("--json", default=str(HERE / "atlas-deep.json"))
    ap.add_argument("--md", default=str(ROOT / "DEEP-INDEX.md"))
    a = ap.parse_args()
    atlas = Path(a.atlas)
    t0 = time.time()

    db_path = Path(a.db)
    if db_path.exists():
        db_path.unlink()
    db = sqlite3.connect(db_path)
    db.executescript("""
    CREATE TABLE skill(id INTEGER PRIMARY KEY, plugin TEXT, path TEXT, name TEXT, description TEXT, license TEXT, source TEXT,
      words INT, headings TEXT, code_langs TEXT, scripts TEXT, script_langs TEXT, refs INT, has_evals INT, tools TEXT, tags TEXT, richness REAL, tag_density TEXT);
    CREATE VIRTUAL TABLE skill_fts USING fts5(name, description, headings, body, tools, tags, content='', tokenize='unicode61');
    """)

    lic_re = re.compile(r"License:\s*\*\*([^*]+)\*\*")
    src_re = re.compile(r"^- Source:\s*(\S+)", re.M)
    rows, tag_count, tool_count = [], Counter(), Counter()
    n = 0
    for plugin in sorted(os.listdir(atlas)):
        pdir = atlas / plugin
        if not pdir.is_dir():
            continue
        lic = src = ""
        sp = pdir / "SOURCE.md"
        if sp.exists():
            s = sp.read_text(encoding="utf-8", errors="ignore")
            m = lic_re.search(s); lic = m.group(1).strip() if m else ""
            m = src_re.search(s); src = m.group(1) if m else ""
        for dp, dn, fn in os.walk(pdir):
            dn[:] = [d for d in dn if d not in ("node_modules", ".git", "__pycache__")]
            for f in fn:
                if f.lower() != "skill.md":
                    continue
                p = Path(dp) / f
                try:
                    text = p.read_text(encoding="utf-8", errors="ignore")
                except Exception:
                    continue
                fm, body = frontmatter(text)
                name = fm.get("name") or Path(dp).name
                desc = fm.get("description", "")
                heads = [h.strip() for h in re.findall(r"^#{1,4}\s+(.+)$", body, re.M)][:40]
                code_langs = Counter(l.lower() for l in re.findall(r"^```(\w+)", body, re.M))
                code_blocks = len(re.findall(r"^```", body, re.M)) // 2
                words = len(body.split())
                # sibling files (one level + scripts/references/templates)
                scripts, script_langs, refs, has_evals = [], Counter(), 0, 0
                for sub in ("", "scripts", "bin", "tools", "src"):
                    d = Path(dp) / sub if sub else Path(dp)
                    if d.is_dir():
                        for q in d.iterdir():
                            if q.is_file() and q.suffix.lower() in LANG and q.name.lower() != "skill.md" and q.suffix.lower() not in (".md", ".json", ".yaml", ".yml", ".html", ".css"):
                                scripts.append((sub + "/" if sub else "") + q.name)
                                script_langs[LANG[q.suffix.lower()]] += 1
                for sub in ("references", "reference", "docs", "resources", "assets", "templates", "examples", "knowledge"):
                    d = Path(dp) / sub
                    if d.is_dir():
                        refs += sum(1 for q in d.rglob("*") if q.is_file())
                if (Path(dp) / "evals").is_dir() or (Path(dp) / "evals.json").exists():
                    has_evals = 1
                full = desc + "\n" + body
                tools = sorted(k for k, rx in _TOOLS.items() if rx.search(full))
                per_k = max(words, 50) / 1000.0
                tag_hits = {k: len(rx.findall(full)) for k, rx in _TAGS.items()}
                # a tag sticks when the text talks about it: >=3 hits, or >=1.5 hits per 1000 words with >=2 hits
                tags = sorted(k for k, h in tag_hits.items() if h >= 3 or (h >= 2 and h / per_k >= 1.5))
                tag_density = {k: round(tag_hits[k] / per_k, 2) for k in tags}
                tag_count.update(tags); tool_count.update(tools)
                rich = richness(words, len(heads), code_blocks, len(scripts), len(tools), refs)
                rel = p.relative_to(atlas).as_posix()
                n += 1
                rows.append((n, plugin, rel, name, desc[:800], lic, src, words, json.dumps(heads, ensure_ascii=False),
                             json.dumps(dict(code_langs)), json.dumps(scripts[:40], ensure_ascii=False), json.dumps(dict(script_langs)),
                             refs, has_evals, " ".join(tools), " ".join(tags), rich, json.dumps(tag_density)))
                db.execute("INSERT INTO skill_fts(rowid, name, description, headings, body, tools, tags) VALUES (?,?,?,?,?,?,?)",
                           (n, name, desc, " | ".join(heads), body[:60000], " ".join(tools), " ".join(tags)))
                if n % 1000 == 0:
                    db.executemany("INSERT INTO skill VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows); rows.clear(); db.commit()
                    print(f"  {n} skills… {time.time() - t0:.0f}s", flush=True)
    db.executemany("INSERT INTO skill VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows); db.commit()

    # compact JSON (no bodies)
    cur = db.execute("SELECT plugin,path,name,description,license,source,words,headings,code_langs,scripts,script_langs,refs,has_evals,tools,tags,richness,tag_density FROM skill")
    cols = [c[0] for c in cur.description]
    data = [dict(zip(cols, r)) for r in cur]
    for d in data:
        for k in ("headings", "code_langs", "scripts", "script_langs", "tag_density"):
            d[k] = json.loads(d[k])
        d["tools"] = d["tools"].split(); d["tags"] = d["tags"].split()
    Path(a.json).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    # markdown report
    total_words = sum(d["words"] for d in data)
    with_scripts = sum(1 for d in data if d["scripts"])
    with_refs = sum(1 for d in data if d["refs"])
    with_evals = sum(1 for d in data if d["has_evals"])
    L = ["# الفهرس العميق لأطلس KOSIF (قراءة كاملة لنص كل مهارة)", "",
         f"- المهارات: **{len(data):,}** في {len({d['plugin'] for d in data}):,} إضافة. إجمالي كلمات SKILL.md: **{total_words:,}**.",
         f"- مهارات تحمل سكربتات: {with_scripts:,} · تحمل مراجع/قوالب: {with_refs:,} · تحمل تقييمات: {with_evals:,}.",
         f"- بُني بـ `tools/deep_index.py` في {time.time() - t0:.0f} ثانية. البحث النصي الكامل: `tools/atlas-deep.sqlite` (FTS5)، والبيانات المدمجة: `tools/atlas-deep.json`.", "",
         "## توزيع المجالات (وسم من قراءة النص الكامل، والمهارة قد تحمل عدة وسوم)", "", "| الوسم | عدد المهارات | أكثر 5 مهارات تركيزاً عليه (كثافة الذكر لكل ألف كلمة · حجم النص) |", "|---|---|---|"]
    by_tag = defaultdict(list)
    for d in data:
        for t in d["tags"]:
            by_tag[t].append(d)
    import math
    for t, c in tag_count.most_common():
        seen, top = set(), []
        for d in sorted(by_tag[t], key=lambda d: d["tag_density"].get(t, 0) * math.log1p(d["words"]), reverse=True):
            if d["name"] in seen:
                continue
            seen.add(d["name"]); top.append(d)
            if len(top) == 5:
                break
        L.append(f"| {t} | {c:,} | " + " · ".join(f"`{d['name']}` ({d['tag_density'].get(t, 0)}/k·{d['words']}w)" for d in top) + " |")
    L += ["", "## الأدوات والمكتبات الأكثر ذكراً في النصوص", "", "| الأداة | عدد المهارات |", "|---|---|"]
    for t, c in tool_count.most_common(60):
        L.append(f"| {t} | {c:,} |")
    L += ["", "## لغات السكربتات المرافقة", ""]
    sl = Counter()
    for d in data:
        sl.update(d["script_langs"])
    L += [f"- {k}: {v:,}" for k, v in sl.most_common()]
    L += ["", "## كيف تبحث", "",
          "```python", "import sqlite3; db = sqlite3.connect('tools/atlas-deep.sqlite')",
          "for r in db.execute(\"SELECT s.name, s.plugin, s.richness FROM skill_fts f JOIN skill s ON s.id=f.rowid WHERE skill_fts MATCH 'ffmpeg AND (cut OR transition)' ORDER BY s.richness DESC LIMIT 20\"): print(r)",
          "```", ""]
    Path(a.md).write_text("\n".join(L), encoding="utf-8")
    print(f"done: {len(data)} skills, {total_words:,} words, {time.time() - t0:.0f}s → {a.db}, {a.json}, {a.md}")


if __name__ == "__main__":
    main()
