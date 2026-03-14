"""Text normalization and tokenization."""

from __future__ import annotations

import re


WORD_RE = re.compile(r"[0-9A-Za-zА-Яа-яЁё]+")


def tokenize(text: str, *, lower: bool = True) -> list[str]:
    tokens = WORD_RE.findall(text)
    if lower:
        tokens = [t.lower() for t in tokens]
    return tokens
