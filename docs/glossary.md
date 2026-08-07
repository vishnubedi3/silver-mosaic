# Glossary

## Overview

Authoritative definitions for key terms used throughout the Silver Mosaic research monograph and repository. Ensures consistent terminology across all documents.

---

## A

**AI-Durability** — The property of a research field where advancing AI capabilities increase rather than decrease demand for human contributions. Formal mathematics exhibits AI-durability because AI-generated proofs require human formalization and verification.

**AlphaProof** — Google DeepMind's neuro-symbolic theorem proving system combining language models with formal verification in Lean. Achieved silver-medal performance at IMO 2024.

**AHP (Analytic Hierarchy Process)** — A structured technique for organizing and analyzing complex decisions, using pairwise comparisons to derive priority weights.

**Asymmetric Cognitive Arbitrage** — The strategic opportunity for zero-budget researchers to exploit the structural elimination of credential signaling in formally verifiable domains, while capital-intensive researchers crowd empirical fields.

---

## B

**Bibliometric Analysis** — Quantitative analysis of publication and citation patterns to assess research impact, trends, and field structure.

**Bootstrap** — A statistical resampling technique for estimating uncertainty by repeatedly sampling from observed data with replacement.

---

## C

**Channel Capacity** — The maximum rate at which information can be reliably transmitted over a communication channel (Shannon, 1948).

**Compensatory Model** — A decision model where high scores on some criteria can offset low scores on others (weighted sum).

**Computational Complexity** — The study of resources (time, space) required to solve computational problems, classified into complexity classes (P, NP, PSPACE, etc.).

**Content Classification** — Systematic labeling of claims by confidence level: VERIFIED (1.0), HIGH CONFIDENCE (0.85-0.95), MODERATE (0.70-0.84), SPECULATIVE (<0.70).

**Crank-Avoidance Protocol** — A 12-rule diagnostic framework for distinguishing legitimate independent research from pseudoscientific claims.

**Curry-Howard Correspondence** — The isomorphism between computer programs and mathematical proofs: types are propositions, programs are proofs.

---

## D

**de Bruijn Criterion** — A proof assistant satisfies this if its kernel (trusted code base) is small enough to be manually verified; proof terms are self-authenticating.

**Diamond Open Access** — Open access publishing with no article processing charges (APCs) for authors and no subscription fees for readers.

**DSP (Draft-Sketch-Prove)** — A theorem proving methodology: draft informal proof, sketch formal structure, prove in proof assistant.

---

## E

**Epistemic Invariance Principle** — The degree to which a claim's validation is independent of the validator's identity, credentials, or institutional affiliation.

**Evidence Grade** — A-F scale for source quality: A (systematic review), B (RCT), C (observational), D (preprint), E (technical report), F (blog), X (unverified).

**EXPTIME** — Complexity class of problems solvable in exponential time.

---

## F

**Feit-Thompson Theorem** — Every finite group of odd order is solvable. Formalized in Coq (2012) and Lean 4 (2023+).

**Formal Verification** — Mathematically proving that a system satisfies its specification, as opposed to testing which only finds bugs.

**FPR (False Positive Rate)** — In crank-avoidance: probability of classifying legitimate research as pseudoscience.

---

## G

**Game-Theoretic Signaling** — A model where agents choose actions that reveal private information; in research, institutional affiliation signals quality in empirical domains but not formal ones.

**Goedel-Prover** — Open-source automated theorem prover using language models, achieving 57.6% on miniF2F benchmark.

---

## H

**Hard Constraint (Gate)** — A non-negotiable filter in the multiplicative utility model: violation = zero utility regardless of other scores.

**HARKing** — Hypothesizing After Results are Known; presenting post-hoc hypotheses as a priori predictions.

---

## I

**IMO (International Mathematical Olympiad)** — Annual mathematics competition for pre-college students; benchmark for AI theorem proving (AlphaProof 2024 silver).

**Intellectual Leverage** — The ratio of durable epistemic value produced to resources consumed, multiplied by verification objectivity.

**Interactive Theorem Prover (ITP)** — A proof assistant where humans guide proof construction (Lean, Coq, Isabelle, Agda).

---

## K

**Kernel (Proof Assistant)** — The minimal trusted code base that checks proof terms; correctness of all proofs depends on kernel correctness.

---

## L

**Lean 4** — A dependently typed functional programming language and proof assistant, successor to Lean 3, with improved performance and metaprogramming.

**LeanDojo** — A toolkit for AI-assisted theorem proving in Lean, providing environments, datasets, and evaluation benchmarks.

**LP Bound (Linear Programming Bound)** — Upper bound on code parameters derived from linear programming duality.

---

## M

**mathlib** — The Lean mathematical library: a unified, collaboratively developed formal mathematics library (134K+ definitions, 283K+ theorems as of 2025).

**mathlib4** — The Lean 4 version of mathlib (sometimes used to distinguish from Lean 3 mathlib).

**Maximum Entropy Weighting** — A method for deriving criterion weights that maximizes entropy subject to ordinal constraints, minimizing arbitrary assumptions.

**miniCTX** — A benchmark for context-aware theorem proving (ICLR 2025 Oral).

**miniF2F** — A benchmark of 488 formalized mathematical problems from high-school to undergraduate level.

**Mojibake** — Garbled text resulting from encoding/decoding mismatch (e.g., UTF-8 interpreted as Latin-1).

**Multiplicative Non-Compensatory Gate Model** — Utility model: U_i = (∏ G_k(i)) × Σ w_j·c_ij, where G_k ∈ {0,1} are hard gates and failure on any gate yields zero utility.

---

## N

**NP-Hard** — At least as hard as the hardest problems in NP; no polynomial-time algorithm known unless P=NP.

**NP-Complete** — In NP and NP-hard; the "hardest" problems in NP.

---

## O

**O(1), O(n), O(N)** — Big-O notation for asymptotic complexity: constant, linear in proof size, linear in corpus size.

**OEIS (On-Line Encyclopedia of Integer Sequences)** — Comprehensive database of integer sequences (oeis.org), freely accessible.

**Open-Source** — Software with source code freely available under permissive licenses (MIT, Apache 2.0, GPL, BSD).

---

## P

**P (Complexity Class)** — Problems solvable in polynomial time by deterministic Turing machine.

**PFR (Polynomial Freiman-Ruzsa) Conjecture** — A central conjecture in additive combinatorics, formalized in Lean 4 in 2023 by Tao et al.

**P-hacking** — Data dredging: performing many analyses and reporting only significant results.

**Proof Assistant** — Software that helps construct and check formal proofs (Lean, Coq, Isabelle, Agda).

**Proof Carrying Code** — Executable code accompanied by a formal proof of its correctness properties.

---

## Q

**QED (Quod Erat Demonstrandum)** — "That which was to be demonstrated"; traditional end-of-proof marker (□).

---

## R

**Replication Crisis** — The finding that many published scientific results cannot be independently replicated (e.g., 36% in psychology).

**Registered Reports** — Publication format where methods and analysis plan are peer-reviewed before data collection.

**Reproducibility** — Ability to independently obtain same results using same code, data, and environment.

---

## S

**SAT Solver** — Algorithm for determining satisfiability of Boolean formulas in CNF; NP-complete in worst case but efficient in practice.

**Scaling Laws** — Empirical power-law relationships between model performance and compute/data/parameters.

**Sensitivity Analysis** — Quantifying how output changes with input parameter variations (±20% standard).

**Shannon's Channel Coding Theorem** — Reliable communication at rates up to channel capacity is possible; impossible above capacity.

**SMT Solver** — Satisfiability Modulo Theories solver; extends SAT with theories (arithmetic, arrays, bit-vectors).

**Sorries** — Lean keyword for admitting a proof gap; `sorry` marks an incomplete proof.

**STP (Self-Play Theorem Proving)** — LLM-based prover that generates its own training data through self-play.

---

## T

**TCB (Trusted Computing Base)** — The set of hardware, firmware, and software components whose correctness is essential for system security/soundness.

**Type Checking** — Verifying that a proof term has the claimed type; linear time in Lean 4 kernel.

**Type Theory** — Formal system where every term has a type; basis for Lean, Coq, Agda (Calculus of Inductive Constructions).

---

## V

**Verification Objectivity Index (A_val)** — A ∈ [0,1] measuring how purely a claim is evaluated on logical correctness vs. social signals.

**V1-V4 Classification** — Content confidence tiers: V1=VERIFIED, V2=HIGH CONFIDENCE, V3=MODERATE, V4=SPECULATIVE.

---

## Z

**Zero-Budget Research** — Research conducted with exactly ₹0/$0 financial outlay, using only freely available tools, data, and compute.

---

## Abbreviations

| Abbreviation | Expansion |
|--------------|-----------|
| AHP | Analytic Hierarchy Process |
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| CI/CD | Continuous Integration / Continuous Deployment |
| CNF | Conjunctive Normal Form |
| CPU | Central Processing Unit |
| GPU | Graphics Processing Unit |
| ITP | Interactive Theorem Prover |
| IMO | International Mathematical Olympiad |
| LOC | Lines of Code |
| LLM | Large Language Model |
| NP | Nondeterministic Polynomial time |
| PFR | Polynomial Freiman-Ruzsa |
| PR | Pull Request |
| RAM | Random Access Memory |
| RL | Reinforcement Learning |
| SAT | Boolean Satisfiability |
| SMT | Satisfiability Modulo Theories |
| SOTA | State of the Art |
| TCB | Trusted Computing Base |
| TCS | Theoretical Computer Science |
| URL | Uniform Resource Locator |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-08-07 | Initial release aligned with manuscript Rev 6 |