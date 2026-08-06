# Run scaffold — zero-budget-fields

## User Prompt (VERBATIM — gospel)
See `query.md`. It is the canonical, character-for-character reference for this run.

## Run config
- vault_tag: `zero-budget-fields`
- query_file_path: `research/runs/zero-budget-fields/query.md`
- modality: **synthesize** (evaluate 20+ candidate fields, rank them on a weighted framework, defend a committed recommendation with evidence chains)
- wrapper_contract: none (standalone deliverable)
- citation_style: **inline** — public deliverable, `[N]` numbered citations + `## Sources` section
- profile/gear: premier (source_target 100–130; doubled depth budget), full tier

## Modality calibration
The prompt asks to *rank* fields, *identify* top-5 and single-best, *explain precisely why* and *defend*. This is an evaluative synthesis: a defended thesis ("the single best field is X") backed by a transparent multi-criteria scoring model and explicit trade-off analysis — not a flat catalog. Every field still gets a structured profile (demand / opportunity / accessibility / recognition / contributions).

## Tier rationale
The query is a multi-attribute, cross-disciplinary optimization with a committed recommendation and explicit counter-argumentation ("defend by comparing against top candidates"). This is `full` tier — deep analysis, contested conclusions, evidence-chain reasoning. response_format: `argumentative`. Register: `analyze` (evaluation-shaped). inference_depth: `deep` (the load-bearing answer lives in the research-practice literature and historical examples of independent contributors, not a quick consensus).

## Scope conditions (binding)
- Budget ₹0 exactly. No paid software, subscriptions, cloud, APIs, datasets, courses, certifications, memberships.
- Outdated hardware: low RAM, older CPU, no GPU, limited storage, slow.
- Free, legal, publicly accessible tools only.
- Exclude fields whose progress depends on expensive hardware, large-scale compute, paid infra, proprietary datasets, lab access, corporate employment, large teams, significant investment.

## Required output contract (from prompt)
1. Rank the 15 highest-leverage fields overall.
2. Identify the 5 strongest recommendations.
3. Explain precisely why these outperform every alternative.
4. Identify the largest risks for each recommendation.
5. Recommend the single best field for maximizing long-term recognition under the constraints.
6. Defend the recommendation by explicit comparison against other top candidates.
7. Per-field profiles: overall ranking, overall score, why it satisfies constraints, why difficult, who succeeds, misconceptions, beginner mistakes, contribution pathways, examples of influential independent contributors, realistic first contributions, free tools, free datasets, free learning resources, free communities, publication opportunities, open-source opportunities, expected timeline.
8. Evidence standard: distinguish established evidence / strong inference / reasoned speculation. No generic career advice or motivational language.

## Tier classification
- pipeline_tier: full
- response_format: argumentative (target 5000–10000 words; premier word_target 8000–16000)
- citation_style: inline

## Levers (step 1 provisional)
- register: analyze (evaluation-shaped: "identify", "rank", "recommend", "defend")
- register_confidence: high
- domain_notes: Academic-first for research-practice evidence; historical case studies of independent contributors (archive.org, university pages, arxiv, OSF); recency matters for the *current* state of each field but the durable argument (what makes a field computable on a laptop) is structural and stable. Evidence norms: prefer documented, replicable examples of independent work; treat "you can't get recognized without credentials" as a hypothesis to test against counterexamples, not an axiom.
- inference_depth: deep (provisional — the answer likely lives in research-practice literature + documented independent-contributor histories)
