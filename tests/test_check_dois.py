#!/usr/bin/env python3
"""
Tests for check-dois.py pattern detection.
"""

import re

def test_doi_pattern_detection():
    """Test DOI pattern detection."""
    bib_section = """1. Author. (2024). Title. DOI: 10.1000/12345
2. Author. (2024). Title. https://doi.org/10.1000/67890
3. Author. (2024). Title. arXiv:1512.08776
4. Author. (2024). Title. https://example.com/paper
"""
    doi_pattern = re.compile(r'(?:DOI:|doi:|https://doi\.org/)\s*([\d.]+/[^\s,;]+)', re.IGNORECASE)
    arxiv_pattern = re.compile(r'arXiv:(\d{4}\.\d{4,5}(?:v\d+)?)', re.IGNORECASE)
    # URL pattern should not match DOI URLs
    url_pattern = re.compile(r'https?://(?!doi\.org)[^\s,;)]+')
    
    dois = doi_pattern.findall(bib_section)
    arxiv_ids = arxiv_pattern.findall(bib_section)
    urls = url_pattern.findall(bib_section)
    
    print(f"DOIs found: {dois}")
    print(f"arXiv IDs found: {arxiv_ids}")
    print(f"URLs found: {urls}")
    
    assert len(dois) == 2, f"Expected 2 DOIs, got {len(dois)}: {dois}"
    assert len(arxiv_ids) == 1, f"Expected 1 arXiv ID, got {len(arxiv_ids)}: {arxiv_ids}"
    assert len(urls) == 1, f"Expected 1 URL, got {len(urls)}: {urls}"

def test_arxiv_pattern():
    """Test arXiv pattern matching."""
    arxiv_pattern = re.compile(r'arXiv:(\d{4}\.\d{4,5}(?:v\d+)?)', re.IGNORECASE)
    
    test_cases = [
        "arXiv:1512.08776",
        "arXiv:2504.21801",
        "arXiv:2502.07640",
        "arXiv:2505.14929",
        "arXiv:2301.12345v2",
    ]
    
    for case in test_cases:
        match = arxiv_pattern.search(case)
        assert match, f"Failed to match: {case}"
        print(f"[OK] Matched: {case} -> {match.group(1)}")

if __name__ == "__main__":
    print("Running check-dois pattern tests...")
    test_doi_pattern_detection()
    print("[OK] test_doi_pattern_detection passed")
    test_arxiv_pattern()
    print("[OK] test_arxiv_pattern passed")
    print("\nAll check-dois pattern tests passed!")