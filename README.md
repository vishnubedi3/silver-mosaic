# Silver Mosaic Research Repository

> **The Laptop-First Theoretical Sciences: An Exhaustive Research Monograph on Maximizing Independent Intellectual Leverage Under Zero-Capital Constraints**

[![Quality Checks](https://github.com/vishnubedi3/silver-mosaic/actions/workflows/quality.yml/badge.svg)](https://github.com/vishnubedi3/silver-mosaic/actions/workflows/quality.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## Overview

This repository contains the **Silver Mosaic** research monograph: a comprehensive, evidence-driven analysis identifying the highest-leverage theoretical fields for independent researchers operating with zero financial capital and legacy hardware.

**Headline Finding**: Under strict zero-budget (₹0/$0) and legacy hardware constraints, **Formal Mathematics & Proof Formalization (Lean 4 / mathlib)** achieves the highest durable, credential-agnostic scientific recognition (Score: 9.13 under AI-durability prioritization), defended over Information Theory (9.07) and Theoretical CS (9.03).

## Repository Structure

```
silver-mosaic/
├── manuscript/
│   └── final-report.md          # Primary deliverable (Revision 6, 7,902 lines)
├── review/
│   ├── editorial-audit-report.md      # Adversarial editorial audit findings
│   └── citation-verification-report.md # Citation coverage analysis
├── docs/
│   ├── methodology.md          # Research methodology standards
│   ├── editorial-standards.md  # Writing & formatting guidelines
│   ├── citation-guide.md       # Citation format & verification
│   ├── reproducibility.md      # Computational reproducibility standards
│   ├── content-classification.md # V1-V4 content confidence taxonomy
│   └── glossary.md             # Authoritative term definitions
├── scripts/
│   ├── verify-citations.py     # Citation format & coverage check
│   ├── check-encoding.py       # UTF-8 & mojibake validation
│   ├── check-crossrefs.py      # Section/figure/table reference validation
│   ├── check-classification.py # Content confidence taxonomy compliance
│   ├── check-dois.py           # DOI/URL accessibility verification
│   └── check-mojibake.py       # Encoding artifact detection
├── .github/workflows/
│   └── quality.yml             # CI/CD quality gates
├── CONTRIBUTING.md             # Evidence-driven contribution standards
├── requirements.txt            # Python dependencies
├── pyproject.toml              # Project configuration
└── .markdownlint.json          # Markdown linting rules
```

## Key Features

- **Evidence-Driven**: Every factual claim traced to verifiable sources
- **Reproducible**: All computational claims run on standard hardware (≤8GB RAM)
- **Formally Verified**: Core claims formalized in Lean 4 / mathlib
- **Adversarially Audited**: Red-team review of all high-confidence claims
- **Transparent Classification**: V1-V4 confidence taxonomy (VERIFIED → SPECULATIVE)

## Quick Start

```bash
# Clone repository
git clone https://github.com/vishnubedi3/silver-mosaic
cd silver-mosaic

# Set up environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run quality checks
python scripts/verify-citations.py manuscript/final-report.md
python scripts/check-encoding.py manuscript/final-report.md
python scripts/check-crossrefs.py manuscript/final-report.md
python scripts/check-classification.py manuscript/final-report.md
```

## Quality Gates (CI/CD)

All PRs must pass:
- ✅ Editorial standards (markdownlint, cspell, link checking)
- ✅ Citation verification (format, coverage, DOI accessibility)
- ✅ Encoding validation (UTF-8, no mojibake)
- ✅ Cross-reference integrity
- ✅ Content classification compliance
- ✅ Lean 4 formal verification (if applicable)

## Contribution Standards

See [CONTRIBUTING.md](CONTRIBUTING.md) for evidence-driven contribution guidelines:
- Require evidence for factual changes
- Require citations for new research
- Require reproducible methodology
- Separate speculative content from verified content
- Use GitHub Discussions for brainstorming, Issues for actionable work

## Manuscript Access

- **Primary**: `manuscript/final-report.md` (Revision 6)
- **GitHub**: View rendered markdown on GitHub
- **Raw**: Download for offline reading

## License

MIT License - see [LICENSE](LICENSE) for details.

## Citation

```bibtex
@techreport{silver-mosaic-2026,
  title = {The Laptop-First Theoretical Sciences: An Exhaustive Research Monograph on Maximizing Independent Intellectual Leverage Under Zero-Capital Constraints},
  author = {Silver Mosaic Research Team},
  institution = {Independent Research},
  year = {2026},
  month = {August},
  note = {Revision 6, 7,902 lines, 137 citations},
  url = {https://github.com/vishnubedi3/silver-mosaic}
}
```

## Contact

- **Issues**: [GitHub Issues](https://github.com/vishnubedi3/silver-mosaic/issues) (actionable work)
- **Discussions**: [GitHub Discussions](https://github.com/vishnubedi3/silver-mosaic/discussions) (brainstorming, methodology)
- **Maintainer**: @vishnubedi3

---

*Last updated: 2026-08-07 | Revision 6 | Aligned with manuscript standards*