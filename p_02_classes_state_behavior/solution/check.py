"""Solution checker (same as template checks).

Run from repo root:

python -m p_02_classes_state_behavior.solution.check
"""

from __future__ import annotations

from p_02_classes_state_behavior.solution.lrucache import LRUCache


def test_basic_put_get() -> None:
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)

    assert cache.get("a") == 1
    assert cache.get("b") == 2
    assert len(cache) == 2


def test_eviction_order() -> None:
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)

    assert cache.get("a") == 1
    cache.put("c", 3)

    assert cache.get("b", default="MISSING") == "MISSING"
    assert cache.items() == [("c", 3), ("a", 1)]


def test_update_existing_key() -> None:
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)

    cache.put("a", 10)
    assert cache.get("a") == 10
    assert cache.items() == [("a", 10), ("b", 2)]


def test_contains_and_len() -> None:
    cache = LRUCache(capacity=1)
    assert "x" not in cache

    cache.put("x", 123)
    assert "x" in cache
    assert len(cache) == 1

    cache.put("y", 999)
    assert "x" not in cache
    assert "y" in cache
    assert len(cache) == 1


def test_capacity_five_eviction() -> None:
    cache = LRUCache(capacity=5)

    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    cache.put("d", 4)
    cache.put("e", 5)

    assert cache.items() == [("e", 5), ("d", 4), ("c", 3), ("b", 2), ("a", 1)]

    assert cache.get("b") == 2
    assert cache.get("a") == 1

    cache.put("f", 6)

    assert cache.get("c", default="MISSING") == "MISSING"
    assert cache.items() == [("f", 6), ("a", 1), ("b", 2), ("e", 5), ("d", 4)]
    assert len(cache) == 5


def test_capacity_validation() -> None:
    try:
        LRUCache(capacity=0)
    except ValueError:
        pass
    else:
        raise AssertionError("capacity=0 must raise ValueError")


def main() -> int:
    tests = [
        test_basic_put_get,
        test_eviction_order,
        test_update_existing_key,
        test_contains_and_len,
        test_capacity_five_eviction,
        test_capacity_validation,
    ]

    for t in tests:
        t()

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
