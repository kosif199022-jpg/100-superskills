# القراءة الكاملة لأطلس KOSIF — بطاقات v2 (تدريج أدلة من النص الكامل لكل مهارة)

- بطاقات: **15,122**؛ منها 6 مقروءة يدوياً بالكامل. متوسط الجودة 2.87/5.
- كل بطاقة: ملخص، مجال أساسي وثانوي (من كثافة الوسوم)، قدرات (من العناوين)، مدخلات/مخرجات (من أقسام المتطلبات/المخرجات)، جودة بأربع درجات وسبب مُعدَّد، أعلام خطر، سكربتات، درجة مركبة.
- التفصيل الكامل في `tools/deep-read/cards.jsonl` و`tools/atlas-deep-read.json` وجدول `card` في SQLite. التقرير الموحّد: `ADVANCED-INDEX.md`.

## المجالات وأفضل 10 في كل مجال (بالجودة ثم المركبة)

### agents-orchestration — 1,758

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `agenthub` (155-agenthub) | 5 | 100 | 6 | — | Multi-agent collaboration plugin that spawns N parallel subagents competing on the same task via git |
| `teams-setup` (2094-brewcode) | 5 | 100 | 7 | needs-paid-api | Creates and manages dynamic teams of domain agents. Triggers: create team, agent team, team status,  |
| `agent-dev` (2103-agent-dev-kit) | 5 | 100 | 5 | — | Builds one TypeScript AI agent or RAG increment from a spec-dev-kit spec (and optional html-generato |
| `jfrog-mcp-management` (1980-jfrog) | 5 | 99 | 2 | — | Use to install, list, or remove MCP servers, and to discover which MCPs the user can install — inclu |
| `agent-capability-analyzer` (1547-plugin-creator) | 5 | 96 | 2 | — | Runs the description-drift experiment — spawns all Claude Code agents simultaneously to collect self |
| `orchestrate-frontend` (2107-frontend-orchestrator-kit) | 5 | 92 | 4 | — | Runs the frontend-only app-dev-kit pipeline — spec-dev-kit to author a spec if needed, html-generato |
| `deployment` (1209-crowdstrike-falcon-fusion) | 5 | 92 | 5 | needs-paid-api | Import, release, and manage Falcon Fusion workflow definitions in a CID. TRIGGER when user asks to i |
| `generate-spec` (2109-spec-dev-kit) | 5 | 92 | 13 | — | Transforms raw user requirements in .spec/context/ into a validated, approved hybrid YAML+Markdown s |
| `agents-pay` (363-aws-agents) | 5 | 90 | 7 | needs-paid-api | Use when THIS agent needs to pay for x402-protected content at runtime: hitting a paywall mid-task,  |
| `building-mcp-server-on-cloudflare` (2693-cloudflare) | 5 | 89 | 0 | — | Builds remote MCP (Model Context Protocol) servers on Cloudflare Workers with tools, OAuth authentic |

### backend-api — 1,522

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `creating-kubernetes-deployments` (1735-kubernetes-deployment-creator) | 5 | 100 | 4 | needs-paid-api | Deploy applications to Kubernetes with production-ready manifests. |
| `backend-dev` (2105-backend-dev-kit) | 5 | 100 | 5 | — | Builds one Express API resource increment from a spec-dev-kit spec (and optional html-generator-kit  |
| `code-to-prd` (198-product-skills) | 5 | 95 | 2 | — | Reverse-engineer any codebase into a complete Product Requirements Document (PRD). Analyzes routes,  |
| `jfrog` (1980-jfrog) | 5 | 93 | 5 | — | Interact with the JFrog Platform via the JFrog CLI, JFrog MCP server and REST/GraphQL APIs. Use this |
| `aiq-research` (2707-nvidia) | 5 | 92 | 1 | — | Use when asked to run deep research or AI-Q research through a reachable NVIDIA AI-Q Blueprint backe |
| `tracking-crypto-prices` (1670-market-price-tracker) | 5 | 90 | 4 | needs-paid-api | Track real-time cryptocurrency prices across exchanges with historical |
| `sentry-enterprise-rbac` (1903-sentry-pack) | 5 | 90 | 0 | needs-paid-api | Configure enterprise role-based access control, SSO/SAML2, and SCIM |
| `hf-cloud-sagemaker-production-defaults` (1514-huggingface-skills) | 5 | 89 | 6 | needs-paid-api | Create a SageMaker endpoint (real-time, real-time scale-to-zero, or async) with autoscaling, CloudWa |
| `routing-dex-trades` (1665-dex-aggregator-router) | 5 | 88 | 6 | needs-paid-api | Route trades across multiple DEXs to find optimal prices with minimal |
| `lokalise-common-errors` (1880-lokalise-pack) | 5 | 88 | 0 | — | Diagnose and fix Lokalise common errors and exceptions. |

### testing-qa — 1,172

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `audit-tests` (1803-intent-labs-pack) | 5 | 100 | 5 | — | Diagnostic-only test suite auditor. Classifies repo type, maps against\ |
| `modernize-test-starter` (3217-ui5-modernization) | 5 | 100 | 6 | — | Modernize QUnit unit tests and OPA5 integration tests to the UI5 Test Starter concept. Use this skil |
| `test-suite-generator` (3595-done-when-pipeline) | 5 | 100 | 3 | needs-paid-api | Turn an EARS spec + done_when.yaml contract into the full test pyramid: existence checks (ripgrep/tr |
| `qa-walkthrough-pr` (2045-qa-walkthrough-pr) | 5 | 99 | 3 | — | Guided manual QA walkthrough of a PR or branch — test plan as a beads epic, stepped interactively. |
| `statistical-analyst` (184-statistical-analyst) | 5 | 98 | 3 | — | Run hypothesis tests, analyze A/B experiment results, calculate sample sizes, and interpret statisti |
| `statistical-analysis` (3202-quantitative-sciences) | 5 | 97 | 1 | — | Guided statistical analysis for research data - test selection, assumption checking, effect sizes, p |
| `787-crisis-debugging-advisor` (247-claude-dev-infrastructure) | 5 | 91 | 1 | — |  |
| `playwright` (1251-playwright) | 5 | 90 | 0 | — | Browser automation with Playwright for Python. Use when testing websites, taking screenshots, fillin |
| `configure-ux-testing` (2145-configure-plugin) | 5 | 89 | 1 | — | UX testing: Playwright E2E, axe-core a11y, visual regression. Use when setting up E2E testing, scree |
| `writing-skills` (2679-superpowers) | 5 | 88 | 1 | — | Use when creating new skills, editing existing skills, or verifying skills work before deployment |

### git-github — 932

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `uxd-prototype-publish` (3010-uxd-prototype) | 5 | 100 | 4 | — | Publish a prototype to a git merge request, GitHub Pages, GitLab Pages, or Vercel. Use when sharing  |
| `exec` (3229-planning) | 5 | 96 | 11 | — | Execute plan tasks sequentially using subagents. Use when user says 'exec', 'execute plan', 'run pla |
| `9613-pull-request` (2476-source-control) | 5 | 95 | 10 | needs-paid-api | When the bundled pr skill or built-in commit-push-pr command resolves in this session, prefer pr for |
| `scaffold-go-cli` (1033-scaffold-go-cli) | 5 | 93 | 0 | — | Scaffold a Go CLI with Cobra, GoReleaser, CI, and Homebrew publishing. Use for "scaffold a Go CLI";  |
| `new` (3230-release-tools) | 5 | 93 | 3 | — | Use when user asks to create a release, cut a release, or publish a version. Auto-detects GitHub vs  |
| `scaffold-go-library` (1034-scaffold-go-library) | 5 | 91 | 0 | — | Scaffold a Go library with changelog-only releases, golangci-lint, and CI. Use for "scaffold a Go li |
| `git-worktree` (2078-yellow-core) | 5 | 91 | 1 | — | Git worktree management for isolated parallel development. Use when reviewing PRs in isolation, work |
| `figma-ci-integration` (1851-figma-pack) | 5 | 89 | 0 | — | Automate Figma design token sync and asset export in CI/CD pipelines. |
| `git-chain` (1233-git-chain) | 5 | 89 | 0 | — | Manage and rebase chains of dependent Git branches (stacked branches). Use when working with multipl |
| `scaffold-zig-cli` (1038-scaffold-zig-cli) | 5 | 89 | 0 | — | Scaffold a new Zig CLI for Zig 0.16 or later with build.zig, cross-compiled releases, and CI. Use fo |

### other — 904

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `aggregating-crypto-news` (1660-crypto-news-aggregator) | 5 | 60 | 5 | — | Aggregate breaking cryptocurrency news from 50+ sources including CoinDesk, |
| `calculating-crypto-taxes` (1663-crypto-tax-calculator) | 5 | 60 | 5 | — | Calculate cryptocurrency tax obligations with cost basis tracking, capital |
| `coreweave-core-workflow-b` (1842-coreweave-pack) | 5 | 42 | 0 | — | Run distributed GPU training jobs on CoreWeave with multi-node PyTorch. |
| `optimizing-gas-fees` (1667-gas-fee-optimizer) | 4 | 52 | 5 | — | Optimize blockchain gas costs by analyzing prices, patterns, and timing. |
| `planning-with-files` (3599-pdforge) | 4 | 52 | 4 | — | Manus 风格的持久化 Markdown 规划系统，用于复杂多步骤任务。 Use when: (1) 任务超过 3 步, (2) 研究需要多个来源, (3) 任务跨越多个会话, (4) 需要追踪错误 |
| `tilelang2ascend-operator-project-init` (1508-tilelang2ascendc-ops-generator) | 4 | 48 | 1 | — | 初始化 AscendC 算子工程并创建可编译的算子骨架。触发场景：(1) 用户要求创建新算子；(2) 关键词：ascendc算子、新建算子、算子目录、算子初始化；(3) 需要基于 ascend-ker |
| `aasm-coder` (2214-majestic-rails) | 4 | 38 | 0 | needs-paid-api | AASM state machines for Rails. |
| `sync-profiles` (1800-claudebase) | 4 | 36 | 0 | — | Use when the user wants to list, create, switch, delete, compare, or inspect config sync profiles. |
| `hugo-new` (1383-hugo-blog) | 4 | 35 | 0 | — | This skill should be used when the user asks to "create new content", "hugo new", "new post", "new b |
| `bun-publish` (2174-typescript-plugin) | 4 | 34 | 0 | — | Bun publish to npm. Use when the user wants to release to npm, preview with --dry-run, publish a sco |

### claude-code-meta — 882

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `output-style-creator` (1547-plugin-creator) | 5 | 100 | 3 | — | Create, validate, and diagnose Claude Code output styles — the file that sets Claude's role, tone, a |
| `skill-creator` (1547-plugin-creator) | 5 | 97 | 10 | — | Use when creating a new skill or updating an existing skill that extends Claude's capabilities with  |
| `obsidian-deploy-integration` (1888-obsidian-pack) | 5 | 87 | 0 | — | Publish Obsidian plugins to the community plugin directory. |
| `skill-interop` (3406-skill-craft) | 5 | 85 | 2 | — | Use when authoring or reviewing a portable multi-host agent skill (Grok, Claude Code, Codex, Hermes) |
| `janitor-report` (1653-skills-janitor) | 5 | 81 | 0 | — | Full health check of all your skills in one report. Use when the user wants to check for errors, fin |
| `framer-local-dev-loop` (1858-framer-pack) | 5 | 81 | 0 | — | Configure Framer local development with hot reload and testing. |
| `hook-development` (301-plugin-dev) | 5 | 79 | 3 | — | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop  |
| `obsidian-upgrade-migration` (1888-obsidian-pack) | 5 | 75 | 0 | — | Migrate Obsidian plugins between API versions and handle breaking changes. |
| `skill-creator-doctor` (247-claude-dev-infrastructure) | 5 | 73 | 8 | — | Create, repair, maintain, and consolidate skills. This skill should be used when users want to creat |
| `validate-skillmd` (1803-intent-labs-pack) | 5 | 70 | 0 | needs-paid-api | Validate a SKILL.md file against the four-tier validation system: Tier 0 (locate), Tier 1 (standard  |

### research — 693

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `aeo` (192-marketing-skills) | 5 | 100 | 3 | needs-paid-api | Answer Engine Optimization (AEO) skill — optimize content to be cited by AI language models (ChatGPT |
| `citation-management` (3199-evidence-lab-core) | 5 | 100 | 8 | needs-paid-api | Comprehensive citation management for academic research. Search OpenAlex, PubMed, and Google Scholar |
| `literature-review` (3206-literature-publication) | 5 | 100 | 3 | — | Plan and conduct reproducible literature reviews with explicit search boundaries, documented screeni |
| `research-summarizer` (198-product-skills) | 5 | 95 | 2 | — | Structured research summarization agent skill for non-dev users. Handles academic papers, web articl |
| `product-research` (217-research-ops-skills) | 5 | 94 | 6 | — | Use when planning and synthesizing product/user research as a method-and-repository discipline — sel |
| `huggingface-paper-publisher` (1514-huggingface-skills) | 5 | 89 | 1 | needs-paid-api | Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking paper |
| `peer-review` (3206-literature-publication) | 5 | 88 | 8 | — | Prepare evidence-bounded, constructive peer-review drafts and structured manuscript assessments. Use |
| `seo-content` (2217-majestic-seo) | 5 | 87 | 3 | — | Create or refresh one SEO or AEO article, from research through audited draft. |
| `soc2-compliance` (214-ra-qm-skills) | 5 | 82 | 3 | — | Use when the user asks to prepare for SOC 2 audits, map Trust Service Criteria, build control matric |
| `litreview` (222-litreview) | 5 | 81 | 4 | needs-paid-api | Academic literature orientation skill that searches papers via free keyless APIs (PubMed E-utilities |

### devops-ci — 582

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `nextflow-development` (314-bio-research) | 5 | 100 | 5 | — | Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing |
| `aiq-deploy` (2707-nvidia) | 5 | 98 | 0 | — | Use when asked to install, deploy, run, validate, troubleshoot, or stop NVIDIA AI-Q Blueprint infras |
| `databricks-bundle-medic` (1844-databricks-pack) | 5 | 95 | 3 | needs-paid-api | Fix the deploy-time foot-guns of Databricks Asset Bundles (DAB) and the infrastructure operations ar |
| `render-deploy` (2993-render) | 5 | 93 | 0 | needs-paid-api | Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providi |
| `shipwright-deploy` (3154-shipwright-deploy) | 5 | 92 | 0 | — | Deploy to Jelastic (Infomaniak) with smoke test verification, rollback support, and Supabase migrati |
| `sentry-ci-integration` (1903-sentry-pack) | 5 | 91 | 0 | — | Integrate Sentry into CI/CD pipelines for automated release creation, |
| `capacity` (2511-azure) | 5 | 88 | 4 | needs-paid-api, hub-doc | Discovers available Azure OpenAI model capacity across regions and projects. Analyzes quota limits,  |
| `sentry-deploy-integration` (1903-sentry-pack) | 5 | 88 | 0 | — | Track deployments and release health in Sentry. |
| `vercel-deploy-integration` (1913-vercel-pack) | 5 | 88 | 0 | — | Deploy and manage Vercel production deployments with promotion, rollback, |
| `lindy-deploy-integration` (1877-lindy-pack) | 5 | 86 | 0 | needs-paid-api | Deploy applications that integrate with Lindy AI agents. |

### legal-contracts — 508

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `gdpr-dsgvo-expert` (214-ra-qm-skills) | 5 | 100 | 3 | — | GDPR and German DSGVO compliance automation. Scans codebases for privacy risks, generates DPIA docum |
| `deal-desk` (147-commercial-skills) | 5 | 100 | 3 | needs-paid-api | Use when reviewing a specific inbound deal before close — when sales has asked for a discount that e |
| `compliance-os` (148-compliance-os) | 5 | 95 | 4 | — | Compliance OS — meta-orchestrator that lets compliance teams CONFIGURE which frameworks apply, COMPU |
| `commercial-policy` (147-commercial-skills) | 5 | 91 | 3 | needs-paid-api | Use when designing or revising a company's commercial policy — the rules of engagement governing dis |
| `tracking-token-launches` (1677-token-launch-tracker) | 5 | 86 | 5 | needs-paid-api | Track new token launches across DEXes with risk analysis and contract |
| `eu-ai-act-specialist` (214-ra-qm-skills) | 5 | 78 | 3 | — | EU AI Act (Regulation (EU) 2024/1689) operational compliance for compliance teams. Three Article-lev |
| `general-counsel-advisor` (138-c-level-skills) | 4 | 82 | 2 | — | General Counsel advisory for startups: contract review (MSA, SaaS, NDA, DPA, employment), IP strateg |
| `use-smart-contract-platform` (1104-circle) | 4 | 78 | 0 | needs-paid-api | Deploy, import, interact with, and monitor smart contracts using Circle Smart Contract Platform APIs |
| `shopify-policy-guardrails` (1905-shopify-pack) | 4 | 77 | 0 | needs-paid-api | Implement Shopify app policy enforcement with ESLint rules for API key |
| `gamma-data-handling` (1860-gamma-pack) | 4 | 76 | 0 | needs-paid-api | Handle data privacy, retention, and compliance for Gamma integrations. |

### productivity-email — 489

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `google-workspace-cli` (150-google-workspace-cli) | 5 | 88 | 5 | — | Google Workspace administration via the gws CLI (github.com/googleworkspace/cli). Install, authentic |
| `granola-ci-integration` (1863-granola-pack) | 5 | 85 | 0 | needs-paid-api | Build automated pipelines from Granola meeting notes to GitHub Issues, |
| `hubspot-contact-dedup` (1868-hubspot-pack) | 5 | 74 | 0 | needs-paid-api | Deduplicate HubSpot contacts at production scale — surviving import storms, wrong-winner merges, fuz |
| `podium-call-transcript-pipeline` (1893-podium-pack) | 5 | 72 | 4 | — | Durable, idempotent ingest pipeline for Podium call transcripts — the layer between |
| `jq-json-processing` (2173-tools-plugin) | 5 | 61 | 0 | — | jq JSON processing: query, filter, transform JSON. Use when parsing JSON files, filtering arrays/obj |
| `meetings` (208-meetings) | 4 | 92 | 3 | needs-paid-api | Use when someone wants to decide whether a meeting is worth calling, price a meeting in dollars, bui |
| `inbox-setup` (206-email) | 4 | 90 | 3 | needs-paid-api | One-time setup skill that builds a personalized inbox triage knowledge base via interactive intervie |
| `inbox-triage` (206-email) | 4 | 90 | 3 | needs-paid-api | Runs a full inbox triage using the knowledge base created by the 'inbox-setup' skill. Light-intake b |
| `react-email` (2994-resend) | 4 | 84 | 0 | needs-paid-api | Use when building HTML email templates with React components, adding a visual email editor to an app |
| `resend` (2994-resend) | 4 | 82 | 0 | needs-paid-api | Use when working with the Resend email API — sending transactional emails (single or batch), receivi |

### database — 473

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `automating-database-backups` (1686-database-backup-automator) | 5 | 100 | 5 | — | Automate database backup processes with scheduling, compression, and |
| `generating-stored-procedures` (1707-stored-procedure-generator) | 5 | 100 | 3 | — | Use when you need to generate, validate, or deploy stored procedures |
| `prisma-upgrade-v7` (2930-prisma) | 5 | 92 | 0 | — | Complete migration guide from Prisma ORM v6 to v7 covering all breaking changes. Use when upgrading  |
| `supabase-deploy-integration` (1908-supabase-pack) | 5 | 90 | 0 | needs-paid-api | Deploy and manage Supabase projects in production. Covers database migrations, |
| `supabase-local-dev-loop` (1908-supabase-pack) | 5 | 89 | 0 | — | Configure Supabase local development with the CLI, Docker, and migration |
| `elevenlabs-upgrade-migration` (1847-elevenlabs-pack) | 5 | 84 | 0 | needs-paid-api | Upgrade ElevenLabs SDK versions and migrate between API model generations. Use when upgrading the el |
| `seo` (2585-seo) | 5 | 74 | 40 | needs-paid-api | Deterministic LLM-first SEO audits for websites, blog posts, and GitHub repositories. Use this when  |
| `setup-warehouse-redshift` (3130-confidence) | 5 | 73 | 0 | — | Set up Redshift as a data warehouse for Confidence. Use when the user chose Redshift for warehouse s |
| `fiftyone-troubleshoot` (3385-fiftyone) | 5 | 72 | 0 | — | Diagnose and fix common FiftyOne issues automatically. Use when a dataset disappeared, the App won't |
| `replatform` (3419-wix) | 5 | 70 | 6 | needs-paid-api | Routes RePlatform source-to-Wix migrations to the next workflow step by inspecting migration project |

### copywriting-marketing — 449

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `design-system` (191-markdown-html-skills) | 5 | 93 | 3 | — | Captures the user's brand identity once via a 10-question onboarding wizard (primary/accent HEX + he |
| `market-research` (217-research-ops-skills) | 5 | 85 | 6 | needs-paid-api | Use when doing upstream market-research methodology — sizing a market as TAM/SAM/SOM computed BOTH t |
| `content-engine` (1520-digital-marketing-pro) | 5 | 81 | 0 | needs-paid-api | Draft marketing content in brand voice — blog posts, ad copy, email sequences, social posts, landing |
| `podium-review-request-automation` (1893-podium-pack) | 5 | 73 | 4 | — | Trigger Podium review requests from Shopify order-shipped events and survive the |
| `content-production` (192-marketing-skills) | 5 | 70 | 4 | — | Full content production pipeline — takes a topic from blank page to published-ready piece. Use when  |
| `lf-output-formatter` (2866-lf-output-formatter) | 4 | 92 | 7 | — | Shared output formatter for every LFX Marketing OS agent. Use it whenever an agent, or a Linux Found |
| `brand-guidance-authoring` (2406-web-design) | 4 | 81 | 1 | — | Author a project's generation-time brand-voice contract (brand-guidance.md) — a named aesthetic, a t |
| `clone` (3129-spotify-ads-api) | 4 | 78 | 0 | needs-paid-api | Clone an existing Spotify Ads API campaign or ad set as a validated draft hierarchy by default, with |
| `drafts` (3129-spotify-ads-api) | 4 | 78 | 0 | — | Default write workflow for Spotify Ads API campaigns, ad sets, and ads. Stage new entities or change |
| `brand-listening` (895-brightdata-plugin) | 4 | 76 | 0 | — | Social listening and brand reputation research using Bright Data's web scraping infrastructure. Coll |

### data-analysis — 398

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `exploring-llm-traces` (2957-posthog) | 5 | 86 | 6 | — | Debug and inspect LLM/AI agent traces using PostHog's MCP tools. Use when the user pastes a trace or |
| `exploring-apm-traces` (2957-posthog) | 5 | 77 | 6 | — | Investigates distributed application performance using PostHog APM (OpenTelemetry span) data via MCP |
| `coreweave-gpu-cost-leak-hunter` (1842-coreweave-pack) | 5 | 69 | 1 | needs-paid-api | Hunt down CoreWeave GPU cost leaks — idle reserved capacity, wrong-GPU-type right-sizing waste, allo |
| `generating-trading-signals` (1662-crypto-signal-generator) | 5 | 68 | 3 | — | Generate trading signals using technical indicators (RSI, MACD, Bollinger |
| `mixpanelyst` (2704-mixpanel-headless) | 5 | 67 | 2 | needs-paid-api | This skill should be used when the user asks about Mixpanel product analytics, event data, funnel an |
| `azuresql-db-container` (2512-azure-sql-database-container) | 4 | 86 | 1 | — | Runs the Azure SQL Database container locally (Private Preview): the real PaaS engine where SERVERPR |
| `sap-sqlscript` (x4371-sap-sqlscript) | 4 | 86 | 0 | — | This skill should be used when the user asks to "write a SQLScript procedure", "create HANA stored p |
| `platform-soql-query` (1444-salesforce-development) | 4 | 86 | 1 | — | SOQL query generation, optimization, and analysis with 100-point scoring. Use this skill when the us |
| `optimizing-sql-queries` (1706-sql-query-optimizer) | 4 | 84 | 2 | vague | Execute use when you need to work with query optimization. |
| `chdb-datastore` (1117-clickhouse-best-practices) | 4 | 84 | 1 | — | Use when the user has tabular data (pandas DataFrame, parquet, csv, Arrow, json) and wants to filter |

### web-frontend — 386

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `a11y-audit` (149-a11y-audit) | 5 | 100 | 2 | — | Accessibility audit skill for scanning, fixing, and verifying WCAG 2.2 Level A and AA compliance acr |
| `markdown-html-orchestrator` (191-markdown-html-skills) | 5 | 100 | 3 | — | Use when a user wants to convert any markdown file in their Claude project into a single-file, light |
| `tsdown` (2943-tsdown) | 5 | 93 | 0 | — | Bundle TypeScript and JavaScript libraries with blazing-fast speed powered by Rolldown. Use when bui |
| `generate-html` (2108-html-generator-kit) | 5 | 91 | 7 | — | Transforms a validated spec from .spec/app/current.json into a clickable multi-page HTML prototype a |
| `power-apps-code-apps` (2354-power-platform) | 5 | 88 | 0 | — | Use when building, scaffolding, debugging, or deploying Microsoft Power Apps Code Apps using React,  |
| `clerk-install-auth` (1837-clerk-pack) | 5 | 87 | 0 | — | Install and configure Clerk SDK/CLI authentication. |
| `clerk-upgrade-migration` (1837-clerk-pack) | 5 | 85 | 0 | — | Manage Clerk SDK version upgrades and handle breaking changes. |
| `engineer-design-diagram` (1722-engineer-design-diagram) | 5 | 84 | 4 | — | Generate production-grade engineering design diagrams (architecture,\ |
| `process-infographic` (x4919-visual-gen) | 5 | 78 | 1 | — | This skill should be used when the user asks to "create an infographic", "generate a process flow",  |
| `exploratory-data-analysis` (3211-structured-data-analysis) | 5 | 73 | 13 | — | Perform bounded, local exploratory analysis of explicitly supported scientific files. Use for redact |

### security — 366

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `auditing-wallet-security` (1680-wallet-security-auditor) | 5 | 98 | 5 | — | Audit wallet security by analyzing token approvals, permissions, and |
| `information-security-manager-iso27001` (214-ra-qm-skills) | 5 | 88 | 2 | — | ISO 27001 ISMS implementation and cybersecurity governance for HealthTech and MedTech companies. Use |
| `sap-dependency-security` (x4361-sap-dependency-security) | 5 | 87 | 1 | — | SAP dependency security and MCP executable trust policy with secure upgrades, cooldowns, staged roll |
| `security-audit` (2664-project) | 5 | 87 | 0 | needs-paid-api | This skill should be used when the user says \"security audit\", \"check for vulnerabilities\", \"se |
| `octopus-security-audit` (2673-claude-octopus) | 5 | 84 | 0 | — | OWASP compliance, vulnerability scanning, and adversarial red team testing — use for security review |
| `podium-auth` (1893-podium-pack) | 5 | 82 | 4 | needs-paid-api | Authenticate production Podium integrations and survive the auth-side failures — |
| `wrangler` (883-cloudflare) | 5 | 77 | 0 | needs-paid-api | Cloudflare Workers CLI for deploying, developing, and managing Workers, KV, R2, D1, Vectorize, Hyper |
| `dx-code-analyzer-run` (1444-salesforce-development) | 5 | 76 | 9 | — | Run Salesforce Code Analyzer to scan code for security, performance, best practice, and code style v |
| `huggingface-llm-trainer` (1514-huggingface-skills) | 5 | 68 | 8 | marketing-fluff, needs-paid-api | Train or fine-tune language and vision models using TRL (Transformer Reinforcement Learning) or Unsl |
| `clay-multi-env-setup` (1836-clay-pack) | 5 | 64 | 0 | needs-paid-api | Configure Clay integrations across development, staging, and production |

### cloud-edge — 287

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `benchmark-sandbox` (3256-vercel) | 5 | 100 | 5 | needs-paid-api | Run vercel-plugin eval scenarios in Vercel Sandboxes instead of local WezTerm panels. Provisions eph |
| `aws-lambda-durable-functions` (370-aws-serverless) | 5 | 91 | 0 | — | Build resilient, long-running, multi-step applications with AWS Lambda durable functions with automa |
| `vercel-advanced-troubleshooting` (1913-vercel-pack) | 5 | 90 | 0 | — | Advanced debugging for hard-to-diagnose Vercel issues including cold |
| `sentry-architecture-variants` (1903-sentry-pack) | 5 | 89 | 0 | needs-paid-api | Configure Sentry error tracking and performance monitoring for different |
| `vercel-migration-deep-dive` (1913-vercel-pack) | 5 | 88 | 0 | — | Migrate to Vercel from other platforms or re-architecture existing Vercel |
| `dynamo-router-starter` (2707-nvidia) | 5 | 87 | 1 | — | Start or patch Dynamo router modes and run router endpoint smoke checks. Use for round-robin, KV-awa |
| `llm-to-bedrock` (375-migration-to-aws) | 5 | 81 | 17 | needs-paid-api | Use when the user wants to migrate code that calls OpenAI, Gemini/Google AI, or the Anthropic API to |
| `dynamo-interconnect-check` (2707-nvidia) | 5 | 80 | 1 | — | Validate that a Dynamo deployment's NIXL/UCX/NCCL interconnect is ready for disaggregated serving ov |
| `wrangler` (2693-cloudflare) | 5 | 76 | 0 | needs-paid-api | Cloudflare Workers CLI for deploying, developing, and managing Workers, KV, R2, D1, Vectorize, Hyper |
| `hyperpod-node-debugger` (374-sagemaker-ai) | 5 | 70 | 4 | — | Diagnose and remediate per-node issues on a HyperPod cluster (EKS or Slurm) — a specific node is unh |

### mobile — 244

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `app-store-optimization` (192-marketing-skills) | 5 | 76 | 8 | needs-paid-api | App Store Optimization (ASO) toolkit for researching keywords, analyzing competitor rankings, genera |
| `dt-setup-ios` (1368-dynatrace) | 4 | 85 | 2 | — | Set up the Dynatrace iOS SDK (OneAgent) in an iOS project using Swift Package Manager. Automates add |
| `expo-deployment` (2695-expo) | 4 | 82 | 0 | — | Deploying Expo apps to iOS App Store, Android Play Store, web hosting, and API routes |
| `mobile-checkout` (1342-dodopayments) | 4 | 78 | 0 | needs-paid-api | Guide for implementing mobile in-app checkout with Dodo Payments across React Native, Flutter, iOS,  |
| `dt-setup-flutter` (1368-dynatrace) | 4 | 78 | 0 | — | Integrate the Dynatrace Flutter Plugin into a Flutter project — dependency setup, config, SDK bootst |
| `revenuecat-troubleshoot` (2996-revenuecat) | 4 | 73 | 0 | needs-paid-api | Diagnose and resolve RevenueCat integration issues — inspects dashboard configuration through the Re |
| `app-store-release-pipeline` (2340-mobile-engineering) | 4 | 70 | 0 | — | Step-by-step guide for automating the iOS App Store and Google Play release pipeline — code signing, |
| `kotlin` (339-appwrite) | 4 | 70 | 0 | needs-paid-api | Appwrite Kotlin SDK skill. Use when building native Android apps or server-side Kotlin/JVM backends  |
| `touch-app` (1567-tonone) | 4 | 67 | 0 | needs-paid-api | Produce a complete mobile app architecture design — platform choice, navigation structure, state man |
| `upgrading-expo` (2695-expo) | 4 | 67 | 0 | — | Guidelines for upgrading Expo SDK versions and fixing dependency issues |

### docs-writing — 217

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `document-sync` (247-claude-dev-infrastructure) | 5 | 88 | 3 | — | A robust skill that analyzes your app's actual codebase, tech stack, configuration, and architecture |
| `yapi-skill` (3611-spellbook-skills) | 5 | 79 | 6 | — | Python stdlib scripts for the YApi OpenAPI (no Java/Docker/MCP) — search interfaces, query details,  |
| `xray-method` (21-codebase-xray) | 5 | 73 | 9 | — | X-ray method: mechanical structure extraction fused with semantic reading into a ground-truth accoun |
| `qms-audit-expert` (214-ra-qm-skills) | 5 | 60 | 1 | — | ISO 13485 internal audit expertise for medical device QMS. Covers audit planning, execution, nonconf |
| `analyze-workflow` (61-codebase-xray) | 5 | 57 | 0 | needs-paid-api | Run an X-ray: document WHAT, WHY, HOW and CONSEQUENCES into phased files, with concurrent-run suppor |
| `computer-usage-summary` (2182-computer-usage-summary-skill) | 5 | 51 | 1 | — | Use when the user asks what they did on a Mac, requests a daily or multi-day ActivityWatch report, n |
| `extracting-chm` (3136-doc-util) | 4 | 83 | 1 | — | This skill handles CHM (Compiled HTML Help) files, the Windows help file format with .chm extension. |
| `ticket-drafting-guidelines` (2143-communication-plugin) | 4 | 78 | 0 | — | What/Why/How prose structure and neutral, positive register for issues, PR descriptions, and tickets |
| `shipwright-changelog` (3152-shipwright-changelog) | 4 | 77 | 0 | — | Parses Conventional Commits from git history, generates Keep-a-Changelog entries, creates version ta |
| `skill-doc-sync` (2673-claude-octopus) | 4 | 76 | 0 | — | Post-ship doc sync across project markdown. Use when: sync docs, update docs, document changes, rele |

### decision-reasoning — 214

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `chief-data-officer-advisor` (138-c-level-skills) | 5 | 74 | 3 | — | Chief Data Officer advisory for startups: AI training data rights and consent provenance, data produ |
| `feature-flags-architect` (168-feature-flags-architect) | 5 | 67 | 3 | needs-paid-api | Use when adding, retiring, or auditing feature flags. Triggers on "add a flag", "ship behind a flag" |
| `coreweave-gpu-node-forensics` (1842-coreweave-pack) | 5 | 57 | 1 | — | Triage a dead or degraded GPU on a CoreWeave node fast — decide reschedule vs GPU-reset vs node-rebo |
| `skill-debate` (2673-claude-octopus) | 4 | 74 | 0 | — | Structured multi-provider AI debates between Claude and available advisors — use for critical decisi |
| `decision-logger` (138-c-level-skills) | 4 | 70 | 1 | needs-paid-api | Two-layer memory architecture for board meeting decisions. Manages raw transcripts (Layer 1) and app |
| `adr` (1450-chronicle) | 4 | 64 | 18 | — | Triage the cockpit decision trail as an inbox and promote the decisions that mattered into Architect |
| `pricing-strategist` (147-commercial-skills) | 4 | 62 | 3 | needs-paid-api | Use when designing or revisiting product pricing — selecting a pricing model (subscription seat-base |
| `skill-decision-support` (2673-claude-octopus) | 4 | 61 | 0 | — | Present options with trade-offs for informed decision-making — use when choosing between approaches |
| `agent-decision-receipts` (214-ra-qm-skills) | 4 | 58 | 1 | — | Mint a tamper-evident, post-quantum-signed receipt for a consequential agent action (deploy, delete, |
| `ce-brainstorm` (1391-compound-engineering) | 4 | 56 | 4 | — | Explore vague or ambitious ideas into a right-sized requirements-only unified plan. Use when the use |

### design-ui — 206

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `fix-cyclic-deps` (3217-ui5-modernization) | 5 | 100 | 3 | — | Detect and resolve cyclic module dependencies introduced during UI5 modernization. Trigger when user |
| `add-app-to-server` (2536-mcp-apps) | 5 | 86 | 0 | — | This skill should be used when the user asks to "add an app to my MCP server", "add UI to my MCP ser |
| `ui-design-system` (198-product-skills) | 5 | 80 | 1 | — | UI design system toolkit for Senior UI Designer including design token generation, component documen |
| `fix-js-globals` (3217-ui5-modernization) | 4 | 80 | 0 | — | Fix JavaScript `no-globals` errors that UI5 linter reports but cannot auto-fix. Use this skill when  |
| `ui-toolkit/web` (330-zoom-plugin) | 4 | 79 | 0 | needs-paid-api | Reference skill for Zoom Video SDK UI Toolkit. Use after routing to a web video workflow when you wa |
| `shopify-checkout-extensions` (1905-shopify-pack) | 4 | 77 | 0 | — | Build Checkout UI Extensions to customize Shopify checkout with sandboxed |
| `shadcn` (2722-vercel) | 4 | 73 | 0 | — | shadcn/ui expert guidance — CLI, component installation, composition patterns, custom registries, th |
| `doc-this-design-system` (3388-doc-this) | 4 | 73 | 0 | — | Use as an optional Discovery agent that extracts design tokens from CSS/SCSS/LESS variables, Tailwin |
| `visual-validator` (2210-majestic-frontend) | 4 | 73 | 0 | — | Validate rendered UI for responsive behavior, visual accessibility, regressions, and design-system c |
| `find-design-agency` (1761-servicegraph) | 4 | 72 | 0 | needs-paid-api | Use whenever the user wants to find, shortlist, vet, or enrich US design and creative agencies — gra |

### accounting-audit — 195

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `kubernetes-operator` (175-kubernetes-operator) | 4 | 92 | 3 | — | Use when building a Kubernetes Operator — custom controllers that reconcile CRD state. Triggers on " |
| `chase-overdue-invoices` (1522-intuit-quickbooks) | 4 | 74 | 0 | needs-paid-api | Send payment reminders for invoices with tone matched to aging. ALWAYS use this skill when the user  |
| `9591-running-retro` (2473-session-flow) | 4 | 72 | 4 | vague, needs-paid-api | Take a mid-session retro checkpoint: a subagent files findings from the transcript so far into a run |
| `9409-reduce` (2428-coupling) | 4 | 71 | 3 | vague | Iteratively reduce coupling at any altitude (documents, code modules, applications, repositories): s |
| `linkedin-content` (197-linkedin) | 4 | 71 | 3 | — | Use when someone wants to write, edit, or lint a LinkedIn post — a story, how-to, opinion piece, car |
| `task-reconcile` (2170-taskwarrior-plugin) | 4 | 66 | 1 | — | Close taskwarrior tasks whose linked GitHub issue/PR closed or merged. Use when stale trackers pile  |
| `mac-mail-searching` (1384-mac-mail-app) | 4 | 66 | 0 | needs-paid-api | This skill should be used when the user wants to search for or find messages in Apple Mail.app — suc |
| `tres-ledger-link` (261-tres-finance-plugin) | 4 | 58 | 0 | — | Build a TRES Finance dashboard ledger URL (Transactions tab) with a precise filter set — date range, |
| `credit-based-billing` (1342-dodopayments) | 4 | 52 | 0 | needs-paid-api | Complete guide for giving customers included, free, prepaid, promotional, or top-up credits using gr |
| `phack-router` (898-p-hacking-skills) | 4 | 51 | 0 | — | Entry point for the p-hacking skills suite. Routes a request to the right sub-skill for (a) mapping  |

### architecture — 174

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `grill-with-docs` (170-grill-with-docs) | 4 | 85 | 3 | needs-paid-api | Docs-anchored grilling session — challenges a plan against the project's existing language (CONTEXT. |
| `blueprint-adr-validate` (2139-blueprint-plugin) | 4 | 84 | 2 | — | Validate ADR relationships, domain consistency, and duplicate ADR numbers. Use when auditing ADRs be |
| `cto-advisor` (138-c-level-skills) | 4 | 70 | 2 | needs-paid-api | Technical leadership guidance for engineering teams, architecture decisions, and technology strategy |
| `9360-map-components` (2415-architecture) | 4 | 63 | 2 | needs-paid-api | Chart the modules inside one deployable as a C4 component view, one directed arrow per internal buil |
| `configuring-service-meshes` (1742-service-mesh-configurator) | 4 | 62 | 4 | vague | Configure this skill configures service meshes like istio and linkerd |
| `9362-map-context` (2415-architecture) | 4 | 60 | 4 | — | Chart one software system's C4 system context from tracked configuration: actors you state and exter |
| `windsurf-reference-architecture` (1915-windsurf-pack) | 4 | 59 | 0 | — | Implement Devin Desktop (formerly Windsurf) reference architecture with optimal project structure |
| `maintainx-reference-architecture` (1882-maintainx-pack) | 4 | 55 | 0 | needs-paid-api | Production-grade architecture patterns for MaintainX integrations. |
| `doc-this-promote` (3388-doc-this) | 4 | 55 | 0 | — | Use to stage doc-this Discovery output (.doc-this-sdd/) into the project's tracked SDLC chain — the  |
| `befund-docs-drift` (251-befund) | 4 | 54 | 0 | — | Extracts falsifiable claims about current code state from CLAUDE.md, README.md, DECISIONS.md, ARCHIT |

### debugging — 161

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `crowdsec` (1208-crowdsec) | 5 | 91 | 2 | — | Use when the user is installing, configuring, operating, or debugging CrowdSec — including cscli, LA |
| `hyperpod-nccl` (374-sagemaker-ai) | 5 | 90 | 1 | — | Diagnose NCCL failures and adjacent training-pod failures on HyperPod GPU clusters (EKS or Slurm) —  |
| `sentry-debug-bundle` (1903-sentry-pack) | 5 | 79 | 0 | needs-paid-api | Collect diagnostic information for Sentry troubleshooting and support |
| `zoom-meeting-sdk-windows` (2723-zoom) | 5 | 76 | 0 | — | Zoom Meeting SDK for Windows - Native C++ SDK for embedding Zoom meetings into Windows desktop appli |
| `customerio-advanced-troubleshooting` (1843-customerio-pack) | 5 | 75 | 0 | needs-paid-api | Apply Customer.io advanced debugging and incident response. |
| `deepgram-debug-bundle` (1845-deepgram-pack) | 5 | 74 | 0 | needs-paid-api | Collect Deepgram debug evidence for support and troubleshooting. |
| `capa-officer` (214-ra-qm-skills) | 5 | 73 | 2 | — | CAPA system management for medical device QMS. Covers root cause analysis, corrective action plannin |
| `rust-reverse-engineering` (1981-rust-reverse-engineering) | 5 | 70 | 9 | — | Use when analyzing a Rust binary without source code, reverse engineering Rust executables or librar |
| `azure-diagnostics` (2511-azure) | 4 | 92 | 12 | hub-doc | Debug Azure production issues on Azure using AppLens, Azure Monitor, resource health, and safe triag |
| `kubectl-debugging` (2157-kubernetes-plugin) | 4 | 78 | 0 | — | Debug K8s pods/nodes with kubectl debug — ephemeral containers, pod copying, debug profiles, interac |

### business-strategy — 152

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `backtesting-trading-strategies` (1678-trading-strategy-backtester) | 5 | 72 | 5 | — | Backtest crypto and traditional trading strategies against historical |
| `x-twitter-growth` (192-marketing-skills) | 5 | 67 | 5 | — | X/Twitter growth engine for building audience, crafting viral content, and analyzing engagement. Use |
| `product-strategist` (198-product-skills) | 4 | 82 | 1 | — | Strategic product leadership toolkit for Head of Product covering OKR cascade generation, quarterly  |
| `document-linking` (2139-blueprint-plugin) | 4 | 78 | 0 | — | Unified ID system for PRDs, ADRs, PRPs, and GitHub issues with bidirectional links. Use when linking |
| `op` (3539-op) | 4 | 76 | 0 | — | Strategy orchestration — 17 strategies including refine, tournament, chain, review, debate, red-team |
| `adversarial-requirements` (3596-forge-teams) | 4 | 76 | 0 | — | Agent Teams 对抗式需求分析。产品倡导者撰写 PRD，技术怀疑者以代码库证据挑战，2 轮对抗后产出经过实战检验的需求文档。 Use when: (1) 新功能需要全面 PRD, (2) 需求 |
| `blueprint-story-reconcile` (2139-blueprint-plugin) | 4 | 74 | 0 | — | Reconcile PRD requirements with a story-audit drift report. Use when marking PRD entries implemented |
| `prd-create` (2973-pwdev-prd) | 4 | 74 | 0 | — | Use when the user wants a new Product Requirements Document — 'criar um PRD', 'escrever os requisito |
| `prd-export` (2973-pwdev-prd) | 4 | 74 | 0 | — | Use when the user wants a PRD exported — 'exportar o PRD', 'gerar o prd.json', 'criar issue com o PR |
| `adversarial-design` (3596-forge-teams) | 4 | 71 | 0 | — | Agent Teams 对抗式架构设计。多个架构师竞争提案，技术评论家挑战弱点，仲裁者综合裁决。 Use when: (1) 重大系统设计决策, (2) 多个可行技术方案, (3) 高风险架构变更,  |

### financial-modeling — 139

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `revenue-operations` (136-business-growth-skills) | 5 | 100 | 3 | — | Analyzes sales pipeline health, revenue forecasting accuracy, and go-to-market efficiency metrics fo |
| `slo-architect` (182-slo-architect) | 5 | 93 | 3 | — | Use when defining, reviewing, or operating SLOs/SLIs/error budgets. Triggers on "define an SLO", "wh |
| `research-finance` (217-research-ops-skills) | 5 | 84 | 6 | — | Use when managing the money for an internal R&D program or portfolio — building a multi-period progr |
| `deep-work` (205-deep-work) | 5 | 81 | 3 | — | Use when someone wants to plan a deep work day, time-block their calendar or task list, budget or cu |
| `senior-pm` (213-pm-skills) | 5 | 69 | 3 | — | Senior Project Manager for enterprise software, SaaS, and digital transformation projects. Specializ |
| `scrum-master` (213-pm-skills) | 5 | 69 | 3 | — | Advanced Scrum Master skill for data-driven agile team analysis and coaching. Use when the user asks |
| `financial-analyst` (189-finance-skills) | 4 | 92 | 4 | — | Performs financial ratio analysis, DCF valuation, budget variance analysis, and rolling forecast con |
| `commercial-forecaster` (147-commercial-skills) | 4 | 91 | 3 | needs-paid-api | Use when building a quarterly bookings forecast, ARR projection, pipeline forecast, NRR projection,  |
| `klingai-cost-controls` (1874-klingai-pack) | 4 | 78 | 0 | needs-paid-api | Implement budget limits, usage alerts, and spending controls for Kling |
| `slo-implementation` (3107-observability-monitoring) | 4 | 77 | 0 | — | Define and implement Service Level Indicators (SLIs) and Service Level Objectives (SLOs) with error  |

### llm-evals — 131

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `uxd-prototype-evaluate` (3010-uxd-prototype) | 5 | 100 | 31 | — | Evaluate a running prototype against a Jira ticket's acceptance criteria, automatically fix what fai |
| `uxd-prototype-export` (3010-uxd-prototype) | 5 | 98 | 10 | hub-doc | Export a prototype page or journey step as static HTML, a React component tree, or a PatternFly impl |
| `catlass-dsl-optimize` (1505-catlass-dsl-generator) | 5 | 88 | 1 | — | Iteratively optimize, speed up, benchmark, and profile one existing CATLASS DSL kernel on Ascend NPU |
| `social-media-analyzer` (192-marketing-skills) | 5 | 84 | 2 | needs-paid-api | Social media campaign analysis and performance tracking. Calculates engagement rates, ROI, and bench |
| `saas-metrics-coach` (189-finance-skills) | 5 | 80 | 3 | — | SaaS financial health advisor. Use when a user shares revenue or customer numbers, or mentions ARR,  |
| `skill-creator` (311-skill-creator) | 5 | 80 | 9 | — | Create new skills, modify and improve existing skills, and measure skill performance. Use when users |
| `create-skill` (1120-ambient-library) | 5 | 79 | 9 | — | Create new skills, modify and improve existing skills, and measure skill performance — with a routin |
| `customer-success-manager` (136-business-growth-skills) | 5 | 67 | 3 | needs-paid-api | Monitors customer health, predicts churn risk, and identifies expansion opportunities using weighted |
| `9466-design` (2439-evals) | 4 | 91 | 3 | — | Design an evaluation suite for an LLM-based application or a Claude Code skill: interview for measur |
| `grade-iterate` (135-agent-launcher-skills) | 4 | 87 | 3 | — | Phase 3 of building a Claude Managed Agent — the bounded grade→iterate loop. Define a CMA outcome (a |

### dataviz-dashboards — 126

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `helm-chart-builder` (172-helm-chart-builder) | 5 | 97 | 2 | — | Helm chart development agent skill and plugin for Claude Code, Codex, Gemini CLI, Cursor, OpenClaw — |
| `tracking-crypto-derivatives` (1659-crypto-derivatives-tracker) | 5 | 74 | 7 | needs-paid-api | Track cryptocurrency futures, options, and perpetual swaps with funding |
| `dt-obs-analytics` (1368-dynatrace) | 4 | 87 | 3 | — | Analyze dashboards and notebooks using Davis analyzers — anomaly detection, novelty scoring, and cor |
| `helm-chart-development` (2157-kubernetes-plugin) | 4 | 78 | 0 | — | Create, test, and package Helm charts — Chart.yaml, templates, dependencies, repo publishing. Use wh |
| `helm-values-management` (2157-kubernetes-plugin) | 4 | 78 | 0 | — | Manage Helm values — override precedence, multi-env configs, --set, schema validation, secrets. Use  |
| `build-dashboard` (317-data) | 4 | 78 | 0 | — | Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive |
| `dashboard-expert` (2704-mixpanel-headless) | 4 | 78 | 0 | — | Full CRUD and analysis for Mixpanel dashboards. Use when the user asks to build, create, analyze, re |
| `data-visualization` (317-data) | 4 | 77 | 0 | — | Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building ch |
| `ar-status` (156-autoresearch-agent) | 4 | 75 | 0 | — | Show experiment dashboard with results, active loops, and progress. Use when the user runs /ar:ar-st |
| `sap-fiori-analytical-chart` (3027-sap-fiori-mcp-server) | 4 | 73 | 0 | — | Add analytical chart (chart + table hybrid) to SAP Fiori Elements List Report using aggregated data. |

### ecommerce — 112

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `9496-manage` (2450-kindle-dedrm) | 5 | 71 | 9 | — | Manage the Kindle for PC 2.8.0 + Calibre DeDRM workflow for personal-use ebook DRM removal on books  |
| `hubspot-agency-multi-portal` (1868-hubspot-pack) | 5 | 70 | 0 | needs-paid-api | Manage 10-100 HubSpot portals for agency clients with credential isolation that prevents cross-porta |
| `analyze-x-mentions` (886-intel) | 5 | 65 | 9 | needs-paid-api | Turn a fetched X/Twitter mentions archive (tweets.jsonl from fetch-x-mentions) into a concise, data- |
| `shopify-onboarding-dev` (3055-shopify-plugin) | 4 | 92 | 4 | — | Get started building on Shopify. Use when a developer asks to build an app, build a theme, create a  |
| `shopify-use-shopify-cli` (3055-shopify-plugin) | 4 | 92 | 4 | — | Choose when the user needs **Shopify CLI** to run or fix something now: validate app or extension co |
| `shopify-install-auth` (1905-shopify-pack) | 4 | 79 | 0 | needs-paid-api | Install and configure Shopify app authentication with OAuth, session |
| `shopify-functions` (1905-shopify-pack) | 4 | 77 | 0 | — | Build Shopify Functions for custom discount, payment, and delivery logic |
| `price-comparison` (895-brightdata-plugin) | 4 | 68 | 0 | needs-paid-api | Shopping price comparison using Bright Data's web scraping infrastructure. Finds where a product is  |
| `seo-ecommerce` (347-legends-seo-dungeon) | 4 | 63 | 0 | needs-paid-api | E-commerce SEO analysis: Google Shopping visibility, Amazon marketplace intelligence, product schema |
| `knowledge-status` (3042-neo-research) | 4 | 61 | 0 | — | Show what's indexed in the neo-research knowledge store — sources, chunk counts, file sizes. Use whe |

### landing-marketing — 102

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `campaign-analytics` (192-marketing-skills) | 5 | 99 | 3 | needs-paid-api | Analyzes campaign performance with multi-touch attribution, funnel conversion analysis, and ROI calc |
| `vpe-advisor` (138-c-level-skills) | 5 | 90 | 3 | — | VP of Engineering advisory for startups: delivery throughput (DORA 4 metrics + bottleneck identifica |
| `paid-ads` (192-marketing-skills) | 4 | 84 | 2 | needs-paid-api | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), L |
| `linkedin-profile` (197-linkedin) | 4 | 82 | 3 | — | Use when someone wants their LinkedIn profile audited or rewritten — headline, About section, experi |
| `ads` (1446-marketing-skills) | 4 | 74 | 0 | needs-paid-api | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), L |
| `conversion-design` (2406-web-design) | 4 | 72 | 0 | needs-paid-api | Design and audit conversion-focused screens — funnel definition, friction-vs-trust balance, form fie |
| `product-analytics` (198-product-skills) | 4 | 71 | 1 | — | Use when defining product KPIs, building metric dashboards, running cohort or retention analysis, or |
| `cro-methodology` (3430-marketing-cro) | 4 | 62 | 0 | needs-paid-api | Audit websites and landing pages for conversion issues and design evidence-based A/B tests. Use when |
| `attribution` (1446-marketing-skills) | 4 | 57 | 0 | needs-paid-api | When the user wants to figure out which marketing actually drives conversions and revenue, choose or |
| `eighty-twenty-funnel-economics` (2199-lvtd-skills) | 3 | 65 | 0 | vague | Diagnose and prioritize sales funnel improvements by economics, conversion, split testing, and high- |

### hr-recruiting — 96

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `product-manager-toolkit` (198-product-skills) | 5 | 83 | 2 | — | Comprehensive toolkit for product managers including RICE prioritization, customer interview analysi |
| `shipwright-plan` (3158-shipwright-plan) | 5 | 66 | 0 | — | Creates detailed implementation plans from spec files via research, interview, external LLM review,  |
| `resume` (2636-resume) | 4 | 78 | 22 | — | Tailor a stored résumé to a job description and render it as a themed PDF. The résumé is supplied on |
| `shipwright-project` (3160-shipwright-project) | 4 | 74 | 0 | — | Decomposes project requirements into well-scoped planning units for /shipwright-plan. Generates CLAU |
| `ar-resume` (156-autoresearch-agent) | 4 | 73 | 0 | — | Resume a paused experiment. Checkout the experiment branch, read results history, continue iterating |
| `find-recruiting-firm` (1761-servicegraph) | 4 | 70 | 0 | needs-paid-api | Use whenever the user wants to find, shortlist, vet, or enrich US recruiting and staffing firms — ex |
| `chro-advisor` (138-c-level-skills) | 4 | 69 | 2 | — | People leadership for scaling companies. Hiring strategy, compensation design, org structure, cultur |
| `langchain-langgraph-human-in-loop` (1875-langchain-py-pack) | 4 | 66 | 0 | — | Build LangGraph 1.0 human-in-the-loop approval flows with interrupt_before\ |
| `cv-builder` (3410-career-tools) | 4 | 62 | 0 | — | Build or update a Curriculum Vitae (CV) by scanning a repo for the person's background (experience,  |
| `9585-keep-going` (2473-session-flow) | 4 | 62 | 3 | vague | Recover and continue after an interruption, rate limit, crash, or gap, or check on off-thread work t |

### healthcare — 86

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `clinical-research` (217-research-ops-skills) | 5 | 91 | 6 | — | Use when designing a prospective clinical study before submission — selecting and classifying endpoi |
| `fda-consultant-specialist` (214-ra-qm-skills) | 5 | 88 | 3 | — | FDA regulatory consultant for medical device companies. Provides 510(k)/PMA/De Novo pathway guidance |
| `mdr-745-specialist` (214-ra-qm-skills) | 5 | 84 | 1 | — | EU MDR 2017/745 compliance specialist for medical device classification, technical documentation, cl |
| `healthcare-providers-enrich` (2666-nimble) | 4 | 58 | 0 | needs-paid-api | Fills gaps in existing healthcare practitioner lists — adds missing phone numbers, credentials, spec |
| `anima-common-errors` (1822-anima-pack) | 4 | 47 | 0 | needs-paid-api | Diagnose and fix common Anima SDK design-to-code errors. |
| `eigenthinking` (1120-ambient-library) | 4 | 46 | 0 | — | Eigenthinking: nine-step framework turning tacit expert knowledge into branded, publishable IP using |
| `launchservices-health` (2159-macos-plugin) | 4 | 45 | 0 | — | Diagnose macOS LaunchServices DB bloat and launchservicesd CPU spikes. Use when launchservicesd is p |
| `improve-retention` (3438-ux-design) | 4 | 44 | 0 | — | Diagnose and fix retention problems using behavior design (B=MAP). Use when the user mentions "users |
| `design-everyday-things` (3432-product-innovation) | 4 | 42 | 0 | — | Apply foundational design principles: affordances, signifiers, constraints, feedback, and conceptual |
| `openevidence-ci-integration` (1890-openevidence-pack) | 3 | 66 | 0 | vague, needs-paid-api | Build a repeatable acceptance gate for an OpenEvidence practice rollout without inventing an API or  |

### scraping-automation — 86

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `apify-upgrade-migration` (1824-apify-pack) | 5 | 87 | 0 | — | Upgrade Apify SDK, apify-client, and Crawlee versions safely. Use when migrating between SDK version |
| `drive-automation-session` (1962-automate) | 5 | 68 | 4 | — | Drive an already-reserved Kobiton device from a natural-language intent. Opens an automation Appium  |
| `firecrawl` (3628-firecrawl) | 4 | 83 | 0 | needs-paid-api, hub-doc | Expert on Firecrawl — web scraping, crawling, search, and browser automation API for AI agents. Use  |
| `web-crawling` (1801-cli-power-skills) | 4 | 78 | 0 | — | Use when scraping web pages, automating browser interactions, crawling sites for content, or extract |
| `just-scrape` (3032-just-scrape) | 4 | 78 | 0 | needs-paid-api | Search, scrape, crawl, extract structured data, and monitor web pages via the ScrapeGraph AI CLI. Us |
| `crawlberg` (2101-crawlberg) | 4 | 77 | 0 | — | Crawl, scrape, and convert websites to Markdown using the local crawlberg CLI and its MCP server. Us |
| `brightdata-cli` (895-brightdata-plugin) | 4 | 70 | 0 | needs-paid-api | Guide for using the Bright Data CLI (`brightdata` / `bdata`) to scrape websites, search the web, ext |
| `sap-btp-intelligent-situation-automation` (x4352-sap-btp-intelligent-situation-automation) | 4 | 69 | 0 | needs-paid-api | This archived skill provides legacy guidance for SAP BTP Intelligent Situation Automation data expor |
| `competitive-intel` (895-brightdata-plugin) | 4 | 69 | 0 | needs-paid-api | Real-time competitive intelligence and market research using Bright Data's web scraping infrastructu |
| `apify-core-workflow-a` (1824-apify-pack) | 4 | 66 | 0 | — | Build a complete web scraping Actor with Crawlee and deploy to Apify. |

### education-learning — 74

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `bible-study` (2620-bible-study) | 5 | 92 | 6 | needs-paid-api | Create a researched one-page Bible study from a verse, passage, or chapter, using only the Bible and |
| `curriculum` (2524-curriculum) | 5 | 91 | 3 | — | Use when the user wants to learn a topic deeply — asks for a curriculum, learning path, self-study p |
| `scvi-tools` (314-bio-research) | 5 | 72 | 8 | — | Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need ( |
| `9499-course-digest` (2451-knowledge) | 5 | 72 | 2 | — | Extract and synthesize online video courses into repo-applicable recommendations. Use when: 'course  |
| `notebooklm` (223-notebooklm) | 5 | 71 | 3 | — | Browser automation skill for controlling Google's NotebookLM. Use when the user wants anything done  |
| `9463-teach` (2437-education) | 4 | 85 | 6 | — | Interactive multi-session learning coach for general topics or repo-grounded concepts; also a single |
| `deep-learning-book` (165-deep-learning-book) | 4 | 72 | 4 | — | Study companion and working knowledge base for the Deep Learning textbook by Goodfellow, Bengio & Co |
| `teach` (1067-bedrock) | 4 | 61 | 0 | needs-paid-api | Teaches the Second Brain to recognize a new external data source. Fetches content from Confluence, G |
| `msa-gauge-rr` (2989-quality-engineering-skills) | 4 | 60 | 0 | — | Measurement System Analysis (MSA) and Gauge Repeatability & Reproducibility (Gauge R&R) — plan, exec |
| `anki-flashcards` (1217-anki-flashcards) | 4 | 53 | 0 | — | Create and manage Anki flashcards via the AnkiConnect API. Use when the user wants to create flashca |

### game-dev — 74

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `9476-dlss5` (2443-gaming) | 4 | 86 | 2 | — | Apply, track, tune, and remove the community DLSS 5 Neural Rendering mod (OptiScaler forks) in a PC  |
| `game-trailer` (1526-gamegen) | 4 | 83 | 0 | — | Produce promo trailers from real gameplay of a Godot 4 game: a beat-synced 16:9 1080p60 trailer, a n |
| `art` (1511-homie) | 4 | 79 | 1 | needs-paid-api | Make a studio's game look like something at build time — a cover from a real frame of the game (free |
| `sprite-pipeline` (2696-game-studio) | 4 | 74 | 0 | — | Generate and normalize 2D sprite animations. Use when the user asks for full-strip generation from a |
| `game` (1511-homie) | 4 | 71 | 0 | needs-paid-api | Make or remix a multiplayer web game inside a Homie studio — every browser renders the game, strange |
| `using-bgs-archive` (878-bgs-modding-superpowers) | 4 | 67 | 0 | — | Use when the user wants to inspect, list, extract, unpack, or repack Bethesda BA2/BSA archives; dete |
| `bevy-game-engine` (2137-bevy-plugin) | 4 | 65 | 0 | — | Bevy game engine: ECS, rendering, input, and asset management. Use when building Bevy games, working |
| `maintaining-modding-environments` (878-bgs-modding-superpowers) | 4 | 51 | 0 | needs-paid-api | Use after first-run for ongoing modpack maintenance: update/install KB packs, author or register cus |
| `game-balance-economy` (2199-lvtd-skills) | 3 | 62 | 1 | vague | Balance game difficulty, resources, rewards, probability, progression, economies, and dominant strat |
| `game-playtest` (2696-game-studio) | 3 | 57 | 0 | vague | Run browser-game playtests and frontend QA. Use when the user asks for smoke tests, screenshot-based |

### storytelling — 70

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `submission` (1213-story-skills) | 4 | 79 | 0 | — | This skill should be used when the user asks to "write a query letter", "query", "querying", "pitch" |
| `story-init` (1213-story-skills) | 4 | 78 | 0 | — | This skill should be used when the user asks to "start a new story", "initialize a story project", " |
| `agile-product-owner` (198-product-skills) | 4 | 72 | 1 | — | Agile product ownership for backlog management and sprint execution. Covers user story writing, acce |
| `friction` (2120-friction) | 4 | 54 | 0 | — | Friction mining lifecycle for Total Recall. Use when working on any friction-related content: writin |
| `handoff` (3549-xm) | 4 | 51 | 0 | — | Session handoff — save comprehensive session state for cross-session continuity |
| `form-deck` (1567-tonone) | 4 | 48 | 0 | needs-paid-api | Use when asked to design a pitch deck, presentation, or slide set. Examples: "design a pitch deck",  |
| `linkedin-content-planner` (3034-linkedin-skills) | 4 | 43 | 0 | needs-paid-api | Generate a 7-day LinkedIn content plan from a theme, audience, and pillars. Produces per-day post pi |
| `linkedin-post-writer` (3034-linkedin-skills) | 4 | 39 | 0 | needs-paid-api | Draft a new LinkedIn post from scratch using one of 20 2026 hook formulas (anaphora, R.I.P., time-an |
| `bmad-sprint-run` (x4909-bmad-sprint-run) | 3 | 69 | 0 | — | This skill should be used when the user says "run the sprint", "autonomous sprint", "run all stories |
| `storybook` (2111-frontend-dev-kit) | 3 | 68 | 0 | — | Write Storybook stories using CSF3 format with TypeScript. One story file per shared/ui primitive, a |

### audio-music — 69

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `game-audio-procedural` (1526-gamegen) | 5 | 100 | 11 | needs-paid-api | Compose game music and design sound effects in code with a bundled numpy/scipy synthesis toolkit, th |
| `music` (1511-homie) | 4 | 85 | 1 | needs-paid-api | Make songs, themes and game scores for a Homie studio with ElevenLabs Music, through the creator's O |
| `sound` (1511-homie) | 4 | 81 | 1 | needs-paid-api | Make a game's sound effects and synthesized music on the creator's own computer, free, with no provi |
| `deepgram-hello-world` (1845-deepgram-pack) | 4 | 77 | 0 | needs-paid-api | Create a minimal working Deepgram transcription example. |
| `demo-video` (1644-framecraft) | 4 | 74 | 0 | — | Generate polished demo videos from a single prompt. Use when the user |
| `elevenlabs-hello-world` (1847-elevenlabs-pack) | 4 | 74 | 0 | needs-paid-api | Generate your first ElevenLabs text-to-speech audio file. Use when starting a new ElevenLabs integra |
| `speak-common-errors` (1906-speak-pack) | 4 | 67 | 0 | needs-paid-api | Diagnose and fix common Speak API errors: authentication failures, audio |
| `video-sdk/web` (3619-zoom-plugin) | 4 | 66 | 0 | — | Expert guidance for building browser-based video sessions with the Zoom Video SDK for Web (@zoom/vid |
| `elevenlabs-cost-tuning` (1847-elevenlabs-pack) | 4 | 64 | 0 | needs-paid-api | Optimize ElevenLabs costs through model selection, character-efficient patterns, caching, and usage  |
| `save-to-spotify` (3131-save-to-spotify) | 4 | 64 | 0 | needs-paid-api | Create polished audio content and save to Spotify. Produces episodes with TTS narration, a rich time |

### rag-knowledge — 64

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `podium-rag-context-bridge` (1893-podium-pack) | 5 | 84 | 4 | — | Bridge a live Podium call transcript or webchat turn to an LLM by fetching relevant |
| `podium-conversation-history-export` (1893-podium-pack) | 5 | 67 | 5 | — | Bulk-export Podium conversation, review, and contact history into a vector-store-ready |
| `langchain-embeddings-search` (1875-langchain-py-pack) | 4 | 80 | 0 | — | Build and query vector stores with LangChain 1.0 without getting burned |
| `fiftyone-embeddings-visualization` (3385-fiftyone) | 4 | 78 | 0 | — | Visualizes datasets in 2D using embeddings with UMAP or t-SNE dimensionality reduction. Use when exp |
| `storing-and-querying-vectors` (366-aws-data-analytics) | 4 | 72 | 0 | — | Store and query vector embeddings using Amazon S3 Vectors, a cost-effective long-term vector storage |
| `train-sentence-transformers` (1514-huggingface-skills) | 4 | 71 | 14 | — | Train or fine-tune sentence-transformers models across `SentenceTransformer` (bi-encoder, dense or s |
| `langchain-data-handling` (1875-langchain-py-pack) | 4 | 59 | 0 | — | Load and chunk documents for LangChain 1.0 RAG pipelines correctly \u2014\ |
| `skillhelp` (2640-skillhelp) | 4 | 52 | 1 | — | Answer help questions about the skills in this repo. Use when the user asks how to set up, install o |
| `fiftyone-find-duplicates` (3385-fiftyone) | 4 | 52 | 0 | — | Finds duplicate or near-duplicate images in FiftyOne datasets using brain similarity computation. Us |
| `together-embeddings` (3214-togetherai-skills) | 3 | 84 | 4 | vague | Dense vector embeddings, semantic search, RAG pipelines, and reranking via Together AI. Generate emb |

### 3d-webgl — 60

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `weekly-review` (212-weekly-review) | 5 | 72 | 3 | — | Use when someone wants to run a weekly review, close open loops, audit stalled projects and commitme |
| `awwwards-motion` (95-awwwards-motion) | 4 | 78 | 0 | — | Build Awwwards-quality web experiences with spring physics, GLSL shaders, R3F, post-processing, part |
| `python-complexity` (1259-python-complexity) | 4 | 56 | 5 | needs-paid-api | Measure Python complexity per function (ruff C901 cyclomatic and complexipy cognitive) and per call  |
| `fiftyone-dataset-import` (3385-fiftyone) | 4 | 50 | 0 | — | Imports datasets into FiftyOne with automatic format detection. Supports all media types (images, vi |
| `linkedin-humanizer` (3034-linkedin-skills) | 4 | 49 | 1 | needs-paid-api | Remove AI tells from LinkedIn posts/comments: 2026 vocabulary density, reveal bridges, staccato frag |
| `coreweave-fabric-diagnostics` (1842-coreweave-pack) | 4 | 49 | 1 | needs-paid-api | Diagnose the most expensive silent failure on a CoreWeave multi-node GPU job: GPUDirect RDMA falling |
| `zsh-gotchas` (2173-tools-plugin) | 4 | 44 | 0 | — | Four zsh expansions that silently rewrite a command: $VAR:word modifiers, a leading =, no word split |
| `webgpu-threejs-tsl` (2221-webgpu-threejs-tsl) | 3 | 75 | 0 | — | Comprehensive guide for developing WebGPU-enabled Three.js applications using TSL (Three.js Shading  |
| `game-studio` (2696-game-studio) | 3 | 64 | 0 | vague | Route early browser-game work. Use when the user needs stack selection and workflow planning across  |
| `aer-referee-sim` (896-aer-skills) | 3 | 45 | 0 | — | Use when a complete draft exists and needs an adversarial internal review before submission — simula |

### excel-spreadsheets — 51

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `lark-sheets` (3618-feishu2codex) | 4 | 79 | 1 | — | 飞书电子表格：创建和操作电子表格。支持创建表格、管理工作表与行列结构（增删/合并/调整尺寸/隐藏/冻结）、读写单元格（值/公式/样式/批注/单元格图片）、查找替换、多操作原子批量更新，以及图表、透视表 |
| `spreadsheet` (1428-openai-office-skills) | 4 | 76 | 0 | needs-paid-api | Use when tasks involve creating, editing, analyzing, or formatting spreadsheets (`.xlsx`, `.csv`, `. |
| `render-xlsx` (3589-xbert-working-paper) | 3 | 75 | 2 | — | Render an XBert working-paper schedule as a real .xlsx file from a structured payload. Use when an X |
| `google-sheets` (2700-google-drive) | 3 | 72 | 0 | — | Analyze and edit connected Google Sheets with range precision. Use when the user wants to create Goo |
| `akbun-davinciresolve-contrast` (1096-akbun-editvideo) | 3 | 72 | 1 | — | 단일 Log→Rec.709 LUT 경로에서 DaVinci Resolve 21.1 스크립팅 API로 새 `CONTRAST` 라벨 노드에 pivot 기준 대비를 적용하고 입력 공간의  |
| `excel-pivot-wizard` (1633-excel-analyst-pro) | 3 | 67 | 0 | vague | Create advanced Excel pivot tables with calculated fields and slicers. |
| `gws-sheets-append` (2907-google-workspace) | 3 | 65 | 0 | vague | Google Sheets: Append a row to a spreadsheet. |
| `excel-lbo-modeler` (1633-excel-analyst-pro) | 3 | 53 | 0 | vague | Build leveraged buyout (LBO) models in Excel with debt schedules and |
| `tres-import-contacts` (261-tres-finance-plugin) | 3 | 47 | 0 | — | Import contacts (address book entries) into TRES Finance from a CSV or XLSX file. Use this skill whe |
| `practice-metrics` (3579-xbert-practice-metrics) | 3 | 44 | 0 | vague, needs-paid-api | Produce the XBert monthly Practice Metrics one-pager — standard partner KPIs, service-line P&L, prio |

### pdf — 51

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `splitting-pdf` (3136-doc-util) | 5 | 100 | 4 | — | This skill should be used when users want to split PDF files by bookmarks or page ranges. Common tri |
| `extracting-pdf` (3136-doc-util) | 5 | 99 | 3 | — | This skill should be used when users want to extract text or tables from PDF files, read PDF content |
| `md-to-pdf` (2096-brewdoc) | 5 | 92 | 2 | — | Convert Markdown to PDF via reportlab or weasyprint engines. Triggers - pdf, md to pdf, markdown to  |
| `markitdown` (3204-document-evidence) | 5 | 91 | 3 | — | Convert heterogeneous documents and selected URIs to Markdown with Microsoft MarkItDown for text ana |
| `scientific-figure` (2657-figures) | 5 | 71 | 3 | — | This skill should be used when the user asks to "create a figure", "make a scientific figure", "crea |
| `scientific-visualization` (3202-quantitative-sciences) | 5 | 69 | 7 | — | Create and audit truthful, accessible, publication-ready scientific figures with Matplotlib, Seaborn |
| `kicad` (110-kicad-happy) | 5 | 64 | 36 | needs-paid-api | Analyze KiCad projects and PDF schematics: schematics, PCB layouts, Gerbers, footprints, symbols, ne |
| `Full-empirical-analysis-skill` (x1186-empirical-analysis-python) | 5 | 60 | 0 | — | Classical end-to-end empirical analysis workflow in the traditional Python econometric stack — panda |
| `mermaid-cli` (1245-mermaid-cli) | 5 | 60 | 0 | — | Generate, validate, and fix diagrams from Mermaid markup using the mermaid-cli (mmdc) tool. Use when |
| `edgeparse` (2901-edgeparse) | 4 | 80 | 0 | — | Extract structured content from any PDF for AI agents, RAG pipelines, and Copilot Skills. Use this s |

### social-content — 49

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `postiz` (x2178-postiz) | 5 | 80 | 4 | needs-paid-api | Postiz is a tool to schedule social media and chat posts to 28+ channels X, LinkedIn, LinkedIn Page, |
| `9503-video-digest` (2451-knowledge) | 5 | 75 | 4 | — | Watch a single public video from YouTube or X (Twitter): transcript, links, and repo-applicability r |
| `social` (1446-marketing-skills) | 4 | 84 | 0 | — | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twit |
| `transcriptapi` (3613-youtube-skills) | 4 | 80 | 0 | needs-paid-api | Use when YouTube is or could be relevant — even if not mentioned: pasted video/channel/playlist link |
| `youtube-data` (3613-youtube-skills) | 4 | 80 | 0 | needs-paid-api | Use when structured YouTube data is needed: pasted video/channel/playlist links, transcripts for ana |
| `youtube-full` (192-marketing-skills) | 4 | 72 | 0 | needs-paid-api | Use when the user needs YouTube transcripts, video search, channel browsing, playlist extraction, or |
| `account-video-downloader` (2990-account-video-downloader) | 4 | 70 | 7 | needs-paid-api | Multi-platform account video extractor — provide a platform name and account ID/link to automaticall |
| `social-media-manager` (192-marketing-skills) | 4 | 60 | 1 | needs-paid-api | When the user wants to develop social media strategy, plan content calendars, manage community engag |
| `adobe-create-social-variations` (103-adobe-for-creativity) | 4 | 48 | 0 | — | Resize, crop, or export any image or video into platform-ready social media assets using Adobe Creat |
| `adobe-resize-photos-and-videos` (103-adobe-for-creativity) | 4 | 48 | 0 | — | Resize photos and videos to exact pixel dimensions or aspect ratios using Adobe tools. Use this skil |

### translation-i18n — 45

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `lokalise-deploy-integration` (1880-lokalise-pack) | 5 | 87 | 0 | — | Deploy Lokalise integrations to Vercel, Netlify, and Cloud Run platforms. |
| `lokalise-local-dev-loop` (1880-lokalise-pack) | 5 | 87 | 0 | — | Configure Lokalise local development with file sync and hot reload. |
| `translate` (886-intel) | 4 | 88 | 4 | — | Translate a whole English EPUB book into a Chinese PDF that keeps the original's format: the same co |
| `using-bgs-translator` (878-bgs-modding-superpowers) | 4 | 78 | 0 | — | Use when the user wants to translate a Bethesda Game Studios plugin (.esp/.esm/.esl) with bgs-transl |
| `jlcpcb` (110-kicad-happy) | 4 | 42 | 0 | needs-paid-api | JLCPCB PCB fabrication and assembly — BOM/CPL generation, basic vs extended parts, assembly constrai |
| `nuxt-i18n` (2918-nuxt-i18n) | 3 | 72 | 0 | hub-doc | Nuxt i18n internationalization module for locale routing, lazy-loaded translations, SEO, browser det |
| `localized-pricing` (1342-dodopayments) | 3 | 69 | 0 | needs-paid-api | Guide for implementing localized pricing, adaptive currency, and purchasing power parity with Dodo P |
| `translator` (3619-zoom-plugin) | 3 | 69 | 0 | needs-paid-api, hub-doc | Reference skill for Zoom AI Services Translator. Use after routing to text translation, one-target-l |
| `transcreation` (1802-content-multiplier) | 3 | 66 | 0 | vague | Transforms marketing content across languages and markets through transcreation — adapting message,  |
| `localize-campaign` (1520-digital-marketing-pro) | 3 | 64 | 0 | vague, needs-paid-api | Localize an entire campaign — emails, ads, social posts, landing pages, video scripts — for multiple |

### real-estate — 42

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `properties` (2162-obsidian-plugin) | 4 | 77 | 0 | — | Obsidian YAML frontmatter properties and aliases: read, set, remove on notes. Use when user mentions |
| `ga4-auth-setup` (1859-ga4-pack) | 4 | 74 | 0 | — | Configure auth for the GA4 Data API — OAuth user credentials for interactive use, or a service accou |
| `ga4-common-reports` (1859-ga4-pack) | 4 | 73 | 0 | needs-paid-api | Copy-paste recipes for the 6-7 reports every site owner actually wants: DAU/MAU/WAU, retention cohor |
| `tags-and-properties` (1343-dominodatalab) | 4 | 65 | 0 | — | Manage Domino tags and properties via the Taxonomy API. Covers tags/namespaces (create, list, update |
| `appfolio-common-errors` (1826-appfolio-pack) | 4 | 61 | 0 | needs-paid-api | Diagnose and fix common AppFolio API integration errors. |
| `hubspot-product-event-sync` (1868-hubspot-pack) | 4 | 59 | 0 | needs-paid-api | Sync backend product events into HubSpot contact and company custom properties using idempotent batc |
| `fix-manifest-json` (3217-ui5-modernization) | 4 | 58 | 0 | — | Fix manifest.json issues that UI5 linter reports but cannot auto-fix. Use this skill when linter out |
| `sap-sac-custom-widget` (x4367-sap-sac-custom-widget) | 4 | 54 | 0 | — | SAP Analytics Cloud (SAC) Custom Widget development. Use when building custom visualizations, extend |
| `obsidian-bases` (1247-obsidian-bases) | 4 | 43 | 0 | needs-paid-api | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when  |
| `appfolio-core-workflow-a` (1826-appfolio-pack) | 3 | 66 | 0 | needs-paid-api | Build property management dashboard with AppFolio API data. |

### animation — 39

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `hyperframes` (2702-hyperframes) | 5 | 99 | 2 | — | Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive v |
| `gsap` (2702-hyperframes) | 5 | 92 | 1 | — | GSAP animation reference for HyperFrames. Covers gsap.to(), from(), fromTo(), easing, stagger, defau |
| `landing` (196-landing) | 5 | 90 | 3 | — | Generates a premium single-page HTML landing page with 3D CSS animations, GSAP scroll effects, and m |
| `interaction-design` (3529-ui-design) | 4 | 81 | 0 | — | Design and implement microinteractions, motion design, transitions, and user feedback patterns. Use  |
| `remotion-markup` (2712-remotion) | 4 | 78 | 0 | — | Content, animation and effects best practices |
| `9357-rotoscope` (2414-animation) | 4 | 59 | 7 | — | Copy a reference animation drawing by drawing: decode the video into its distinct drawings, trace ea |
| `top-design` (3438-ux-design) | 4 | 54 | 0 | — | Create award-winning, immersive web experiences at the level of Awwwards-featured agencies. Use when |
| `video` (2681-emulo) | 4 | 50 | 0 | — | Use when a brief has to become a film. Turns a one line ask into a Claude Design prompt written in t |
| `adobe-design-from-template` (103-adobe-for-creativity) | 4 | 46 | 0 | — | Create any visual design using Adobe Express templates — flyers, posters, social media posts (Instag |
| `remotion-interactivity` (2712-remotion) | 3 | 70 | 0 | — | Structure Remotion markup for interactivity |

### code-review-refactor — 38

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `python-refactor-workflow` (80-python-development) | 4 | 75 | 0 | — | Measure, rewrite, verify against the tests, then report the delta. TRIGGER WHEN: the user asks to re |
| `ast-grep-search` (2140-code-quality-plugin) | 4 | 47 | 0 | — | Find and replace code patterns structurally with ast-grep. Use when matching code by AST structure,  |
| `code-dead-code` (2140-code-quality-plugin) | 4 | 44 | 0 | — | Detect dead code, unused exports, unreachable branches, and orphaned files. Use when reducing mainte |
| `workflow-checkpoint-refactor` (2175-workflow-orchestration-plugin) | 3 | 65 | 0 | — | Multi-phase refactoring with checkpoint files that survive context limits. Use when refactoring span |
| `refactoring-patterns` (3429-code-craftsmanship) | 3 | 64 | 0 | — | Apply named refactoring transformations to improve code structure without changing behavior. Use whe |
| `skill-refactor` (2975-pwdev-skills) | 3 | 64 | 6 | vague | Review or refactor an existing SKILL.md and its bundled resources — a smaller always-loaded core, co |
| `review` (246-altimate-code) | 3 | 44 | 0 | vague | Review dbt project changes — dbt models (models/**/*.sql), schema.yml, dbt_project.yml, sources.yml, |
| `code-review` (1534-condux) | 3 | 43 | 0 | — | One-shot code review. Produces a diagnostic report categorized by severity (Critical / Important / M |
| `ruby-coder` (2214-majestic-rails) | 3 | 36 | 0 | — | Clear, maintainable Ruby code. |
| `receiving-code-review` (2679-superpowers) | 3 | 33 | 0 | — | Use when receiving code review feedback, before implementing suggestions, especially if feedback see |

### powerpoint-slides — 37

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `slides` (1428-openai-office-skills) | 4 | 92 | 5 | — | Create and edit presentation slide decks (`.pptx`) with PptxGenJS, bundled layout helpers, and rende |
| `edit-presentation` (2112-pptx-dev-kit) | 4 | 92 | 8 | — | Edit or update an existing PowerPoint .pptx in place — change slide copy, add or delete or reorder s |
| `build-pptx` (2112-pptx-dev-kit) | 4 | 91 | 3 | — | Render a finished deck.json into a .pptx with the pptx-dev-kit layout engine — never write a new pyt |
| `presentation-builder` (2663-presentation) | 4 | 82 | 0 | — | This skill should be used when the user asks to "create a presentation", "make slides", "build a sli |
| `powerpoint-neutralizing` (1386-office) | 4 | 79 | 1 | — | Use this skill when the user asks to "neutralize a pptx", "neutralize a presentation", "standardize  |
| `skill-doc-delivery` (2673-claude-octopus) | 4 | 71 | 0 | — | Convert markdown to DOCX, PPTX, XLSX, PDF office documents — use when you need exportable deliverabl |
| `gamma-migration-deep-dive` (1860-gamma-pack) | 4 | 67 | 0 | — | Deep dive into migrating to Gamma from other presentation platforms. |
| `gamma-core-workflow-a` (1860-gamma-pack) | 4 | 60 | 0 | needs-paid-api | Generate presentations, documents, and webpages via Gamma API. |
| `markitdown` (3136-doc-util) | 3 | 65 | 0 | — | This skill should be used when users want to convert documents to Markdown using markitdown. Common  |
| `skill-deck` (2673-claude-octopus) | 3 | 62 | 0 | — | Generate slide deck presentations from briefs — use when you need slides, pitch decks, or visual sum |

### video-generation — 28

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `klingai-team-setup` (1874-klingai-pack) | 4 | 80 | 0 | needs-paid-api | Configure Kling AI for teams with per-project API keys, usage quotas, |
| `klingai-model-catalog` (1874-klingai-pack) | 4 | 78 | 0 | needs-paid-api | Explore Kling AI models, versions, and capabilities for video and image |
| `video` (1446-marketing-skills) | 4 | 60 | 0 | needs-paid-api | When the user wants to create, generate, or produce video content using AI tools or programmatic fra |
| `scenario-war-room` (138-c-level-skills) | 4 | 49 | 1 | — | Cross-functional what-if modeling for cascading multi-variable scenarios. Unlike single-assumption s |
| `together-video` (3214-togetherai-skills) | 3 | 81 | 3 | vague | Text-to-video and image-to-video generation via Together AI, including keyframe control, model and d |
| `runway-webhooks-events` (1900-runway-pack) | 3 | 65 | 0 | vague, needs-paid-api | Convert authoritative Runway task polling into durable internal events or signed customer callbacks  |
| `runway-core-workflow-b` (1900-runway-pack) | 3 | 63 | 0 | vague, needs-paid-api | Prepare, submit, and preserve Runway image-to-video or video-to-video work with validated media prov |
| `video-gen` (2976-pwdev-social-media) | 3 | 58 | 0 | — | Produz vídeo curto — roteiro, storyboard, prompts por cena e geração via Runway quando há chave. Use |
| `wavespeed-cli` (3396-wavespeed-cli) | 3 | 52 | 0 | needs-paid-api | Generate, edit, animate, upscale, or transform AI media using the WaveSpeed CLI from Codex. Use when |
| `bootstrapped-finance` (2209-majestic-founder) | 2 | 40 | 0 | vague, needs-paid-api | Assess runway, spending choices, growth economics, and survival scenarios for a bootstrapped busines |

### video-editing — 20

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `video` (1511-homie) | 5 | 82 | 5 | needs-paid-api | Make trailers, music videos, cutscenes and page recordings for a Homie studio — a gameplay trailer c |
| `ffmpeg` (235-mas-video-lab) | 4 | 59 | 0 | — | Transcode and compress video with FFmpeg, inspect streams with ffprobe, build filtergraphs and HLS o |
| `record-screen` (2354-power-platform) | 4 | 50 | 2 | — | Record a Chrome browser tab to video via CLI. Use when the user wants to capture a screen recording  |
| `davinci-resolve` (235-mas-video-lab) | 3 | 65 | 0 | vague | Automate DaVinci Resolve media and timelines with its scripting API, build Fusion workflows, and con |
| `davinciresolve-style-essay` (1096-akbun-editvideo) | 3 | 50 | 0 | — | 기술 원리·개념·트레이드오프를 목소리로 설명하는 영상의 편집 스타일 essay. 얼굴 없이 B-roll·화면 녹화·필요한 그래픽으로 주장을 뒷받침하고, 개인 경험은 시청자 맥락과  |
| `wl-record-pixelflux` (2759-charly-selkies) | 3 | 43 | 0 | — | Desktop video recorder via selkies WebSocket capture bridge for selkies-desktop. Use when working wi |
| `akbun-davinciresolve-logconvert` (1096-akbun-editvideo) | 3 | 42 | 1 | — | DaVinci Resolve 21.1 스크립팅 API로 클립마다 Log 촬영 여부를 근거 기준으로 `Log`·`비Log`·`미확인`으로 판정하고, `Log`로 확인된 클립에만 Co |
| `wl-screenshot-pixelflux` (2759-charly-selkies) | 3 | 40 | 0 | vague | Screenshot via selkies WebSocket capture bridge for selkies-desktop. Use when working with the wl-sc |
| `whisper` (2760-charly-tools) | 2 | 45 | 0 | vague | OpenAI Whisper local speech-to-text. Use when working with the whisper candy. |
| `cuda` (2739-charly-distros) | 2 | 39 | 0 | vague | CUDA toolkit, cuDNN, ONNX Runtime, and NVIDIA GPU development libraries from negativo17 repos. Depen |

### math-science — 16

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `latex-and-venue-formatting` (3206-literature-publication) | 4 | 73 | 2 | — | Prepare, repair, compile, and validate LaTeX manuscripts against the current official requirements o |
| `comfy-math-strings` (2142-comfyui-plugin) | 4 | 47 | 0 | — | ComfyUI compute/string nodes: constants, sliders, math expressions, string concat/split/replace/rege |
| `long-form-math` (1244-long-form-math) | 3 | 55 | 0 | — | Write mathematics in a long-form, understanding-focused style with detailed proofs and rich expositi |
| `math-unicode` (3259-claude-math) | 3 | 37 | 0 | — | Use when a response needs mathematical notation (equations, filters, set-builder notation, statistic |
| `write-math` (1057-write-math) | 2 | 64 | 0 | vague | Apply mathematical exposition conventions from Tao, Knuth, and Halmos whenever writing or discussing |
| `color-math-accessibility` (2199-lvtd-skills) | 2 | 62 | 0 | vague | Calculate, review, and generate web color systems using RGB, HSL, LAB, OKLCH, contrast ratios, lumin |
| `frontend-math-foundations` (2199-lvtd-skills) | 2 | 62 | 0 | vague | Explain and apply foundational math for front-end development, including arithmetic, algebra, ratios |
| `write-latex` (1052-write-latex) | 2 | 54 | 0 | vague | Apply LaTeX typesetting conventions from AMS, IEEE, ISO 80000-2, and Knuth. Use when writing or revi |
| `solo` (296-math-proof) | 2 | 31 | 0 | vague | Work on one hard mathematics problem in this session yourself, with no sub-agents: reason in stages, |
| `check-web-design` (890-web) | 2 | 31 | 1 | vague | Check a built web page against a design reference and report how far off it is, as measured JSON plu |

### image-generation — 13

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `comfyui-node-scaffold` (2142-comfyui-plugin) | 4 | 78 | 2 | — | Scaffold a new ComfyUI custom-node repo (TypeScript + bun build, CI, release-please, vitest+pytest)  |
| `comfy-node` (2142-comfyui-plugin) | 4 | 76 | 0 | — | Orchestrate a ComfyUI node pack from idea to registry: scaffold, create + seed the repo, open the gi |
| `comfyui-layer` (2736-charly-comfyui) | 2 | 57 | 0 | vague | ComfyUI image generation service on port 8188 with CUDA GPU support. Use when working with ComfyUI,  |
| `comfyui` (2736-charly-comfyui) | 2 | 57 | 0 | vague | ComfyUI image generation server with CUDA GPU support. Runs as a supervisord service on port 8188 wi |
| `image-gen` (2976-pwdev-social-media) | 2 | 28 | 0 | — | Gera imagem por IA via Ideogram, Leonardo ou Flux usando os scripts do plugin, ou entrega o prompt o |
| `prompt-craft` (2976-pwdev-social-media) | 2 | 24 | 0 | vague | Constrói prompts para geradores de imagem e vídeo — estrutura, parâmetros, referência de estilo e ne |

### word-docs — 10

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `syllabus` (227-syllabus) | 5 | 80 | 4 | — | Generates a curated supplementary reading list from any course syllabus using Consensus academic sea |
| `doc` (1428-openai-office-skills) | 4 | 77 | 1 | — | Use when the task involves reading, creating, or editing `.docx` documents, especially when formatti |
| `lark-drive` (3618-feishu2codex) | 3 | 65 | 0 | needs-paid-api | 飞书云空间（云盘/云存储）：管理 Drive 文件和文件夹，包含上传/下载、创建文件夹、复制/移动/删除、查看元数据、评论/权限/订阅、标题、版本、飞书文档密级标签（secure labels）和本地 |
| `rebind-office` (2370-report-regeneration) | 3 | 47 | 1 | — | Pipeline stage 3 (the Office/docx surgical output engine) for report-regeneration — the Office analo |
| `fs-pack` (3568-xbert-fs-pack) | 3 | 37 | 0 | vague | Compose a year-end financial statement pack for an Australian client — SPFS structure by default, GP |
| `adobe-anydocx` (103-adobe-for-creativity) | 2 | 57 | 0 | vague | MANDATORY when a Word/DOCX task's source content is an uploaded PDF — including when the PDF's text  |
| `stp-finalisation` (3582-xbert-stp-finalisation) | 2 | 33 | 0 | vague, needs-paid-api | Annual STP Phase 2 finalisation review for Australian clients — verify every employee's YTD payroll  |
| `ias-prep` (3571-xbert-ias-prep) | 2 | 26 | 0 | vague | IAS readiness methodology for Australian clients — verify the client is ready to lodge an Instalment |
| `gst-prep-nz` (3570-xbert-gst-prep-nz) | 2 | 24 | 0 | vague | GST readiness methodology for New Zealand clients — verify the client is ready to file their GST101A |
| `super-check` (3583-xbert-super-check) | 2 | 24 | 0 | vague, needs-paid-api | Quarterly Superannuation Guarantee check for Australian clients — verify SG calculated, posted, paid |

### captions-subtitles — 8

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `subtitles` (3613-youtube-skills) | 3 | 64 | 0 | needs-paid-api | Use when subtitles or the spoken text of a YouTube video is needed: pasted video links or IDs, reque |
| `akbun-describe-twitter-transcript` (1097-akbun-learning) | 3 | 49 | 3 | vague | x.com(트위터) post 링크와 함께 영상 자막 변환을 요청할 때만 사용한다. |
| `davinciresolve-subtitle-devtalk` (1096-akbun-editvideo) | 3 | 44 | 0 | — | 말하는 개발자 브이로그의 오버레이 자막을 만드는 devtalk 스타일. 편집 스타일(essay·project·reflection)의 글자 표에 따라 대사 자막(Resolve Cre |
| `davinciresolve-subtitle-travelnote` (1096-akbun-editvideo) | 3 | 42 | 1 | — | DaVinci Resolve에서 Gmarket Sans로 차분한 여행 브이로그용 한글 자막과 챕터 제목을 만드는 travelnote 스타일. 장면 설명 대신 장소·시간·분위기를 짧 |
| `remotion-captions` (2712-remotion) | 2 | 58 | 0 | vague | Transcribing, displaying and animating captions |
| `manage-disposal-and-regulatory-compliance` (2403-waste-recycling-operations) | 2 | 56 | 0 | vague, needs-paid-api | Choose the disposal path (direct-haul to a Subtitle D landfill vs consolidate through a transfer sta |
| `akbun-draw-webtoon-d` (1094-akbun-draw) | 2 | 28 | 0 | vague | 사용자의 실제 이야기(경험담, 회상, 썰)를 인스타그램 세로형(3:4) 흑백 다큐멘터리 웹툰으로 만든다. 스타일은 고정이다 — 거친 검정 잉크 낙서선, 흰 배경, 플랫 회색 음영, |
| `akbun-draw-sketchbook-card` (1094-akbun-draw) | 2 | 21 | 0 | vague | 개념·주제를 손글씨 제목·체크리스트와 액자 속 연필 일러스트가 있는 스파이럴 스케치북 카드 스타일로 그리는 이미지 생성 프롬프트를 만든다. |

### photography-lighting — 8

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `iso42001-specialist` (214-ra-qm-skills) | 5 | 81 | 3 | — | ISO/IEC 42001:2023 AI Management System (AIMS) specialist for compliance teams running internal audi |
| `quality-manager-qms-iso13485` (214-ra-qm-skills) | 4 | 58 | 1 | — | ISO 13485 Quality Management System implementation and maintenance for medical device organizations. |
| `aims-audit` (148-compliance-os) | 4 | 56 | 0 | — | /cs:aims-audit <scope> — ISO/IEC 42001 AIMS internal-audit 6-question forcing interrogation. Use bef |
| `fda-qsr-audit-prep` (148-compliance-os) | 4 | 48 | 0 | — | /cs:fda-qsr-audit-prep <scope> — FDA 21 CFR 820 (QSR / QMSR) audit 6-question forcing interrogation. |
| `governance-status` (1473-axonflow) | 2 | 56 | 0 | vague, stub | Check active governance policies and recent activity summary |
| `framework-selection-and-control-mapping` (2267-cybersecurity-grc) | 2 | 40 | 0 | vague | Choose the right security-compliance framework for the org's size/risk/customer demand, scope the au |

### prompt-engineering — 8

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `cortex-prompt` (1567-tonone) | 4 | 62 | 0 | — | Build a production-ready prompt package — system prompt, few-shot examples, output format, edge case |
| `prompt-optimization` (1547-plugin-creator) | 4 | 57 | 0 | outdated | Optimize CLAUDE.md files and Skills for Claude Code CLI. Use when reviewing, creating, or improving  |
| `langchain-prompt-engineering` (1875-langchain-py-pack) | 4 | 55 | 0 | needs-paid-api | Manage LangChain 1.0 prompts like code \u2014 LangSmith prompt hub versioning,\n\ |
| `groq-core-workflow-a` (1864-groq-pack) | 3 | 40 | 0 | vague, needs-paid-api, hub-doc | Execute Groq's primary workflow: chat completions with tool use and JSON mode. |
| `voice-profile` (3597-humanize) | 2 | 33 | 1 | vague | Use when the user wants AI drafts to sound like *them* (or their team) rather than like a generic pr |
| `prompt-pattern-selection` (2361-prompt-engineering) | 2 | 32 | 0 | vague | Choose the prompting pattern — zero-shot, few-shot, chain-of-thought, decomposition/chaining, role f |
| `notebook-llm-on-supercomputers` (2747-charly-jupyter) | 2 | 30 | 0 | — | LLMs on Supercomputers course notebook collection (TU Wien AI Factory Austria). 15 Jupyter notebooks |
| `zero-shot` (1990-epistemic-cooperative) | 2 | 27 | 0 | vague | Use when the user asks to \"check zero-shot\", \"audit few-shot anchoring\", \"find example anchorin |

### ai-safety-security — 6

| المهارة (الإضافة) | جودة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|
| `adversarial-review` (3596-forge-teams) | 4 | 54 | 0 | — | Agent Teams 对抗式审查 + 红队攻击。多 agent 并行审查（规格/代码/安全/红队），交叉检验，综合裁决。 Use when: (1) 重大功能发布前审查, (2) 涉及安全敏感代码, |
| `gws-modelarmor-create-template` (2907-google-workspace) | 3 | 49 | 0 | vague | Google Model Armor: Create a new Model Armor template. |
| `run-adversarial-attacks-and-jailbreaks` (2232-ai-red-teaming) | 2 | 56 | 0 | vague | Execute the prioritized attacks against an AI system within the rules of engagement — direct and ind |
| `harden-and-remediate-ai-system` (2232-ai-red-teaming) | 2 | 52 | 0 | vague | Triage red-team findings by likelihood×impact and drive defense-in-depth remediation — layered input |
