# Repository Map

## Directory Structure

```
silver-mosaic/
│
├── manuscript/                          # PRIMARY DELIVERABLE
│   └── final-report.md                  # The complete monograph (7,897 lines)
│                                        # Revision 6 - Second-Pass Expansion
│
├── review/                              # QUALITY ASSURANCE
│   ├── adversarial-review.md            # 12-role adversarial audit (28 findings)
│   └── methodology.md                   # Research methodology documentation
│
├── data/                                # RESEARCH ARTIFACTS
│   ├── query.md                         # Canonical research prompt (verbatim)
│   ├── scaffold.md                      # Run configuration and tier rationale
│   ├── run-manifest.json                # Pipeline status manifest
│   ├── prompt-decomposition.json        # Sub-questions, entities, required sections
│   ├── audit-findings.json              # Audit ledger
│   ├── citation-check.json              # Citation verification log
│   ├── patch-log.json                   # Applied patch ledger
│   ├── polish-log.json                  # Quality hygiene log
│   ├── readability-decisions.json       # Readability audit decisions
│   └── readability-recommendations.json # Readability improvement recommendations
│
├── archive/                             # HISTORICAL (non-authoritative)
│   ├── ARCHIVE-INDEX.md                 # Archive governance policy
│   ├── v1-final-report.md              # Superseded initial draft
│   ├── coverage-matrix.md              # Superseded coverage analysis
│   ├── evidence-digest.md              # Superseded evidence synthesis
│   └── search-plan.md                  # Superseded search methodology
│
├── docs/                                # DOCUMENTATION
│   └── repository-map.md               # This file
│
├── README.md                            # Project overview and quick start
├── CONTRIBUTING.md                      # Contribution guidelines
├── LICENSE                              # Apache 2.0
└── .gitignore                           # Standard ignores
```

## File Descriptions

### manuscript/

| File | Description | Size |
|---|---|---|
| `final-report.md` | Complete 25-chapter, 5-volume research monograph recommending Formal Mathematics (Lean 4) as the optimal zero-budget field | ~7,900 lines, ~87,000 words |

### review/

| File | Description |
|---|---|
| `adversarial-review.md` | Multi-pass adversarial audit report with 8 Critical, 11 Major, 9 Minor findings |
| `methodology.md` | Research methodology, evaluation framework, and epistemic standards |

### data/

| File | Description |
|---|---|
| `query.md` | Verbatim canonical research prompt |
| `scaffold.md` | Run configuration, tier rationale, and scope conditions |
| `run-manifest.json` | Pipeline status and completion tracking |
| `prompt-decomposition.json` | Sub-questions, entity list, required sections |
| `audit-findings.json` | Audit ledger with finding counts |
| `citation-check.json` | Citation verification results |
| `patch-log.json` | Applied patch history |
| `polish-log.json` | Quality hygiene log |
| `readability-decisions.json` | Readability audit decisions |
| `readability-recommendations.json` | Readability improvement recommendations |

### archive/

| File | Description | Status |
|---|---|---|
| `ARCHIVE-INDEX.md` | Archive governance policy and inventory | ARCHIVED |
| `v1-final-report.md` | Initial preliminary draft (superseded) | ARCHIVED |
| `coverage-matrix.md` | Pipeline step 1 decomposition (superseded) | ARCHIVED |
| `evidence-digest.md` | Interim synthesis digest (superseded) | ARCHIVED |
| `search-plan.md` | Search plan and evidence records (superseded) | ARCHIVED |

## Document Relationships

```
query.md (canonical prompt)
    │
    ▼
scaffold.md (run configuration)
    │
    ▼
prompt-decomposition.json (sub-questions, entities)
    │
    ▼
final-report.md (main deliverable)
    │
    ├──▲── adversarial-review.md (quality audit)
    │
    ├──▲── audit-findings.json (audit ledger)
    │
    └──▲── citation-check.json (citation verification)
```

## Version History

| Version | Date | Description |
|---|---|---|
| v1 | 2026-08-05 | Initial draft (superseded) |
| v4 | 2026-08-06 | Adversarially audited revision (superseded) |
| v5 | 2026-08-06 | First-principles rebuild (superseded) |
| v6 | 2026-08-06 | Second-pass expansion (current) |
