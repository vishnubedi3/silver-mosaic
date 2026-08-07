#!/usr/bin/env python3
"""
Content classification check script for Silver Mosaic manuscript.
Validates that all claims have proper classification tags.
"""

import re
import sys
from collections import Counter
from pathlib import Path

# Use ASCII-safe output for Windows console compatibility
CHECK = "[OK]"
CROSS = "[ERR]"
WARN = "[WARN]"
INFO = "[INFO]"

def check_classification(filepath):
    """Check content classification compliance."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    warnings = []
    
    # Valid classification tags
    valid_tags = {"VERIFIED", "HIGH CONFIDENCE", "MODERATE", "SPECULATIVE"}
    tag_pattern = re.compile(r'\[(VERIFIED|HIGH CONFIDENCE|MODERATE|SPECULATIVE)\]')
    
    # Find all inline classification tags
    inline_tags = tag_pattern.findall(content)
    tag_counts = Counter(inline_tags)
    
    print(f"Inline classification tags found: {sum(tag_counts.values())}")
    for tag, count in tag_counts.most_common():
        print(f"  {tag}: {count}")
    
    # Check for unknown tags
    all_bracketed = re.findall(r'\[([A-Z][A-Z\s]+)\]', content)
    for tag in all_bracketed:
        if tag not in valid_tags and len(tag) > 2:
            # Might be a citation like [1, 2] or acronym
            if not re.match(r'^[\d,\s-]+$', tag) and tag not in {'ET AL', 'ET AL.', 'I.E.', 'E.G.', 'I.E', 'E.G'}:
                # Sanitize tag for ASCII output
                safe_tag = tag.encode('ascii', 'replace').decode('ascii')
                warnings.append(f"Unknown bracket tag: [{safe_tag}]")
    
    # Check for section-level classification
    # Look for section headers with classification in them
    section_pattern = re.compile(r'^(#{2,4})\s+(.+)$', re.MULTILINE)
    sections = section_pattern.findall(content)
    
    classified_sections = 0
    for level, title in sections:
        if any(tag in title for tag in valid_tags):
            classified_sections += 1
    
    print(f"Total sections: {len(sections)}")
    print(f"Sections with classification in header: {classified_sections}")
    
    # Check for executive summary confidence bars
    confidence_bars = re.findall(r'█+░*', content)
    if confidence_bars:
        print(f"Confidence bars found: {len(confidence_bars)}")
    else:
        warnings.append("No confidence bars (█░) found in document")
    
    # Check for speculative content without marking
    # FIXED: Replace variable-width look-behind with a fixed-width approach
    # Instead of look-behind, we check if the keyword is NOT preceded by a tag
    speculative_keywords = [
        'may ', 'might ', 'could ', 'potentially ', 'likely ',
        'predicted ', 'forecast ', 'projected ', 'estimated ',
        'hypothesize', 'conjecture', 'speculate', 'assume '
    ]
    
    speculative_unmarked = 0
    for keyword in speculative_keywords:
        # Find all occurrences of the keyword
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        for match in pattern.finditer(content):
            # Check if there's a classification tag within 50 chars before
            start = max(0, match.start() - 50)
            context = content[start:match.start()]
            if not any(tag in context for tag in valid_tags):
                speculative_unmarked += 1
    
    if speculative_unmarked > 5:
        warnings.append(f"Possible unmarked speculative language: {speculative_unmarked} occurrences of hedging keywords")
    
    # Check for unverified claims masquerading as facts
    fact_keywords = ['proves', 'demonstrates', 'establishes', 'confirms', 'shows that', 'proven']
    unverified_facts = 0
    for keyword in fact_keywords:
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        for match in pattern.finditer(content):
            start = max(0, match.start() - 50)
            context = content[start:match.start()]
            if not any(tag in context for tag in ['VERIFIED', 'HIGH CONFIDENCE']):
                unverified_facts += 1
    
    if unverified_facts > 10:
        warnings.append(f"Possible unverified factual claims: {unverified_facts} occurrences of strong assertion keywords")
    
    # Check for missing appendix classification table
    if 'Classification Summary' not in content and 'classification table' not in content.lower():
        warnings.append("No classification summary table found in appendix")
    
    # Check for consistent tag formatting
    bad_format = re.findall(r'\[verified\]|\[high confidence\]|\[moderate\]|\[speculative\]', content, re.IGNORECASE)
    if bad_format:
        warnings.append(f"Inconsistent tag capitalization: {len(bad_format)} occurrences")
    
    # Report
    if errors:
        print(f"\n{CROSS} ERRORS:")
        for e in errors:
            safe_e = e.encode('ascii', 'replace').decode('ascii')
            print(f"  - {safe_e}")
    
    if warnings:
        print(f"\n{WARN} WARNINGS:")
        for w in warnings:
            safe_w = w.encode('ascii', 'replace').decode('ascii')
            print(f"  - {safe_w}")
    
    if not errors and not warnings:
        print(f"{CHECK} Content classification compliant")
        return True
    elif not errors:
        print(f"\n{WARN} Warnings only - review recommended")
        return True
    else:
        print(f"\n{CROSS} {len(errors)} error(s) found")
        return False

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "manuscript/final-report.md"
    success = check_classification(filepath)
    sys.exit(0 if success else 1)