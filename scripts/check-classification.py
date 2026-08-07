#!/usr/bin/env python3
"""
Content classification check script for Silver Mosaic manuscript.
Validates that all claims have proper classification tags.
"""

import re
import sys
from collections import Counter
from pathlib import Path

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
                warnings.append(f"Unknown bracket tag: [{tag}]")
    
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
    speculative_keywords = [
        'may ', 'might ', 'could ', 'potentially ', 'likely ',
        'predicted ', 'forecast ', 'projected ', 'estimated ',
        'hypothesize', 'conjecture', 'speculate', 'assume '
    ]
    
    speculative_unmarked = 0
    for keyword in speculative_keywords:
        # Find occurrences not near classification tags
        pattern = re.compile(rf'(?<!\[(?:VERIFIED|HIGH CONFIDENCE|MODERATE|SPECULATIVE)\]\s*){keyword}', re.IGNORECASE)
        matches = pattern.findall(content)
        speculative_unmarked += len(matches)
    
    if speculative_unmarked > 5:
        warnings.append(f"Possible unmarked speculative language: {speculative_unmarked} occurrences of hedging keywords")
    
    # Check for unverified claims masquerading as facts
    fact_keywords = ['proves', 'demonstrates', 'establishes', 'confirms', 'shows that', 'proven']
    unverified_facts = 0
    for keyword in fact_keywords:
        pattern = re.compile(rf'(?<!\[(?:VERIFIED|HIGH CONFIDENCE)\]\s*){keyword}', re.IGNORECASE)
        matches = pattern.findall(content)
        unverified_facts += len(matches)
    
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
        print("\nERRORS:")
        for e in errors:
            print(f"  - {e}")
    
    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"  - {w}")
    
    if not errors and not warnings:
        print("✅ Content classification compliant")
        return True
    elif not errors:
        print("\n⚠️  Warnings only - review recommended")
        return True
    else:
        print(f"\n❌ {len(errors)} error(s) found")
        return False

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "manuscript/final-report.md"
    success = check_classification(filepath)
    sys.exit(0 if success else 1)