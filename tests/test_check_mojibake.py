#!/usr/bin/env python3
"""
Tests for check-mojibake.py
"""

import subprocess
import sys
import tempfile
import os

def run_check_mojibake(content_bytes):
    """Run check-mojibake.py on given content bytes and return result."""
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.md', delete=False) as f:
        f.write(content_bytes)
        temp_path = f.name
    
    try:
        result = subprocess.run(
            [sys.executable, 'scripts/check-mojibake.py', temp_path],
            capture_output=True, text=True, timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    finally:
        os.unlink(temp_path)

def test_clean_content():
    """Test clean content passes."""
    content = b"# Test\n\nClean content with em-dash \xe2\x80\x94 and en-dash \xe2\x80\x93 and rupee \xe2\x82\xb9\n"
    code, stdout, stderr = run_check_mojibake(content)
    assert code == 0, f"Clean content should pass: {stdout}"

def test_mojibake_em_dash():
    """Test double-encoded em-dash is detected."""
    content = b"# Test\n\nMojibake: \xc3\xa2\xe2\x80\x94 test\n"
    code, stdout, stderr = run_check_mojibake(content)
    assert code != 0, f"Mojibake should fail: {stdout}"
    assert "em-dash" in stdout

def test_mojibake_rupee():
    """Test double-encoded rupee is detected."""
    content = b"# Test\n\nMojibake rupee: \xc3\xa2\xe2\x82\xb9 test\n"
    code, stdout, stderr = run_check_mojibake(content)
    assert code != 0, f"Mojibake should fail: {stdout}"
    assert "rupee" in stdout.lower()

def test_mojibake_euro():
    """Test double-encoded euro is detected."""
    content = b"# Test\n\nMojibake euro: \xc3\xa2\xe2\x82\xac test\n"
    code, stdout, stderr = run_check_mojibake(content)
    assert code != 0, f"Mojibake should fail: {stdout}"
    assert "euro" in stdout.lower()

def test_mojibake_accented():
    """Test double-encoded accented characters."""
    content = b"# Test\n\nMojibake e-acute: \xc3\x83\xc2\xa9 test\n"
    code, stdout, stderr = run_check_mojibake(content)
    assert code != 0, f"Mojibake should fail: {stdout}"
    assert "e-acute" in stdout.lower() or "eacute" in stdout.lower()

if __name__ == "__main__":
    print("Running check-mojibake tests...")
    test_clean_content()
    print("[OK] test_clean_content passed")
    test_mojibake_em_dash()
    print("[OK] test_mojibake_em_dash passed")
    test_mojibake_rupee()
    print("[OK] test_mojibake_rupee passed")
    test_mojibake_euro()
    print("[OK] test_mojibake_euro passed")
    test_mojibake_accented()
    print("[OK] test_mojibake_accented passed")
    print("\nAll check-mojibake tests passed!")