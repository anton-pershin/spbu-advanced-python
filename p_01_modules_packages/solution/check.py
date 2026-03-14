"""Self-checks for the reference solution."""

from __future__ import annotations

from p_01_modules_packages.solution.textstats import count_words, top_n, tokenize


def test_tokenize_lowering() -> None:
    tokens = tokenize("Hello, HELLO!", lower=True)
    assert tokens == ["hello", "hello"]


def test_tokenize_no_lowering() -> None:
    tokens = tokenize("Hello, HELLO!", lower=False)
    assert tokens == ["Hello", "HELLO"]


def test_count_words() -> None:
    freqs = count_words(["a", "b", "a"])
    assert freqs == {"a": 2, "b": 1}


def test_top_n_ordering() -> None:
    freqs = {"b": 2, "a": 2, "c": 1}
    assert top_n(freqs, 2) == [("a", 2), ("b", 2)]


def main() -> int:
    tests = [
        test_tokenize_lowering,
        test_tokenize_no_lowering,
        test_count_words,
        test_top_n_ordering,
    ]

    for t in tests:
        t()

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
