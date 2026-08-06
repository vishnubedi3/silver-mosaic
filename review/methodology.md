# Research Methodology

## Overview

This document describes the research methodology used to produce the monograph *The Laptop-First Theoretical Sciences*.

## Research Question

**Canonical Query:** "Identify the highest-leverage fields where a single independent individual, possessing only an outdated computer and a budget of exactly zero, can make original contributions, answer meaningful open-ended questions, build a public reputation, and remain valuable over the next decade."

## Hard Constraints (Non-Negotiable)

1. **Budget:** ₹0 / $0. No paid software, subscriptions, cloud services, APIs, datasets, courses, certifications, or memberships.
2. **Hardware:** Legacy consumer hardware (≤4-8 GB RAM, dual/quad-core CPU, integrated graphics, mechanical HDD or slow SSD).
3. **Tools:** Free, legal, publicly accessible (FOSS) only.
4. **Credit:** Cognition-first recognition (verification by correctness, not institutional affiliation).

## Evaluation Framework

### Multiplicative Non-Compensatory Gate Model

Fields must satisfy all 4 hard gates to survive elimination:

$$\mathcal{U}_i = \left( \prod_{k=1}^4 G_k(i) \right) \times \sum_{j=1}^{10} w_j \cdot c_{ij}$$

If any gate $G_k(i) = 0$, the field's utility collapses to zero regardless of compensatory scores.

### 10 Weighted Criteria

| # | Criterion | Weight | Description |
|---|---|---|---|
| C1 | Zero Financial Cost | 0.120 | Complete absence of paywalls/fees |
| C2 | Hardware Compatibility | 0.130 | Runs on legacy hardware |
| C3 | Open Problem Volume | 0.120 | Richness of attackable questions |
| C4 | Long-Term Demand | 0.100 | 10-20 year growth outlook |
| C5 | Accessibility | 0.080 | Learning curve and entry barriers |
| C6 | Credential-Agnostic Recognition | 0.120 | Attribution by correctness, not pedigree |
| C7 | Intellectual Leverage | 0.150 | Primary optimization target |
| C8 | AI Durability | 0.070 | Resilience to AI automation |
| C9 | Publication Ease | 0.060 | Diamond OA availability |
| C10 | Toolchain Richness | 0.050 | Free software ecosystem maturity |

### Weight Derivation

Baseline weights were derived using two independent methods:

1. **Analytic Hierarchy Process (AHP):** Pairwise comparison matrix with consistency ratio CR = 0.032
2. **Maximum Entropy Weighting:** Ordinal importance ranks with Lagrange multiplier optimization

Both methods converge within ±3% of the baseline, confirming robustness.

## Data Collection

### Sources

- Peer-reviewed academic literature
- Official documentation (Lean 4, mathlib, arXiv)
- Historical case studies of independent researchers
- Community statistics (GitHub, Lean Zulip, MathOverflow)
- Benchmark results (miniF2F, miniCTX, PutnamBench)

### Verification

- All citations matched to bibliography entries
- Factual claims verified against primary sources
- Mathematical formulas re-derived
- Adversarial review conducted (12-role simulation, 10 passes)

## Sensitivity Analysis

Four weighting profiles were tested:
- **Profile A (Baseline):** Equal emphasis on all criteria
- **Profile B (Accessibility-First):** Prioritizes low barriers to entry
- **Profile C (Depth-First):** Prioritizes intellectual leverage
- **Profile D (AI-Durability-First):** Prioritizes long-term anti-obsolescence

Top-5 cluster invariant across all profiles. Formal Mathematics enters Rank 1 under Profile D.

## Epistemic Standards

Claims are categorized into three tiers:

1. **Established Evidence:** Verified by multiple independent sources, formally proven, or machine-checked.
2. **Strong Inference:** Supported by strong circumstantial evidence, consistent with established theory, but not formally proven.
3. **Reasoned Speculation:** Plausible extrapolation from established evidence, explicitly labeled as uncertain.

## Limitations

- Evaluation is necessarily reductive: complex fields are summarized by 10 criteria
- Weights reflect the canonical query's priorities, not universal values
- AI durability projections are inherently uncertain
- The recommendation is conditional on the AI-durability-prioritized weighting profile
