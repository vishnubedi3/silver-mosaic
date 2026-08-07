#!/usr/bin/env python3
"""
Test runner for all verification scripts.
"""

import sys
import subprocess

def run_tests():
    """Run all test files."""
    test_files = [
        'tests/test_check_encoding.py',
        'tests/test_verify_citations.py',
        'tests/test_check_classification.py',
        'tests/test_check_crossrefs.py',
        'tests/test_check_mojibake.py',
        'tests/test_check_dois.py',
    ]
    
    results = {}
    for test_file in test_files:
        print(f"\n{'='*60}")
        print(f"Running {test_file}")
        print(f"{'='*60}")
        
        result = subprocess.run(
            [sys.executable, test_file],
            capture_output=True, text=True, timeout=60
        )
        
        results[test_file] = result.returncode == 0
        
        if result.returncode == 0:
            print(f"[OK] {test_file} PASSED")
        else:
            print(f"[ERR] {test_file} FAILED")
            print(f"STDOUT:\n{result.stdout}")
            print(f"STDERR:\n{result.stderr}")
    
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for test_file, passed in results.items():
        status = "[OK] PASS" if passed else "[ERR] FAIL"
        print(f"  {status}: {test_file}")
    
    all_passed = all(results.values())
    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed")
    
    return all_passed

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)