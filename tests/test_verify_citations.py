#!/usr/bin/env python3
"""
Tests for verify-citations.py
"""

import subprocess
import sys
import tempfile
import os

def run_verify_citations(content):
    """Run verify-citations.py on given content and return result."""
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.md', delete=False) as f:
        f.write(content.encode('utf-8'))
        temp_path = f.name
    
    try:
        result = subprocess.run(
            [sys.executable, 'scripts/verify-citations.py', temp_path],
            capture_output=True, text=True, timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    finally:
        os.unlink(temp_path)

def test_valid_citations():
    """Test that valid citations pass."""
    content = """# Test

Some text [1] and more [2, 3].

## Chapter 25: Comprehensive Categorized Bibliography

1. Author, A. (2024). Title. Journal.
2. Author, B. (2024). Title. Journal.
3. Author, C. (2024). Title. Journal.
"""
    code, stdout, stderr = run_verify_citations(content)
    assert code == 0, f"Valid citations should pass, got code {code}: {stdout}"

def test_missing_bibliography():
    """Test that missing bibliography entries are detected."""
    content = """# Test

Some text [1] and [4].

## Chapter 25: Comprehensive Categorized Bibliography

1. Author, A. (2024). Title. Journal.
2. Author, B. (2024). Title. Journal.
3. Author, C. (2024). Title. Journal.
"""
    code, stdout, stderr = run_verify_citations(content)
    assert code != 0, f"Missing bibliography should fail"
    assert "4" in stdout

def test_duplicate_bibliography():
    """Test that duplicate bibliography entries are detected."""
    content = """# Test

Some text [1].

## Chapter 25: Comprehensive Categorized Bibliography

1. Author, A. (2024). Title. Journal.
1. Author, B. (2024). Title. Journal.
2. Author, C. (2024). Title. Journal.
"""
    code, stdout, stderr = run_verify_citations(content)
    assert code != 0, f"Duplicate bibliography should fail"
    assert "Duplicate" in stdout

def test_citation_ranges():
    """Test citation ranges."""
    content = """# Test

Some text [1-3].

## Chapter 25: Comprehensive Categorized Bibliography

1. Author, A. (2024). Title. Journal.
2. Author, B. (2024). Title. Journal.
3. Author, C. (2024). Title. Journal.
"""
    code, stdout, stderr = run_verify_citations(content)
    assert code == 0, f"Citation ranges should work: {stdout}"

def test_invalid_range():
    """Test invalid citation range (start >= end)."""
    content = """# Test

Some text [3-1].

## Chapter 25: Comprehensive Categorized Bibliography

1. Author, A. (2024). Title. Journal.
2. Author, B. (2024). Title. Journal.
3. Author, C. (2024). Title. Journal.
"""
    code, stdout, stderr = run_verify_citations(content)
    assert code != 0, f"Invalid range should fail"
    assert "Invalid citation range" in stdout

if __name__ == "__main__":
    print("Running verify-citations tests...")
    test_valid_citations()
    print("[OK] test_valid_citations passed")
    test_missing_bibliography()
    print("[OK] test_missing_bibliography passed")
    test_duplicate_bibliography()
    print("[OK] test_duplicate_bibliography passed")
    test_citation_ranges()
    print("[OK] test_citation_ranges passed")
    test_invalid_range()
    print("[OK] test_invalid_range passed")
    print("\nAll verify-citations tests passed!")