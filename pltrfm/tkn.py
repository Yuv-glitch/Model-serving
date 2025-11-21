import unicodedata

ZERO_WIDTH = ["\u200b", "\u200d", "\u200c", "\u200e", "\u200f", "\ufeff"]

def contains_zero_width(text):
    return any(c in text for c in ZERO_WIDTH)

def contains_homoglyphs(text):
    return any("CYRILLIC" in unicodedata.name(c, "") or
               "GREEK" in unicodedata.name(c, "")
               for c in text)

def token_analyzer(text: str):
    flags = []
    if contains_zero_width(text):
        flags.append("zero-width")
    if contains_homoglyphs(text):
        flags.append("homoglyph")
    return flags
