#!/usr/bin/env python3
"""
Tests for check-classification.py
"""

import subprocess
import sys
import tempfile
import os

def run_check_classification(content):
    """Run check-classification.py on given content and return result."""
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.md', delete=False) as f:
        f.write(content.encode('utf-8'))
        temp_path = f.name
    
    try:
        result = subprocess.run(
            [sys.executable, 'scripts/check-classification.py', temp_path],
            capture_output=True, text=True, timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    finally:
        os.unlink(temp_path)

def test_valid_classification():
    """Test that valid classification passes."""
    content = """# Test

## Verified Results

[VERIFIED] This is verified.

### Section 1.1

[HIGH CONFIDENCE] This is high confidence.

████████████████████ 100%
"""
    code, stdout, stderr = run_check_classification(content)
    assert "Inline classification tags found: 2" in stdout

def test_no_classification_tags():
    """Test document with no classification tags."""
    content = """# Test

Some text without classification.

## Section 1.1

More text.
"""
    code, stdout, stderr = run_check_classification(content)
    assert "Inline classification tags found: 0" in stdout
    assert "Warnings only" in stdout or "WARNINGS" in stdout

def test_unknown_tags():
    """Test unknown bracket tags are warned."""
    content = """# Test

[UNKNOWN TAG] Some text.

[VERIFIED] Valid tag.
"""
    code, stdout, stderr = run_check_classification(content)
    assert "Unknown bracket tag" in stdout

def test_confidence_bars():
    """Test confidence bars detection."""
    content = """# Test

████████████████████ 100%
██████████████████    75%
"""
    code, stdout, stderr = run_check_classification(content)
    assert "Confidence bars found: 2" in stdout

def test_no_confidence_bars():
    """Test missing confidence bars warning."""
    content = """# Test

No confidence bars here.
"""
    code, stdout, stderr = run_check_classification(content)
    assert "No confidence bars" in stdout or "Warnings only" in stdout

def test_speculative_keywords():
    """Test speculative keyword detection."""
    # Need > 5 occurrences to trigger warning (threshold is > 5)
    content = """# Test

[VERIFIED] This is verified.

This may be speculative. This might be uncertain. This could be wrong. This is potentially problematic. This is likely incorrect. This is predicted to fail. This is forecast to be wrong. This is projected to fail. This is estimated to be wrong.
"""
    code, stdout, stderr = run_check_classification(content)
    # Should warn about unmarked speculative language (> 5 occurrences)
    assert "unmarked speculative" in stdout.lower() or "speculative" in stdout.lower()

def test_bad_format_tags():
    """Test lowercase tag detection."""
    content = """# Test

[verified] lowercase tag.
"""
    code, stdout, stderr = run_check_classification(content)
    assert "Inconsistent tag capitalization" in stdout

if __name__ == "__main__":
    print("Running check-classification tests...")
    test_valid_classification()
    print("[OK] test_valid_classification passed")
    test_no_classification_tags()
    print("[OK] test_no_classification_tags passed")
    test_unknown_tags()
    print("[OK] test_unknown_tags passed")
    test_confidence_bars()
    print("[OK] test_confidence_bars passed")
    test_no_confidence_bars()
    print("[OK] test_no_confidence_bars passed")
    test_speculative_keywords()
    print("[OK] test_speculative_keywords passed")
    test_bad_format_tags()
    print("[OK] test_bad_format_tags passed")
    print("\nAll check-classification tests passed!")