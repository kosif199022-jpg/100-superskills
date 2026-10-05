# DEEP-READ: LOCAL HEURISTIC CARDS FOR 15,122 SKILLS

Cards: 14,793 skills (local extraction + word counting, no external LLM).
Average quality: 3.14/5

### other (3,709)
- `1001-add-goreleaser-homebrew/2285-add-goreleaser-homebrew/SKILL.md` (4/5)
- `1006-bootstrap-project/2290-bootstrap-project/SKILL.md` (4/5)
- `1011-create-issue/2295-create-issue/SKILL.md` (4/5)
- `1012-create-plugin/2296-create-plugin/SKILL.md` (4/5)
- `1015-lint-and-fix/2299-lint-and-fix/SKILL.md` (4/5)

### testing-qa (3,011)
- `1000-add-community-files/2284-add-community-files/SKILL.md` (4/5)
- `1002-add-scrut-cli-tests/2286-add-scrut-cli-tests/SKILL.md` (4/5)
- `1009-commit/2293-commit/SKILL.md` (4/5)
- `1010-create-deferred-issues/2294-create-deferred-issues/SKILL.md` (4/5)
- `102-sendsets/225-sendsets-cli/SKILL.md` (4/5)

### database (2,876)
- `1005-address-review/2289-address-review/SKILL.md` (4/5)
- `1007-check-zsh-scripts/2291-check-zsh-scripts/SKILL.md` (4/5)
- `1029-review-branch/2312-review-branch/SKILL.md` (4/5)
- `1031-review-dependabot-config/2314-review-dependabot-config/SKILL.md` (4/5)
- `1046-upgrade-everything/2329-upgrade-everything/SKILL.md` (4/5)

### video-editing (2,444)
- `1003-address-issue/2287-address-issue/SKILL.md` (4/5)
- `1016-manage-repo-licensing/2300-manage-repo-licensing/SKILL.md` (4/5)
- `1021-pin-everything/2304-pin-everything/SKILL.md` (4/5)
- `103-adobe-for-creativity/230-adobe-batch-edit-photos/SKILL.md` (4/5)
- `103-adobe-for-creativity/232-adobe-create-social-variations/SKILL.md` (4/5)

### prompt-engineering (1,134)
- `1004-address-issue-in-worktree/2288-address-issue-in-worktree/SKILL.md` (4/5)
- `1008-clean-up-agent-config/2292-clean-up-agent-config/SKILL.md` (4/5)
- `1013-create-worktree/2297-create-worktree/SKILL.md` (4/5)
- `1014-handle-secrets/2298-handle-secrets/SKILL.md` (4/5)
- `1023-pr/2306-pr/SKILL.md` (4/5)

### audio-music (686)
- `107-airwallex-agentos/262-awx-best-practices/SKILL.md` (4/5)
- `107-airwallex-agentos/263-beneficiary-creation/SKILL.md` (4/5)
- `107-airwallex-agentos/264-card-provisioning/SKILL.md` (4/5)
- `107-airwallex-agentos/265-contract-to-billing/SKILL.md` (4/5)
- `107-airwallex-agentos/266-manage-cashflow/SKILL.md` (4/5)

### financial-modeling (494)
- `10-termination-self-monitoring/15-termination-self-monitoring/SKILL.md` (4/5)
- `1018-monitor-pr/2302-monitor-pr/SKILL.md` (4/5)
- `103-adobe-for-creativity/235-adobe-document-review/SKILL.md` (4/5)
- `106-airtable/258-marketing-ops/SKILL.md` (4/5)
- `106-airtable/259-product-ops/SKILL.md` (4/5)

### animation (252)
- `100-ui-motion/211-thermal-finger-trail/SKILL.md` (4/5)
- `1394-stark/3323-android-design/SKILL.md` (4/5)
- `1394-stark/3324-apple-design/SKILL.md` (4/5)
- `1394-stark/3325-cross-platform-design/SKILL.md` (4/5)
- `1394-stark/3326-design-router/SKILL.md` (4/5)

### excel-spreadsheets (187)
- `103-adobe-for-creativity/227-adobe-anyexcel/SKILL.md` (4/5)
- `103-adobe-for-creativity/228-adobe-anypdf/SKILL.md` (4/5)
- `103-adobe-for-creativity/229-adobe-anypptx/SKILL.md` (4/5)
- `1040-set-up-installers/2323-set-up-installers/SKILL.md` (4/5)
- `1051-write-homebrew-formula/2334-write-homebrew-formula/SKILL.md` (4/5)

## Search
```python
import sqlite3; db=sqlite3.connect('tools/atlas-deep.sqlite')
for r in db.execute("SELECT path, quality_overall FROM card_fts JOIN card ON path WHERE card_fts MATCH 'excel' ORDER BY quality_overall DESC LIMIT 5"): print(r)
```