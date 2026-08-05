## Coverage Matrix — query phrase → atomic item mapping

| Query phrase (verbatim) | Mapped atomic item(s) | Scope check | Gap? |
|---|---|---|---|
| "highest-leverage fields" | SQ1, Evaluation model, Top-15 | OK — core deliverable | No |
| "single independent individual" | Accessibility, Recognition (no-team scope condition) | OK | No |
| "outdated computer" | Compatibility with outdated hardware (eval criterion) | OK | No |
| "budget of exactly zero" | Zero financial cost (eval criterion), scope_conditions | OK | No |
| "answer meaningful open-ended questions" | SQ2, Research Opportunity | OK | No |
| "build a public reputation" | SQ5 Recognition Potential | OK | No |
| "valuable over the next decade" | SQ2 long-term demand, time_horizons | OK | No |
| "Do not optimize for salaries" | register=analyze; no salary/career framing | OK | No |
| "intellectual leverage" | Eval criterion "Intellectual leverage" | OK | No |
| "No paid software, subscriptions, cloud services, APIs, datasets, courses, certifications, or memberships" | Zero financial cost (all sub-items), scope_conditions | OK | No |
| "free, legal, publicly accessible tools" | Ability to work with free resources, scope_conditions | OK | No |
| "Original research / Analytical thinking / ... / Reproducible experimentation using lightweight tools" (contribution list) | SQ6 Contribution Types | OK | No |
| "Do not recommend fields where progress depends on expensive hardware / large compute / paid infra / proprietary datasets / lab access / corporate employment / large teams / significant investment" | Exclusions, scope_conditions, evaluation | OK — explicit exclusion gate | No |
| All 21 scope fields (CS, AI, SE, Cybersecurity, Math, Stats, Econ, Physics, Biology, Medicine, Philosophy, Cognitive Sci, Linguistics, Systems Eng, Education, Climate, OR, Network Sci, Info Theory, HCI, Open Source) | entities (all present) | OK | No |
| "For each field investigate: Demand / Research Opportunity / Accessibility / Recognition Potential / Contribution Types" | Per-field profile schema (17 attributes) | OK | No |
| "Evaluation Framework — rank every field using weighted criteria" (10 criteria) | Evaluation model, Top-15 ranking | OK | No |
| "For every field include: ... Expected timeline" (17 attributes) | Per-field profile schema | OK | No |
| "Final Analysis — rank 15, five strongest, why outperform, largest risks, single best field, defend vs others" | required_sections, Top-15, Top-5, Single-best, Risk register | OK | No |
| "Clearly distinguish established evidence / strong inference / reasoned speculation" | Evidence-tiering section | OK | No |
| "Avoid generic career advice, motivational language" | register; evidence-standard framing | OK | No |

**Result: zero `Gap? = YES` rows.** No decomposition fix needed.

Note: the prompt's per-field list implies a *broad* landscape survey across all 21 named fields plus interdisciplinary combinations (formal verification, meta-science, scientometrics, recreational math were added as entities because the prompt explicitly says "Search broadly ... including ... emerging interdisciplinary fields" — these are legitimate expansions, not narrowing).
