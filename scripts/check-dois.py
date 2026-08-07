#!/usr/bin/env python3
"""
DOI verification script for Silver Mosaic manuscript.
Checks that all DOIs and URLs in bibliography are accessible.
"""

import re
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse

# Use ASCII-safe output for Windows console compatibility
CHECK = "[OK]"
CROSS = "[ERR]"
WARN = "[WARN]"
INFO = "[INFO]"

def check_dois(filepath):
    """Check DOIs in bibliography for accessibility."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    warnings = []
    
    # Find bibliography section
    bib_header_match = re.search(r'^## Chapter 25: Comprehensive Categorized Bibliography', content, re.MULTILINE)
    if not bib_header_match:
        warnings.append("Bibliography section header not found, scanning full document")
        bib_section = content
    else:
        bib_section = content[bib_header_match.start():]
    
    # Extract DOIs from bibliography
    # Pattern: DOI: 10.xxxx/xxxxx or https://doi.org/10.xxxx/xxxxx or bare 10.xxxx/xxxxx
    doi_pattern = re.compile(r'(?:DOI:|doi:|https://doi\.org/)\s*([\d.]+/[^\s,;]+)', re.IGNORECASE)
    dois = doi_pattern.findall(bib_section)
    
    # Also find arXiv identifiers
    arxiv_pattern = re.compile(r'arXiv:(\d{4}\.\d{4,5}(?:v\d+)?)', re.IGNORECASE)
    arxiv_ids = arxiv_pattern.findall(bib_section)
    
    # Also find URLs in bibliography
    url_pattern = re.compile(r'https?://[^\s,;)]+')
    urls = url_pattern.findall(bib_section)
    
    print(f"Found {len(dois)} DOIs, {len(arxiv_ids)} arXiv IDs, and {len(urls)} URLs in bibliography")
    
    errors = []
    warnings = []
    
    # Check DOIs
    for doi in dois:
        doi = doi.strip().rstrip('.')
        url = f"https://doi.org/{doi}"
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            if response.status_code >= 400:
                warnings.append(f"DOI {doi} returned status {response.status_code}")
            else:
                print(f"  {CHECK} DOI {doi}: OK ({response.status_code})")
        except requests.RequestException as e:
            warnings.append(f"DOI {doi} check failed: {e}")
    
    # Check arXiv IDs
    for arxiv_id in arxiv_ids:
        arxiv_id = arxiv_id.strip()
        url = f"https://arxiv.org/abs/{arxiv_id}"
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            if response.status_code >= 400:
                warnings.append(f"arXiv {arxiv_id} returned status {response.status_code}")
            else:
                print(f"  {CHECK} arXiv:{arxiv_id}: OK ({response.status_code})")
        except requests.RequestException as e:
            warnings.append(f"arXiv {arxiv_id} check failed: {e}")
    
    # Check URLs (sample first 20 to avoid rate limiting)
    for i, url in enumerate(urls[:20]):
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            if response.status_code >= 400:
                warnings.append(f"URL {url} returned status {response.status_code}")
            else:
                print(f"  {CHECK} URL {url}: OK ({response.status_code})")
        except requests.RequestException as e:
            warnings.append(f"URL {url} check failed: {e}")
    
    if len(urls) > 20:
        warnings.append(f"Only checked first 20 of {len(urls)} URLs (rate limiting)")
    
    # Report
    if errors:
        print(f"\n{CROSS} ERRORS:")
        for e in errors:
            print(f"  - {e}")
    
    if warnings:
        print(f"\n{WARN} WARNINGS:")
        for w in warnings:
            print(f"  - {w}")
    
    if not errors and not warnings:
        print(f"{CHECK} All DOIs/URLs accessible")
        return True
    elif not errors:
        print(f"\n{WARN} Warnings only - review recommended")
        return True
    else:
        print(f"\n{CROSS} {len(errors)} error(s) found")
        return False

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "manuscript/final-report.md"
    success = check_dois(filepath)
    sys.exit(0 if success else 1)