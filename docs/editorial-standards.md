# Editorial Standards

## Overview

This document defines the writing, formatting, and citation standards for all textual content in the Silver Mosaic repository. It ensures consistency, clarity, and professional quality across all documents.

---

## 1. Writing Standards

### 1.1 Voice and Tone
- **Academic formal**: Objective, precise, evidence-based
- **Active voice preferred**: "We analyze" not "It is analyzed"
- **Present tense for established facts**: "Shannon proves" not "Shannon proved"
- **Past tense for historical events**: "Shannon published in 1948"
- **Hedging appropriate to confidence**: "suggests" (moderate), "demonstrates" (high)

### 1.2 Clarity and Precision
- Define all technical terms on first use
- Avoid: "very", "really", "quite", "extremely" (use precise quantifiers)
- Avoid: "obviously", "clearly", "trivially" (let evidence speak)
- Prefer: "≤ 8 GB" over "8 GB or less"
- Prefer: "approximately 16%" over "about 16%"

### 1.3 Conciseness
- Target: 1 idea per sentence, 1 topic per paragraph
- Eliminate: redundant transitions, filler phrases
- Use: lists for parallel items, tables for structured data

---

## 2. Formatting Standards

### 2.1 Document Structure
```markdown
# Title (H1 - only one per document)

## Section (H2)

### Subsection (H3)

#### Sub-subsection (H4)
```

- Maximum heading depth: H4
- Numbered sections for manuscript chapters only
- Unnumbered for supplementary documents

### 2.2 Text Formatting
| Element | Syntax | Example |
|---------|--------|---------|
| Bold | `**text**` | **definition** |
| Italic | `*text*` | *emphasis* |
| Inline code | `` `code` `` | `mathlib` |
| Code block | ```lang ``` | ```lean4 ... ``` |
| Math inline | `$...$` | $E = mc^2$ |
| Math display | `$$...$$` | $$\int f = F$$ |

### 2.3 Lists
- **Ordered**: For sequential steps, ranked items
- **Unordered**: For parallel items, options
- **Definition**: For term: explanation pairs
- Maximum nesting: 2 levels

### 2.4 Tables
- Use GitHub-flavored markdown tables
- Header row required
- Alignment: left (text), right (numbers), center (symbols)
- No empty cells — use "—" or "N/A"

---

## 3. Citation Standards

### 3.1 In-Text Citations
- Format: `[Author, Year]` or `[Number]`
- Multiple: `[Author, Year; Author, Year]` or `[1, 2, 3]`
- Ranges: `[1-5]` for consecutive bibliography entries
- Page numbers: `[Author, Year, p. 42]` when quoting

### 3.2 Bibliography Entries
```
N. Author, A. Coauthor, and B. Editor. (Year). "Title." *Journal*, Vol(Issue), Pages. DOI/URL.
```

**Required fields**: Authors, Year, Title, Venue
**Optional**: DOI, URL, arXiv ID, Pages, Volume, Issue

### 3.3 Citation Types
| Type | Format | Example |
|------|--------|---------|
| Journal | [Author, Year] | [Shannon, 1948] |
| Conference | [Author, Year] | [Cook, 1971] |
| Preprint | [Author, Year] | [AlphaProof Team, 2025] |
| Technical Report | [Org, Year] | [NSA, 2019-2024] |
| Software | [Org, Year] | [Lean FRO, 2024] |
| Dataset | [Org, Year] | [Sloane, 2024] |
| Thesis | [Author, Year] | [Carneiro, 2019] |
| Book | [Author, Year] | [Tao, 2016] |

### 3.4 Special Cases
- **Self-citations**: No special formatting, but disclose in PR
- **Unpublished work**: Mark `[unpublished]` or `[in preparation]`
- **Personal communication**: `[A. Researcher, personal communication, 2026]`
- **Forthcoming**: `[Author, forthcoming]` with venue if known

---

## 4. Mathematical Notation

### 4.1 Inline Math
- Use `$...$` for inline: $x \in \mathbb{R}$, $\mathcal{L}_{int}$
- Keep simple: avoid multi-line inline expressions
- Variables: italic ($x$, $n$, $\alpha$)
- Constants: upright ($e$, $\pi$, $i$)
- Operators: upright ($\sin$, $\log$, $\max$, $\arg\max$)

### 4.2 Display Math
- Use `$$...$$` for displayed equations
- Number important equations: `\tag{1}` or `\label{eq:name}`
- Align multi-line: `aligned` environment

### 4.3 Notation Consistency
| Concept | Symbol | LaTeX |
|---------|--------|-------|
| Intellectual Leverage | $\mathcal{L}_{int}$ | `\mathcal{L}_{int}` |
| Verification Objectivity | $\mathcal{A}_{val}$ | `\mathcal{A}_{val}` |
| Resource Consumed | $\mathcal{R}_{consumed}$ | `\mathcal{R}_{consumed}` |
| Utility | $\mathcal{U}_i$ | `\mathcal{U}_i` |
| Weight vector | $\mathbf{w}$ | `\mathbf{w}` |
| Score matrix | $\mathbf{C}$ | `\mathbf{C}` |
| Complexity classes | $\mathsf{P}$, $\mathsf{NP}$ | `\mathsf{P}` |

### 4.4 Special Symbols
| Symbol | Name | LaTeX | Unicode |
|--------|------|-------|---------|
| — | Em dash | `---` or `—` | U+2014 |
| – | En dash | `--` or `–` | U+2013 |
| ≤ | Less than or equal | `\le` | U+2264 |
| ≥ | Greater than or equal | `\ge` | U+2265 |
| → | Right arrow | `\to` | U+2192 |
| ∀ | For all | `\forall` | U+2200 |
| ∃ | There exists | `\exists` | U+2203 |
| ∧ | Logical and | `\land` | U+2227 |
| ∨ | Logical or | `\lor` | U+2228 |
| ¬ | Not | `\lnot` | U+00AC |
| □ | QED | `\square` | U+25A1 |

---

## 5. Terminology Standards

### 5.1 Capitalization
| Term | Correct | Incorrect |
|------|---------|-----------|
| Lean 4 | Lean 4 | lean 4, Lean4 |
| mathlib | mathlib | Mathlib, MathLib |
| mathlib4 | mathlib4 (if needed) | Mathlib4 |
| GitHub | GitHub | github, Github |
| arXiv | arXiv | ArXiv, arxiv |
| LaTeX | LaTeX | latex, Latex |
| GPU | GPU | gpu |
| CPU | CPU | cpu |
| RAM | RAM | ram |
| API | API | api |
| CI/CD | CI/CD | ci/cd |

### 5.2 Hyphenation
| Compound | Form | Rule |
|----------|------|------|
| zero-budget | hyphenated | adjective before noun |
| type-checking | hyphenated | compound adjective |
| open-source | hyphenated | established compound |
| long-term | hyphenated | compound adjective |
| high-level | hyphenated | compound adjective |
| laptop-first | hyphenated | compound adjective |
| proof-carrying | hyphenated | compound adjective |

### 5.3 Abbreviations
- Define on first use: "Large Language Model (LLM)"
- Common exceptions (no definition needed): AI, GPU, CPU, RAM, API, URL, DOI, ISBN, ISSN, arXiv, LaTeX, Lean 4
- Plural: LMs, GPUs (no apostrophe)
- Periods: U.S., Ph.D. (with periods); AI, CPU (without)

---

## 6. Section-Specific Standards

### 6.1 Abstract / Executive Summary
- 150-300 words
- Structure: Problem → Method → Key Result → Implication
- No citations (self-contained)
- Accessible to non-specialists

### 6.2 Introduction
- Motivate problem (why it matters)
- State contributions (numbered list)
- Preview structure (roadmap)
- Define scope and limitations

### 6.3 Related Work / Literature Review
- Thematic organization (not chronological)
- Critical synthesis (not annotated bibliography)
- Identify gaps explicitly
- Position current work

### 6.4 Methodology
- Sufficient detail for reproduction
- Justify design choices
- Acknowledge limitations
- Reference standard methods

### 6.5 Results
- Present objectively (no interpretation)
- Tables/figures self-contained (captions + labels)
- Statistical rigor (see methodology.md)
- Negative results included

### 6.6 Discussion
- Interpret results in context
- Compare with prior work
- Acknowledge limitations honestly
- Speculate clearly marked

### 6.7 Conclusion
- Summarize key findings
- State implications
- Future work (concrete, actionable)
- No new claims

---

## 7. Visual Elements

### 7.1 Figures
- Format: PNG (raster), SVG (vector)
- Resolution: ≥300 DPI for raster
- Captions: descriptive, self-contained
- Labels: (a), (b), (c) for multi-panel
- Alt text for accessibility

### 7.2 Tables
- Header row with units
- Alignment: numbers right, text left
- Significant figures consistent
- Footnotes for special notes

### 7.3 Code Listings
- Language specified: ```lean4, ```python, ```bash
- Line numbers for >20 lines
- Highlight key lines with comments
- Max 80 chars/line

---

## 8. Accessibility

### 8.1 Language
- Plain English where possible
- Jargon defined on first use
- Acronyms expanded on first use
- Avoid: idioms, cultural references

### 8.2 Structure
- Heading hierarchy logical (H1→H2→H3)
- Lists for scanability
- Tables for data, not layout
- Alt text for all images

### 8.3 Math Accessibility
- LaTeX source provided for all math
- Verbal descriptions for key equations
- Unicode fallback where possible

---

## 9. Quality Checklist

### Pre-Submission
- [ ] All citations verified (DOI/URL accessible)
- [ ] Cross-references resolve (sections, figures, tables, equations)
- [ ] Mathematical notation consistent
- [ ] Terminology standardized
- [ ] Speculative content marked `[SPECULATIVE]`
- [ ] UTF-8 encoding, no mojibake
- [ ] Balanced brackets/parentheses/braces
- [ ] Automated checks pass

### Editorial Review
- [ ] Voice and tone appropriate
- [ ] Clarity and precision achieved
- [ ] Formatting consistent
- [ ] Accessibility standards met
- [ ] No orphaned sections/figures/tables

---

## 10. Tools and Automation

### 9.1 Recommended Tools
| Task | Tool | Config |
|------|------|--------|
| Markdown lint | `markdownlint` | `.markdownlint.json` |
| Spell check | `cspell` | `cspell.json` (technical dict) |
| Link check | `markdown-link-check` | `.linkcheckrc` |
| Citation format | Custom script | `scripts/verify-citations.py` |
| Encoding check | Custom script | `scripts/check-encoding.py` |
| Math rendering | `pandoc` + `mathjax` | — |

### 9.2 CI Integration
```yaml
# .github/workflows/editorial.yml
- markdownlint
- cspell
- markdown-link-check
- citation-format-check
- encoding-check
- cross-ref-check
```

---

## Appendix: Quick Reference Card

### Common Fixes
| Issue | Fix |
|-------|-----|
| `lean 4` | `Lean 4` |
| `mathlib4` | `mathlib` |
| `---` (hyphens) | `—` (em dash) |
| `--` (hyphens) | `–` (en dash) |
| `>=` | `≥` |
| `<=` | `≤` |
| `->` | `→` |
| `Square.` | `$\square$` |
| `a empirical` | `an empirical` |
| `very important` | `critical` / `essential` |
| `obviously` | (remove) |
| `[1][2]` | `[1, 2]` |

### Keyboard Shortcuts (VS Code)
| Action | Shortcut |
|--------|----------|
| Insert em dash | Alt+Shift+- |
| Insert en dash | Alt+- |
| Insert ≤ | Alt+, |
| Insert ≥ | Alt+. |
| Insert → | Alt+Shift+. |