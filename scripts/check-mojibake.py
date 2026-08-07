#!/usr/bin/env python3
"""
Mojibake detection script for Silver Mosaic manuscript.
Detects encoding corruption artifacts (mojibake) in the manuscript.
Distinct from check-encoding.py which validates UTF-8 encoding;
this script specifically detects and reports mojibake patterns.
"""

import re
import sys
from pathlib import Path

# Use ASCII-safe output for Windows console compatibility
CHECK = "[OK]"
CROSS = "[ERR]"
WARN = "[WARN]"
INFO = "[INFO]"

def safe_print(s):
    """Print string with unsafe characters replaced."""
    replacements = {
        '\u20b9': "[RUPEE]",
        '\u20ac': "[EURO]",
        '\u2014': "[EM-DASH]",
        '\u2013': "[EN-DASH]",
        '\u201c': "[LDQUO]",
        '\u201d': "[RDQUO]",
        '\u2018': "[LSQUO]",
        '\u2019': "[RSQUO]",
        '\u2030': "[PERMILLE]",
        '\u2022': "[BULLET]",
        '\u2026': "[ELLIPSIS]",
    }
    for unsafe, safe in replacements.items():
        s = s.replace(unsafe, safe)
    print(s)

def check_mojibake(filepath):
    """Detect mojibake encoding corruption in the manuscript."""
    with open(filepath, 'rb') as f:
        content = f.read()
    
    errors = []
    warnings = []
    
    # Known mojibake patterns (UTF-8 bytes that result from double-encoding)
    # These are specific byte sequences that indicate corruption
    mojibake_patterns = {
        # Double-encoded em-dash: — (U+2014) = E2 80 94 -> double-encoded as C3 A2 E2 80 94 or similar
        b'\xc3\xa2\xe2\x80\x94': 'em-dash (—) double-encoded',
        b'\xc3\xa2\xe2\x80\x93': 'en-dash (–) double-encoded',
        b'\xc3\xa2\xe2\x80\x9c': 'left double quote (") double-encoded',
        b'\xc3\xa2\xe2\x80\x9d': 'right double quote (") double-encoded',
        b'\xc3\xa2\xe2\x80\x98': 'left single quote (\') double-encoded',
        b'\xc3\xa2\xe2\x80\x99': 'right single quote (\') double-encoded',
        b'\xc3\xa2\xe2\x80\x9a': 'single low-9 quote double-encoded',
        b'\xc3\xa2\xe2\x80\xb0': 'per mille sign (‰) double-encoded',
        b'\xc3\xa2\xe2\x80\xa2': 'bullet (•) double-encoded',
        b'\xc3\xa2\xe2\x80\xa6': 'ellipsis (…) double-encoded',
        b'\xc3\xa2\xe2\x80\x89': 'thin space ( ) double-encoded',
        b'\xc3\xa2\xe2\x80\x8a': 'hair space ( ) double-encoded',
        b'\xc3\xa2\xe2\x80\x8b': 'zero-width space ( ) double-encoded',
        b'\xc3\xa2\xe2\x80\x8c': 'zero-width non-joiner ( ) double-encoded',
        b'\xc3\xa2\xe2\x80\x8e': 'left-to-right mark ( ) double-encoded',
        b'\xc3\xa2\xe2\x80\x8f': 'right-to-left mark ( ) double-encoded',
        b'\xc3\xa2\xe2\x80\xaa': 'left-to-right embedding ( ) double-encoded',
        b'\xc3\xa2\xe2\x80\xab': 'right-to-left embedding ( ) double-encoded',
        b'\xc3\xa2\xe2\x80\xac': 'pop directional formatting ( ) double-encoded',
        b'\xc3\xa2\xe2\x80\xad': 'left-to-right override ( ) double-encoded',
        b'\xc3\xa2\xe2\x80\xae': 'right-to-left override ( ) double-encoded',
        b'\xc3\xa2\xe2\x81\xa0': 'function application ( ) double-encoded',
        b'\xc3\xa2\xe2\x8a\x92': 'left double angle bracket ( ) double-encoded',
        b'\xc3\xa2\xe2\x8a\x93': 'right double angle bracket ( ) double-encoded',
        b'\xc3\xa2\xe2\x82\xac': 'euro sign (€) double-encoded (appears as â€)',
        b'\xc3\xa2\xe2\x82\xb9': 'rupee sign double-encoded (appears as â₹)',
        b'\xc3\xa2\xe2\x80\xb0': 'per mille (‰) double-encoded',
        b'\xc3\xa2\xe2\x80\x9a': 'single low-9 quote double-encoded',
        
        # Double-encoded Latin-1 accented characters
        b'\xc3\x83\xc2\xa9': 'e-acute (é) double-encoded',
        b'\xc3\x83\xc2\xa8': 'e-grave (è) double-encoded',
        b'\xc3\x83\xc2\xb6': 'o-diaeresis (ö) double-encoded',
        b'\xc3\x83\xc2\xbc': 'u-diaeresis (ü) double-encoded',
        b'\xc3\x83\xc2\x9f': 'sharp-s (ß) double-encoded',
        b'\xc3\x83\xc2\xb1': 'n-tilde (ñ) double-encoded',
        b'\xc3\x83\xc2\xa7': 'c-cedilla (ç) double-encoded',
        b'\xc3\x83\xc2\xa0': 'a-grave (à) double-encoded',
        b'\xc3\x83\xc2\xa1': 'a-acute (á) double-encoded',
        b'\xc3\x83\xc2\xa2': 'a-circumflex (â) double-encoded',
        b'\xc3\x83\xc2\xa3': 'a-tilde (ã) double-encoded',
        b'\xc3\x83\xc2\xa4': 'a-diaeresis (ä) double-encoded',
        b'\xc3\x83\xc2\xa5': 'a-ring (å) double-encoded',
        b'\xc3\x83\xc2\xa6': 'ae-ligature (æ) double-encoded',
        b'\xc3\x83\xc2\xa7': 'c-cedilla (ç) double-encoded',
        b'\xc3\x83\xc2\xa8': 'e-grave (è) double-encoded',
        b'\xc3\x83\xc2\xa9': 'e-acute (é) double-encoded',
        b'\xc3\x83\xc2\xaa': 'e-circumflex (ê) double-encoded',
        b'\xc3\x83\xc2\xab': 'e-diaeresis (ë) double-encoded',
        b'\xc3\x83\xc2\xac': 'i-grave (ì) double-encoded',
        b'\xc3\x83\xc2\xad': 'i-acute (í) double-encoded',
        b'\xc3\x83\xc2\xae': 'i-circumflex (î) double-encoded',
        b'\xc3\x83\xc2\xaf': 'i-diaeresis (ï) double-encoded',
        b'\xc3\x83\xc2\xb0': 'eth (ð) double-encoded',
        b'\xc3\x83\xc2\xb1': 'n-tilde (ñ) double-encoded',
        b'\xc3\x83\xc2\xb2': 'o-grave (ò) double-encoded',
        b'\xc3\x83\xc2\xb3': 'o-acute (ó) double-encoded',
        b'\xc3\x83\xc2\xb4': 'o-circumflex (ô) double-encoded',
        b'\xc3\x83\xc2\xb5': 'o-tilde (õ) double-encoded',
        b'\xc3\x83\xc2\xb6': 'o-diaeresis (ö) double-encoded',
        b'\xc3\x83\xc2\xb7': 'division (÷) double-encoded',
        b'\xc3\x83\xc2\xb8': 'o-slash (ø) double-encoded',
        b'\xc3\x83\xc2\xb9': 'u-grave (ù) double-encoded',
        b'\xc3\x83\xc2\xba': 'u-acute (ú) double-encoded',
        b'\xc3\x83\xc2\xbb': 'u-circumflex (û) double-encoded',
        b'\xc3\x83\xc2\xbc': 'u-diaeresis (ü) double-encoded',
        b'\xc3\x83\xc2\xbd': 'y-acute (ý) double-encoded',
        b'\xc3\x83\xc2\xbe': 'thorn (þ) double-encoded',
        b'\xc3\x83\xc2\xbf': 'y-diaeresis (ÿ) double-encoded',
    }
    
    def safe_print(s):
        replacements = {
            '\u20b9': "[RUPEE]",
            '\u20ac': "[EURO]",
            '\u2014': "[EM-DASH]",
            '\u2013': "[EN-DASH]",
            '\u201c': "[LDQUO]",
            '\u201d': "[RDQUO]",
            '\u2018': "[LSQUO]",
            '\u2019': "[RSQUO]",
            '\u2030': "[PERMILLE]",
            '\u2022': "[BULLET]",
            '\u2026': "[ELLIPSIS]",
        }
        for unsafe, safe in replacements.items():
            s = s.replace(unsafe, safe)
        print(s)
    
    errors = []
    warnings = []
    total_mojibake = 0
    
    # Search for mojibake in the raw bytes
    for pattern_bytes, description in mojibake_patterns.items():
        count = content.count(pattern_bytes)
        if count > 0:
            total_mojibake += count
            errors.append(f"Mojibake detected: {description} appears {count} times")
    
    # Also check for common mojibake indicators in decoded text
    try:
        text = content.decode('utf-8')
        # Look for common mojibake characters in decoded text
        mojibake_chars = {
            '\u00e2': 'latin small letter a with circumflex (â) - likely mojibake',
            '\u20ac': 'euro sign (€) - likely mojibake',
            '\u201c': 'left double quote (") - may be mojibake',
            '\u201d': 'right double quote (") - may be mojibake',
            '\u2018': 'left single quote (\') - may be mojibake',
            '\u2019': 'right single quote (\') - may be mojibake',
            '\u2014': 'em-dash (—) - should be checked if intended',
            '\u2013': 'en-dash (–) - should be checked if intended',
        }
        
        for char, description in mojibake_chars.items():
            count = text.count(char)
            if count > 0:
                # Only warn if it's not likely intentional (e.g., em-dashes in prose are normal)
                if char in ['\u00e2', '\u20ac']:
                    warnings.append(f"Potential mojibake char {description}: appears {count} times")
    except UnicodeDecodeError:
        errors.append("File contains invalid UTF-8 sequences")
    
    # Report
    def safe_print(s):
        replacements = {
            '\u20b9': "[RUPEE]",
            '\u20ac': "[EURO]",
            '\u2014': "[EM-DASH]",
            '\u2013': "[EN-DASH]",
            '\u201c': "[LDQUO]",
            '\u201d': "[RDQUO]",
            '\u2018': "[LSQUO]",
            '\u2019': "[RSQUO]",
            '\u2030': "[PERMILLE]",
            '\u2022': "[BULLET]",
            '\u2026': "[ELLIPSIS]",
        }
        for unsafe, safe in replacements.items():
            s = s.replace(unsafe, safe)
        print(s)
    
    safe_print(f"Mojibake scan complete. Byte-pattern matches: {total_mojibake}")
    
    if errors:
        safe_print(f"\n[ERR] ERRORS:")
        for e in errors:
            safe_print(f"  - {e}")
    
    if warnings:
        safe_print(f"\n[WARN] WARNINGS:")
        for w in warnings:
            safe_print(f"  - {w}")
    
    if not errors and not warnings:
        safe_print("[OK] No mojibake detected")
        return True
    elif not errors:
        safe_print(f"\n[WARN] Warnings only - review recommended")
        return True
    else:
        safe_print(f"\n[ERR] {len(errors)} mojibake error(s) detected")
        return False

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "manuscript/final-report.md"
    success = check_mojibake(filepath)
    sys.exit(0 if success else 1)