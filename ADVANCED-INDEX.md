# الفهرس المتقدم لأطلس KOSIF (دمج الفهارس الثلاثة)

طبقة واحدة متسقة فوق: (1) الفهرس الآلي بكثافة الوسوم، (2) تدريج الأدلة لكل مهارة من نصها الكامل، (3) خريطة المهارات الخارقة الـ108 إلى مصادرها. كل رقم هنا مشتق من عدّ أدلة ملموسة في النص (كتل كود، أوامر، مسارات، قيم بوحدات، جداول، سكربتات في المجلد، مراجع، أقسام)، لا من تقدير حر.

## المنهج

- **الجودة (1–5)** = 0.35 خصوصية + 0.30 إجرائية + 0.25 اكتمال + 0.10 أمان. الخصوصية من كثافة الأدلة الملموسة مع خصم للكلمات التسويقية؛ الإجرائية من السكربتات والأوامر وأقسام الخطوات والأخطاء؛ الاكتمال من تغطية دورة الحياة (نظرة، متطلبات، خطوات، مخرجات، أخطاء، أمثلة، فحص) والعمق والمراجع؛ الأمان ينخفض مع أوامر مدمّرة بلا حراسة ويهبط إلى 1 عند تسرّب مفتاح.
- **الصلة بالوسم** = كثافة ذكر الوسم لكل ألف كلمة (تتشبّع عند 30).
- **البنية** = سكربتات ×0.25 + مراجع ×0.05 (حتى 8) + تقييمات ×0.2 + كتل كود ×0.03 (حتى 10).
- **الدرجة المركبة (0–100)** = 45% جودة + 35% صلة بالوسم + 20% بنية. تُحسب لكل (مهارة، وسم) فتختلف المهارة نفسها بين وسومها.
- الست مهارات المقروءة يدوياً (`tools/deep-read/cards.sample-human.jsonl`) تتقدّم درجاتها على المُدرِّج.
- إزالة التكرار في القوائم: مهارتان كحد أقصى لكل إضافة، ولا تكرار للاسم نفسه.

## أرقام عامة

- مهارات مدرَّجة: **15,122** · تحمل سكربتات فعلية في مجلدها: 1,482 (10%).
- توزيع الجودة: 5/5: 533 · 4/5: 3,008 · 3/5: 5,569 · 2/5: 5,999 · 1/5: 13.
- أعلام الخطر: vague 8,452، needs-paid-api 3,170، stub 904، hub-doc 344، destructive-actions 59، marketing-fluff 26، outdated 9، security-risk 1.

## الوسوم: الحجم والجودة وأفضل 10 (بالدرجة المركبة بعد إزالة التكرار)

| الوسم | المهارات | متوسط الجودة | 5/5 | بسكربتات | أفضل 10 (الاسم · الجودة · المركبة) |
|---|---|---|---|---|---|
| agents-orchestration | 6,082 | 3.07 | 304 | 838 | `agenthub` 5/100 · `teams-setup` 5/100 · `agent-dev` 5/100 · `jfrog-mcp-management` 5/99 · `agent-capability-analyzer` 5/96 · `herdr` 4/92 · `orchestrating-multi-agent-systems` 4/92 · `workflow-builder` 4/92 · `pm-skills` 4/92 · `orchestrate-frontend` 5/92 |
| backend-api | 5,506 | 3.25 | 306 | 468 | `creating-kubernetes-deployments` 5/100 · `backend-dev` 5/100 · `code-to-prd` 5/95 · `jfrog` 5/93 · `aiq-research` 5/92 · `tracking-crypto-prices` 5/90 · `sentry-enterprise-rbac` 5/90 · `vercel-advanced-troubleshooting` 5/90 · `hf-cloud-sagemaker-production-defaults` 5/89 · `routing-dex-trades` 5/88 |
| testing-qa | 5,018 | 3.09 | 273 | 549 | `audit-tests` 5/100 · `modernize-test-starter` 5/100 · `test-suite-generator` 5/100 · `qa-walkthrough-pr` 5/99 · `statistical-analyst` 5/98 · `statistical-analysis` 5/97 · `286-browser-automation` 4/92 · `313-browser-automation` 4/92 · `340-browser-automation` 4/92 · `playwright-kit-ops` 4/92 |
| legal-contracts | 3,689 | 2.99 | 135 | 387 | `gdpr-dsgvo-expert` 5/100 · `deal-desk` 5/100 · `compliance-os` 5/95 · `commercial-policy` 5/91 · `tracking-token-launches` 5/86 · `general-counsel-advisor` 4/82 · `azure-compliance` 4/80 · `validating-api-contracts` 4/78 · `use-smart-contract-platform` 4/78 · `eu-ai-act-specialist` 5/78 |
| claude-code-meta | 3,472 | 2.92 | 149 | 477 | `output-style-creator` 5/100 · `skill-creator` 5/97 · `plugin-factory` 4/92 · `plugin-update` 4/92 · `plugin-settings` 4/92 · `9468-plugin-eval` 4/88 · `health-plugins` 4/88 · `obsidian-deploy-integration` 5/87 · `working-with-claude-code` 4/86 · `skill-interop` 5/85 |
| git-github | 3,454 | 3.20 | 235 | 459 | `uxd-prototype-publish` 5/100 · `exec` 5/96 · `9613-pull-request` 5/95 · `render-deploy` 5/93 · `scaffold-go-cli` 5/93 · `new` 5/93 · `9569-clean` 4/92 · `9612-commit` 4/92 · `scaffold-go-library` 5/91 · `agenthub` 5/91 |
| research | 3,304 | 2.92 | 119 | 377 | `aeo` 5/100 · `citation-management` 5/100 · `literature-review` 5/100 · `research-summarizer` 5/95 · `product-research` 5/94 · `compliance-os` 5/92 · `mechanical-engineering-research` 4/92 · `huggingface-paper-publisher` 5/89 · `peer-review` 5/88 · `research` 4/88 |
| database | 2,926 | 3.16 | 160 | 353 | `automating-database-backups` 5/100 · `generating-stored-procedures` 5/100 · `prisma-upgrade-v7` 5/92 · `managing-database-recovery` 4/92 · `managing-deployment-rollbacks` 4/92 · `supabase-deploy-integration` 5/90 · `database-documentation-gen` 4/89 · `supabase-local-dev-loop` 5/89 · `detecting-performance-bottlenecks` 4/88 · `databricks-uc-migration-pilot` 4/88 |
| docs-writing | 2,865 | 3.19 | 163 | 368 | `markdown-html-orchestrator` 5/100 · `database-documentation-gen` 4/89 · `new` 5/88 · `document-sync` 5/88 · `changelog-orchestrator` 3/84 · `md-document` 4/84 · `extracting-chm` 4/83 · `firecrawl` 4/83 · `yapi-skill` 5/79 · `working-with-claude-code` 4/78 |
| devops-ci | 2,817 | 3.26 | 191 | 312 | `creating-kubernetes-deployments` 5/100 · `nextflow-development` 5/100 · `aiq-deploy` 5/98 · `revenue-operations` 5/97 · `databricks-bundle-medic` 5/95 · `render-deploy` 5/93 · `managing-deployment-rollbacks` 4/92 · `deploying-monitoring-stacks` 4/92 · `use-sealos` 4/92 · `finetuning` 4/92 |
| security | 2,703 | 3.22 | 141 | 200 | `auditing-wallet-security` 5/98 · `validating-authentication-implementations` 4/89 · `information-security-manager-iso27001` 5/88 · `sap-dependency-security` 5/87 · `security-audit` 5/87 · `ciso-advisor` 4/86 · `helm-chart-builder` 5/85 · `figma-ci-integration` 5/84 · `klaviyo-ci-integration` 5/84 · `octopus-security-audit` 5/84 |
| data-analysis | 2,164 | 3.26 | 128 | 263 | `generating-stored-procedures` 5/98 · `investigate-metric` 4/91 · `azuresql-db-container` 4/86 · `exploring-llm-traces` 5/86 · `sap-sqlscript` 4/86 · `platform-soql-query` 4/86 · `optimizing-sql-queries` 4/84 · `chdb-datastore` 4/84 · `chdb-sql` 4/83 · `dv-query` 4/82 |
| decision-reasoning | 1,876 | 2.88 | 77 | 213 | `meetings` 4/81 · `skill-debate` 4/74 · `chief-data-officer-advisor` 5/74 · `chief-ai-officer-advisor` 5/74 · `uxd-prototype-create` 5/74 · `plan-review` 4/73 · `chief-customer-officer-advisor` 5/70 · `adr-authoring` 3/70 · `databricks-cluster-forensics` 5/68 · `compliance-os` 5/68 |
| web-frontend | 1,770 | 3.27 | 104 | 221 | `a11y-audit` 5/100 · `modernize-test-starter` 5/100 · `markdown-html-orchestrator` 5/100 · `uxd-prototype-export` 5/98 · `tsdown` 5/93 · `md-document` 4/92 · `generate-html` 5/91 · `pf-css-var-scan` 4/89 · `landing` 5/89 · `power-apps-code-apps` 5/88 |
| productivity-email | 1,719 | 3.08 | 76 | 126 | `meetings` 4/92 · `inbox-setup` 4/90 · `inbox-triage` 4/90 · `google-workspace-cli` 5/88 · `granola-ci-integration` 5/85 · `react-email` 4/84 · `resend` 4/82 · `zoom-mcp` 4/80 · `klingai-team-setup` 4/80 · `notion-meeting-intelligence` 4/80 |
| copywriting-marketing | 1,699 | 3.04 | 86 | 237 | `design-system` 5/93 · `lf-output-formatter` 4/92 · `campaign-analytics` 5/89 · `market-research` 5/85 · `content-engine` 5/81 · `brand-guidance-authoring` 4/81 · `paid-ads` 4/80 · `kubectl-debugging` 4/78 · `clone` 4/78 · `drafts` 4/78 |
| debugging | 1,567 | 3.24 | 123 | 140 | `azure-diagnostics` 4/92 · `crowdsec` 5/91 · `hyperpod-nccl` 5/90 · `sentry-debug-bundle` 5/79 · `twinmind-debug-bundle` 5/78 · `kubectl-debugging` 4/78 · `typescript-debugging` 4/78 · `debugging-strategies` 4/78 · `obsidian-observability` 4/78 · `zoom-meeting-sdk-windows` 5/76 |
| design-ui | 1,281 | 3.10 | 54 | 128 | `fix-cyclic-deps` 5/100 · `modernize-test-starter` 5/93 · `generate-html` 5/89 · `add-app-to-server` 5/86 · `nuxt-ui` 4/86 · `superloopy-frontend` 3/84 · `ui-design-system` 5/80 · `ui-toolkit/web` 4/79 · `domino-ui-design` 4/79 · `reka-ui` 4/78 |
| architecture | 1,206 | 2.93 | 41 | 120 | `grill-with-docs` 4/85 · `blueprint-adr-validate` 4/84 · `sentry-architecture-variants` 5/81 · `architecture-decision-records` 4/77 · `zoom-meeting-sdk-windows` 5/74 · `architect-python` 3/72 · `ddd-best-practices` 3/72 · `rivet-sdk` 3/70 · `sales-engineer` 5/70 · `adr-authoring` 3/70 |
| cloud-edge | 1,115 | 3.28 | 66 | 117 | `benchmark-sandbox` 5/100 · `ensemble-rule-review` 4/92 · `launch-with-aws` 4/92 · `aws-lambda-durable-functions` 5/91 · `turnstile-spin` 4/90 · `vercel-advanced-troubleshooting` 5/90 · `sentry-architecture-variants` 5/89 · `building-mcp-server-on-cloudflare` 5/89 · `vercel-migration-deep-dive` 5/88 · `dynamo-router-starter` 5/87 |
| business-strategy | 998 | 3.05 | 55 | 120 | `product-strategist` 4/82 · `document-linking` 4/78 · `product-manager-toolkit` 5/77 · `op` 4/76 · `adversarial-requirements` 4/76 · `trello-pipeline` 2/76 · `blueprint-story-reconcile` 4/74 · `prd-create` 4/74 · `prd-export` 4/74 · `code-to-prd` 5/72 |
| 3d-webgl | 968 | 3.12 | 66 | 183 | `awwwards-motion` 4/78 · `webgpu-threejs-tsl` 3/75 · `weekly-review` 5/72 · `saas-metrics-coach` 5/66 · `customer-success-manager` 5/65 · `threejs-data-visualization` 2/64 · `game-studio` 3/64 · `linkedin-profile` 4/62 · `pf-figma-diff` 4/58 · `lf-output-formatter` 4/58 |
| accounting-audit | 955 | 2.96 | 27 | 129 | `kubernetes-operator` 4/92 · `research-finance` 5/81 · `render-xlsx` 3/75 · `chase-overdue-invoices` 4/74 · `seo-content` 5/72 · `month-end-prep` 3/72 · `9591-running-retro` 4/72 · `9409-reduce` 4/71 · `linkedin-content` 4/71 · `kanban-workflow` 3/70 |
| financial-modeling | 897 | 3.09 | 39 | 105 | `revenue-operations` 5/100 · `slo-architect` 5/93 · `financial-analyst` 4/92 · `commercial-forecaster` 4/91 · `research-finance` 5/84 · `deep-work` 5/81 · `validating-performance-budgets` 3/81 · `klingai-cost-controls` 4/78 · `slo-implementation` 4/77 · `forecast` 4/74 |
| dataviz-dashboards | 880 | 3.28 | 54 | 78 | `helm-chart-builder` 5/97 · `dt-obs-analytics` 4/87 · `helm-chart-development` 4/78 · `helm-values-management` 4/78 · `build-dashboard` 4/78 · `dashboard-expert` 4/78 · `data-visualization` 4/77 · `creating-apm-dashboards` 3/76 · `ar-status` 4/75 · `tracking-crypto-derivatives` 5/74 |
| ecommerce | 849 | 3.21 | 47 | 125 | `shopify-onboarding-dev` 4/92 · `shopify-use-shopify-cli` 4/92 · `expo-deployment` 4/82 · `shopify-install-auth` 4/79 · `shopify-sdk-patterns` 4/78 · `podium-review-request-automation` 5/73 · `amazon-location-service` 4/73 · `pnpm` 3/72 · `fetch-app-reviews` 3/71 · `app-store-optimization` 5/71 |
| llm-evals | 800 | 3.05 | 51 | 149 | `uxd-prototype-evaluate` 5/100 · `uxd-prototype-export` 5/98 · `tracking-regression-tests` 4/92 · `9466-design` 4/91 · `catlass-dsl-optimize` 5/88 · `grade-iterate` 4/87 · `social-media-analyzer` 5/84 · `catlass-dsl-develop` 4/83 · `eval` 4/83 · `9469-validate` 4/82 |
| mobile | 725 | 2.89 | 31 | 48 | `dt-setup-ios` 4/85 · `expo-deployment` 4/82 · `amplify-workflow` 4/80 · `mobile-checkout` 4/78 · `dt-setup-flutter` 4/78 · `apollo-kotlin` 3/78 · `apollo-ios` 3/77 · `app-store-optimization` 5/76 · `build-zoom-meeting-sdk-app` 3/76 · `supabase-architecture-variants` 3/74 |
| landing-marketing | 656 | 3.03 | 37 | 90 | `campaign-analytics` 5/99 · `vpe-advisor` 5/90 · `paid-ads` 4/84 · `linkedin-profile` 4/82 · `landing` 5/80 · `commercial-forecaster` 4/75 · `ads` 4/74 · `conversion-design` 4/72 · `markitdown` 5/71 · `product-analytics` 4/71 |
| hr-recruiting | 649 | 3.18 | 46 | 145 | `product-manager-toolkit` 5/83 · `vpe-advisor` 5/82 · `interview` 4/82 · `resume` 4/78 · `migrating-to-workflow-sdk` 3/78 · `shipwright-project` 4/74 · `ar-resume` 4/73 · `cv-craft` 3/71 · `find-recruiting-firm` 4/70 · `chro-advisor` 4/69 |
| scraping-automation | 628 | 3.17 | 31 | 64 | `apify-upgrade-migration` 5/87 · `firecrawl` 4/83 · `tavily-best-practices` 4/80 · `web-crawling` 4/78 · `just-scrape` 4/78 · `crawlberg` 4/77 · `playwright` 5/74 · `agent-browser` 4/73 · `scraper-builder` 5/70 · `brightdata-cli` 4/70 |
| healthcare | 603 | 3.19 | 45 | 81 | `clinical-research` 5/91 · `fda-consultant-specialist` 5/88 · `mdr-745-specialist` 5/84 · `aeo` 5/68 · `openevidence-ci-integration` 3/66 · `openevidence-core-workflow-a` 3/66 · `checking-hipaa-compliance` 3/66 · `audit-tests` 5/65 · `abridge-core-workflow-b` 3/65 · `probe-sdk` 2/64 |
| rag-knowledge | 463 | 3.06 | 26 | 61 | `together-embeddings` 3/84 · `podium-rag-context-bridge` 5/84 · `langchain-embeddings-search` 4/80 · `fiftyone-embeddings-visualization` 4/78 · `genkit-production-expert` 3/72 · `storing-and-querying-vectors` 4/72 · `train-sentence-transformers` 4/71 · `podium-call-transcript-pipeline` 5/69 · `rag-kag-decision` 3/68 · `vertex-agent-builder` 3/67 |
| code-review-refactor | 452 | 2.92 | 17 | 38 | `python-refactor-method` 5/76 · `python-refactor-workflow` 4/75 · `md-review` 4/70 · `refactor-plugin` 3/66 · `new` 5/66 · `skill-creator` 5/65 · `workflow-checkpoint-refactor` 3/65 · `refactoring-patterns` 3/64 · `skill-refactor` 3/64 · `rails-refactorer` 4/59 |
| real-estate | 449 | 2.95 | 23 | 30 | `properties` 4/77 · `ga4-auth-setup` 4/74 · `ga4-common-reports` 4/73 · `exploring-llm-traces` 5/67 · `seo-image-gen` 5/67 · `appfolio-core-workflow-a` 3/66 · `mixpanelyst` 5/65 · `tags-and-properties` 4/65 · `property-based-testing` 4/65 · `enterprise-spring-xml` 3/65 |
| education-learning | 405 | 3.01 | 33 | 65 | `bible-study` 5/92 · `curriculum` 5/91 · `9463-teach` 4/85 · `clinical-research` 5/77 · `scvi-tools` 5/72 · `optimizing-deep-learning-models` 3/72 · `9499-course-digest` 5/72 · `deep-learning-book` 4/72 · `notebooklm` 5/71 · `syllabus` 5/70 |
| storytelling | 356 | 2.91 | 11 | 47 | `submission` 4/79 · `story-init` 4/78 · `agile-product-owner` 4/72 · `sap-sac-scripting` 4/71 · `bmad-sprint-run` 3/69 · `storybook` 3/68 · `scrum-master` 5/66 · `rfp-responder` 5/65 · `blueprint-story-audit` 3/61 · `blueprint-story-reconcile` 4/61 |
| audio-music | 354 | 3.42 | 22 | 17 | `game-audio-procedural` 5/100 · `music` 4/85 · `together-audio` 3/84 · `sound` 4/81 · `transcribe` 3/81 · `deepgram-hello-world` 4/77 · `hyperframes` 5/74 · `demo-video` 4/74 · `elevenlabs-hello-world` 4/74 · `game-trailer` 4/72 |
| translation-i18n | 327 | 3.30 | 33 | 37 | `translate` 4/88 · `lokalise-deploy-integration` 5/87 · `lokalise-local-dev-loop` 5/87 · `using-bgs-translator` 4/78 · `bible-study` 5/73 · `nuxt-i18n` 3/72 · `together-audio` 3/71 · `splitting-pdf` 5/70 · `localized-pricing` 3/69 · `translator` 3/69 |
| pdf | 250 | 3.47 | 31 | 69 | `splitting-pdf` 5/100 · `extracting-pdf` 5/99 · `md-to-pdf` 5/92 · `markitdown` 5/91 · `html-to-pdf` 4/81 · `edgeparse` 4/80 · `pdf-ocr-adding` 4/77 · `pdf-xfa-printing` 4/77 · `documenso-hello-world` 4/75 · `opencite` 4/74 |
| math-science | 246 | 3.38 | 19 | 28 | `latex-and-venue-formatting` 4/73 · `chief-customer-officer-advisor` 5/68 · `math-olympiad` 5/65 · `write-math` 2/64 · `translate` 4/64 · `mixpanelyst` 5/63 · `color-math-accessibility` 2/62 · `css-math-units` 2/62 · `ops-evaluation` 4/62 · `mechanical-engineering-research` 4/60 |
| animation | 203 | 2.89 | 4 | 11 | `hyperframes` 5/99 · `gsap` 5/92 · `landing` 5/90 · `interaction-design` 4/81 · `remotion-markup` 4/78 · `together-video` 3/72 · `remotion-interactivity` 3/70 · `remotion` 3/65 · `tailwind-design-system` 3/64 · `fix-web-rendering-performance` 3/61 |
| social-content | 198 | 3.06 | 9 | 27 | `social` 4/84 · `postiz` 5/80 · `transcriptapi` 4/80 · `youtube-data` 4/80 · `social-media-analyzer` 5/77 · `9503-video-digest` 5/75 · `youtube-full` 4/72 · `account-video-downloader` 4/70 · `fetch-tiktok-mentions` 3/69 · `brand-listening` 4/69 |
| excel-spreadsheets | 176 | 2.91 | 9 | 22 | `lark-sheets` 4/79 · `spreadsheet` 4/76 · `render-xlsx` 3/75 · `google-sheets` 3/72 · `akbun-davinciresolve-contrast` 3/72 · `gdoc-to-markdown` 5/67 · `excel-pivot-wizard` 3/67 · `google-workspace-cli` 5/66 · `gws-sheets-append` 3/65 · `markitdown` 5/65 |
| game-dev | 171 | 2.60 | 3 | 17 | `9476-dlss5` 4/86 · `game-trailer` 4/83 · `video` 5/82 · `game-audio-procedural` 5/81 · `art` 4/79 · `sprite-pipeline` 4/74 · `using-bgs-archive` 4/67 · `using-bgs-papyrus` 3/65 · `bevy-game-engine` 4/65 · `game-studio` 3/64 |
| powerpoint-slides | 155 | 3.05 | 7 | 32 | `slides` 4/92 · `edit-presentation` 4/92 · `build-pptx` 4/91 · `presentation-builder` 4/82 · `powerpoint-neutralizing` 4/79 · `md-slides` 4/72 · `skill-doc-delivery` 4/71 · `gamma-migration-deep-dive` 4/67 · `markitdown` 5/65 · `skill-deck` 3/62 |
| word-docs | 104 | 3.05 | 5 | 30 | `syllabus` 5/80 · `doc` 4/77 · `grants` 5/72 · `lf-output-formatter` 4/70 · `render-pdf` 3/69 · `litreview` 5/68 · `infer-office` 4/68 · `markitdown` 5/66 · `skill-doc-delivery` 4/66 · `lark-drive` 3/65 |
| video-editing | 94 | 3.31 | 14 | 16 | `video` 5/76 · `demo-video` 4/73 · `9499-course-digest` 5/70 · `davinci-resolve` 3/65 · `hyperframes` 5/65 · `9503-video-digest` 5/65 · `transcribe` 3/61 · `slides` 4/60 · `ffmpeg` 4/59 · `speak-local-dev-loop` 4/56 |
| video-generation | 91 | 3.29 | 2 | 8 | `research-finance` 5/84 · `together-video` 3/81 · `klingai-team-setup` 4/80 · `klingai-model-catalog` 4/78 · `cfo-advisor` 4/73 · `runway-install-auth` 3/65 · `runway-webhooks-events` 3/65 · `airunway-aks-setup` 3/62 · `video` 4/60 · `video-gen` 3/58 |
| photography-lighting | 88 | 3.45 | 15 | 26 | `compliance-os` 5/90 · `fda-consultant-specialist` 5/82 · `iso42001-specialist` 5/81 · `eu-ai-act-specialist` 5/67 · `audit-search` 2/56 · `governance-status` 2/56 · `aims-audit` 4/56 · `playwright-planning` 4/52 · `ciso-advisor` 4/52 · `general-counsel-advisor` 4/51 |
| prompt-engineering | 82 | 3.13 | 3 | 10 | `prompt-engineering-patterns` 3/66 · `cortex-prompt` 4/62 · `prompt-optimization` 4/57 · `agent-development` 4/57 · `prompt-engineer-toolkit` 4/56 · `prompts` 2/56 · `langchain-prompt-engineering` 4/55 · `clade-policy-guardrails` 3/47 · `langchain-development` 4/45 · `skill-meta-prompt` 4/43 |
| captions-subtitles | 54 | 3.43 | 11 | 14 | `app-store-optimization` 5/67 · `hyperframes` 5/65 · `subtitles` 3/64 · `remotion-captions` 2/58 · `manage-disposal-and-regulatory-compliance` 2/56 · `quickdesign` 4/51 · `hyperframes-cli` 4/50 · `akbun-describe-twitter-transcript` 3/49 · `record-screen` 4/48 · `aso` 4/47 |
| ai-safety-security | 54 | 3.28 | 5 | 5 | `chief-ai-officer-advisor` 5/66 · `run-adversarial-attacks-and-jailbreaks` 2/56 · `adversarial-review` 4/54 · `red-team-agent` 2/54 · `octopus-security-audit` 5/52 · `harden-and-remediate-ai-system` 2/52 · `langchain-security-basics` 4/51 · `gws-modelarmor-create-template` 3/49 · `op` 4/46 · `forge-teams` 4/43 |
| image-generation | 50 | 3.06 | 1 | 7 | `together-images` 3/84 · `comfyui-node-scaffold` 4/78 · `comfy-node` 4/76 · `comfyui-workflow-design` 3/71 · `comfyui-api` 3/67 · `comfyui-layer` 2/57 · `comfyui` 2/57 · `flux` 2/56 · `building-gitops-workflows` 3/56 · `image` 4/55 |

## أفضل 10 بالتفصيل في وسوم الوسائط والبرومبت والإكسل

### video-editing — 94 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `video` (1511-homie) | 5 | 10/k | 76 | 5 | needs-paid-api | Make trailers, music videos, cutscenes and page recordings for a Homie studio — a gameplay trailer captured fr |
| 2 | `demo-video` (1644-framecraft) | 4 | 25/k | 73 | 0 | — | Generate polished demo videos from a single prompt. Use when the user |
| 3 | `9499-course-digest` (2451-knowledge) | 5 | 6/k | 70 | 2 | — | Extract and synthesize online video courses into repo-applicable recommendations. Use when: 'course digest', ' |
| 4 | `davinci-resolve` (235-mas-video-lab) | 3 | 30/k | 65 | 0 | vague | Automate DaVinci Resolve media and timelines with its scripting API, build Fusion workflows, and configure ren |
| 5 | `hyperframes` (2702-hyperframes) | 5 | 3/k | 65 | 2 | — | Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, an |
| 6 | `9503-video-digest` (2451-knowledge) | 5 | 3/k | 65 | 4 | — | Watch a single public video from YouTube or X (Twitter): transcript, links, and repo-applicability recommendat |
| 7 | `transcribe` (886-intel) | 3 | 12/k | 61 | 3 | — | Turn audio into plain-text words, transcribed locally with whisper — a finite file or URL, or a live stream ca |
| 8 | `slides` (1428-openai-office-skills) | 4 | 5/k | 60 | 5 | — | Create and edit presentation slide decks (`.pptx`) with PptxGenJS, bundled layout helpers, and render/validati |
| 9 | `ffmpeg` (235-mas-video-lab) | 4 | 16/k | 59 | 0 | — | Transcode and compress video with FFmpeg, inspect streams with ffprobe, build filtergraphs and HLS outputs, an |
| 10 | `speak-local-dev-loop` (1906-speak-pack) | 4 | 13/k | 56 | 0 | needs-paid-api | Configure Speak local development with mocked tutors and audio testing. |

### animation — 203 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `hyperframes` (2702-hyperframes) | 5 | 25/k | 99 | 2 | — | Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, an |
| 2 | `gsap` (2702-hyperframes) | 5 | 60/k | 92 | 1 | — | GSAP animation reference for HyperFrames. Covers gsap.to(), from(), fromTo(), easing, stagger, defaults, timel |
| 3 | `landing` (196-landing) | 5 | 19/k | 90 | 3 | — | Generates a premium single-page HTML landing page with 3D CSS animations, GSAP scroll effects, and mouse-paral |
| 4 | `interaction-design` (3529-ui-design) | 4 | 30/k | 81 | 0 | — | Design and implement microinteractions, motion design, transitions, and user feedback patterns. Use when addin |
| 5 | `remotion-markup` (2712-remotion) | 4 | 48/k | 78 | 0 | — | Content, animation and effects best practices |
| 6 | `together-video` (3214-togetherai-skills) | 3 | 19/k | 72 | 3 | vague | Text-to-video and image-to-video generation via Together AI, including keyframe control, model and dimension s |
| 7 | `remotion-interactivity` (2712-remotion) | 3 | 24/k | 70 | 0 | — | Structure Remotion markup for interactivity |
| 8 | `remotion` (235-mas-video-lab) | 3 | 38/k | 65 | 0 | — | Create React video compositions with Remotion, parameterize timelines with props, and configure CLI or server- |
| 9 | `tailwind-design-system` (3096-frontend-mobile-development) | 3 | 23/k | 64 | 0 | — | Build scalable design systems with Tailwind CSS v4, design tokens, component libraries, and responsive pattern |
| 10 | `fix-web-rendering-performance` (1530-webcraft) | 3 | 23/k | 61 | 0 | — | Audit and fix web rendering performance, including animations, scrolling, layout thrashing, and expensive visu |

### captions-subtitles — 54 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `app-store-optimization` (192-marketing-skills) | 5 | 4/k | 67 | 8 | needs-paid-api | App Store Optimization (ASO) toolkit for researching keywords, analyzing competitor rankings, generating metad |
| 2 | `hyperframes` (2702-hyperframes) | 5 | 3/k | 65 | 2 | — | Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, an |
| 3 | `subtitles` (3613-youtube-skills) | 3 | 22/k | 64 | 0 | needs-paid-api | Use when subtitles or the spoken text of a YouTube video is needed: pasted video links or IDs, requests to tra |
| 4 | `remotion-captions` (2712-remotion) | 2 | 38/k | 58 | 0 | vague | Transcribing, displaying and animating captions |
| 5 | `manage-disposal-and-regulatory-compliance` (2403-waste-recycling-operations) | 2 | 26/k | 56 | 0 | vague, needs-paid-api | Choose the disposal path (direct-haul to a Subtitle D landfill vs consolidate through a transfer station) and  |
| 6 | `quickdesign` (259-quickdesign) | 4 | 6/k | 51 | 0 | needs-paid-api | Use the `quickdesign` CLI to generate AI media — UGC promo videos, image edits, product creatives, video upsca |
| 7 | `hyperframes-cli` (2702-hyperframes) | 4 | 7/k | 50 | 0 | — | HyperFrames CLI tool — hyperframes init, lint, inspect, preview, render, transcribe, tts, doctor, browser, inf |
| 8 | `akbun-describe-twitter-transcript` (1097-akbun-learning) | 3 | 6/k | 49 | 3 | vague | x.com(트위터) post 링크와 함께 영상 자막 변환을 요청할 때만 사용한다. |
| 9 | `record-screen` (2354-power-platform) | 4 | 3/k | 48 | 2 | — | Record a Chrome browser tab to video via CLI. Use when the user wants to capture a screen recording of a brows |
| 10 | `aso` (1446-marketing-skills) | 4 | 4/k | 47 | 0 | needs-paid-api | When the user wants to audit or optimize an App Store or Google Play listing. Also use when the user mentions  |

### audio-music — 354 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `game-audio-procedural` (1526-gamegen) | 5 | 31/k | 100 | 11 | needs-paid-api | Compose game music and design sound effects in code with a bundled numpy/scipy synthesis toolkit, then export |
| 2 | `music` (1511-homie) | 4 | 29/k | 85 | 1 | needs-paid-api | Make songs, themes and game scores for a Homie studio with ElevenLabs Music, through the creator's OWN ElevenL |
| 3 | `together-audio` (3214-togetherai-skills) | 3 | 91/k | 84 | 6 | vague | Text-to-speech and speech-to-text via Together AI, including REST, streaming, and realtime WebSocket TTS, plus |
| 4 | `sound` (1511-homie) | 4 | 23/k | 81 | 1 | needs-paid-api | Make a game's sound effects and synthesized music on the creator's own computer, free, with no provider or acc |
| 5 | `transcribe` (886-intel) | 3 | 33/k | 81 | 3 | — | Turn audio into plain-text words, transcribed locally with whisper — a finite file or URL, or a live stream ca |
| 6 | `deepgram-hello-world` (1845-deepgram-pack) | 4 | 28/k | 77 | 0 | needs-paid-api | Create a minimal working Deepgram transcription example. |
| 7 | `hyperframes` (2702-hyperframes) | 5 | 9/k | 74 | 2 | — | Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, an |
| 8 | `demo-video` (1644-framecraft) | 4 | 30/k | 74 | 0 | — | Generate polished demo videos from a single prompt. Use when the user |
| 9 | `elevenlabs-hello-world` (1847-elevenlabs-pack) | 4 | 24/k | 74 | 0 | needs-paid-api | Generate your first ElevenLabs text-to-speech audio file. Use when starting a new ElevenLabs integration, test |
| 10 | `game-trailer` (1526-gamegen) | 4 | 18/k | 72 | 0 | — | Produce promo trailers from real gameplay of a Godot 4 game: a beat-synced 16:9 1080p60 trailer, a native 9:16 |

### video-generation — 91 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `research-finance` (217-research-ops-skills) | 5 | 15/k | 84 | 6 | — | Use when managing the money for an internal R&D program or portfolio — building a multi-period program budget  |
| 2 | `together-video` (3214-togetherai-skills) | 3 | 45/k | 81 | 3 | vague | Text-to-video and image-to-video generation via Together AI, including keyframe control, model and dimension s |
| 3 | `klingai-team-setup` (1874-klingai-pack) | 4 | 27/k | 80 | 0 | needs-paid-api | Configure Kling AI for teams with per-project API keys, usage quotas, |
| 4 | `klingai-model-catalog` (1874-klingai-pack) | 4 | 27/k | 78 | 0 | needs-paid-api | Explore Kling AI models, versions, and capabilities for video and image |
| 5 | `cfo-advisor` (138-c-level-skills) | 4 | 14/k | 73 | 3 | needs-paid-api | Financial leadership for startups and scaling companies. Financial modeling, unit economics, fundraising strat |
| 6 | `runway-install-auth` (1900-runway-pack) | 3 | 25/k | 65 | 0 | vague, needs-paid-api | Install and verify a server-side Runway Dev client without spending generation credits or exposing an organiza |
| 7 | `runway-webhooks-events` (1900-runway-pack) | 3 | 25/k | 65 | 0 | vague, needs-paid-api | Convert authoritative Runway task polling into durable internal events or signed customer callbacks without cl |
| 8 | `airunway-aks-setup` (2511-azure) | 3 | 19/k | 62 | 0 | — | Set up AI Runway on AKS — from bare cluster to running model. Covers cluster verification, controller install, |
| 9 | `video` (1446-marketing-skills) | 4 | 12/k | 60 | 0 | needs-paid-api | When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. A |
| 10 | `video-gen` (2976-pwdev-social-media) | 3 | 20/k | 58 | 0 | — | Produz vídeo curto — roteiro, storyboard, prompts por cena e geração via Runway quando há chave. Use quando o  |

### image-generation — 50 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `together-images` (3214-togetherai-skills) | 3 | 31/k | 84 | 4 | vague, hub-doc | Text-to-image generation and image editing via Together AI, including FLUX and Kontext models, LoRA-based styl |
| 2 | `comfyui-node-scaffold` (2142-comfyui-plugin) | 4 | 18/k | 78 | 2 | — | Scaffold a new ComfyUI custom-node repo (TypeScript + bun build, CI, release-please, vitest+pytest) consuming  |
| 3 | `comfy-node` (2142-comfyui-plugin) | 4 | 24/k | 76 | 0 | — | Orchestrate a ComfyUI node pack from idea to registry: scaffold, create + seed the repo, open the gitops adopt |
| 4 | `comfyui-workflow-design` (2819-comfyui) | 3 | 26/k | 71 | 0 | — | Use for designing or editing ComfyUI workflow JSON, image/video pipelines, nodes, LoRA, ControlNet, IP-Adapter |
| 5 | `comfyui-api` (2819-comfyui) | 3 | 29/k | 67 | 0 | vague | Use for ComfyUI API work: queue prompts, status, models, downloads, progress, queue/history, and connectivity  |
| 6 | `comfyui-layer` (2736-charly-comfyui) | 2 | 67/k | 57 | 0 | vague | ComfyUI image generation service on port 8188 with CUDA GPU support. Use when working with ComfyUI, image gene |
| 7 | `comfyui` (2736-charly-comfyui) | 2 | 68/k | 57 | 0 | vague | ComfyUI image generation server with CUDA GPU support. Runs as a supervisord service on port 8188 with persist |
| 8 | `flux` (1567-tonone) | 2 | 63/k | 56 | 0 | vague | Data engineer — databases, migrations, pipelines, schema design, and query optimization. |
| 9 | `building-gitops-workflows` (1727-gitops-workflow-builder) | 3 | 19/k | 56 | 0 | vague, needs-paid-api | Execute use when constructing GitOps workflows using ArgoCD or Flux. |
| 10 | `image` (1446-marketing-skills) | 4 | 10/k | 55 | 0 | needs-paid-api | When the user wants to create, generate, edit, or optimize images for marketing — blog heroes, social graphics |

### social-content — 198 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `social` (1446-marketing-skills) | 4 | 25/k | 84 | 0 | — | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Ins |
| 2 | `postiz` (x2178-postiz) | 5 | 13/k | 80 | 4 | needs-paid-api | Postiz is a tool to schedule social media and chat posts to 28+ channels X, LinkedIn, LinkedIn Page, Reddit, I |
| 3 | `transcriptapi` (3613-youtube-skills) | 4 | 26/k | 80 | 0 | needs-paid-api | Use when YouTube is or could be relevant — even if not mentioned: pasted video/channel/playlist links, video I |
| 4 | `youtube-data` (3613-youtube-skills) | 4 | 31/k | 80 | 0 | needs-paid-api | Use when structured YouTube data is needed: pasted video/channel/playlist links, transcripts for analysis, vid |
| 5 | `social-media-analyzer` (192-marketing-skills) | 5 | 13/k | 77 | 2 | needs-paid-api | Social media campaign analysis and performance tracking. Calculates engagement rates, ROI, and benchmarks acro |
| 6 | `9503-video-digest` (2451-knowledge) | 5 | 9/k | 75 | 4 | — | Watch a single public video from YouTube or X (Twitter): transcript, links, and repo-applicability recommendat |
| 7 | `youtube-full` (192-marketing-skills) | 4 | 26/k | 72 | 0 | needs-paid-api | Use when the user needs YouTube transcripts, video search, channel browsing, playlist extraction, or content m |
| 8 | `account-video-downloader` (2990-account-video-downloader) | 4 | 11/k | 70 | 7 | needs-paid-api | Multi-platform account video extractor — provide a platform name and account ID/link to automatically fetch ho |
| 9 | `fetch-tiktok-mentions` (886-intel) | 3 | 33/k | 69 | 1 | — | Fetch a brand's TikTok videos from hashtag pages, user pages and keyword searches into docs/intel/tiktok/<slug |
| 10 | `brand-listening` (895-brightdata-plugin) | 4 | 19/k | 69 | 0 | — | Social listening and brand reputation research using Bright Data's web scraping infrastructure. Collects what  |

### prompt-engineering — 82 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `prompt-engineering-patterns` (3103-llm-application-dev) | 3 | 18/k | 66 | 1 | vague | This skill should be used when the user asks to "optimize a prompt", "improve prompt performance", "design a p |
| 2 | `cortex-prompt` (1567-tonone) | 4 | 17/k | 62 | 0 | — | Build a production-ready prompt package — system prompt, few-shot examples, output format, edge case handling, |
| 3 | `prompt-optimization` (1547-plugin-creator) | 4 | 10/k | 57 | 0 | outdated | Optimize CLAUDE.md files and Skills for Claude Code CLI. Use when reviewing, creating, or improving system pro |
| 4 | `agent-development` (301-plugin-dev) | 4 | 8/k | 57 | 1 | — | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent  |
| 5 | `prompt-engineer-toolkit` (192-marketing-skills) | 4 | 6/k | 56 | 2 | — | Turns marketing prompts into tested, versioned production assets: A/B prompt evaluation against structured tes |
| 6 | `prompts` (718-prompt-template) | 2 | 40/k | 56 | 0 | vague, stub | Generate prompt template management systems |
| 7 | `langchain-prompt-engineering` (1875-langchain-py-pack) | 4 | 9/k | 55 | 0 | needs-paid-api | Manage LangChain 1.0 prompts like code \u2014 LangSmith prompt hub versioning,\n\ |
| 8 | `clade-policy-guardrails` (1835-claude-pack) | 3 | 13/k | 47 | 0 | vague | Implement content safety guardrails for Claude \u2014 input filtering,\n\ |
| 9 | `langchain-development` (2158-langchain-plugin) | 4 | 5/k | 45 | 0 | needs-paid-api | LangChain JS/TS framework for building LLM-powered apps. Use when working with chat models, prompt templates,  |
| 10 | `skill-meta-prompt` (2673-claude-octopus) | 4 | 4/k | 43 | 0 | — | Craft better prompts using proven optimization techniques — use when your prompt needs refinement |

### agents-orchestration — 6,082 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `agenthub` (155-agenthub) | 5 | 45/k | 100 | 6 | — | Multi-agent collaboration plugin that spawns N parallel subagents competing on the same task via git worktree  |
| 2 | `teams-setup` (2094-brewcode) | 5 | 28/k | 100 | 7 | needs-paid-api | Creates and manages dynamic teams of domain agents. Triggers: create team, agent team, team status, cleanup te |
| 3 | `agent-dev` (2103-agent-dev-kit) | 5 | 78/k | 100 | 5 | — | Builds one TypeScript AI agent or RAG increment from a spec-dev-kit spec (and optional html-generator-kit prot |
| 4 | `jfrog-mcp-management` (1980-jfrog) | 5 | 29/k | 99 | 2 | — | Use to install, list, or remove MCP servers, and to discover which MCPs the user can install — including quest |
| 5 | `agent-capability-analyzer` (1547-plugin-creator) | 5 | 99/k | 96 | 2 | — | Runs the description-drift experiment — spawns all Claude Code agents simultaneously to collect self-reported  |
| 6 | `herdr` (1454-herdr) | 4 | 28/k | 92 | 6 | — | Help with Herdr configuration, CLI, popup and tiled panes, plugins, and coordinating agents across panes. |
| 7 | `orchestrating-multi-agent-systems` (1570-ai-sdk-agents) | 4 | 70/k | 92 | 3 | vague, needs-paid-api | Execute orchestrate multi-agent systems with handoffs, routing, and |
| 8 | `workflow-builder` (186-workflow-builder) | 4 | 51/k | 92 | 3 | — | Design and write deterministic multi-agent workflow scripts (.js files in .claude/workflows/) for Claude Code' |
| 9 | `pm-skills` (213-pm-skills) | 4 | 31/k | 92 | 3 | — | Use when coordinating project-delivery work across the 8 project-management sub-skills — sprint/velocity analy |
| 10 | `orchestrate-frontend` (2107-frontend-orchestrator-kit) | 5 | 20/k | 92 | 4 | — | Runs the frontend-only app-dev-kit pipeline — spec-dev-kit to author a spec if needed, html-generator-kit to p |

### llm-evals — 800 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `uxd-prototype-evaluate` (3010-uxd-prototype) | 5 | 47/k | 100 | 31 | — | Evaluate a running prototype against a Jira ticket's acceptance criteria, automatically fix what fails, then r |
| 2 | `uxd-prototype-export` (3010-uxd-prototype) | 5 | 23/k | 98 | 10 | hub-doc | Export a prototype page or journey step as static HTML, a React component tree, or a PatternFly implementation |
| 3 | `tracking-regression-tests` (1967-regression-test-tracker) | 4 | 34/k | 92 | 3 | — | Track and manage regression test suites across releases. |
| 4 | `9466-design` (2439-evals) | 4 | 45/k | 91 | 3 | — | Design an evaluation suite for an LLM-based application or a Claude Code skill: interview for measurable succe |
| 5 | `catlass-dsl-optimize` (1505-catlass-dsl-generator) | 5 | 23/k | 88 | 1 | — | Iteratively optimize, speed up, benchmark, and profile one existing CATLASS DSL kernel on Ascend NPU with corr |
| 6 | `grade-iterate` (135-agent-launcher-skills) | 4 | 40/k | 87 | 3 | — | Phase 3 of building a Claude Managed Agent — the bounded grade→iterate loop. Define a CMA outcome (a required  |
| 7 | `social-media-analyzer` (192-marketing-skills) | 5 | 18/k | 84 | 2 | needs-paid-api | Social media campaign analysis and performance tracking. Calculates engagement rates, ROI, and benchmarks acro |
| 8 | `catlass-dsl-develop` (1505-catlass-dsl-generator) | 4 | 26/k | 83 | 1 | — | Develop, debug, review, test, benchmark, profile, and optionally optimize one CATLASS DSL kernel from an appro |
| 9 | `eval` (2624-eval) | 4 | 21/k | 83 | 1 | — | Grade a real run of a skill against its own committed contract, then turn each confirmed failure into a perman |
| 10 | `9469-validate` (2439-evals) | 4 | 19/k | 82 | 3 | needs-paid-api | Statically validate a `claude plugin eval` suite (`prompt.md`, `case.yaml`, `graders/*.md`) before any run spe |

### ai-safety-security — 54 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `chief-ai-officer-advisor` (138-c-level-skills) | 5 | 4/k | 66 | 3 | needs-paid-api | Chief AI Officer advisory for startups: model build-vs-buy decisions (API vs fine-tune vs in-house), AI risk c |
| 2 | `run-adversarial-attacks-and-jailbreaks` (2232-ai-red-teaming) | 2 | 30/k | 56 | 0 | vague | Execute the prioritized attacks against an AI system within the rules of engagement — direct and indirect prom |
| 3 | `adversarial-review` (3596-forge-teams) | 4 | 12/k | 54 | 0 | — | Agent Teams 对抗式审查 + 红队攻击。多 agent 并行审查（规格/代码/安全/红队），交叉检验，综合裁决。 Use when: (1) 重大功能发布前审查, (2) 涉及安全敏感代码, (3) 需要红队攻 |
| 4 | `red-team-agent` (3045-adlc-agent-engineering) | 2 | 24/k | 54 | 0 | vague | Use when the user invokes $red-team-agent, or asks to run the Agent Red Team workflow from the adlc-agent-engi |
| 5 | `octopus-security-audit` (2673-claude-octopus) | 5 | 5/k | 52 | 0 | — | OWASP compliance, vulnerability scanning, and adversarial red team testing — use for security reviews |
| 6 | `harden-and-remediate-ai-system` (2232-ai-red-teaming) | 2 | 22/k | 52 | 0 | vague | Triage red-team findings by likelihood×impact and drive defense-in-depth remediation — layered input/output gu |
| 7 | `langchain-security-basics` (1875-langchain-py-pack) | 4 | 6/k | 51 | 0 | needs-paid-api | Harden a LangChain 1.0 chain or LangGraph agent against prompt injection,\ |
| 8 | `gws-modelarmor-create-template` (2907-google-workspace) | 3 | 15/k | 49 | 0 | vague | Google Model Armor: Create a new Model Armor template. |
| 9 | `op` (3539-op) | 4 | 4/k | 46 | 0 | — | Strategy orchestration — 17 strategies including refine, tournament, chain, review, debate, red-team, brainsto |
| 10 | `forge-teams` (3596-forge-teams) | 4 | 5/k | 43 | 0 | — | Agent Teams 版 7 阶段产品开发流水线。自动识别意图：bug 描述→对抗调试，审查请求→红队审查，新功能→完整流水线。 对抗辩论 + 并行实现 + 红队审查 + 对抗调试。 Use when: (1) 新项目 |

### excel-spreadsheets — 176 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `lark-sheets` (3618-feishu2codex) | 4 | 20/k | 79 | 1 | — | 飞书电子表格：创建和操作电子表格。支持创建表格、管理工作表与行列结构（增删/合并/调整尺寸/隐藏/冻结）、读写单元格（值/公式/样式/批注/单元格图片）、查找替换、多操作原子批量更新，以及图表、透视表、条件格式、筛选器、 |
| 2 | `spreadsheet` (1428-openai-office-skills) | 4 | 29/k | 76 | 0 | needs-paid-api | Use when tasks involve creating, editing, analyzing, or formatting spreadsheets (`.xlsx`, `.csv`, `.tsv`) with |
| 3 | `render-xlsx` (3589-xbert-working-paper) | 3 | 51/k | 75 | 2 | — | Render an XBert working-paper schedule as a real .xlsx file from a structured payload. Use when an XBert plugi |
| 4 | `google-sheets` (2700-google-drive) | 3 | 47/k | 72 | 0 | — | Analyze and edit connected Google Sheets with range precision. Use when the user wants to create Google Sheets |
| 5 | `akbun-davinciresolve-contrast` (1096-akbun-editvideo) | 3 | 26/k | 72 | 1 | — | 단일 Log→Rec.709 LUT 경로에서 DaVinci Resolve 21.1 스크립팅 API로 새 `CONTRAST` 라벨 노드에 pivot 기준 대비를 적용하고 입력 공간의 기준값과 클리핑을  |
| 6 | `gdoc-to-markdown` (1067-bedrock) | 5 | 11/k | 67 | 1 | — | Internal fetcher module for Google Docs and Sheets. Fetches content via MCP (preferred, when available), Googl |
| 7 | `excel-pivot-wizard` (1633-excel-analyst-pro) | 3 | 72/k | 67 | 0 | vague | Create advanced Excel pivot tables with calculated fields and slicers. |
| 8 | `google-workspace-cli` (150-google-workspace-cli) | 5 | 4/k | 66 | 5 | — | Google Workspace administration via the gws CLI (github.com/googleworkspace/cli). Install, authenticate, and a |
| 9 | `gws-sheets-append` (2907-google-workspace) | 3 | 51/k | 65 | 0 | vague | Google Sheets: Append a row to a spreadsheet. |
| 10 | `markitdown` (3204-document-evidence) | 5 | 3/k | 65 | 3 | — | Convert heterogeneous documents and selected URIs to Markdown with Microsoft MarkItDown for text analysis, sea |

### financial-modeling — 897 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `revenue-operations` (136-business-growth-skills) | 5 | 31/k | 100 | 3 | — | Analyzes sales pipeline health, revenue forecasting accuracy, and go-to-market efficiency metrics for SaaS rev |
| 2 | `slo-architect` (182-slo-architect) | 5 | 21/k | 93 | 3 | — | Use when defining, reviewing, or operating SLOs/SLIs/error budgets. Triggers on "define an SLO", "what should  |
| 3 | `financial-analyst` (189-finance-skills) | 4 | 77/k | 92 | 4 | — | Performs financial ratio analysis, DCF valuation, budget variance analysis, and rolling forecast construction  |
| 4 | `commercial-forecaster` (147-commercial-skills) | 4 | 26/k | 91 | 3 | needs-paid-api | Use when building a quarterly bookings forecast, ARR projection, pipeline forecast, NRR projection, or commit/ |
| 5 | `research-finance` (217-research-ops-skills) | 5 | 15/k | 84 | 6 | — | Use when managing the money for an internal R&D program or portfolio — building a multi-period program budget  |
| 6 | `deep-work` (205-deep-work) | 5 | 13/k | 81 | 3 | — | Use when someone wants to plan a deep work day, time-block their calendar or task list, budget or cut shallow  |
| 7 | `validating-performance-budgets` (1782-performance-budget-validator) | 3 | 46/k | 81 | 3 | vague | Validate application performance against defined budgets to identify |
| 8 | `klingai-cost-controls` (1874-klingai-pack) | 4 | 31/k | 78 | 0 | needs-paid-api | Implement budget limits, usage alerts, and spending controls for Kling |
| 9 | `slo-implementation` (3107-observability-monitoring) | 4 | 29/k | 77 | 0 | — | Define and implement Service Level Indicators (SLIs) and Service Level Objectives (SLOs) with error budgets an |
| 10 | `forecast` (2539-monday-crm) | 4 | 24/k | 74 | 0 | — | Build a forecast dashboard in monday — committed, best-case, and pipeline views by close month, rendered as re |

### accounting-audit — 955 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `kubernetes-operator` (175-kubernetes-operator) | 4 | 29/k | 92 | 3 | — | Use when building a Kubernetes Operator — custom controllers that reconcile CRD state. Triggers on "build an o |
| 2 | `research-finance` (217-research-ops-skills) | 5 | 13/k | 81 | 6 | — | Use when managing the money for an internal R&D program or portfolio — building a multi-period program budget  |
| 3 | `render-xlsx` (3589-xbert-working-paper) | 3 | 26/k | 75 | 2 | — | Render an XBert working-paper schedule as a real .xlsx file from a structured payload. Use when an XBert plugi |
| 4 | `chase-overdue-invoices` (1522-intuit-quickbooks) | 4 | 45/k | 74 | 0 | needs-paid-api | Send payment reminders for invoices with tone matched to aging. ALWAYS use this skill when the user asks to "s |
| 5 | `seo-content` (2217-majestic-seo) | 5 | 8/k | 72 | 3 | — | Create or refresh one SEO or AEO article, from research through audited draft. |
| 6 | `month-end-prep` (335-small-business) | 3 | 27/k | 72 | 0 | needs-paid-api | Reconciles the accounting ledger (MYOB, NetSuite, QuickBooks, Xero, or Zoho Books) against PayPal, Shopify, Sq |
| 7 | `9591-running-retro` (2473-session-flow) | 4 | 12/k | 72 | 4 | vague, needs-paid-api | Take a mid-session retro checkpoint: a subagent files findings from the transcript so far into a running ledge |
| 8 | `9409-reduce` (2428-coupling) | 4 | 12/k | 71 | 3 | vague | Iteratively reduce coupling at any altitude (documents, code modules, applications, repositories): scan for ch |
| 9 | `linkedin-content` (197-linkedin) | 4 | 12/k | 71 | 3 | — | Use when someone wants to write, edit, or lint a LinkedIn post — a story, how-to, opinion piece, carousel scri |
| 10 | `kanban-workflow` (3610-yylo) | 3 | 38/k | 70 | 0 | — | Comprehensive guide for using YYLO Ledger task management. Covers all commands (create, list, search, get, mar |

### 3d-webgl — 968 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `awwwards-motion` (95-awwwards-motion) | 4 | 30/k | 78 | 0 | — | Build Awwwards-quality web experiences with spring physics, GLSL shaders, R3F, post-processing, particles, Fra |
| 2 | `webgpu-threejs-tsl` (2221-webgpu-threejs-tsl) | 3 | 96/k | 75 | 0 | — | Comprehensive guide for developing WebGPU-enabled Three.js applications using TSL (Three.js Shading Language). |
| 3 | `weekly-review` (212-weekly-review) | 5 | 7/k | 72 | 3 | — | Use when someone wants to run a weekly review, close open loops, audit stalled projects and commitments, get t |
| 4 | `saas-metrics-coach` (189-finance-skills) | 5 | 4/k | 66 | 3 | — | SaaS financial health advisor. Use when a user shares revenue or customer numbers, or mentions ARR, MRR, churn |
| 5 | `customer-success-manager` (136-business-growth-skills) | 5 | 3/k | 65 | 3 | needs-paid-api | Monitors customer health, predicts churn risk, and identifies expansion opportunities using weighted scoring m |
| 6 | `threejs-data-visualization` (2690-build-web-data-visualization) | 2 | 35/k | 64 | 0 | vague | Render WebGL-accelerated data visualizations with Three.js, raw WebGL, deck.gl, luma.gl, PixiJS, Sigma.js, Plo |
| 7 | `game-studio` (2696-game-studio) | 3 | 62/k | 64 | 0 | vague | Route early browser-game work. Use when the user needs stack selection and workflow planning across design, im |
| 8 | `linkedin-profile` (197-linkedin) | 4 | 6/k | 62 | 3 | — | Use when someone wants their LinkedIn profile audited or rewritten — headline, About section, experience bulle |
| 9 | `pf-figma-diff` (2998-patternfly) | 4 | 4/k | 58 | 4 | vague | Diff Figma designs to identify what changed and generate code update checklists. Use when syncing code with up |
| 10 | `lf-output-formatter` (2866-lf-output-formatter) | 4 | 4/k | 58 | 7 | — | Shared output formatter for every LFX Marketing OS agent. Use it whenever an agent, or a Linux Foundation mark |

### game-dev — 171 مهارة

| # | المهارة (الإضافة) | جودة | كثافة | مركبة | سكربتات | أعلام | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `9476-dlss5` (2443-gaming) | 4 | 21/k | 86 | 2 | — | Apply, track, tune, and remove the community DLSS 5 Neural Rendering mod (OptiScaler forks) in a PC game on Wi |
| 2 | `game-trailer` (1526-gamegen) | 4 | 33/k | 83 | 0 | — | Produce promo trailers from real gameplay of a Godot 4 game: a beat-synced 16:9 1080p60 trailer, a native 9:16 |
| 3 | `video` (1511-homie) | 5 | 14/k | 82 | 5 | needs-paid-api | Make trailers, music videos, cutscenes and page recordings for a Homie studio — a gameplay trailer captured fr |
| 4 | `game-audio-procedural` (1526-gamegen) | 5 | 13/k | 81 | 11 | needs-paid-api | Compose game music and design sound effects in code with a bundled numpy/scipy synthesis toolkit, then export |
| 5 | `art` (1511-homie) | 4 | 32/k | 79 | 1 | needs-paid-api | Make a studio's game look like something at build time — a cover from a real frame of the game (free), painted |
| 6 | `sprite-pipeline` (2696-game-studio) | 4 | 47/k | 74 | 0 | — | Generate and normalize 2D sprite animations. Use when the user asks for full-strip generation from approved so |
| 7 | `using-bgs-archive` (878-bgs-modding-superpowers) | 4 | 18/k | 67 | 0 | — | Use when the user wants to inspect, list, extract, unpack, or repack Bethesda BA2/BSA archives; determine arch |
| 8 | `using-bgs-papyrus` (878-bgs-modding-superpowers) | 3 | 22/k | 65 | 0 | — | Use when the user wants to compile Papyrus PSC to PEX, decompile PEX to PSC, detect Creation Kit Papyrus toolc |
| 9 | `bevy-game-engine` (2137-bevy-plugin) | 4 | 17/k | 65 | 0 | — | Bevy game engine: ECS, rendering, input, and asset management. Use when building Bevy games, working with enti |
| 10 | `game-studio` (2696-game-studio) | 3 | 34/k | 64 | 0 | vague | Route early browser-game work. Use when the user needs stack selection and workflow planning across design, im |

## أفضل 50 مهارة في الأطلس كله (جودة ثم بنية، بإزالة التكرار)

| # | المهارة (الإضافة) | المجال | جودة | سكربتات | مراجع | كلمات | الوصف |
|---|---|---|---|---|---|---|---|
| 1 | `seo` (2585-seo) | database | 5 | 40 | 49 | 2,443 | Deterministic LLM-first SEO audits for websites, blog posts, and GitHub repositories. Use this when  |
| 2 | `kicad` (110-kicad-happy) | pdf | 5 | 36 | 20 | 10,259 | Analyze KiCad projects and PDF schematics: schematics, PCB layouts, Gerbers, footprints, symbols, ne |
| 3 | `shiploop` (3406-skill-craft) | testing-qa | 5 | 34 | 43 | 9,259 | Markdown-authoritative delivery harness. Start or resume once, follow the script's current action pa |
| 4 | `speckit-generator` (377-speckit-generator) | agents-orchestration | 5 | 6 | 50 | 2,559 | Project-focused specification and task management system. Run /speckit.init to install 8 project-loc |
| 5 | `skill-creator-doctor` (247-claude-dev-infrastructure) | claude-code-meta | 5 | 8 | 0 | 5,620 | Create, repair, maintain, and consolidate skills. This skill should be used when users want to creat |
| 6 | `postiz` (x2178-postiz) | social-content | 5 | 4 | 12 | 3,848 | Postiz is a tool to schedule social media and chat posts to 28+ channels X, LinkedIn, LinkedIn Page, |
| 7 | `llm-to-bedrock` (367-aws-startup-advisor) | cloud-edge | 5 | 17 | 12 | 6,098 | Use when the user wants to migrate code that calls OpenAI, Gemini/Google AI, or the Anthropic API to |
| 8 | `replatform` (3419-wix) | database | 5 | 6 | 77 | 5,665 | Routes RePlatform source-to-Wix migrations to the next workflow step by inspecting migration project |
| 9 | `deploy` (2098-brewtools) | devops-ci | 5 | 4 | 4 | 4,112 | GitHub Actions deployment: workflows, releases, GHCR, CI/CD with safety gates. Triggers: deploy, rel |
| 10 | `xray-method` (21-codebase-xray) | docs-writing | 5 | 9 | 6 | 4,438 | X-ray method: mechanical structure extraction fused with semantic reading into a ground-truth accoun |
| 11 | `huggingface-llm-trainer` (1514-huggingface-skills) | security | 5 | 8 | 10 | 3,500 | Train or fine-tune language and vision models using TRL (Transformer Reinforcement Learning) or Unsl |
| 12 | `autopilot` (1452-dispatch) | agents-orchestration | 5 | 33 | 3 | 5,809 | Execute a flightplan task tree end-to-end with a multi-agent dev → review → score quality loop. |
| 13 | `semble-setup` (2094-brewcode) | agents-orchestration | 5 | 9 | 15 | 8,398 | Installs, audits, repairs, updates, enables, reindexes or removes the semble_code semantic code-sear |
| 14 | `dx-code-analyzer-run` (1444-salesforce-development) | security | 5 | 9 | 14 | 3,245 | Run Salesforce Code Analyzer to scan code for security, performance, best practice, and code style v |
| 15 | `create-skill` (1120-ambient-library) | llm-evals | 5 | 9 | 5 | 6,342 | Create new skills, modify and improve existing skills, and measure skill performance — with a routin |
| 16 | `jfrog-init` (1980-jfrog) | agents-orchestration | 5 | 19 | 20 | 3,308 | Set up and verify the JFrog plugin. Run on first install, to complete initial configuration, or to d |
| 17 | `uxd-prototype-evaluate` (3010-uxd-prototype) | llm-evals | 5 | 31 | 21 | 1,261 | Evaluate a running prototype against a Jira ticket's acceptance criteria, automatically fix what fai |
| 18 | `skill-creator` (311-skill-creator) | llm-evals | 5 | 9 | 2 | 5,151 | Create new skills, modify and improve existing skills, and measure skill performance. Use when users |
| 19 | `9610-babysit-prs` (2476-source-control) | git-github | 5 | 22 | 14 | 5,501 | Babysit the user's own open GitHub pull requests as a tiered fleet loop. The safe default discovers  |
| 20 | `shopify-hydrogen` (3055-shopify-plugin) | backend-api | 5 | 5 | 2 | 17,776 | Hydrogen storefront implementation cookbooks. Some of the available recipes are: B2B Commerce, Bundl |
| 21 | `google-workspace-cli` (150-google-workspace-cli) | productivity-email | 5 | 5 | 5 | 1,556 | Google Workspace administration via the gws CLI (github.com/googleworkspace/cli). Install, authentic |
| 22 | `feature-dev` (2106-feature-dev-kit) | agents-orchestration | 5 | 9 | 25 | 3,421 | Builds a complete React feature end-to-end from a request or an existing spec, following Feature-Sli |
| 23 | `hotline-dial` (2043-hotline) | agents-orchestration | 5 | 23 | 5 | 7,484 | Call another Claude Code workspace — quick calls, work orders, conference calls. 'Call/dial/message/ |
| 24 | `skill-forge` (3121-batterie) | agents-orchestration | 5 | 5 | 10 | 2,097 | Orchestrates all skill development — required before writing or editing any SKILL.md file. Unified 6 |
| 25 | `agents-pay` (363-aws-agents) | agents-orchestration | 5 | 7 | 5 | 3,680 | Use when THIS agent needs to pay for x402-protected content at runtime: hitting a paywall mid-task,  |
| 26 | `generate-html` (2108-html-generator-kit) | web-frontend | 5 | 7 | 20 | 2,683 | Transforms a validated spec from .spec/app/current.json into a clickable multi-page HTML prototype a |
| 27 | `engineer-design-diagram` (1722-engineer-design-diagram) | web-frontend | 5 | 4 | 15 | 2,107 | Generate production-grade engineering design diagrams (architecture,\ |
| 28 | `generate-spec` (2109-spec-dev-kit) | agents-orchestration | 5 | 13 | 11 | 1,984 | Transforms raw user requirements in .spec/context/ into a validated, approved hybrid YAML+Markdown s |
| 29 | `uncertainty-and-units` (3202-quantitative-sciences) | testing-qa | 5 | 7 | 6 | 2,376 | Track physical units and propagate measurement uncertainty in scientific calculations using pint and |
| 30 | `exec` (3229-planning) | git-github | 5 | 11 | 13 | 4,552 | Execute plan tasks sequentially using subagents. Use when user says 'exec', 'execute plan', 'run pla |
| 31 | `benchmark-sandbox` (3256-vercel) | cloud-edge | 5 | 5 | 0 | 2,918 | Run vercel-plugin eval scenarios in Vercel Sandboxes instead of local WezTerm panels. Provisions eph |
| 32 | `modernize-test-starter` (3217-ui5-modernization) | testing-qa | 5 | 6 | 5 | 1,937 | Modernize QUnit unit tests and OPA5 integration tests to the UI5 Test Starter concept. Use this skil |
| 33 | `app-store-optimization` (192-marketing-skills) | mobile | 5 | 8 | 4 | 2,251 | App Store Optimization (ASO) toolkit for researching keywords, analyzing competitor rankings, genera |
| 34 | `audit-tests` (1803-intent-labs-pack) | testing-qa | 5 | 5 | 9 | 2,989 | Diagnostic-only test suite auditor. Classifies repo type, maps against\ |
| 35 | `instrument-data-to-allotrope` (314-bio-research) | database | 5 | 4 | 4 | 1,296 | Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JS |
| 36 | `podium-rate-limit-survival` (1893-podium-pack) | backend-api | 5 | 4 | 3 | 2,440 | Survive the rate-limit failure modes that crater production Podium integrations — |
| 37 | `creating-kubernetes-deployments` (1735-kubernetes-deployment-creator) | backend-api | 5 | 4 | 18 | 1,009 | Deploy applications to Kubernetes with production-ready manifests. |
| 38 | `exploratory-data-analysis` (3211-structured-data-analysis) | web-frontend | 5 | 13 | 7 | 1,368 | Perform bounded, local exploratory analysis of explicitly supported scientific files. Use for redact |
| 39 | `drive-automation-session` (1962-automate) | scraping-automation | 5 | 4 | 3 | 3,183 | Drive an already-reserved Kobiton device from a natural-language intent. Opens an automation Appium  |
| 40 | `citation-management` (3199-evidence-lab-core) | research | 5 | 8 | 12 | 1,613 | Comprehensive citation management for academic research. Search OpenAlex, PubMed, and Google Scholar |
| 41 | `compliance-os` (148-compliance-os) | legal-contracts | 5 | 4 | 9 | 1,432 | Compliance OS — meta-orchestrator that lets compliance teams CONFIGURE which frameworks apply, COMPU |
| 42 | `python-refactor-method` (40-python-development) | testing-qa | 5 | 7 | 13 | 1,713 | Restructure tangled code into a clear equivalent, preserving behavior. TRIGGER WHEN: the user asks f |
| 43 | `rust-reverse-engineering` (1981-rust-reverse-engineering) | debugging | 5 | 9 | 5 | 1,988 | Use when analyzing a Rust binary without source code, reverse engineering Rust executables or librar |
| 44 | `exploring-llm-traces` (2957-posthog) | data-analysis | 5 | 6 | 3 | 1,705 | Debug and inspect LLM/AI agent traces using PostHog's MCP tools. Use when the user pastes a trace or |
| 45 | `analyze-x-mentions` (886-intel) | ecommerce | 5 | 9 | 0 | 2,738 | Turn a fetched X/Twitter mentions archive (tweets.jsonl from fetch-x-mentions) into a concise, data- |
| 46 | `agenthub` (155-agenthub) | agents-orchestration | 5 | 6 | 3 | 1,075 | Multi-agent collaboration plugin that spawns N parallel subagents competing on the same task via git |
| 47 | `peer-review` (3206-literature-publication) | research | 5 | 8 | 15 | 1,346 | Prepare evidence-bounded, constructive peer-review drafts and structured manuscript assessments. Use |
| 48 | `splitting-pdf` (3136-doc-util) | pdf | 5 | 4 | 2 | 1,158 | This skill should be used when users want to split PDF files by bookmarks or page ranges. Common tri |
| 49 | `deployment` (1209-crowdstrike-falcon-fusion) | agents-orchestration | 5 | 5 | 1 | 2,643 | Import, release, and manage Falcon Fusion workflow definitions in a CID. TRIGGER when user asks to i |
| 50 | `game-audio-procedural` (1526-gamegen) | audio-music | 5 | 11 | 11 | 1,501 | Compose game music and design sound effects in code with a bundled numpy/scipy synthesis toolkit, th |

## جدول متقاطع: الوسم × الجودة

| الوسم | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| agents-orchestration | 304 | 1,600 | 2,390 | 1,787 | 1 |
| backend-api | 306 | 1,750 | 2,479 | 971 | 0 |
| testing-qa | 273 | 1,235 | 2,183 | 1,327 | 0 |
| legal-contracts | 135 | 665 | 1,911 | 978 | 0 |
| claude-code-meta | 149 | 833 | 1,093 | 1,397 | 0 |
| git-github | 235 | 1,124 | 1,191 | 904 | 0 |
| research | 119 | 478 | 1,712 | 995 | 0 |
| database | 160 | 835 | 1,242 | 689 | 0 |
| docs-writing | 163 | 789 | 1,356 | 557 | 0 |
| devops-ci | 191 | 905 | 1,177 | 544 | 0 |
| security | 141 | 725 | 1,417 | 420 | 0 |
| data-analysis | 128 | 726 | 884 | 426 | 0 |
| decision-reasoning | 77 | 321 | 770 | 708 | 0 |
| web-frontend | 104 | 650 | 630 | 386 | 0 |
| productivity-email | 76 | 498 | 636 | 509 | 0 |
| copywriting-marketing | 86 | 428 | 657 | 528 | 0 |
| debugging | 123 | 542 | 485 | 417 | 0 |
| design-ui | 54 | 407 | 435 | 385 | 0 |
| architecture | 41 | 263 | 467 | 435 | 0 |
| cloud-edge | 66 | 389 | 450 | 210 | 0 |
| business-strategy | 55 | 245 | 392 | 306 | 0 |
| 3d-webgl | 66 | 265 | 358 | 279 | 0 |
| accounting-audit | 27 | 136 | 564 | 228 | 0 |
| financial-modeling | 39 | 206 | 445 | 207 | 0 |
| dataviz-dashboards | 54 | 321 | 323 | 182 | 0 |
| ecommerce | 47 | 267 | 352 | 183 | 0 |
| llm-evals | 51 | 209 | 270 | 270 | 0 |
| mobile | 31 | 154 | 243 | 297 | 0 |
| landing-marketing | 37 | 147 | 269 | 203 | 0 |
| hr-recruiting | 46 | 200 | 225 | 178 | 0 |
| scraping-automation | 31 | 172 | 300 | 125 | 0 |
| healthcare | 45 | 168 | 247 | 143 | 0 |
| rag-knowledge | 26 | 109 | 195 | 133 | 0 |
| code-review-refactor | 17 | 102 | 160 | 173 | 0 |
| real-estate | 23 | 100 | 159 | 167 | 0 |
| education-learning | 33 | 84 | 141 | 147 | 0 |
| storytelling | 11 | 72 | 148 | 125 | 0 |
| audio-music | 22 | 158 | 121 | 53 | 0 |
| translation-i18n | 33 | 106 | 115 | 73 | 0 |
| pdf | 31 | 95 | 85 | 39 | 0 |
| math-science | 19 | 102 | 79 | 46 | 0 |
| animation | 4 | 46 | 76 | 77 | 0 |
| social-content | 9 | 54 | 75 | 60 | 0 |
| excel-spreadsheets | 9 | 33 | 67 | 67 | 0 |
| game-dev | 3 | 25 | 44 | 99 | 0 |
| powerpoint-slides | 7 | 49 | 44 | 55 | 0 |
| word-docs | 5 | 21 | 52 | 26 | 0 |
| video-editing | 14 | 28 | 25 | 27 | 0 |
| video-generation | 2 | 31 | 49 | 9 | 0 |
| photography-lighting | 15 | 27 | 29 | 17 | 0 |
| prompt-engineering | 3 | 25 | 34 | 20 | 0 |
| captions-subtitles | 11 | 11 | 22 | 10 | 0 |
| ai-safety-security | 5 | 17 | 20 | 12 | 0 |
| image-generation | 1 | 18 | 14 | 17 | 0 |

## خريطة المهارات الخارقة الـ108 ← مصادرها في الأطلس (مع جودة كل مصدر)

| # | المهارة الخارقة | المصادر الثمانية (الاسم · جودة/5) | متوسط جودة المصادر |
|---|---|---|---|
| 01 | `claude-animation-studio` | gsap · 5 · awwwards-motion · 4 · hyperframes · 5 · remotion-maps · 2 · animate · 2 · 9525-animate · 2 | 3.3 |
| 02 | `trend-animation-styles` | kinetic-inflated-hero · 2 · awwwards-motion · 4 · web-typography · 4 · scrollytelling-and-parallax-data-visualization · 2 · top-design · 4 · scroll-blur-manifesto · 2 | 3.0 |
| 03 | `kinetic-typography-arabic` | web-typography · 4 · font-opt · 2 · kinetic-inflated-hero · 2 · captions · 3 · remotion-captions · 2 · geist · 4 | 2.8 |
| 04 | `character-animation-2d` | 9525-animate · 2 · 9527-sprite · 2 · sprite-pipeline · 4 · akbun-draw-cartoon-b · 3 · animate · 2 · klingai-image-to-video · 4 | 2.8 |
| 05 | `explainer-edu-animation` | diagram · 3 · process-infographic · 5 · teaching-block-synthesized · 2 · engineer-design-diagram · 5 · 9459-eli5 · 4 · skill-teaching · 2 | 3.5 |
| 06 | `cinematic-3d-scene` | webgpu-threejs-tsl · 3 · three-webgl-game · 2 · web-3d-asset-pipeline · 2 · awwwards-motion · 4 · threejs-data-visualization · 2 · thermal-finger-trail · 2 | 2.5 |
| 07 | `data-in-motion` | d3-data-visualization · 3 · data-visualization · 3 · client-rendered-dashboard-data-blob · 3 · end-of-period-dashboard · 2 · helm-chart-builder · 5 · dashboard · 3 | 3.2 |
| 08 | `ui-motion-microinteractions` | scroll-blur-manifesto · 2 · spring-profile-config-overlay-dedupe · 3 · spring · 2 · create-spring-boot-java-project · 3 · enterprise-spring-xml · 3 · gsap · 5 | 3.0 |
| 09 | `image-prompt-forge` | comfyui-layer · 2 · ideogram-core-workflow-b · 3 · comfyui · 2 · prompt-governance · 3 · ideogram-ci-integration · 3 · prompt-eval-and-regression · 2 | 2.5 |
| 10 | `video-prompt-director` | runway-core-workflow-a · 3 · runway-core-workflow-b · 3 · klingai-image-to-video · 4 · klingai-text-to-video · 4 · video · 4 · cfo-advisor · 4 | 3.7 |
| 11 | `cinema-director-7layers` | audit-agency-continuity · 2 · brand-film · 2 · creator-visual-director · 3 · frontend-design-director · 3 · narrated-product-film · 2 · revision-continuity · 4 | 2.7 |
| 12 | `storyboard-shotlist` | video-content-strategist · 3 · creator-script-agent · 2 · video-content-strategist · 3 · video-script · 3 · 9424-script-the-deterministic-work · 2 · interview-script · 2 | 2.5 |
| 13 | `brand-identity-logo` | brand-guidelines · 3 · brand-book-assembly · 2 · generate-logo · 3 · brand-voice-and-messaging · 2 · brand-landingpage · 4 · form-brand · 3 | 2.8 |
| 14 | `svg-illustration-icons` | generate-favicon · 4 · akbun-draw-book-illustration · 3 · svg-figure · 4 · diagram · 3 · vector · 2 · engineer-design-diagram · 5 | 3.5 |
| 15 | `diagrams-mermaid-architecture` | ln-25-architecture-diagram-builder · 2 · diagram · 3 · architecture-diagram · 4 · mermaid-cli · 5 · aws-architecture-diagram · 4 · akbun-draw-architecture · 3 | 3.5 |
| 16 | `pixel-art-game-assets` | 9528-tileset · 2 · phaser-2d-game · 2 · 9527-sprite · 2 · godot-gdscript-patterns · 2 · unity-ecs-patterns · 2 · godot-gdscript-patterns · 2 | 2.0 |
| 17 | `thumbnail-social-graphics` | creator-thumbnail-agent · 2 · youtube-search · 4 · youtube-full · 4 · youtube-api · 4 · youtube-transcript · 2 · cover-image · 4 | 3.3 |
| 18 | `photo-lighting-plan` | vibe-portrait · 4 · chronograph-look-through-exposure-scan · 2 · exposure-effect · 2 · exposure-onboarding · 2 · akbun-davinciresolve-exposure · 4 · design-fx-and-interest-rate-hedge · 3 | 2.8 |
| 19 | `image-critique-reverse-prompt` | vision-inference-optimization · 3 · processing-computer-vision-tasks · 3 · product-vision · 2 · vision-sft · 2 · vision-sft · 2 · pdf-ocr-adding · 4 | 2.7 |
| 20 | `ai-art-style-library` | style-extractor · 3 · style-writer · 2 · adhd-output-style · 2 · Structure · ? · Education · ? · prior-art · 3 · style-pack · 2 · art · 4 | 2.7 |
| 21 | `product-photo-mockups` | product-catalog-management · 3 · catalog · 2 · seo-ecommerce · 4 · shopify-migration-deep-dive · 4 · shopify-admin · 4 · shopify-app-pricing · 3 | 3.3 |
| 22 | `comics-picture-books` | reader-panel · 4 · story-init · 4 · panel · 3 · internal-narrative · 2 · game-story-world-character · 2 · akbun-draw-book-illustration · 3 | 3.0 |
| 23 | `ad-creative-30s` | launch-ad-campaign · 3 · ad-creative · 3 · paid-advertising · 3 · codex-hook-wire-schema-from-binary · 3 · test-a-commit-blocking-hook · 4 · commercial-policy · 5 | 3.5 |
| 24 | `reels-shorts-factory` | story-reels · 2 · social-video-hooks · 2 · davinciresolve-youtube-shorts · 2 · block-no-verify-hook · 4 · block-no-verify-hook · 4 · captions · 3 | 2.8 |
| 25 | `video-editing-captions` | captions · 3 · ffmpeg · 4 · subtitles · 3 · ffmpeg · 2 · remotion-captions · 2 · hyperframes · 5 | 3.2 |
| 26 | `prompt-master-pro` | prompt-engineering-patterns · 3 · prompt-engineering-patterns · 3 · enrich-prompt · 2 · prompt-pattern-selection · 2 · prompt-engineering · 3 · langchain-prompt-engineering · 4 | 2.8 |
| 27 | `system-prompt-architect` | persona-exec-assistant · 2 · persona-exec-assistant · 2 · grafana-assistant-cli · 3 · persona-ci-integration · 3 · persona-common-errors · 3 · assistant · 3 | 2.7 |
| 28 | `agent-tool-instructions` | agent-host-skill-loading · 3 · setup-mcp-agent-analytics · 4 · agent-skill-init · 4 · agent-team-orchestration · 4 · agent-sync-check-workflow · 2 · agent-sync-generate-workflow · 2 | 3.2 |
| 29 | `structured-output-json` | json-schema · 2 · structured-output-design · 2 · resilient-extraction-and-parsing · 2 · use-zod · 4 · mongodb-schema-design · 4 · schema-review · 3 | 2.8 |
| 30 | `llm-judge-evals` | prompt-eval-and-regression · 2 · eval-ladder · 3 · eval-regression · 2 · build-llm-judge · 2 · eval-harness-first · 2 · eval-harness-first · 2 | 2.2 |
| 31 | `rag-knowledge-base` | retrieval-review · 3 · rag-retrieval-audit · 2 · rag-audit-workflow · 2 · azuresql-db-rag · 4 · embedding-strategies · 2 · rag-implementation · 2 | 2.5 |
| 32 | `prompt-injection-defense` | generating-security-audit-reports · 3 · finding-security-misconfigurations · 3 · checking-session-security · 3 · security-audit · 3 · security-requirement-extraction · 2 · scanning-api-security · 3 | 2.8 |
| 33 | `context-window-budget` | token-optimization · 2 · memory · 2 · tree-ring-memory · 4 · slack-app-token-rotation · 3 · tracking-token-launches · 5 · detecting-memory-leaks · 3 | 3.2 |
| 34 | `few-shot-dataset-curation` | trace-to-training-data · 2 · trace-to-training-data · 2 · gcp-examples-expert · 3 · fine-tune · 2 · ai-evaluation-dataset · 2 · dataset-curation · 3 | 2.3 |
| 35 | `custom-gpt-claude-project` | grafana-assistant-cli · 3 · actions-billing-usage · 3 · github-actions-auth-security · 4 · github-actions-startup-failure-triage · 4 · gh-actions-validator · 3 · assistant · 3 | 3.3 |
| 36 | `excel-power-formulas` | excel-pivot-wizard · 3 · excel-dcf-modeler · 2 · render-xlsx · 3 · excel · 2 · adobe-anyexcel · 2 · google-sheets · 3 | 2.5 |
| 37 | `excel-financial-models` | excel-dcf-modeler · 2 · excel-lbo-modeler · 3 · dcf-valuation · 3 · chronograph-budget-vs-actuals-variance · 2 · cash-flow-snapshot · 4 · financial-analyst · 4 | 3.0 |
| 38 | `excel-data-cleaning-automation` | claude-code-plugin-release-automation · 4 · merge-main · 4 · gh-pr-merge-delete-branch-closes-dependent-pr · 3 · git-pr-merge-unblock · 4 · pr-amend-force-push-lost-to-racing-merge · 3 · merge-main · 4 | 3.7 |
| 39 | `word-documents-pro` | infer-office · 4 · infer-report-structure · 4 · publish-report-board · 4 · dev-report · 3 · import-template · 3 · investigation-report · 2 | 3.3 |
| 40 | `powerpoint-decks` | pptx-deck-context · 2 · pptx-reference-deck-analysis · 2 · presentation-builder · 4 · create-presentation · 3 · edit-presentation · 4 · slides · 4 | 3.2 |
| 41 | `google-workspace-automation` | google-workspace-cli · 5 · google-drive · 2 · gws-gmail-forward · 3 · gws-gmail-read · 3 · session-workspace · 2 · workspace-doctor · 2 | 2.8 |
| 42 | `pdf-forms-reports` | pdf-ocr-adding · 4 · pdf-report · 2 · pdf-xfa-extracting · 3 · audit-report · 3 · extracting-pdf · 5 · report-injection-guard · 3 | 3.3 |
| 43 | `office-prompts-library` | email-template-engineering · 3 · email-tmpl · 2 · copilot-agent-eval-harness · 2 · infer-office · 4 · resolve-copilot-pr-feedback · 5 · prompt-governance · 3 | 3.2 |
| 44 | `dashboards-dataviz` | kpi-dashboard-design · 3 · d3-data-visualization · 3 · gantt-chart-visualization · 3 · kpi-dashboard-design · 2 · dashboard-layout-review · 2 · analytics · 3 | 2.7 |
| 45 | `sql-data-analysis` | postgres-sql · 4 · sql-server-query · 2 · exploratory-data-analysis · 5 · write-query · 3 · ingesting-into-data-lake · 3 · ga4-data-api-query · 4 | 3.5 |
| 46 | `web-scraping-automation` | playwright · 5 · 286-browser-automation · 4 · 313-browser-automation · 4 · 340-browser-automation · 4 · agent-browser · 4 · 9552-playwright · 3 | 4.0 |
| 47 | `notebooks-python-analysis` | jupyter-ml-notebook · 3 · jupyter-mcp · 3 · jupyter · 2 · macos-python-scripting · 2 · python-simple-scripts · 2 · python-guidelines · 2 | 2.3 |
| 48 | `forecasting-probability` | forecasting-time-series-data · 3 · forecast · 2 · build-forecast · 2 · chronograph-cashflow-forecast · 3 · churn-risk · 2 · risk-analysis · 3 | 2.5 |
| 49 | `ab-testing-experiments` | experiment-analysis · 2 · setting-up-experiment-tracking · 3 · oss-contribution-shape-by-conversion-rate · 3 · surge-experiment · 3 · surge-experiment · 3 · diagnosing-experiment-results · 3 | 2.8 |
| 50 | `research-deep-citations` | research-writing-literature · 2 · research-verify · 2 · 13208-research-verify · 2 · deep-research · 3 · 9413-do-your-research-deep · 3 · analytics-verify · 3 | 2.5 |
| 51 | `landing-page-premium` | landing-page-generator · 4 · landing-page-audit · 2 · visual-html-renderer · 4 · oss-contribution-shape-by-conversion-rate · 3 · tailwind-best-practices · 2 · markdown-html-orchestrator · 5 | 3.3 |
| 52 | `website-design-system` | tailwind-design-system · 3 · tailwind-design-system · 3 · tailwind-best-practices · 2 · ui-design-system · 5 · nuxt-ui · 4 · nuxt-ui · 4 | 3.5 |
| 53 | `frontend-react-app` | react-state-management · 2 · react-state-management · 2 · react-component · 3 · react-component-craft · 2 · create-react-component · 2 · react-component-convention · 2 | 2.2 |
| 54 | `backend-api-design` | building-graphql-server · 3 · backend-dev · 5 · api-plugin-openapi-hygiene · 2 · aws-http-server-on-lambda-web-adapter · 3 · fastapi-app · 4 | 3.4 |
| 55 | `database-schema-migrations` | prisma-database-setup · 4 · prisma-database-setup · 4 · azuresql-db-schema-migration · 4 · prisma-schema · 3 · database-migration · 3 · database-migration · 3 | 3.5 |
| 56 | `fullstack-saas-starter` | supabase-auth-storage-realtime-core · 3 · supabase-deploy-integration · 5 · supabase-js · 2 · stripe-developer · 4 · supabase · 2 · saas-scaffolder · 4 | 3.3 |
| 57 | `mobile-app-builder` | reverse-engineer-react-native-hermes-app · 2 · flutter-app · 3 · expo-ui-swift-ui · 3 · ios-app-intents · 3 · android-design · 3 · android-design · 3 | 2.8 |
| 58 | `cloudflare-edge-deploy` | wrangler · 5 · Configuration · ? · wrangler · 5 · Configuration · ? · cloudflare · 3 · cloudflare · 3 · cloudflare-deploy · 3 · nextjs-on-cloudflare · 2 | 3.5 |
| 59 | `docker-ci-devops` | guidewire-ci-cd-pipeline · 4 · generating-docker-compose-files · 3 · ci-cd-integration · 4 · ci-pipeline-design · 2 · azure-kubernetes-app-deploy · 3 · azure-kubernetes-app-deploy · 3 | 3.2 |
| 60 | `debugging-root-cause` | debug · 3 · power-automate-debug · 4 · sentry-debug-issue · 3 · debug · 2 · lint-and-fix · 4 · troubleshoot · 3 | 3.2 |
| 61 | `code-review-refactor` | code-review-and-quality · 4 · code-review-and-quality · 4 · code-review-and-quality · 4 · code-review-and-quality · 4 · code-review · 2 · clean-code-workflow · 3 | 3.5 |
| 62 | `testing-suite-complete` | playwright-testing · 3 · Configuration · ? · analyzing-test-coverage · 4 · e2e-testing-patterns · 3 · unit-test · 2 | 3.0 |
| 63 | `security-audit-stride` | security-audit · 3 · generating-security-audit-reports · 3 · analyzing-security-headers · 3 · security-audit · 5 · octopus-security-audit · 5 · Modes · ? · river-review-security-audit · 3 | 3.7 |
| 64 | `git-github-workflow` | git-pr-merge-unblock · 4 · git-commit · 4 · git-worktree-convention · 4 · git-merge-request · 4 · git-worktree · 4 · gh-pr-merge-delete-branch-closes-dependent-pr · 3 | 3.8 |
| 65 | `automation-scripts-cli` | go-cli-release-automation · 2 · google-workspace-cli · 5 · cli-design-and-arg-parsing · 2 · cli-cfg · 2 · add-scrut-cli-tests · 5 · scaffold-go-cli · 5 | 3.5 |
| 66 | `browser-automation-playwright` | 9552-playwright · 3 · playwright · 5 · agent-browser · 3 · e2e-automation · 2 · 286-browser-automation · 4 · 313-browser-automation · 4 | 3.5 |
| 67 | `performance-optimization` | optimizing-cache-performance · 3 · optimize-build-and-cache · 3 · web-performance-optimization · 4 · alchemy-performance-tuning · 3 · canva-performance-tuning · 3 · firecrawl-performance-tuning · 3 | 3.2 |
| 68 | `accessibility-wcag` | pf-a11y-keyboard · 3 · accessibility-and-inclusive-visualization · 2 · accessibility-implementation · 2 · pf-a11y-test-gen · 2 · a11y-audit · 5 · pf-a11y-keyboard · 3 | 2.8 |
| 69 | `seo-content-architecture` | seo-schema · 3 · seo-schema · 3 · seo-backlinks · 4 · seo-backlinks · 4 · seo-implement · 2 · implement-technical-seo-and-structured-data · 2 | 3.0 |
| 70 | `technical-docs-readme` | generating-api-docs · 3 · technical-documentation · 4 · docs-create-workflow · 3 · documentation · 2 · diataxis-documentation · 2 · readme-craft · 3 | 2.8 |
| 71 | `python-pro` | uv-package-manager · 4 · uv-package-manager · 4 · uv-package-manager · 4 · uv-python-versions · 4 · python-typing-reference · 2 · python-typing · 2 | 3.3 |
| 72 | `typescript-node-pro` | migrate-to-deno · 3 · migrate-to-deno · 3 · javascript-testing-patterns · 3 · javascript-testing-patterns · 3 · typescript-debugging · 4 · mastering-typescript · 4 | 3.3 |
| 73 | `legacy-code-migration` | strangler-fig-migration · 2 · assemblyai-upgrade-migration · 3 · bamboohr-upgrade-migration · 3 · techsmith-upgrade-migration · 3 · together-upgrade-migration · 3 · adobe-upgrade-migration · 3 | 2.8 |
| 74 | `software-architecture-adr` | system-design · 4 · ln-21-system-design-baseline-builder · 2 · clean-architecture · 3 · akbun-draw-architecture · 3 · ln-22-current-architecture-documenter · 2 · architecture · 2 | 2.7 |
| 75 | `game-dev-web` | phaser-2d-game · 2 · rust-bracket-game-loop · 2 · godot-gdscript-patterns · 2 · unity-ecs-patterns · 2 · godot-gdscript-patterns · 2 · unity-ecs-patterns · 2 | 2.0 |
| 76 | `arabic-copywriting` | copywriting · 2 · marketing-psychology · 3 · copywriting · 3 · marketing-context · 3 · archetypes-brand-voice · 2 · content-engine · 5 | 3.0 |
| 77 | `storytelling-scripts` | game-story-world-character · 2 · plot-structure · 2 · character-management · 3 · book-fiction · 2 · book-screenplay · 2 · archetypes-storytelling-arcs · 2 | 2.2 |
| 78 | `translation-localization-ar` | language-config · 2 · i18n-foundations-and-icu · 2 · localization-qa-and-pseudo-loc · 2 · language-audit · 2 · 9454-curate-language · 2 · nuxt-i18n · 3 | 2.2 |
| 79 | `newsletter-email-marketing` | send-email-campaign · 3 · form-email · 3 · email-sequence · 3 · aimm-newsletter · 2 · email-template-engineering · 3 · email-tmpl · 2 | 2.7 |
| 80 | `voiceover-tts-direction` | elevenlabs-core-workflow-a · 3 · elevenlabs-hello-world · 4 · speech-recognition-and-synthesis · 3 · voice-agent-architecture-and-latency · 3 · twilio-voice-conversation-relay · 3 · human-voice · 2 | 3.0 |
| 81 | `podcast-production` | joined-audio-transcript-drift · 4 · transcript-to-content-pipeline · 2 · write-realtime-audio-code · 2 · choose-audio-dsp-architecture · 2 · implement-and-optimize-realtime-audio · 3 · interview-me · 4 | 2.8 |
| 82 | `music-song-brief` | music · 4 · 9607-suno · 4 · write-realtime-audio-code · 2 · choose-audio-dsp-architecture · 2 · implement-and-optimize-realtime-audio · 3 · joined-audio-transcript-drift · 4 | 3.2 |
| 83 | `audio-mastering-analysis` | joined-audio-transcript-drift · 4 · sound · 4 · write-realtime-audio-code · 2 · choose-audio-dsp-architecture · 2 · implement-and-optimize-realtime-audio · 3 · write-realtime-audio-code · 2 | 2.8 |
| 84 | `youtube-channel-strategy` | creator-thumbnail-agent · 2 · creator-seo-agent · 2 · youtube-channels · 4 · youtube-api · 4 · youtube-full · 4 · youtube-packaging · 2 | 3.0 |
| 85 | `accounting-ifrs-journal` | tax-reconciliation · 3 · ias-prep · 2 · vat-prep · 2 · tres-ledger-link · 4 · accounting-inbox · 3 · reconciliation-automatch · 3 | 2.8 |
| 86 | `invoices-quotes-contracts` | contract-to-billing · 3 · contract-and-proposal-writer · 4 · contract-review · 3 · box-legal-workflows-contract · 3 · implement-metered-billing · 2 · contract-review-and-redline · 2 | 2.8 |
| 87 | `business-plan-prd` | prd-roadmap · 4 · prd-stories · 3 · code-to-prd · 5 · create-prd · 2 · market-segments · 2 · market-sizing · 2 | 3.0 |
| 88 | `pitch-deck-investor` | build-investor-pipeline · 2 · presentation-builder · 4 · startup-financial-modeling · 4 · lf-member-pitch-deck · 3 · akbun-presentation-paper · 2 · akbun-presentation-visual · 2 | 2.8 |
| 89 | `market-competitor-research` | competitor-analysis · 2 · competitor-analysis · 2 · swot-analysis · 2 · competitive-positioning-analysis · 2 · competitor-positioning · 4 · competitor-analysis · 3 | 2.5 |
| 90 | `ecommerce-store-listings` | shopify-app-store-review · 4 · design-shopify-build · 2 · ship-app-store-ready · 2 · shopify-custom-data · 4 · shopify-prod-checklist · 4 · shopify-advanced-troubleshooting · 4 | 3.3 |
| 91 | `curriculum-course-builder` | curriculum · 5 · training-machine-learning-models · 3 · deep-learning-book · 4 · syllabus · 5 · optimizing-deep-learning-models · 3 · adapting-transfer-learning-models · 3 | 3.8 |
| 92 | `flashcards-quiz-exam-prep` | anki-flashcards · 4 · deep-learning-book · 4 · practice-health-check · 2 · practice-metrics · 3 · optimizing-deep-learning-models · 3 · adapting-transfer-learning-models · 3 | 3.2 |
| 93 | `math-science-tutor` | math-unicode · 3 · long-form-math · 3 · collab-proof · 4 · red-green-proof · 2 · balance-sheet-explain · 3 · write-math · 2 | 2.8 |
| 94 | `language-coach-arabic-english` | polyglot-language-coach · 2 · polyglot-language-coach · 2 · akbun-learning-english · 2 · agent-learning-coach · 2 · 9454-curate-language · 2 · mcp-language-server-orphan-fd-exhaustion · 2 | 2.0 |
| 95 | `book-to-skill-knowledge` | deep-learning-book · 4 · second-brain · 3 · obsidian-power-user · 3 · customer-learning-notes · 3 · knowledge-compiler · 2 · 9498-book-distill · 3 | 3.0 |
| 96 | `genius-council-decision` | codex-advisor · 2 · fable-advisor · 2 · tool-advisor · 3 · business-investment-advisor · 3 · marketing-council · 3 · second-opinion · 3 | 2.7 |
| 97 | `red-team-premortem` | strategy-red-team · 2 · identify-assumptions-existing · 2 · pre-mortem · 3 · pre-mortem · 2 · identify-assumptions-new · 2 · stress-test · 3 | 2.3 |
| 98 | `fact-checker-verifier` | verify-claims · 3 · rp-source-evidence · 2 · rp-source-evidence · 2 · citation-management · 5 · hallucination-checks · 2 · analytics-verify · 3 | 2.8 |
| 99 | `strategy-decision-sensitivity` | seo-roadmap-prioritization · 2 · experimentation-strategy-roadmap · 3 · good-strategy-bad-strategy · 3 · interactive-planning · 4 · brand-strategy · 3 · planning-flow · 3 | 3.0 |
| 100 | `ideation-100-ideas` | brainstorm-ideas-existing · 2 · brainstorm-ideas-new · 2 · brainstorm · 3 · brainstorm · 2 · positioning-ideas · 2 · ce-brainstorm · 4 | 2.5 |
| 101 | `pro-video-editor-ffmpeg` | ffmpeg · 4 · losslesscut · 3 · ffmpeg · 2 · low-latency-live-streaming · 2 · streaming-architecture-and-protocol-selection · 3 · joined-audio-transcript-drift · 4 | 3.0 |
| 102 | `davinci-resolve-pipeline` | davinci-resolve · 3 · render-networking · 2 · resolve-copilot-pr-feedback · 5 · resolve-copilot-pr-feedback · 5 · render-background-workers · 3 · render-blueprints · 3 | 3.5 |
| 103 | `prompt-architect-reasoning-models` | prompt-engineering · 3 · reasoning · 2 · prompt-engineering · 3 · codex-reasoning-level-calibration · 2 · unslop-reasoning · 2 · prompt-engineering-patterns · 3 | 2.5 |
| 104 | `llm-judge-eval-lab` | prompt-eval-and-regression · 2 · eval-ladder · 3 · eval-regression · 2 · eval · 2 · eval-harness-first · 2 · eval-harness-first · 2 | 2.2 |
| 105 | `motion-director-pro` | remotion-best-practices · 3 · remotion-create · 3 · remotion-video-builder · 2 · kinetic-inflated-hero · 2 · gsap · 5 · brand-film · 2 | 2.8 |
| 106 | `audio-reactive-captions-studio` | captions · 3 · whisper · 2 · subtitles · 3 · hyperframes · 5 · fetch-tiktok-mentions · 3 · remotion-captions · 2 | 3.0 |
| 107 | `excel-model-architect` | chronograph-budget-vs-actuals-variance · 2 · build-cash-forecast-and-liquidity-plan · 2 · experiment-sensitivity-optimization · 3 · thirteen-week-cash-forecast · 3 · variance-analysis · 3 · forecast-and-alert · 2 | 2.5 |
| 108 | `excel-automation-power` | aws-http-server-on-lambda-web-adapter · 3 · lambda · 2 · excel-pivot-wizard · 3 · aws-lambda-durable-functions · 5 · aws-lambda-managed-instances · 4 · lean-startup · 3 | 3.3 |

## كيف تستعلم

```python
import sqlite3; db = sqlite3.connect('tools/atlas-deep.sqlite')
# أفضل 10 في وسم، بالدرجة المركبة لذلك الوسم:
for r in db.execute("SELECT a.name, a.plugin, a.quality, t.density, t.composite FROM skill_tag t JOIN advanced_skill a ON a.path=t.path WHERE t.tag='video-editing' ORDER BY t.composite DESC LIMIT 10"): print(r)
# بحث نصي كامل ثم ترتيب بالجودة:
for r in db.execute("SELECT a.name, a.quality, a.composite FROM skill_fts f JOIN advanced_skill a ON a.id=f.rowid WHERE skill_fts MATCH 'ffmpeg AND loudnorm' ORDER BY a.quality DESC, a.composite DESC LIMIT 10"): print(r)
# مهارات بسكربتات وجودة 5 في مجال الإكسل:
for r in db.execute("SELECT name, plugin, scripts FROM advanced_skill WHERE domain='excel-spreadsheets' AND quality=5 ORDER BY composite DESC"): print(r)
```
