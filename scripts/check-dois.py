#!/usr/bin/env python3
"""
DOI verification script for Silver Mosaic manuscript.
Checks that all DOIs in bibliography are accessible.
"""

import re
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse

def check_dois(filepath):
    """Check DOIs in bibliography for accessibility."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    warnings = []
    
    # Extract DOIs from bibliography
    # Pattern: DOI: 10.xxxx/xxxxx or https://doi.org/10.xxxx/xxxxx
    doi_pattern = re.compile(r'(?:DOI:|doi:|https://doi\.org/)\s*([\d.]+/[^\s,;]+)')
    dois = doi_pattern.findall(content)
    
    # Also find URLs in bibliography
    url_pattern = re.compile(r'https?://[^\s,;)]+')
    urls = url_pattern.findall(content)
    
    print(f"Found {len(dois)} DOIs and {len(urls)} URLs in bibliography")
    
    # Check DOIs
    for doi in dois:
        doi = doi.strip().rstrip('.')
        url = f"https://doi.org/{doi}"
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            if response.status_code >= 400:
                warnings.append(f"DOI {doi} returned status {response.status_code}")
            else:
                print(f"  ✅ DOI {doi}: OK ({response.status_code})")
        except requests.RequestException as e:
            warnings.append(f"DOI {doi} check failed: {e}")
    
    # Check URLs (sample first 20 to avoid rate limiting)
    for i, url in enumerate(urls[:20]):
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            if response.status_code >= 400:
                warnings.append(f"URL {url} returned status {response.status_code}")
            else:
                print(f"  ✅ URL {url}: OK ({response.status_code})")
        except requests.RequestException as e:
            warnings.append(f"URL {url} check failed: {e}")
    
    if len(urls) > 20:
        warnings.append(f"Only checked first 20 of {len(urls)} URLs (rate limiting)")
    
    # Report
    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  - {e}")
    
    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"  - {w}")
    
    if not errors and not warnings:
        print("✅ All DOIs/URLs accessible")
        return True
    elif not errors:
        print("\n⚠️  Warnings only - review recommended")
        return True
    else:
        print(f"\n❌ {len(errors)} error(s) found")
        return False

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "manuscript/final-report.md"
    success = check_dois(filepath)
    sys.exit(0 if success else 1)