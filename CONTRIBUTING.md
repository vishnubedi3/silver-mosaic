# Contributing to Silver Mosaic

## Research Contribution Standards

This repository maintains high standards for research quality, traceability, and evidence-driven contributions. All contributors must adhere to the following standards.

---

## 1. Evidence Requirements

### Factual Changes
- **Every factual claim must be accompanied by a verifiable source**
- Acceptable sources: peer-reviewed publications, official documentation, reproducible computational results, primary sources
- Unacceptable sources: unattributed claims, hearsay, AI-generated content without verification
- Format: `[Author, Year]` or `[Source URL]` inline; full citation in bibliography

### New Research Contributions
- Must include: methodology description, data sources, computational environment, reproduction instructions
- Computational results must be reproducible with provided code/data
- Statistical claims require: sample size, confidence intervals, p-values, effect sizes

---

## 2. Citation Standards

### Required Citations
- All new factual claims in manuscript files (`manuscript/*.md`)
- All new entries in bibliography (`manuscript/final-report.md` bibliography section)
- All methodological assertions in `docs/methodology.md`

### Citation Format
```
[Author, Year] for inline citations
Full bibliographic entry in bibliography section
DOI/URL when available
```

### Citation Quality
- Prefer primary sources over secondary
- Verify all citations resolve to accessible content
- Flag paywalled sources with `[paywall]` note
- Preprint servers (arXiv, bioRxiv) acceptable with version date

---

## 3. Reproducible Methodology

### Computational Research
- All code must be in `code/` or `notebooks/` directories
- Include: `requirements.txt` / `environment.yml` / `Dockerfile`
- Document: hardware requirements, runtime, random seeds
- Provide: expected outputs, validation criteria

### Analytical Research
- Document: assumptions, derivation steps, boundary conditions
- Provide: mathematical proofs in LaTeX or Lean 4 formalization
- Link: to formal verification artifacts where applicable

### Data Research
- Raw data in `data/raw/` (or reference to public repository)
- Processed data in `data/processed/` with processing scripts
- Data dictionaries and schema documentation

---

## 4. Content Classification

### Verified Content ✅
- Peer-reviewed publications with citations
- Reproduced computational results with code
- Formal proofs (Lean 4, Coq, Isabelle)
- Official documentation with version numbers

### Speculative Content ⚠️
- Must be clearly marked with `[SPECULATIVE]` tag
- Hypotheses, conjectures,未经证实的 claims
- AI-generated content without human verification
- Forward-looking statements without citations

### Separation Rules
- Verified content in main manuscript sections
- Speculative content in dedicated "Future Work" / "Speculative Analysis" subsections
- Never mix verified and speculative claims without clear demarcation

---

## 5. Contribution Workflow

### Brainstorming → GitHub Discussions
- Use **GitHub Discussions** for:
  - Research direction exploration
  - Methodology design debates
  - Literature survey coordination
  - Preliminary hypothesis formation
- Tag with: `research`, `methodology`, `literature`, `hypothesis`

### Actionable Work → GitHub Issues
- Use **GitHub Issues** for:
  - Specific manuscript edits with evidence
  - Citation additions/verification
  - Code implementation tasks
  - Reproduction attempts
- Template required: evidence, scope, acceptance criteria
- Labels: `evidence-required`, `citation-needed`, `reproduction`, `editorial`

### Pull Requests
- All changes via PR with:
  - Evidence summary (what changed, why, sources)
  - Citation diff (added/removed/modified)
  - Reproducibility verification (if computational)
  - Editorial review checklist completion

---

## 6. Documentation Standards

### Required Documentation (`docs/`)
```
docs/
├── methodology.md          # Research methodology standards
├── editorial-standards.md  # Writing, citation, formatting rules
├── citation-guide.md       # Citation format, tools, verification
├── reproducibility.md      # Computational reproduction guides
├── content-classification.md # Verified vs speculative guidelines
└── glossary.md             # Domain-specific terminology
```

### Documentation Requirements
- All `.md` files use consistent formatting (see `editorial-standards.md`)
- Cross-references between methodology and manuscript
- Version-controlled with manuscript revisions
- Updated with each major revision

---

## 7. Automation (GitHub Actions)

### Required Checks
```yaml
# .github/workflows/quality.yml
- Link checking (all internal/external URLs)
- Citation format validation
- Markdown linting
- Bibliography consistency (cited ↔ bibliography)
- Cross-reference validation (section numbers, figure numbers)
- Spell checking (technical dictionary)
- Encoding validation (UTF-8, no mojibake)
```

### Pre-commit Hooks
- Citation format check
- Trailing whitespace removal
- Line ending normalization (LF)

---

## 8. Review Process

### Minimum Reviews
- **Factual changes**: 1 domain expert + 1 editor
- **Citation changes**: 1 citation verifier
- **Computational changes**: 1 reproducer
- **Editorial changes**: 1 editor

### Review Checklist
- [ ] Evidence provided for all factual claims
- [ ] Citations verified and formatted correctly
- [ ] Speculative content clearly marked
- [ ] Reproducibility confirmed (if applicable)
- [ ] Cross-references valid
- [ ] No encoding issues
- [ ] Automated checks pass

---

## 9. Version Control

### Commit Messages
```
type(scope): brief description

- Evidence: [source]
- Citations: [added/removed/modified]
- Verification: [method]
```
Types: `feat`, `fix`, `docs`, `refactor`, `evidence`, `citation`, `repro`

### Branching
- `main`: publication-ready revisions only
- `feat/*`: evidence-backed feature branches
- `fix/*`: citation/editorial fixes
- `repro/*`: computational reproduction attempts

---

## 10. Enforcement

### Automated Enforcement
- PRs failing automated checks cannot merge
- Unverified factual claims flagged by `evidence-required` label
- Uncited claims flagged by `citation-needed` label

### Manual Enforcement
- Maintainers verify evidence quality
- Editors enforce style and classification standards
- Domain experts validate technical accuracy

---

## Quick Reference

| Action | Where | Evidence Required |
|--------|-------|-------------------|
| New factual claim | Manuscript | Citation + source |
| New citation | Bibliography | Verified accessible |
| Computational result | Code/notebook | Reproduction instructions |
| Speculative hypothesis | Discussion → Issue | Marked `[SPECULATIVE]` |
| Editorial fix | PR | Style guide compliance |
| Methodology change | `docs/methodology.md` | Consensus + documentation |

---

## Contact

For questions about contribution standards:
- Open a **GitHub Discussion** with label `contribution-standards`
- Reference this document: `CONTRIBUTING.md`
- Maintainers: @vishnubedi3

---

*Last updated: 2026-08-07 | Version 1.0 | Aligned with manuscript Revision 6*