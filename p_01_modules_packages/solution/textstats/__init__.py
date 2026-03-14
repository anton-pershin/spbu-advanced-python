"""Reference solution version of textstats."""

from __future__ import annotations

from .normalize import tokenize
from .stats import count_words, top_n

__all__ = [
    "tokenize",
    "count_words",
    "top_n",
]
