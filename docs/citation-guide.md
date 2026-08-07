# Citation Guide

## Overview

This guide provides detailed standards for citing sources in the Silver Mosaic repository. It covers citation formats, verification procedures, tools, and best practices.

---

## 1. Citation Philosophy

### 1.1 Principles
- **Traceability**: Every factual claim traceable to a verifiable source
- **Accessibility**: Prefer open-access sources; note paywalls
- **Precision**: Cite specific pages/sections, not entire works
- **Currency**: Prefer recent sources for rapidly evolving fields
- **Diversity**: Balance foundational works with recent advances

### 1.2 Citation Hierarchy
1. **Primary sources**: Original research, official docs, formal proofs
2. **Secondary sources**: Reviews, surveys, textbooks (for established knowledge)
3. **Tertiary sources**: Encyclopedias, overviews (only for background)
4. **Gray literature**: Preprints, technical reports, theses (with grade)

---

## 2. Citation Formats by Source Type

### 2.1 Journal Articles
```
[Number] Author, A., Author, B., & Author, C. (Year). "Title." *Journal Name*, Volume(Issue), Page–Page. DOI: 10.xxxx/xxxxx
```
**Example:**
```
[1] Shannon, C. E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*, 27(3), 379–423. DOI: 10.1002/j.1538-7305.1948.tb01338.x
```

### 2.2 Conference Papers
```
[Number] Author, A. & Author, B. (Year). "Title." *Proceedings of Conference Name*, Page–Page. DOI: 10.xxxx/xxxxx
```
**Example:**
```
[2] Cook, S. A. (1971). "The Complexity of Theorem-Proving Procedures." *Proceedings of STOC '71*, 151–158. DOI: 10.1145/800157.805047
```

### 2.3 Preprints (arXiv, bioRxiv, etc.)
```
[Number] Author, A., Author, B., & Author, C. (Year). "Title." *arXiv:YYMM.NNNNN [cs.CC]*. Version N.
```
**Example:**
```
[3] AlphaProof Team. (2025). "Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning." *arXiv:2502.07640 [cs.AI]*. Version 2.
```

### 2.4 Technical Reports / White Papers
```
[Number] Organization. (Year). "Title." *Report Series*, Report Number. URL
```
**Example:**
```
[4] National Security Agency. (2019–2024). "Ghidra Software Reverse Engineering Framework." *NSA Research Directorate*. https://ghidra-sre.org
```

### 2.5 Software / Code Repositories
```
[Number] Organization. (Year). "Title." *Repository Name*. Version X.Y.Z. URL
```
**Example:**
```
[5] Lean FRO. (2024). "Reservoir: The Lean Package Registry." *GitHub: leanprover/reservoir*. v1.2.3. https://github.com/leanprover/reservoir
```

### 2.6 Datasets
```
[Number] Author/Org. (Year). "Title." *Repository*. Version. DOI/URL
```
**Example:**
```
[6] Sloane, N. J. A. & The OEIS Foundation. (2024). "The On-Line Encyclopedia of Integer Sequences." *OEIS*. https://oeis.org
```

### 2.7 Theses / Dissertations
```
[Number] Author, A. (Year). "Title." *Degree Type Thesis*, Institution. URL
```
**Example:**
```
[7] Carneiro, M. (2019). "The Type Theory of Lean." *Master's Thesis*, Carnegie Mellon University. https://github.com/mcarneiro/lean-type-theory
```

### 2.8 Books / Monographs
```
[Number] Author, A. (Year). *Title*. Edition. Publisher. DOI/ISBN
```
**Example:**
```
[8] Tao, T. (2016). *The Erdos Discrepancy Problem*. Discrete Analysis, 2016:1, 29 pp. DOI: 10.19086/da.614
```

### 2.9 Online Resources (Documentation, Blogs, etc.)
```
[Number] Author/Org. (Year). "Title." *Source*. URL (accessed YYYY-MM-DD)
```
**Example:**
```
[9] The Lean Community. (2024). "mathlib Statistics." *leanprover-community.github.io/mathlib_stats.html*. https://leanprover-community.github.io/mathlib_stats.html (accessed 2026-08-07)
```

### 2.10 Personal Communications
```
[Number] Author, A. (Year). Personal communication.
```
**Example:**
```
[10] A. Researcher. (2026). Personal communication.
```

---

## 3. In-Text Citation Patterns

### 3.1 Parenthetical (Numeric)
```
The result follows from the completeness theorem [1].
Multiple independent proofs exist [1, 2, 3].
The foundational work spans decades [1-5].
```
### 3.2 Narrative (Author-Year)
```
Shannon [1] proved the channel coding theorem.
Shannon and Weaver [1, 2] established the mathematical theory.
Recent advances by AlphaProof Team [3] and DeepSeek [4] demonstrate...
```

### 3.3 Specific Locations
```
The proof uses the cut-elimination lemma [1, §4.2].
See [1, p. 42] for the exact statement.
The bound is given in Theorem 3.1 [1].
```

---

## 4. Citation Verification Checklist

### 4.1 Pre-Citation Verification
- [ ] Source exists and is accessible
- [ ] DOI/URL resolves correctly
- [ ] Metadata matches (authors, year, title, venue)
- [ ] Version identified (for preprints/software)
- [ ] Page numbers/sections verified
- [ ] Evidence grade assigned (A–X)

### 4.2 Post-Citation Verification
- [ ] Citation format matches style guide
- [ ] Bibliography entry complete
- [ ] Cross-reference resolves (in-text ↔ bibliography)
- [ ] No duplicate entries
- [ ] Citation count matches usage

### 4.3 Automated Verification
```bash
# Run citation verification
python scripts/verify-citations.py manuscript/final-report.md

# Check link accessibility
markdown-link-check manuscript/final-report.md

# Verify DOI resolution
python scripts/check-dois.py manuscript/final-report.md
```

---

## 5. Bibliography Management

### 5.1 Bibliography Structure
```
### 25.1 Foundational References
1. Entry...
2. Entry...

### 25.2 Journal Articles
3. Entry...

### 25.3 Conference Proceedings
...
```

### 5.2 Numbering Rules
- Sequential throughout document (1, 2, 3...)
- Grouped by category for readability
- No gaps in numbering
- New entries appended at end of appropriate section

### 5.3 Entry Maintenance
- **Add**: When new claim requires citation
- **Update**: When source metadata corrected
- **Remove**: Only if citation removed from text AND no other usage
- **Consolidate**: If duplicate entries discovered

---

## 6. Special Citation Cases

### 6.1 Multiple Works by Same Author
```
[1] Shannon, C. E. (1948). "A Mathematical Theory of Communication." ...
[2] Shannon, C. E. (1949). "Communication Theory of Secrecy Systems." ...
```
In-text: `[Shannon, 1948]` and `[Shannon, 1949]` or `[1]` and `[2]`

### 6.2 Same Author, Same Year
```
[1] Author, A. (2024a). "Title A." ...
[2] Author, A. (2024b). "Title B." ...
```
In-text: `[Author, 2024a]` and `[Author, 2024b]`

### 6.3 Corporate Authors
```
[1] The Lean Community. (2024). "mathlib." ...
[2] World Wide Web Consortium. (2023). "WCAG 2.2." ...
```

### 6.4 Anonymous / Unknown Authors
```
[1] Anonymous. (2018). "Superpermutation Lower Bound." ...
```
Or use title:
```
[1] "Superpermutation Lower Bound." (2018). ...
```

### 6.5 Translations
```
[1] Author, A. (Year). "Original Title." *Journal*. (Original work published Year)
```
In-text: `[Author, Year/Year]`

### 6.6 Secondary Citations (Citing a Citation)
```
[1] Author, A. (Year). "Title." *Journal*. (as cited in Author, B., Year)
```
**Avoid when possible** — always prefer primary source.

---

## 7. Citation Quality Gates

### 7.1 Minimum Standards (All Citations)
- [ ] Source type identified
- [ ] All required fields present
- [ ] DOI/URL verified accessible
- [ ] Evidence grade assigned
- [ ] Format consistent

### 7.2 Enhanced Standards (High-Confidence Claims)
- [ ] Primary source verified
- [ ] Multiple independent sources
- [ ] Recent (<5 years for fast-moving fields)
- [ ] Reproducibility verified (if computational)

### 7.3 Publication Standards (Major Revisions)
- [ ] 100% citation verification
- [ ] Spot-check 20%+ by independent reviewer
- [ ] All URLs archived (Internet Archive / perma.cc)
- [ ] Citation graph analyzed for coverage

---

## 8. Tools and Workflows

### 8.1 Recommended Tools
| Task | Tool | Notes |
|------|------|-------|
| Reference management | Zotero / Mendeley / JabRef | Export BibTeX |
| DOI lookup | doi.org / CrossRef | Auto-complete metadata |
| arXiv search | arXiv.org / Semantic Scholar | Version tracking |
| Link checking | markdown-link-check | CI integration |
| Format validation | Custom Python scripts | See `scripts/` |

### 8.2 Workflow: Adding a Citation
1. **Find source** → Verify accessibility & metadata
2. **Assign evidence grade** → A–X per methodology.md
3. **Add to bibliography** → Next sequential number, correct section
4. **Insert in-text** → `[N]` at claim location
5. **Verify** → Run `verify-citations.py`
6. **Commit** → `citation: add [N] for [claim]`

### 8.3 Workflow: Fixing a Citation
1. **Identify issue** → Format, metadata, accessibility
2. **Correct bibliography entry** → Update in place
3. **Verify all usages** → Check all in-text references
4. **Run verification** → `verify-citations.py`
5. **Commit** → `citation: fix [N] — [issue]`

---

## 9. Common Errors to Avoid

| Error | Example | Fix |
|-------|---------|-----|
| Missing DOI | `[1] Author. (2024). "Title." *J.`, no DOI | Add DOI |
| Dead URL | `http://old-site.com/paper` | Archive / find current |
| Incomplete entry | `[1] Author. "Title."` | Add venue, year, pages |
| Wrong format | `[1] Author (2024) Title Journal` | Follow template |
| Duplicate entry | `[1]` and `[5]` same source | Consolidate |
| Unverified claim | "It is well known that..." | Add citation or mark speculative |
| Page range missing | `[1] Author. (2024). "Title." *J.*, 10.` | Add page range |

---

## 10. Citation Metrics Tracking

### 9.1 Repository-Level Metrics
| Metric | Target | Current |
|--------|--------|---------|
| Citation verification rate | 100% | — |
| Open-access ratio | >50% | — |
| Primary source ratio | >70% | — |
| Recent sources (<5 yr) | >60% | — |
| Evidence grade A–C ratio | >80% | — |

### 9.2 Per-Document Metrics
- Total citations
- Unique sources
- Citation density (citations/1000 words)
- Uncited bibliography entries
- Cross-reference integrity

---

## Appendix: Quick Templates

### Journal Article
```
[N] Surname, I., & Surname, I. (Year). "Title." *Journal*, Vol(Issue), Start–End. DOI: 10.xxxx/xxxxx
```

### Conference Paper
```
[N] Surname, I. (Year). "Title." *Proc. Conference*, Start–End. DOI: 10.xxxx/xxxxx
```

### Preprint
```
[N] Surname, I. (Year). "Title." *arXiv:YYMM.NNNNN [cat]*. Version N.
```

### Software
```
[N] Organization. (Year). "Title." *Repo*. Version. URL
```

### Dataset
```
[N] Author/Org. (Year). "Title." *Repo*. Version. DOI/URL
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-08-07 | Initial release aligned with manuscript Rev 6 |