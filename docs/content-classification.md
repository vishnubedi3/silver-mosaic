# Content Classification Guide

## Overview

This guide defines how to classify, label, and separate verified content from speculative content in the Silver Mosaic repository. Clear demarcation ensures intellectual honesty and helps readers assess confidence levels.

---

## 1. Classification Taxonomy

### 1.1 Four-Tier Classification System

| Tier | Label | Confidence | Criteria | Examples |
|------|-------|------------|----------|----------|
| **V1** | `VERIFIED` | 1.0 | Formal proof / mathematical necessity / multiple independent replications | Lean 4 theorems, Shannon's theorems, Feit-Thompson |
| **V2** | `HIGH CONFIDENCE` | 0.85–0.95 | Strong convergent evidence, formal verification, single strong study | AlphaProof IMO results, mathlib statistics, verified compiler |
| **V3** | `MODERATE CONFIDENCE` | 0.70–0.84 | Single strong study, formal verification of subset, expert consensus | Scoring model weights, hardware viability assessments |
| **V4** | `SPECULATIVE` | < 0.70 | Hypotheses, conjectures, forward-looking, single source, AI-generated | 10-20 year predictions, AI timeline forecasts, crank-avoidance efficacy |

### 1.2 Visual Indicators

| Tier | Inline Tag | Section Header | Confidence Bar |
|------|------------|----------------|----------------|
| V1 | `✅ VERIFIED` | `## Verified Results` | `████████████ 100%` |
| V2 | `✅ HIGH CONFIDENCE` | `## High-Confidence Findings` | `███████████░ 90%` |
| V3 | `⚠️ MODERATE` | `## Moderate-Confidence Analysis` | `████████░░░░ 75%` |
| V4 | `🔮 SPECULATIVE` | `## Speculative Projections` | `████░░░░░░░ 50%` |

---

## 2. Classification Rules

### 2.1 Mandatory Classification
Every factual claim in manuscript files must carry an explicit or implicit classification:
- **Explicit**: Inline tag `[VERIFIED]`, `[HIGH CONFIDENCE]`, `[MODERATE]`, `[SPECULATIVE]`
- **Implicit**: Section-level classification applies to all claims within

### 2.2 Section-Level Classification
```markdown
## Verified Results {#verified}

All claims in this section are **VERIFIED** unless explicitly marked otherwise.

### 1.1 Formal Proof of Theorem X
[VERIFIED] Theorem X has been formalized in Lean 4 without sorries.

## Speculative Projections {#speculative}

All claims in this section are **SPECULATIVE** and represent hypotheses.

### 5.1 AI Timeline Forecast
[SPECULATIVE] AGI may arrive by 2030 based on scaling trends.
```

### 2.3 Inline Classification (When Mixing)
```markdown
The Feit-Thompson theorem is formalized in Lean 4 [VERIFIED]. 
However, the full classification of finite simple groups remains [SPECULATIVE] for complete formalization.
```

---

## 3. Criteria for Each Tier

### 3.1 VERIFIED (1.0)
**Required**: ALL of the following
- [ ] Formal proof in Lean 4/Coq/Isabelle WITHOUT sorries
- [ ] OR mathematical necessity (tautology, definitional truth)
- [ ] OR multiple (≥3) independent replications with identical results
- [ ] Source code/artifacts publicly available and reproducible
- [ ] No dependence on unverified assumptions

**Examples**:
- `2 + 2 = 4` (definitional)
- `√2 is irrational` (Lean 4 proof)
- `Feit-Thompson theorem` (Lean 4 formalization complete)
- `Shannon's channel coding theorem` (multiple textbook proofs)

### 3.2 HIGH CONFIDENCE (0.85–0.95)
**Required**: ALL of the following
- [ ] Formal verification of core claims (may have sorries in periphery)
- [ ] OR single strong study with rigorous methodology + independent audit
- [ ] OR expert consensus with documented methodology
- [ ] Reproducible computational results (seeds, env documented)
- [ ] Sensitivity analysis shows robustness (±20% params)

**Examples**:
- AlphaProof solving 3/5 IMO 2024 problems (Nature 2025)
- mathlib 4.9.0 statistics (134K defs, 283K theorems, 772 contributors)
- Lean 4 kernel ~3-5K LOC verified independently
- Verified compiler CompCert (formal semantic preservation)

### 3.3 MODERATE CONFIDENCE (0.70–0.84)
**Required**: AT LEAST 2 of the following
- [ ] Formal verification of subset (core lemmas proven)
- [ ] Strong single study with good methodology
- [ ] Expert consensus (documented, with weights)
- [ ] Reproducible computation (with caveats)
- [ ] Sensitivity analysis partially complete

**Examples**:
- Scoring model weights derived via AHP + MaxEnt (methodology documented)
- Hardware viability assessments (based on spec sheets + user reports)
- Bibliometric analysis (based on available APIs, with coverage limits)
- Cost estimates (based on current pricing, subject to change)

### 3.4 SPECULATIVE (< 0.70)
**Any of the following triggers this tier**:
- [ ] Forward-looking prediction (>1 year horizon)
- [ ] Single source without independent verification
- [ ] AI-generated content without human expert review
- [ ] Hypothesis/conjecture not yet tested
- [ ] Dependence on unverified assumptions
- [ ] Extrapolation beyond data range
- [ ] "Expert opinion" without structured elicitation

**Examples**:
- "AGI by 2030" (scaling law extrapolation)
- "Lean 4 will dominate theorem proving by 2030" (market forecast)
- "Crank-avoidance protocol eliminates 90% of pseudoscience" (untested)
- "AI will formalize 90% of mathlib by 2028" (scaling projection)

---

## 4. Implementation in Documents

### 4.1 Manuscript (`manuscript/final-report.md`)
- Section-level classification headers
- Inline tags for mixed-content paragraphs
- Confidence bars in executive summary
- Appendix: Complete classification table

### 4.2 Research Notebooks (`notebooks/`)
```python
# Cell marker
# [VERIFIED] This result reproduces exactly
result = compute_verified()

# [SPECULATIVE] This projection assumes continued scaling
projection = extrapolate(scaling_law, years=10)
```

### 4.3 Code Comments
```python
# VERIFIED: This algorithm matches published result exactly
def verified_algorithm():
    ...

# SPECULATIVE: Heuristic not yet validated
def experimental_heuristic():
    ...
```

### 4.4 GitHub Issues/PRs
```markdown
## Classification: [SPECULATIVE]
This PR adds a projection for 2030 AI capabilities based on...

## Classification: [VERIFIED]
This PR formalizes Theorem X in Lean 4 without sorries...
```

---

## 5. Visual Design System

### 5.1 Confidence Badges
```markdown
![VERIFIED](https://img.shields.io/badge/VERIFIED-brightgreen)
![HIGH CONFIDENCE](https://img.shields.io/badge/HIGH_CONFIDENCE-green)
![MODERATE](https://img.shields.io/badge/MODERATE-yellow)
![SPECULATIVE](https://img.shields.io/badge/SPECULATIVE-orange)
```

### 5.2 Confidence Bars (Text)
```
VERIFIED:        ████████████████████ 100%
HIGH CONFIDENCE: ██████████████████░░  90%
MODERATE:        ████████░░░░░░░░░░░░  75%
SPECULATIVE:     ████░░░░░░░░░░░░░░░░  40%
```

### 5.3 Inline Tags
```
[✅ VERIFIED]           → Green checkmark
[✅ HIGH CONFIDENCE]    → Green checkmark
[⚠️ MODERATE]           → Yellow warning
[🔮 SPECULATIVE]        → Crystal ball
```

---

## 6. Upgrading/Downgrading Classifications

### 6.1 Upgrade Path
```
SPECULATIVE → MODERATE → HIGH CONFIDENCE → VERIFIED
```

**Requirements for upgrade**:
| From → To | Evidence Required |
|-----------|-------------------|
| SPECULATIVE → MODERATE | Preliminary empirical validation OR expert elicitation |
| MODERATE → HIGH CONFIDENCE | Formal verification of core OR independent replication |
| HIGH CONFIDENCE → VERIFIED | Complete formal proof OR ≥3 independent replications |

### 6.2 Downgrade Triggers
- Failed replication attempt
- Discovered error in methodology
- New evidence contradicting claim
- Assumption proven false
- Sorries discovered in formal proof

**Process**: 
1. Open GitHub Issue with `downgrade` label
2. Document evidence for downgrade
3. Update all affected sections
4. Notify dependent claims

---

## 7. Separation in Practice

### 7.1 Document Structure Template
```markdown
# Title

## Abstract
[Overall classification: HIGH CONFIDENCE with SPECULATIVE projections in §5]

## 1. Verified Foundations {#verified}
All claims VERIFIED.

### 1.1 Theorem A
[VERIFIED] Proof in Lean 4.

## 2. High-Confidence Results {#high-conf}
All claims HIGH CONFIDENCE.

### 2.1 Empirical Finding B
[HIGH CONFIDENCE] Reproduced 5× with seeds.

## 3. Moderate Analysis {#moderate}
All claims MODERATE CONFIDENCE.

### 3.1 Model C
[MODERATE] Sensitivity analysis shows ±15% stability.

## 4. Speculative Extensions {#speculative}
All claims SPECULATIVE.

### 4.1 Future Projection D
[SPECULATIVE] Based on scaling law extrapolation.

## Appendix: Classification Summary
| Section | Classification | Key Claims |
|---------|---------------|------------|
| 1 | VERIFIED | Theorem A, Lemma B |
| 2 | HIGH CONFIDENCE | Finding B, Result C |
| 3 | MODERATE | Model C, Estimate D |
| 4 | SPECULATIVE | Projection D, Forecast E |
```

### 7.2 Mixed-Content Paragraphs
```markdown
The kernel size is 3,000–5,000 lines [VERIFIED], 
which makes formal verification tractable [HIGH CONFIDENCE].
However, the broader compiler is substantially larger [MODERATE],
and full end-to-end verification remains [SPECULATIVE].
```

---

## 8. Review Process

### 8.1 Classification Review Checklist
- [ ] Every claim has explicit or inherited classification
- [ ] Section-level classification declared
- [ ] Inline tags for mixed content
- [ ] Confidence bars in executive summary
- [ ] Appendix table complete and accurate
- [ ] No unverified claims masquerading as verified
- [ ] Speculative content clearly demarcated

### 8.2 Reviewer Responsibilities
| Role | Check |
|------|-------|
| Domain Expert | Technical accuracy of VERIFIED/HIGH claims |
| Methodologist | Classification criteria applied correctly |
| Editor | Visual indicators, formatting, consistency |
| Reproducer | Computational claims reproducible |

---

## 9. Automation

### 9.1 Validation Scripts
```python
# scripts/check_classification.py
import re

REQUIRED_TAGS = ["VERIFIED", "HIGH CONFIDENCE", "MODERATE", "SPECULATIVE"]

def check_classification(filepath):
    with open(filepath) as f:
        content = f.read()
    
    # Check section-level classification
    sections = re.findall(r'^##\s+(.+)\s*\{#(\w+)\}', content, re.MULTILINE)
    classified_sections = [s for s in sections if any(t in s[0] for t in REQUIRED_TAGS)]
    
    # Check inline tags
    inline_tags = re.findall(r'\[(VERIFIED|HIGH CONFIDENCE|MODERATE|SPECULATIVE)\]', content)
    
    # Report
    print(f"Sections: {len(sections)}, Classified: {len(classified_sections)}")
    print(f"Inline tags: {len(inline_tags)}")
    print(f"Tag distribution: {Counter(inline_tags)}")
```

### 9.2 CI Integration
```yaml
# .github/workflows/classification.yml
- name: Check classifications
  run: python scripts/check_classification.py manuscript/final-report.md
```

---

## 10. Examples from Current Manuscript

| Claim | Current Classification | Evidence |
|-------|----------------------|----------|
| Lean 4 kernel ~3-5K LOC | VERIFIED | Lean 4 source, independent audits |
| mathlib 134K defs, 283K thms | HIGH CONFIDENCE | mathlib stats page, reproducible |
| AlphaProof IMO 2024 silver | HIGH CONFIDENCE | Nature 2025, reproducible |
| 10-20 year demand forecasts | MODERATE | Sensitivity analysis, expert weights |
| AGI by 2030 | SPECULATIVE | Scaling law extrapolation |
| Crank-avoidance efficacy | SPECULATIVE | Untested protocol |
| Lean 4 dominance by 2030 | SPECULATIVE | Market projection |

---

## 11. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-08-07 | Initial release aligned with manuscript Rev 6 |