#!/usr/bin/env python3
"""
Encoding validation script for Silver Mosaic manuscript.
Checks for UTF-8 validity and mojibake.
"""

import sys
from pathlib import Path

def check_encoding(filepath):
    """Check file encoding and detect mojibake."""
    with open(filepath, 'rb') as f:
        content = f.read()
    
    errors = []
    warnings = []
    
    # Check for BOM
    if content.startswith(b'\xef\xbb\xbf'):
        print("✅ UTF-8 BOM present")
    elif content.startswith(b'\xff\xfe') or content.startswith(b'\xfe\xff'):
        errors.append("File has UTF-16 BOM - should be UTF-8")
    else:
        warnings.append("No BOM detected (UTF-8 without BOM is acceptable)")
    
    # Try to decode as UTF-8
    try:
        text = content.decode('utf-8')
        print("✅ Valid UTF-8 encoding")
    except UnicodeDecodeError as e:
        errors.append(f"Invalid UTF-8 at position {e.start}: {e.reason}")
        return False
    
    # Check for common mojibake patterns
    mojibake_patterns = {
        'â€"': 'em-dash (—)',
        'â€"': 'en-dash (–)',
        'â€œ': 'left double quote (")',
        'â€': 'right double quote (")',
        'â€\u0153': 'left single quote (\')',
        'â€\u0099': 'right single quote (\')',
        'â\u20ac': 'euro sign (€)',
        'â\u20ac\u0153': 'rupee sign (₹)',
        'Ã©': 'e-acute (é)',
        'Ã¨': 'e-grave (è)',
        'Ã¶': 'o-diaeresis (ö)',
        'Ã¼': 'u-diaeresis (ü)',
        'ÃŸ': 'sharp-s (ß)',
        'Ã±': 'n-tilde (ñ)',
        'Ã§': 'c-cedilla (ç)',
        'Ã ': 'a-grave (à)',
        'Ã¡': 'a-acute (á)',
        'Ã¢': 'a-circumflex (â)',
        'Ã£': 'a-tilde (ã)',
        'Ã¤': 'a-diaeresis (ä)',
        'Ã¥': 'a-ring (å)',
        'Ã¦': 'ae-ligature (æ)',
        'Ã§': 'c-cedilla (ç)',
        'Ã¨': 'e-grave (è)',
        'Ã©': 'e-acute (é)',
        'Ãª': 'e-circumflex (ê)',
        'Ã«': 'e-diaeresis (ë)',
        'Ã¬': 'i-grave (ì)',
        'Ã­': 'i-acute (í)',
        'Ã®': 'i-circumflex (î)',
        'Ã¯': 'i-diaeresis (ï)',
        'Ã°': 'eth (ð)',
        'Ã±': 'n-tilde (ñ)',
        'Ã²': 'o-grave (ò)',
        'Ã³': 'o-acute (ó)',
        'Ã´': 'o-circumflex (ô)',
        'Ãµ': 'o-tilde (õ)',
        'Ã¶': 'o-diaeresis (ö)',
        'Ã·': 'division (÷)',
        'Ã¸': 'o-slash (ø)',
        'Ã¹': 'u-grave (ù)',
        'Ãº': 'u-acute (ú)',
        'Ã»': 'u-circumflex (û)',
        'Ã¼': 'u-diaeresis (ü)',
        'Ã½': 'y-acute (ý)',
        'Ã¾': 'thorn (þ)',
        'Ã¿': 'y-diaeresis (ÿ)',
    }
    
    # Search for mojibake in the raw bytes
    for pattern, description in mojibake_patterns.items():
        pattern_bytes = pattern.encode('latin-1')
        count = content.count(pattern_bytes)
        if count > 0:
            errors.append(f"Mojibake detected: '{pattern}' ({description}) appears {count} times")
    
    # Check for replacement characters (�)
    replacement_count = text.count('\ufffd')
    if replacement_count > 0:
        errors.append(f"Unicode replacement character (�) appears {replacement_count} times")
    
    # Check for control characters (except normal whitespace)
    control_chars = set()
    for i, ch in enumerate(text):
        if ord(ch) < 32 and ch not in '\n\r\t':
            control_chars.add((ch, ord(ch), i))
    
    if control_chars:
        for ch, code, pos in list(control_chars)[:10]:
            warnings.append(f"Control character U+{code:04X} at position {pos}")
    
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
        print("✅ Encoding clean")
        return True
    elif not errors:
        print("\n⚠️  Warnings only")
        return True
    else:
        print(f"\n❌ {len(errors)} encoding error(s)")
        return False

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "manuscript/final-report.md"
    success = check_encoding(filepath)
    sys.exit(0 if success else 1)