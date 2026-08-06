---
archive_status: ARCHIVED
referential_status: NON-REFERENTIAL
archived_date: 2026-08-06
superseded_by: research/notes/final_report_zero-budget-fields.md (Current Working Draft)
notes: Intermediate working note from early pipeline stage (search-plan.md). Retained strictly for historical traceability.
---

# [ARCHIVED - NON-REFERENTIAL] Historical Pipeline Artifact: search-plan.md

> **HISTORICAL ARCHIVE NOTICE:** This document is an intermediate artifact produced during earlier research steps. Its findings, analyses, and data have been fully integrated into and superseded by the master Current Working Draft at . This file is non-referential.

---

# Search plan + corpus notes (width sweep, step 2)

Lenses: A=breadth, B=citation-chain/depth (academic), C=adversarial, D=period-pinned (none — no time_periods).

## Executed searches (evidence record)
| Lens | Query | Target | Key findings captured |
|---|---|---|---|
| A | independent researcher no affiliation published math solved problem | recognition feasibility | Mixed: "good research is good research" but credential bias; double-blind venues; theory fields have unaffiliated-publishing traditions; examples: Andreas Madsen, Alexia Jolicoeur-Martineau (ICLR), published solo |
| A/B | Lean mathlib contributions community | formal proof accessibility | mathlib >2M lines, half undergrad math formalized, daily open contributions, Lean free, Zulip community |
| A | metascience reproducibility opportunities free data | meta-science ecosystem | Replication Database open; registered reports; OSF free; "manifesto for reproducible science"; RoRI |
| A | recreational math open problems OEIS amateur | experimental/rec math | OEIS "sequences needing more terms"; BB(5) proven by anonymous Coq user + Discord amateurs; superpermutation lower bound (anonymous 4chan); Greg Egan |
| B | TCS complexity without expensive hardware laptop | theory CS | Open-problem registries (sublinear.info, TOPS, TLCA); theory is hardware-independent ("cleanroom of complexity") |
| A | statistics methodology free software R open problems | statistics | R free; replication/simulation replication (RepliSims) in R; registered-report culture |
| A | cybersecurity vuln research free tools recognition | cybersecurity | Ghidra, radare2, x64dbg, Frida free; CVE credit; but competitive + some hardware |
| A | accessibility HCI research independent free tools | HCI/accessibility | WCAG free; WAVE/axe free; published comparison of 6 free accessibility evaluators shows a real method gap |
| B | information/coding theory open problems no lab | info theory | Finite-blocklength IT open problems; unsolved problems in IT; open problems in coding theory; purely mathematical |
| B | experimental mathematics computational discovery | experimental math | Journal of Experimental Mathematics; PSLQ; computer-assisted proofs (Kepler, four-color, Feigenbaum) legitimate |
| A | network science open problems datasets | network science | Open-data mandates; open-access NWS journal; data-driven (needs datasets) |
| B | mechanism design game theory free resources | economics theory | Free textbooks (AGT, Roth, Handbook of Comp Social Choice); math-computational side open (EC conf) |
| A | mathematical biology theoretical ecology laptop | math bio | Open ODE tools, EcoEvoApps; modeling on laptop; theory accessible, empirical grounding needs domain data |
| A | combinatorial optimization OR free solvers | OR/optimization | OR-Tools, SCIP, HiGHS free; CP-SAT primer; benchmark-driven recognition |
| A | open source build reputation contributions | open source | OSS contribution builds reputation; few-maintainer projects; inbound attention; but crowded in mainstream |
| B | formal verification software correctness Lean Coq independent | formal verification | Lean 4 free; Cedar uses Lean; Erdos problems solved w/ Lean; community-driven |
| C | (adversarial) "you can't get recognized without credentials" | challenge assumption | Counterexamples strong in combinatorics/experimental math (Royen GCI, Yitang Zhang, Marjorie Rice, BB(5), superpermutation); weaker in ML/empirical fields |
| C | (adversarial) AI solving math problems (OpenAI ten advances) | automation/saturation risk | Theory problems are being auto-attacked by AI; raises saturation risk for *solving* known open problems; pushes value toward verification, surveys, methodology, benchmarks, "undiscovered" niches |

## Corpus gaps / notes
- Fields needing lab/proprietary data (wet-lab biology, medicine RCTs, climate *measurement*, some physics) largely EXCLUDED or downweighted — only their theory/synthesis/method wings remain viable.
- ML model training excluded (compute); ML *theory/interpretation/evaluation* viable.
- Adversarial lens found a key structural insight: **the durable value shifts toward (a) fields computable on a laptop, (b) contribution types that resist automation** (verification, critical evaluation, synthesis, benchmark/taxonomy construction) **rather than raw novelty claims**.
