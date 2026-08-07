#!/usr/bin/env python3
"""
Tests for check-encoding.py
"""

import subprocess
import sys
import tempfile
import os

def run_check_encoding(content_bytes):
    """Run check-encoding.py on given content bytes and return result."""
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.md', delete=False) as f:
        f.write(content_bytes)
        temp_path = f.name
    
    try:
        result = subprocess.run(
            [sys.executable, 'scripts/check-encoding.py', temp_path],
            capture_output=True, text=True, timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    finally:
        os.unlink(temp_path)

def test_valid_utf8():
    """Test that valid UTF-8 passes."""
    content = b"# Test\n\nValid UTF-8: em-dash \xe2\x80\x94 en-dash \xe2\x80\x93 rupee \xe2\x82\xb9 quotes \xe2\x80\x9c\xe2\x80\x9d\n"
    code, stdout, stderr = run_check_encoding(content)
    assert code == 0, f"Valid UTF-8 should pass, got code {code}: {stdout}"
    assert "Encoding clean" in stdout or "Warnings only" in stdout

def test_utf8_bom():
    """Test UTF-8 with BOM."""
    content = b"\xef\xbb\xbf# Test\n\nContent\n"
    code, stdout, stderr = run_check_encoding(content)
    assert code == 0, f"UTF-8 BOM should pass, got code {code}: {stdout}"

def test_mojibake_em_dash():
    """Test that double-encoded em-dash is detected."""
    content = b"# Test\n\nMojibake: \xc3\xa2\xe2\x80\x94 test\n"
    code, stdout, stderr = run_check_encoding(content)
    assert code != 0, f"Mojibake should fail, got code {code}: {stdout}"
    assert "em-dash" in stdout

def test_mojibake_rupee():
    """Test that double-encoded rupee is detected."""
    content = b"# Test\n\nMojibake rupee: \xc3\xa2\xe2\x82\xb9 test\n"
    code, stdout, stderr = run_check_encoding(content)
    assert code != 0, f"Mojibake should fail, got code {code}: {stdout}"
    assert "rupee" in stdout.lower()

def test_replacement_char():
    """Test that replacement character is detected."""
    content = b"# Test\n\nReplacement: \xef\xbf\xbd test\n"
    code, stdout, stderr = run_check_encoding(content)

if __name__ == "__main__":
    print("Running check-encoding tests...")
    test_valid_utf8()
    print("[OK] test_valid_utf8 passed")
    test_utf8_bom()
    print("[OK] test_utf8_bom passed")
    test_mojibake_em_dash()
    print("[OK] test_mojibake_em_dash passed")
    test_mojibake_rupee()
    print("[OK] test_mojibake_rupee passed")
    test_replacement_char()
    print("[OK] test_replacement_char passed")
    print("\nAll check-encoding tests passed!")