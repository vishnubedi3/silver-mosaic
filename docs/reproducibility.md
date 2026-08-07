# Reproducibility Guide

## Overview

This guide defines the standards for computational reproducibility in the Silver Mosaic repository. All computational claims must be independently verifiable by any researcher with standard hardware.

---

## 1. Reproducibility Principles

### 1.1 Core Requirements
- **Deterministic**: Same inputs → same outputs (fixed seeds, pinned versions)
- **Accessible**: Runs on standard hardware (≤8GB RAM, no GPU required)
- **Documented**: Complete environment specification + step-by-step instructions
- **Verifiable**: Expected outputs provided + validation scripts
- **Archived**: Immutable snapshots of code, data, environment

### 1.2 Reproducibility Levels
| Level | Description | Required For |
|-------|-------------|--------------|
| **L1: Computational** | Same code + data + env = same results | All computational claims |
| **L2: Methodological** | Same method described = same conclusions | All analytical claims |
| **L3: Conceptual** | Same principles = consistent findings | All theoretical claims |
| **L4: Independent** | Different team/code = same results | Publication-grade claims |

---

## 2. Environment Specification

### 2.1 Required Files
```
project/
├── requirements.txt          # Python deps (pip freeze)
├── environment.yml           # Conda env (if used)
├── Dockerfile                # Container (preferred)
├── pyproject.toml            # Modern Python packaging
├── .python-version           # Python version pin
└── README-repro.md           # Reproduction instructions
```

### 2.2 Python Environment (requirements.txt)
```text
# Pinned to exact versions
numpy==1.26.4
scipy==1.13.0
pandas==2.2.1
matplotlib==3.8.3
lean4==4.9.0  # if applicable
```

### 2.3 Conda Environment (environment.yml)
```yaml
name: silver-mosaic
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11.9
  - pip=24.0
  - pip:
    - numpy==1.26.4
    - scipy==1.13.0
```

### 2.4 Docker (Recommended)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "scripts/verify.py"]
```
Build: `docker build -t silver-mosaic .`
Run: `docker run --rm silver-mosaic`

---

## 3. Code Organization

### 3.1 Directory Structure
```
code/
├── src/
│   ├── silver_mosaic/
│   │   ├── __init__.py
│   │   ├── analysis.py
│   │   ├── verification.py
│   │   └── utils.py
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_analysis.ipynb
│   └── 03_verification.ipynb
├── scripts/
│   ├── run_analysis.py
│   ├── verify_results.py
│   └── generate_figures.py
├── tests/
│   ├── test_analysis.py
│   └── test_verification.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── logs/
├── requirements.txt
├── environment.yml
├── Dockerfile
├── pytest.ini
└── README-repro.md
```

### 3.2 Code Quality Standards
- **Type hints**: All public functions (`def func(x: int) -> float:`)
- **Docstrings**: Google/NumPy style for all public APIs
- **Tests**: ≥80% coverage for core logic
- **Linting**: `ruff`, `mypy --strict`, `black`
- **Pre-commit**: `pre-commit run --all-files`

---

## 4. Reproducibility Workflow

### 4.1 For Contributors (Creating Reproducible Artifacts)

#### Step 1: Environment Setup
```bash
# Clone and setup
git clone https://github.com/vishnubedi3/silver-mosaic
cd silver-mosaic
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Step 2: Run Verification
```bash
# Full verification
python scripts/verify_results.py

# Or with Docker
docker build -t silver-mosaic .
docker run --rm silver-mosaic
```

#### Step 3: Validate Outputs
```bash
# Check expected outputs exist
ls outputs/figures/ outputs/tables/

# Compare with reference
python scripts/compare_outputs.py --reference ref/
```

### 4.2 For Reviewers (Verifying Claims)

#### Automated Verification
```bash
# Run full test suite
pytest tests/ -v --cov=src/silver_mosaic

# Check reproducibility
python scripts/verify_reproducibility.py --iterations 5

# Validate environment
python scripts/check_environment.py
```

#### Manual Verification
1. Review `README-repro.md` for completeness
2. Check all seeds documented
3. Verify expected outputs match
4. Confirm hardware requirements met

---

## 4.3 For Computational Notebooks

### Notebook Standards
- **Kernel**: Explicitly specified (Python 3.11)
- **Execution order**: Linear, restart-and-run tested
- **Outputs**: Saved in notebook (committed)
- **Parameters**: Configurable at top cell
- **Documentation**: Markdown cells explaining each step

### Notebook Verification
```bash
# Execute notebook headless
jupyter nbconvert --execute --to notebook \
  --output verified.ipynb notebooks/02_analysis.ipynb

# Check execution time
# Check all cells executed
# Check outputs match committed version
```

---

## 5. Data Management

### 5.1 Data Organization
```
data/
├── raw/                    # Immutable source data
│   ├── source1.csv
│   └── source2.json
├── processed/              # Derived data
│   ├── cleaned.csv
│   └── features.parquet
├── external/               # Large/external (symlinks)
│   └── large_dataset/ -> /mnt/data/
├── schemas/                # Data dictionaries
│   ├── source1_schema.json
│   └── processed_schema.json
└── README.md               # Provenance, licenses, updates
```

### 5.2 Data Provenance
Every processed dataset must document:
- Source (URL, DOI, access date)
- Transformation code (script + version)
- Parameters used
- Quality checks performed
- Checksum (SHA256)

### 5.3 Data Versioning
- **Small data (<100MB)**: Git LFS or committed
- **Large data**: DVC, Hugging Face Hub, Zenodo, Figshare
- **Immutable**: Raw data never modified
- **Reproducible**: Processing pipeline versioned with code

---

## 5.4 Random Seeds & Determinism

### Seed Documentation
```python
# Top of every script/notebook
SEEDS = {
    "numpy": 42,
    "random": 12345,
    "torch": 2024,
    "tensorflow": 2024,
    "sklearn": 42,
}
```

### Seed Usage
```python
import numpy as np
import random

# Set all seeds
np.random.seed(SEEDS["numpy"])
random.seed(SEEDS["random"])
# torch.manual_seed(SEEDS["torch"])  # if using PyTorch
```

### Verification
- Run 5× with same seeds → identical outputs
- Document any non-deterministic operations (OS, hardware)

---

## 6. Verification Scripts

### 6.1 Core Verification Script
```python
# scripts/verify_results.py
#!/usr/bin/env python3
"""
Verification script for Silver Mosaic computational claims.
Run: python scripts/verify_results.py
"""
import json
import hashlib
from pathlib import Path

def verify_outputs():
    """Verify all expected outputs exist and match checksums."""
    manifest = Path("outputs/manifest.json")
    if not manifest.exists():
        raise FileNotFoundError("Output manifest not found")
    
    with open(manifest) as f:
        expected = json.load(f)
    
    for filepath, expected_hash in expected.items():
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"Missing output: {filepath}")
        
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            raise ValueError(f"Checksum mismatch: {filepath}")
    
    print("✅ All outputs verified")

def verify_environment():
    """Verify runtime environment matches specification."""
    import sys
    import numpy as np
    
    assert sys.version_info >= (3, 10), "Python ≥3.10 required"
    assert np.__version__ == "1.26.4", f"NumPy version mismatch: {np.__version__}"
    # Add more checks...
    
    print("✅ Environment verified")

def main():
    verify_environment()
    verify_outputs()
    print("🎉 All verification checks passed")

if __name__ == "__main__":
    main()
```

### 6.2 Reproducibility Test
```python
# tests/test_reproducibility.py
import subprocess
import json

def test_deterministic():
    """Run analysis 5 times, verify identical outputs."""
    outputs = []
    for i in range(5):
        result = subprocess.run(
            ["python", "scripts/run_analysis.py"],
            capture_output=True, text=True
        )
        assert result.returncode == 0
        with open("outputs/results.json") as f:
            outputs.append(json.load(f))
    
    # All runs should produce identical results
    for i in range(1, 5):
        assert outputs[i] == outputs[0], f"Run {i} differs from run 0"

def test_seeds_documented():
    """Verify all seeds are documented."""
    import scripts.run_analysis as analysis
    assert hasattr(analysis, "SEEDS"), "SEEDS dict missing"
    assert len(analysis.SEEDS) > 0, "No seeds documented"
```

---

## 7. Lean 4 Formal Verification Reproducibility

### 7.1 Lean 4 Environment
```lean4
-- lean-toolchain
leanprover/lean4:v4.9.0
```

### 7.2 Lake Build Verification
```bash
# In formal/ directory
lake build
# Should complete without sorries for core theorems
```

### 7.3 Mathlib Version Pinning
```toml
# lakefile.toml
[[require]]
name = "mathlib"
scope = "leanprover-community"
rev = "4.9.0"  # Pinned to specific version
```

### 7.3 Proof Verification
```bash
# Verify no sorries in core theorems
lake build 2>&1 | grep -c "sorry"
# Should be 0 for core claims

# Export proof terms
lake build --export-deps
```

---

## 8. Hardware & Performance Standards

### 8.1 Minimum Requirements
| Resource | Minimum | Recommended |
|----------|---------|-------------|
| CPU | x86-64, 2 cores | x86-64, 4+ cores |
| RAM | 8 GB | 16+ GB |
| Disk | 10 GB free | 50+ GB free |
| GPU | None required | Optional (CUDA) |
| OS | Linux/macOS/Windows | Linux |

### 8.2 Performance Budgets
| Task | Max Time (8GB RAM) | Max Memory |
|------|-------------------|------------|
| Full analysis | 30 min | 4 GB |
| Verification | 5 min | 2 GB |
| Figure generation | 10 min | 2 GB |
| Lean 4 build | 20 min | 6 GB |

---

## 9. Documentation Standards

### 9.1 README-repro.md Template
```markdown
# Reproduction Guide: [Analysis Name]

## Overview
Brief description of what this analysis computes.

## Requirements
- Python ≥3.10
- [Other requirements]

## Quick Start
```bash
python scripts/run_analysis.py
```

## Expected Outputs
| File | Description | Checksum (SHA256) |
|------|-------------|-------------------|
| outputs/results.json | Main results | abc123... |
| outputs/figures/fig1.png | Figure 1 | def456... |

## Verification
```bash
python scripts/verify_results.py
```

## Expected Runtime
- Analysis: ~15 min
- Verification: ~2 min

## Hardware Requirements
- RAM: ≥4 GB
- CPU: 2+ cores
- Disk: 2 GB free

## Troubleshooting
| Issue | Solution |
|-------|----------|
| Memory error | Reduce batch size in config |
| Import error | Check Python version, reinstall deps |

## Contact
Open GitHub Issue with label `reproduction`
```

---

## 10. CI/CD Integration

### 10.1 GitHub Actions Workflow
```yaml
# .github/workflows/reproducibility.yml
name: Reproducibility Check
on: [push, pull_request]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run verification
        run: python scripts/verify_results.py
      - name: Run tests
        run: pytest tests/ -v
      - name: Check reproducibility
        run: python tests/test_reproducibility.py
```

### 10.2 Artifact Upload
```yaml
- name: Upload outputs
  uses: actions/upload-artifact@v4
  with:
    name: verification-outputs
    path: outputs/
    retention-days: 30
```

---

## 11. Troubleshooting Common Issues

| Issue | Diagnosis | Solution |
|-------|-----------|----------|
| Different outputs | Non-determinism | Check all seeds, sort inputs, fix thread count |
| Import errors | Version mismatch | Re-create environment from lock file |
| Memory errors | Insufficient RAM | Reduce batch size, use streaming |
| Slow runtime | Inefficient code | Profile, optimize, or increase budget |
| Lean build fails | Mathlib version | Pin mathlib version in lakefile.toml |

---

## 12. Continuous Improvement

- Quarterly reproducibility audits
- Track: verification success rate, flaky test rate
- Update standards based on failures
- Share learnings in `docs/reproducibility-lessons.md`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-08-07 | Initial release |