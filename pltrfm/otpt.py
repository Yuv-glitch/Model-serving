import re

leak_patterns = [
    r"(?i)safety policy",
    r"(?i)system prompt",
    r"(?i)as a language model",
    r"(?i)internal instruction",
    r"(?i)do not reveal",
]

compiled = [re.compile(p) for p in leak_patterns]

def is_leaking_output(text: str) -> bool:
    return any(p.search(text) for p in compiled)
