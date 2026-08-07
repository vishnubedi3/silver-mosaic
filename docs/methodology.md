# Research Methodology Standards

## Overview

This document defines the methodological standards for all research conducted in the Silver Mosaic repository. It ensures reproducibility, traceability, and evidence-driven rigor across all research artifacts.

---

## 1. Research Design Principles

### 1.1 First-Principles Approach
- All analyses begin from fundamental axioms and definitions
- No reliance on unverified assumptions or "common knowledge"
- Every inferential step must be explicitly justified

### 1.2 Multi-Method Triangulation
- Quantitative analysis (bibliometrics, computational experiments)
- Qualitative analysis (literature synthesis, expert knowledge)
- Formal verification (proof assistants, model checking)
- Cross-validation across methods required for high-confidence claims

### 1.3 Adversarial Validation
- Red-team review of all high-confidence claims
- Explicit stress-testing of assumptions
- Crank-avoidance protocol (12 diagnostic rules)
- Sensitivity analysis for all parametric claims

---

## 2. Literature Review Methodology

### 2.1 Systematic Search
- **Databases**: arXiv, PubMed, IEEE Xplore, ACM DL, Google Scholar, Semantic Scholar
- **Search strategy**: Boolean combinations, citation chaining, author tracking
- **Time bounds**: Explicit date ranges with justification
- **Inclusion/exclusion**: Pre-registered criteria

### 2.2 Evidence Grading
| Grade | Description | Weight |
|-------|-------------|--------|
| A | Systematic review / meta-analysis | 1.0 |
| B | Peer-reviewed RCT / controlled experiment | 0.9 |
| C | Peer-reviewed observational / quasi-experimental | 0.7 |
| D | Preprint / working paper (verified) | 0.5 |
| E | Technical report / white paper | 0.4 |
| F | Blog post / informal communication | 0.2 |
| X | Unverified / anecdotal | 0.0 |

### 2.3 Citation Management
- All citations tracked in bibliography with evidence grades
- DOI/URL verified at time of inclusion
- Version control for preprints (arXiv version numbers)
- Paywall status noted

---

## 3. Computational Research Standards

### 3.1 Environment Specification
```yaml
# Required in every computational artifact
environment:
  os: "Ubuntu 22.04 / macOS 13+ / Windows 11"
  python: "3.10+"
  dependencies: requirements.txt / environment.yml / Dockerfile
  hardware: "CPU: x86-64, RAM: ≥8GB, GPU: optional"
  runtime: "Expected wall-clock time"
  seeds: "All random seeds documented"
```

### 3.2 Reproducibility Requirements
- **Deterministic**: Fixed seeds, pinned dependencies, containerized
- **Verifiable**: Expected outputs provided, validation scripts included
- **Portable**: Runs on standard hardware (≤8GB RAM, no GPU required)
- **Documented**: Step-by-step reproduction instructions

### 3.3 Code Quality
- Type hints (Python 3.10+)
- Docstrings for all public functions
- Unit tests for core algorithms (≥80% coverage)
- Static analysis (mypy, ruff, pylint)

---

## 4. Formal Verification Standards

### 4.1 Proof Assistant Requirements
- **Primary**: Lean 4 (mathlib4)
- **Acceptable**: Coq, Isabelle/HOL, Agda
- **Kernel**: Minimal trusted code base documented
- **Dependencies**: mathlib version pinned

### 4.2 Formalization Standards
- **Definitions**: Faithful to mathematical source
- **Theorems**: Complete statements with all assumptions explicit
- **Proofs**: `sorry`-free for core claims
- **Documentation**: Lean 4 doc comments for all public APIs

### 4.3 Verification Artifacts
- `.lean` files in `formal/` directory
- `lake` build configuration
- CI: `lake build` passes on every commit
- Export: Proof terms, dependency graphs

---

## 5. Quantitative Analysis Standards

### 5.1 Statistical Rigor
- Pre-registered hypotheses where possible
- Multiple comparison correction (Bonferroni, FDR)
- Effect sizes with confidence intervals
- Power analysis for negative results

### 5.2 Sensitivity Analysis
- All parametric claims require:
  - Baseline parameter values with sources
  - ±20% perturbation (or domain-appropriate range)
  - Threshold analysis (where conclusions flip)
  - Visualization of stability regions

### 5.3 Uncertainty Quantification
- Aleatoric vs epistemic uncertainty separated
- Monte Carlo / bootstrap for complex distributions
- Credible intervals for Bayesian analyses
- Clear distinction: statistical vs practical significance

---

## 6. Qualitative Analysis Standards

### 6.1 Thematic Analysis
- Coding framework pre-registered or iteratively developed with audit trail
- Inter-coder reliability (κ ≥ 0.8) for multi-coder studies
- Negative case analysis required
- Reflexivity statement from analysts

### 6.2 Expert Elicitation
- Structured protocols (Delphi, AHP, Cooke's method)
- Calibration questions for expert weighting
- Transparency: selection criteria, conflicts of interest
- Aggregation method justified

---

## 7. Formal Argumentation Standards

### 7.1 Argument Structure
```
Claim
├── Premise 1 (source: [citation])
├── Premise 2 (source: [citation])
├── Inference Rule (deductive/inductive/abductive)
└── Conclusion (with confidence level)
```

### 7.2 Confidence Levels
| Level | Description | Threshold |
|-------|-------------|-----------|
| Certain | Formal proof / mathematical necessity | 1.0 |
| Very High | Multiple independent replications | 0.95 |
| High | Strong convergent evidence | 0.85 |
| Moderate | Single strong study / formal verification | 0.70 |
| Low | Preliminary / single source | 0.50 |
| Speculative | Hypothesis / conjecture | < 0.50 |

### 7.3 Adversarial Review
- Every claim ≥ Moderate confidence requires red-team review
- Steelman strongest counterarguments
- Document: failed attempts to falsify
- Update confidence based on review outcome

---

## 8. Version Control & Traceability

### 8.1 Artifact Versioning
- Manuscript: Semantic versioning (Major.Minor.Patch)
- Code: Git tags matching manuscript versions
- Data: Immutable snapshots with checksums
- Formal proofs: mathlib version + commit hash

### 8.2 Change Tracking
- Every factual change: evidence + citation diff
- Every methodological change: rationale + impact assessment
- Every confidence update: review record + new evidence

---

## 9. Quality Gates

### 9.1 Pre-Commit (Automated)
- [ ] UTF-8 encoding valid
- [ ] Citation format valid
- [ ] Cross-references resolve
- [ ] No mojibake / encoding artifacts
- [ ] Markdown lint passes

### 9.2 Pre-Merge (Manual + Automated)
- [ ] Evidence provided for all new claims
- [ ] Citations verified accessible
- [ ] Computational results reproduced
- [ ] Formal proofs build (`lake build`)
- [ ] Cross-references valid
- [ ] Confidence levels calibrated
- [ ] Speculative content marked

### 9.3 Publication (Major Version)
- [ ] Full adversarial review complete
- [ ] All citations verified (spot-check 20%+)
- [ ] Reproducibility confirmed by independent party
- [ ] Sensitivity analysis complete
- [ ] Documentation synchronized

---

## 10. Continuous Improvement

### 10.1 Methodology Reviews
- Quarterly methodology retrospectives
- Update standards based on:
  - New tooling (better verification, analysis)
  - Community best practices
  - Failed replications / errors discovered
  - Contributor feedback

### 10.2 Metrics Tracking
- Citation verification rate
- Reproducibility success rate
- Adversarial review findings
- Time-to-evidence for claims

---

## Appendix: Methodology Checklist Template

```markdown
## Methodology Checklist for: [Claim/Analysis ID]

### Design
- [ ] Research question precisely formulated
- [ ] Hypotheses pre-registered (if confirmatory)
- [ ] Methods selected with justification

### Evidence
- [ ] All sources cited with evidence grades
- [ ] Paywall status noted
- [ ] Preprint versions pinned

### Computation
- [ ] Environment specified
- [ ] Seeds documented
- [ ] Reproduction verified

### Formal
- [ ] Definitions faithful
- [ ] Theorems complete
- [ ] Proofs sorry-free
- [ ] Build passes

### Analysis
- [ ] Sensitivity analysis complete
- [ ] Uncertainty quantified
- [ ] Confidence levels calibrated

### Review
- [ ] Self-review complete
- [ ] Adversarial review scheduled
- [ ] Confidence updated post-review

### Documentation
- [ ] Methodology documented
- [ ] Limitations stated
- [ ] Data/code availability declared
```