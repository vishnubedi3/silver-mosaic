#!/usr/bin/env python3
"""
Encoding validation script for Silver Mosaic manuscript.
Checks for UTF-8 validity and mojibake.
"""

import sys
from pathlib import Path

# Use ASCII-safe output for Windows console compatibility
CHECK = "[OK]"
CROSS = "[ERR]"
WARN = "[WARN]"
INFO = "[INFO]"

# Safe replacements for special characters in output
SAFE_RUPEE = "[RUPEE]"
SAFE_EURO = "[EURO]"
SAFE_EM_DASH = "[EM-DASH]"
SAFE_EN_DASH = "[EN-DASH]"
SAFE_LDQUO = "[LDQUO]"
SAFE_RDQUO = "[RDQUO]"
SAFE_LSQUO = "[LSQUO]"
SAFE_RSQUO = "[RSQUO]"
SAFE_PERMILLE = "[PERMILLE]"
SAFE_BULLET = "[BULLET]"
SAFE_ELLIPSIS = "[ELLIPSIS]"
SAFE_EACUTE = "[E-ACUTE]"
SAFE_EGRAVE = "[E-GRAVE]"
SAFE_ODIAERESIS = "[O-DIAERESIS]"
SAFE_UDIAERESIS = "[U-DIAERESIS]"
SAFE_SHARP_S = "[SHARP-S]"
SAFE_NTILDE = "[N-TILDE]"
SAFE_CCEDILLA = "[C-CEDILLA]"
SAFE_AGRAVE = "[A-GRAVE]"
SAFE_AACUTE = "[A-ACUTE]"
SAFE_ACIRC = "[A-CIRC]"
SAFE_ATILDE = "[A-TILDE]"
SAFE_ADIAERESIS = "[A-DIAERESIS]"
SAFE_ARING = "[A-RING]"
SAFE_AELIG = "[AE-LIG]"
SAFE_CCEDILLA = "[C-CEDILLA]"
SAFE_EGRAVE = "[E-GRAVE]"
SAFE_EACUTE = "[E-ACUTE]"
SAFE_ECIRC = "[E-CIRC]"
SAFE_EDIAERESIS = "[E-DIAERESIS]"
SAFE_IGRAVE = "[I-GRAVE]"
SAFE_IACUTE = "[I-ACUTE]"
SAFE_ICIRC = "[I-CIRC]"
SAFE_IDIAERESIS = "[I-DIAERESIS]"
SAFE_ETH = "[ETH]"
SAFE_NTILDE = "[N-TILDE]"
SAFE_OGRAVE = "[O-GRAVE]"
SAFE_OACUTE = "[O-ACUTE]"
SAFE_OCIRC = "[O-CIRC]"
SAFE_OTILDE = "[O-TILDE]"
SAFE_ODIAERESIS = "[O-DIAERESIS]"
SAFE_ODIVIDE = "[O-DIVIDE]"
SAFE_OSLASH = "[O-SLASH]"
SAFE_UGRAVE = "[U-GRAVE]"
SAFE_UACUTE = "[U-ACUTE]"
SAFE_UCIRC = "[U-CIRC]"
SAFE_UDIAERESIS = "[U-DIAERESIS]"
SAFE_YACUTE = "[Y-ACUTE]"
SAFE_THORN = "[THORN]"
SAFE_YDIAERESIS = "[Y-DIAERESIS]"

def safe_print(s):
    """Print string with unsafe characters replaced."""
    # Replace common problematic Unicode chars
    replacements = {
        '\u20b9': SAFE_RUPEE,
        '\u20ac': SAFE_EURO,
        '\u2014': SAFE_EM_DASH,
        '\u2013': SAFE_EN_DASH,
        '\u201c': SAFE_LDQUO,
        '\u201d': SAFE_RDQUO,
        '\u2018': SAFE_LSQUO,
        '\u2019': SAFE_RSQUO,
        '\u2030': SAFE_PERMILLE,
        '\u2022': SAFE_BULLET,
        '\u2026': SAFE_ELLIPSIS,
        '\xe9': SAFE_EACUTE,
        '\xe8': SAFE_EGRAVE,
        '\xf6': SAFE_ODIAERESIS,
        '\xfc': SAFE_UDIAERESIS,
        '\xdf': SAFE_SHARP_S,
        '\xf1': SAFE_NTILDE,
        '\xe7': SAFE_CCEDILLA,
        '\xe0': SAFE_AGRAVE,
        '\xe1': SAFE_AACUTE,
        '\xe2': SAFE_ACIRC,
        '\xe3': SAFE_ATILDE,
        '\xe4': SAFE_ADIAERESIS,
        '\xe5': SAFE_ARING,
        '\xe6': SAFE_AELIG,
        '\xe7': SAFE_CCEDILLA,
        '\xe8': SAFE_EGRAVE,
        '\xe9': SAFE_EACUTE,
        '\xea': SAFE_ECIRC,
        '\xeb': SAFE_EDIAERESIS,
        '\xec': SAFE_IGRAVE,
        '\xed': SAFE_IACUTE,
        '\xee': SAFE_ICIRC,
        '\xef': SAFE_IDIAERESIS,
        '\xf0': SAFE_ETH,
        '\xf1': SAFE_NTILDE,
        '\xf2': SAFE_OGRAVE,
        '\xf3': SAFE_OACUTE,
        '\xf4': SAFE_OCIRC,
        '\xf5': SAFE_OTILDE,
        '\xf6': SAFE_ODIAERESIS,
        '\xf7': SAFE_ODIVIDE,
        '\xf8': SAFE_OSLASH,
        '\xf9': SAFE_UGRAVE,
        '\xfa': SAFE_UACUTE,
        '\xfb': SAFE_UCIRC,
        '\xfc': SAFE_UDIAERESIS,
        '\xfd': SAFE_YACUTE,
        '\xfe': SAFE_THORN,
        '\xff': SAFE_YDIAERESIS,
    }
    for unsafe, safe in replacements.items():
        s = s.replace(unsafe, safe)
    print(s)

def check_encoding(filepath):
    """Check file encoding and detect mojibake."""
    with open(filepath, 'rb') as f:
        content = f.read()
    
    errors = []
    warnings = []
    
    # Check for BOM
    if content.startswith(b'\xef\xbb\xbf'):
        safe_print(f"{CHECK} UTF-8 BOM present")
    elif content.startswith(b'\xff\xfe') or content.startswith(b'\xfe\xff'):
        errors.append("File has UTF-16 BOM - should be UTF-8")
    else:
        warnings.append("No BOM detected (UTF-8 without BOM is acceptable)")
    
    # Try to decode as UTF-8
    try:
        text = content.decode('utf-8')
        safe_print(f"{CHECK} Valid UTF-8 encoding")
    except UnicodeDecodeError as e:
        errors.append(f"Invalid UTF-8 at position {e.start}: {e.reason}")
        return False
    
    # Check for common mojibake patterns as BYTE SEQUENCES (not latin-1 strings)
    # These are the UTF-8 bytes that result from double-encoding common characters
    # Double-encoding: original UTF-8 bytes interpreted as Latin-1, then re-encoded as UTF-8
    mojibake_patterns = {
        # Double-encoded em-dash: — (U+2014) = E2 80 94 -> C3 A2 E2 80 94
        b'\xc3\xa2\xe2\x80\x94': 'em-dash (—) double-encoded',
        # Double-encoded en-dash: – (U+2013) = E2 80 93 -> C3 A2 E2 80 93
        b'\xc3\xa2\xe2\x80\x93': 'en-dash (–) double-encoded',
        # Double-encoded left double quote: " (U+201C) = E2 80 9C -> C3 A2 E2 80 9C
        b'\xc3\xa2\xe2\x80\x9c': 'left double quote (") double-encoded',
        # Double-encoded right double quote: " (U+201D) = E2 80 9D -> C3 A2 E2 80 9D
        b'\xc3\xa2\xe2\x80\x9d': 'right double quote (") double-encoded',
        # Double-encoded left single quote: ' (U+2018) = E2 80 98 -> C3 A2 E2 80 98
        b'\xc3\xa2\xe2\x80\x98': 'left single quote (\') double-encoded',
        # Double-encoded right single quote: ' (U+2019) = E2 80 99 -> C3 A2 E2 80 99
        b'\xc3\xa2\xe2\x80\x99': 'right single quote (\') double-encoded',
        # Double-encoded single low-9 quote: ' (U+201A) = E2 80 9A -> C3 A2 E2 80 9A
        b'\xc3\xa2\xe2\x80\x9a': 'single low-9 quote (\') double-encoded',
        # Double-encoded per mille sign: ‰ (U+2030) = E2 80 B0 -> C3 A2 E2 80 B0
        b'\xc3\xa2\xe2\x80\xb0': 'per mille sign (‰) double-encoded',
        # Double-encoded bullet: • (U+2022) = E2 80 A2 -> C3 A2 E2 80 A2
        b'\xc3\xa2\xe2\x80\xa2': 'bullet (•) double-encoded',
        # Double-encoded ellipsis: … (U+2026) = E2 80 A6 -> C3 A2 E2 80 A6
        b'\xc3\xa2\xe2\x80\xa6': 'ellipsis (…) double-encoded',
        # Double-encoded narrow no-break space: (U+202F) = E2 80 AF -> C3 A2 E2 80 AF
        b'\xc3\xa2\xe2\x80\xaf': 'narrow no-break space double-encoded',
        # Double-encoded medium mathematical space: (U+205F) = E2 81 9F -> C3 A2 E2 81 9F
        b'\xc3\xa2\xe2\x81\x9f': 'medium mathematical space double-encoded',
        # Double-encoded zero-width non-joiner: (U+200C) = E2 80 8C -> C3 A2 E2 80 8C
        b'\xc3\xa2\xe2\x80\x8c': 'zero-width non-joiner double-encoded',
        # Double-encoded left-to-right mark: (U+200E) = E2 80 8E -> C3 A2 E2 80 8E
        b'\xc3\xa2\xe2\x80\x8e': 'left-to-right mark double-encoded',
        # Double-encoded right-to-left mark: (U+200F) = E2 80 8F -> C3 A2 E2 80 8F
        b'\xc3\xa2\xe2\x80\x8f': 'right-to-left mark double-encoded',
        # Double-encoded euro sign: € (U+20AC) = E2 82 AC -> C3 A2 E2 82 AC
        b'\xc3\xa2\xe2\x82\xac': 'euro sign double-encoded',
        # Double-encoded rupee sign: ₹ (U+20B9) = E2 82 B9 -> C3 A2 E2 82 B9
        b'\xc3\xa2\xe2\x82\xb9': 'rupee sign double-encoded',
        # Double-encoded per mille sign: ‰ (U+2030) = E2 80 B0 -> C3 A2 E2 80 B0
        b'\xc3\xa2\xe2\x80\xb0': 'per mille sign double-encoded',
        # Double-encoded single low-9 quote: ' (U+201A) = E2 80 9A -> C3 A2 E2 80 9A
        b'\xc3\xa2\xe2\x80\x9a': 'single low-9 quote double-encoded',
        
        # Double-encoded Latin-1 accented characters (C3 83 prefix)
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
    
    # Search for mojibake in the raw bytes
    for pattern_bytes, description in mojibake_patterns.items():
        count = content.count(pattern_bytes)
        if count > 0:
            errors.append(f"Mojibake detected: {description} appears {count} times")
    
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
        safe_print(f"\n{CROSS} ERRORS:")
        for e in errors:
            safe_print(f"  - {e}")
    
    if warnings:
        safe_print(f"\n{WARN} WARNINGS:")
        for w in warnings:
            safe_print(f"  - {w}")
    
    if not errors and not warnings:
        safe_print(f"{CHECK} Encoding clean")
        return True
    elif not errors:
        safe_print(f"\n{WARN} Warnings only")
        return True
    else:
        safe_print(f"\n{CROSS} {len(errors)} encoding error(s)")
        return False

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "manuscript/final-report.md"
    success = check_encoding(filepath)
    sys.exit(0 if success else 1)