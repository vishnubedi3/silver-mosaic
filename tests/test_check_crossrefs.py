#!/usr/bin/env python3
"""
Tests for check-crossrefs.py
"""

import subprocess
import sys
import tempfile
import os

def run_check_crossrefs(content):
    """Run check-crossrefs.py on given content and return result."""
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.md', delete=False) as f:
        f.write(content.encode('utf-8'))
        temp_path = f.name
    
    try:
        result = subprocess.run(
            [sys.executable, 'scripts/check-crossrefs.py', temp_path],
            capture_output=True, text=True, timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    finally:
        os.unlink(temp_path)

def test_valid_crossrefs():
    """Test valid cross-references pass."""
    content = """# Test

## Section 1.1: Introduction

### Section 1.1.1: Details

See Section 1.1 for details.

## Chapter 2: Methods

Reference to Chapter 1.
"""
    code, stdout, stderr = run_check_crossrefs(content)
    assert code == 0, f"Valid crossrefs should pass: {stdout}"

def test_missing_section_ref():
    """Test missing section reference is warned."""
    content = """# Test

See Section 99.9 for details.

## Section 1.1: Introduction
"""
    code, stdout, stderr = run_check_crossrefs(content)
    assert "Section reference not found" in stdout or "Warnings only" in stdout

def test_missing_chapter_ref():
    """Test missing chapter reference is warned."""
    content = """# Test

See Chapter 99 for details.

## Chapter 1: Introduction
"""
    code, stdout, stderr = run_check_crossrefs(content)
    assert "Chapter reference not found" in stdout or "Warnings only" in stdout

def test_math_notation():
    """Test math notation balance."""
    content = """# Test

Inline math: $E = mc^2$.

Display math:
$$E = mc^2$$
"""
    code, stdout, stderr = run_check_crossrefs(content)
    assert code == 0

def test_unmatched_math():
    """Test unmatched math delimiters."""
    content = """# Test

Unmatched math: $E = mc^2
"""
    code, stdout, stderr = run_check_crossrefs(content)
    assert "Unmatched" in stdout or "Warnings only" in stdout

if __name__ == "__main__":
    print("Running check-crossrefs tests...")
    test_valid_crossrefs()
    print("[OK] test_valid_crossrefs passed")
    test_missing_section_ref()
    print("[OK] test_missing_section_ref passed")
    test_missing_chapter_ref()
    print("[OK] test_missing_chapter_ref passed")
    test_math_notation()
    print("[OK] test_math_notation passed")
    test_unmatched_math()
    print("[OK] test_unmatched_math passed")
    print("\nAll check-crossrefs tests passed!")