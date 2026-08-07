#!/usr/bin/env python3
"""
Citation verification script for Silver Mosaic manuscript.
Verifies that all citations are valid and properly formatted.
"""

import re
import sys
from pathlib import Path

def verify_citations(manuscript_path):
    """Verify all citations in the manuscript."""
    with open(manuscript_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    warnings = []
    
    # Find all in-text citations: [1], [1, 2], [1-3]
    in_text_citations = re.findall(r'\[(\d+(?:[,\s-]\d+)*)\]', content)
    
    # Extract all unique citation numbers referenced
    referenced = set()
    for cite in in_text_citations:
        parts = re.split(r'[,\s-]+', cite)
        for p in parts:
            if p.isdigit():
                referenced.add(int(p))
            elif '-' in p:
                try:
                    start, end = map(int, p.split('-'))
                    referenced.update(range(start, end + 1))
                except ValueError:
                    errors.append(f"Invalid citation range: {p}")
    
    # Find bibliography entries: ^1. Author...
    bib_entries = re.findall(r'^(\d+)\.\s', content, re.MULTILINE)
    bibliography = {int(n) for n in bib_entries}
    
    # Check for missing bibliography entries
    missing = referenced - bibliography
    if missing:
        errors.append(f"Citations referenced but not in bibliography: {sorted(missing)}")
    
    # Check for unused bibliography entries
    unused = bibliography - referenced
    if unused:
        warnings.append(f"Bibliography entries not cited: {sorted(unused)}")
    
    # Check for duplicate bibliography entries
    seen = set()
    duplicates = set()
    for n in bib_entries:
        num = int(n)
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    if duplicates:
        errors.append(f"Duplicate bibliography entries: {sorted(duplicates)}")
    
    # Check citation format consistency
    # Check for [1][2] instead of [1, 2]
    bad_format = re.findall(r'\[\d+\]\[\d+\]', content)
    if bad_format:
        warnings.append(f"Citations should use [1, 2] format, not [1][2]: {len(bad_format)} occurrences")
    
    # Check for citation ranges
    ranges = re.findall(r'\[\d+-\d+\]', content)
    for r in ranges:
        match = re.match(r'\[(\d+)-(\d+)\]', r)
        if match:
            start, end = int(match.group(1)), int(match.group(2))
            if start >= end:
                errors.append(f"Invalid citation range (start >= end): {r}")
    
    # Print results
    print(f"Total in-text citations: {len(in_text_citations)}")
    print(f"Unique references: {len(referenced)}")
    print(f"Bibliography entries: {len(bibliography)}")
    
    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  - {e}")
    
    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"  - {w}")
    
    if not errors and not warnings:
        print("✅ All citations valid")
        return True
    elif not errors:
        print("\n⚠️  Warnings only - review recommended")
        return True
    else:
        print(f"\n❌ {len(errors)} error(s) found")
        return False

if __name__ == "__main__":
    manuscript = sys.argv[1] if len(sys.argv) > 1 else "manuscript/final-report.md"
    success = verify_citations(manuscript)
    sys.exit(0 if success else 1)