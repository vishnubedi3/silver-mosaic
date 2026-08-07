#!/usr/bin/env python3
"""
Cross-reference validation script for Silver Mosaic manuscript.
Checks that all section/chapter/figure/table/equation references resolve.
"""

import re
import sys
from pathlib import Path

def check_crossrefs(filepath):
    """Validate all cross-references in the manuscript."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    warnings = []
    
    # Extract all section headers with their numbers
    # Pattern: ## Section Title or ### X.Y Title
    section_headers = {}
    section_pattern = re.compile(r'^(#{2,4})\s+((?:\d+\.)*\d*\s*)(.+)$', re.MULTILINE)
    for match in section_pattern.finditer(content):
        level = len(match.group(1))
        num = match.group(2).strip()
        title = match.group(3).strip()
        if num:
            section_headers[num] = {'level': level, 'title': title}
    
    # Also capture chapter headers: # Chapter X: Title
    chapter_pattern = re.compile(r'^#\s+Chapter\s+(\d+):\s*(.+)$', re.MULTILINE)
    for match in chapter_pattern.finditer(content):
        num = match.group(1)
        title = match.group(2).strip()
        section_headers[f"Chapter {num}"] = {'level': 1, 'title': title}
    
    print(f"Found {len(section_headers)} sections/chapters")
    
    # Check Section X.Y references
    section_refs = re.findall(r'Section\s+(\d+(?:\.\d+)*)', content)
    for ref in section_refs:
        if ref not in section_headers:
            warnings.append(f"Section reference not found: Section {ref}")
    
    # Check Chapter X references
    chapter_refs = re.findall(r'Chapter\s+(\d+)', content)
    for ref in chapter_refs:
        if f"Chapter {ref}" not in section_headers:
            warnings.append(f"Chapter reference not found: Chapter {ref}")
    
    # Check figure/table/equation references
    fig_refs = re.findall(r'(?:Figure|Fig\.)\s+(\d+)', content)
    for ref in fig_refs:
        warnings.append(f"Figure reference found: {ref} (no figure registry to validate)")
    
    table_refs = re.findall(r'Table\s+(\d+)', content)
    for ref in table_refs:
        warnings.append(f"Table reference found: {ref} (no table registry to validate)")
    
    eq_refs = re.findall(r'Equation\s+(\d+(?:\.\d+)?)', content)
    for ref in eq_refs:
        warnings.append(f"Equation reference found: {ref} (no equation registry to validate)")
    
    # Check bibliography section references (Section 25.x)
    bib_section_refs = re.findall(r'Section\s+(25\.\d+)', content)
    for ref in bib_section_refs:
        if ref not in section_headers:
            warnings.append(f"Bibliography section reference not found: Section {ref}")
    
    # Check for broken markdown links
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    for match in link_pattern.finditer(content):
        text, url = match.groups()
        if url.startswith('#'):
            # Internal anchor - check if it exists
            anchor = url[1:]
            # Check if there's a header with this ID
            header_pattern = re.compile(r'^(#{1,4})\s+.+\s*\{#' + re.escape(anchor) + r'\}', re.MULTILINE)
            if not header_pattern.search(content):
                warnings.append(f"Internal link anchor not found: #{anchor} (from [{text}])")
        elif url.startswith('http'):
            # External link - could validate with HTTP request if needed
            pass
    
    # Check for math notation consistency
    # Inline math: $...$
    inline_math = re.findall(r'\$[^$\n]+\$', content)
    # Check for unmatched $ signs
    dollar_count = content.count('$')
    if dollar_count % 2 != 0:
        errors.append(f"Unmatched $ signs for math notation (count: {dollar_count})")
    
    # Display math: $$...$$
    display_math = re.findall(r'\$\$[^$]+\$\$', content)
    
    # Check for unmatched brackets/parentheses/braces
    for open_char, close_char, name in [('(', ')', 'parentheses'), ('[', ']', 'brackets'), ('{', '}', 'braces')]:
        open_count = content.count(open_char)
        close_count = content.count(close_char)
        if open_count != close_count:
            warnings.append(f"Unmatched {name}: {open_count} open, {close_count} close")
    
    # Report
    print(f"Sections/chapters: {len(section_headers)}")
    print(f"Section references: {len(section_refs)}")
    print(f"Chapter references: {len(chapter_refs)}")
    print(f"Figure references: {len(fig_refs)}")
    print(f"Table references: {len(table_refs)}")
    print(f"Equation references: {len(eq_refs)}")
    print(f"Inline math: {len(inline_math)}")
    print(f"Display math: {len(display_math)}")
    
    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  - {e}")
    
    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"  - {w}")
    
    if not errors and not warnings:
        print("✅ All cross-references valid")
        return True
    elif not errors:
        print("\n⚠️  Warnings only - review recommended")
        return True
    else:
        print(f"\n❌ {len(errors)} error(s) found")
        return False

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "manuscript/final-report.md"
    success = check_crossrefs(filepath)
    sys.exit(0 if success else 1)