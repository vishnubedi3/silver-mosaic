---
archive_status: ARCHIVED
referential_status: NON-REFERENTIAL
archived_date: 2026-08-06
superseded_by: research/notes/final_report_zero-budget-fields.md (Current Working Draft)
notes: Intermediate working note from early pipeline stage (evidence-digest.md). Retained strictly for historical traceability.
---

# [ARCHIVED - NON-REFERENTIAL] Historical Pipeline Artifact: evidence-digest.md

> **HISTORICAL ARCHIVE NOTICE:** This document is an intermediate artifact produced during earlier research steps. Its findings, analyses, and data have been fully integrated into and superseded by the master Current Working Draft at . This file is non-referential.

---

# Evidence digest — zero-budget-fields

## Recognition feasibility (independent researchers)
- Independent/unaffiliated publication is possible; double-blind venues (AAAI, IJCAI, ICLR) reduce bias. Documented cases: Andreas Madsen, Alexia Jolicoeur-Martineau published solo at top ML venues. [3][4]
- Institutional bias is real: blind reviews often carry affiliation; grant access and museum/specimen access are the hard barriers, not publishing itself. [1][2]
- **Strong inference:** theoretical math/CS and "paper-and-laptop" fields have the longest unaffiliated-publishing traditions; empirical/clinical fields impose the most institutional friction. [1][2][4]

## Formal proof / Lean (high-scoring candidate)
- mathlib (Lean's math library) is community-maintained, free, >2M lines, formalizes >half the undergraduate math curriculum; contributions are daily and recognition is purely by contribution. [5][6][34]
- Lean 4 is free, runs on a laptop, has a supportive Zulip community; used for Liquid Tensor (Scholze), PFR (Tao), and 2026 Erdős problems solved w/ Lean. [5][6][34][35]
- **Established evidence:** formal proof is a genuine, open, laptop-computable frontier with a strong norm of crediting every contributor. [5][6]

## Experimental / recreational mathematics (high-scoring candidate)
- Documented amateur/outsider contributions: BB(5) proven by an anonymous Coq user + a Discord working group; superpermutation lower bound by an anonymous 4chan poster; Greg Egan improved superpermutation upper bound. [10]
- Thomas Royen (retired statistician) proved the Gaussian correlation inequality; Yitang Zhang (outsider); Marjorie Rice (no math degree) found 4 pentagonal tilings; Aubrey de Grey (a biologist) posted the chromatic-number-of-the-plane ≥5 construction. [13]
- OEIS is an open, contribution-driven integer-sequence database with "sequences needing more terms" workflows; experimental-math results (Kepler conjecture, four-color theorem, Feigenbaum constant) are legitimate and peer-accepted. [11][14]
- **Established evidence:** combinatorics, recreational math, and experimental math are accessible to outsiders and yield citable, credited work. [10][13][14]

## Theoretical computer science / complexity (high-scoring)
- Rich, free open-problem registries: sublinear-time, TOPS (computational geometry), TLCA (lambda calculus/type theory), parameterized complexity. [15]
- Complexity theory is defined on a Turing machine — hardware-independent by construction; reasoning needs only paper + laptop. [16]
- **Adversarial note:** known open problems now attract AI-assisted attacks (e.g., OpenAI's "ten advances"); *solving* a famous conjecture is getting more contested, pushing value toward surveys, classification, verification, and new sub-problems. [27]

## Statistics / statistical methodology
- R is free and the lingua franca; registered reports and open data normalize; simulation-replication research (RepliSims) is a genuine method niche run in R. [18][19][17]
- Methodological-statistics research (estimator properties, bias-correction, simulation studies) is computable on a laptop and citable.

## Information theory / coding theory
- Open-problem catalogs exist in finite-blocklength information theory and coding theory; purely mathematical, no laboratory required. [24][25][26]

## Cybersecurity / reverse engineering
- Free professional-grade tools: Ghidra, radare2, x64dbg, Frida, Wireshark. [20][21]
- Recognition via CVE credit and public analysis; but competitive, needs some compute/space, and bounty hunting monetizes (out of scope for "intellectual leverage" framing). Moderate fit. [20]

## HCI / accessibility
- WCAG is free; free evaluators (WAVE, axe, ANDI). A published study comparing six free accessibility evaluators found large differences and *no systematic method* to compare them — a real, unmet methodological gap. [22][23]

## Network science
- Open-data mandates and open-access journals; but value is data-driven — the *theory* wing is laptop-computable, the empirical wing needs open datasets. [28]

## Economics / mechanism design theory
- Excellent free resources (Algorithmic Game Theory, Roth, Handbook of Computational Social Choice); math-computational side is accessible and open at the ACM EC conference. [29]

## Mathematical biology / theoretical ecology
- Open ODE/modeling tools (ODE-Designer, EcoEvoApps); theory and modeling run on a laptop. Empirical grounding needs domain data. [30]

## Operations research / optimization
- Free solvers (OR-Tools/CP-SAT, SCIP, HiGHS); benchmark-driven recognition (MiniZinc); combinatorial problems solvable on a laptop. [31]

## Open source
- OSS contribution demonstrably builds reputation; inbound attention from maintainer work; few-maintainer projects are abundant; but mainstream niches are crowded. [32][33]

## Adversarial synthesis (step 3 contradiction/consensus)
- **Consensus:** the highest-leverage, constraint-satisfying niches are those where (a) the work is computable on a laptop, (b) contribution is credited to individuals regardless of affiliation, and (c) the contribution type (verification, evaluation, synthesis, taxonomy, benchmark) is durable against AI automation of raw novelty claims.
- **Contradiction/tension:** "purely mathematical novelty" (solving open conjectures) is high-leverage but increasingly auto-attacked by AI; "verification and formalization" is more durable but slower-recognition; "methodology/benchmarks/taxonomy" is durable and recognition-friendly but less prestigious.
