"""Frequency computation helpers."""

from __future__ import annotations

from collections import Counter


def count_words(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))


def top_n(freqs: dict[str, int], n: int) -> list[tuple[str, int]]:
    items = list(freqs.items())
    items.sort(key=lambda kv: (-kv[1], kv[0]))
    return items[:n]
