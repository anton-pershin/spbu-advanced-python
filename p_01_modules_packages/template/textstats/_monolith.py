"""Monolithic implementation ("before" refactor).

This module is intentionally written as a single file to demonstrate why splitting into
modules and packages is useful.

Run from repo root:

python -m p_01_modules_packages.template.textstats._monolith p_01_modules_packages/template/data/sample.txt --top 10
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


WORD_RE = re.compile(r"[0-9A-Za-zА-Яа-яЁё]+")


def tokenize(text: str, *, lower: bool) -> list[str]:
    tokens = WORD_RE.findall(text)
    if lower:
        tokens = [t.lower() for t in tokens]
    return tokens


def read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8", errors="replace")


def count_words(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))


def top_n(freqs: dict[str, int], n: int) -> list[tuple[str, int]]:
    items = list(freqs.items())
    items.sort(key=lambda kv: (-kv[1], kv[0]))
    return items[:n]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="textstats")
    parser.add_argument("paths", nargs="+", help="Input text files")
    parser.add_argument("--top", type=int, default=10, help="How many items to show")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--lower", dest="lower", action="store_true", default=True)
    group.add_argument("--no-lower", dest="lower", action="store_false")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    all_tokens: list[str] = []
    for p in args.paths:
        all_tokens.extend(tokenize(read_text(p), lower=args.lower))

    freqs = count_words(all_tokens)
    for word, count in top_n(freqs, args.top):
        print(f"{word}\t{count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
