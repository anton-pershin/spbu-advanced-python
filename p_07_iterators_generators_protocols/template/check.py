"""Lightweight checks (no pytest yet).

Run from repo root:

python -m p_07_iterators_generators_protocols.template.check

The checks intentionally use only the public API:

from p_07_iterators_generators_protocols.template.streaming import ...
"""

from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from p_07_iterators_generators_protocols.template.streaming import (
    LineIterator,
    LogRecord,
    build_pipeline,
    chain_sources,
    chunked,
    consume_batches,
    filter_by_level,
    flatten,
    iter_lines,
    load_pipeline,
    parse_log_line,
    parse_records,
    read_lines,
    summarize_levels,
    take,
)


def _sample_lines() -> list[str]:
    return [
        "2024-05-01T10:00:00,INFO,worker started\n",
        "2024-05-01T10:01:00,ERROR,disk full\n",
        "broken line\n",
        "\n",
        "2024-05-01T10:02:00,ERROR,network timeout\n",
        "2024-05-01T10:03:00,WARN,slow request\n",
    ]


class CountingIterable:
    def __init__(self, items: list[int]) -> None:
        self._items = items
        self.next_calls = 0

    def __iter__(self):
        for item in self._items:
            self.next_calls += 1
            yield item


class MemorySource:
    def __init__(self, lines: list[str]) -> None:
        self._lines = lines

    def __iter__(self):
        yield from self._lines


class Collector:
    def __init__(self) -> None:
        self.batches: list[tuple[LogRecord, ...]] = []

    def consume(self, batch):
        self.batches.append(tuple(batch))


def test_line_iterator_and_generator() -> None:
    iterator = LineIterator(["a\n", "b\n"])
    assert iter(iterator) is iterator
    assert next(iterator) == "a"
    assert list(iterator) == ["b"]

    generated = iter_lines(["x\n", "y\n"])
    assert next(generated) == "x"
    assert list(generated) == ["y"]


def test_parse_and_filter_pipeline_bits() -> None:
    record = parse_log_line("2024-05-01T10:01:00,ERROR,disk full")
    assert record == LogRecord(
        timestamp="2024-05-01T10:01:00",
        level="ERROR",
        message="disk full",
    )

    records = list(parse_records(_sample_lines()))
    assert [item.level for item in records] == ["INFO", "ERROR", "ERROR", "WARN"]

    errors = list(filter_by_level(records, "error"))
    assert [item.message for item in errors] == ["disk full", "network timeout"]


def test_take_is_lazy() -> None:
    source = CountingIterable([1, 2, 3, 4])
    assert list(take(source, 2)) == [1, 2]
    assert source.next_calls == 2


def test_flatten_and_chunked() -> None:
    assert list(flatten([[1, 2], (), [3]])) == [1, 2, 3]
    assert list(chunked([1, 2, 3, 4, 5], 2)) == [(1, 2), (3, 4), (5,)]


def test_protocols_and_high_level_pipeline() -> None:
    source = MemorySource(_sample_lines())
    pipeline = build_pipeline(source, level="ERROR", limit=2, chunk_size=1)

    collector = Collector()
    consumed = consume_batches(pipeline, collector)

    assert consumed == 2
    assert [batch[0].message for batch in collector.batches] == ["disk full", "network timeout"]


def test_file_reading_and_summary() -> None:
    with TemporaryDirectory() as tmp_dir:
        path = Path(tmp_dir) / "events.log"
        path.write_text("".join(_sample_lines()), encoding="utf-8")

        assert list(read_lines(str(path)))[:2] == [
            "2024-05-01T10:00:00,INFO,worker started",
            "2024-05-01T10:01:00,ERROR,disk full",
        ]

        combined = list(
            chain_sources(
                [
                    MemorySource(["left\n"]),
                    read_lines(str(path)),
                ]
            )
        )
        assert combined[0] == "left\n"
        assert combined[1] == "2024-05-01T10:00:00,INFO,worker started"

        loaded = list(load_pipeline(str(path), level="ERROR", limit=2, chunk_size=2))
        assert len(loaded) == 1
        assert [record.level for record in loaded[0]] == ["ERROR", "ERROR"]

        summary = summarize_levels(read_lines(str(path)))
        assert summary == {"ERROR": 2, "INFO": 1, "WARN": 1}


def main() -> int:
    tests = [
        test_line_iterator_and_generator,
        test_parse_and_filter_pipeline_bits,
        test_take_is_lazy,
        test_flatten_and_chunked,
        test_protocols_and_high_level_pipeline,
        test_file_reading_and_summary,
    ]

    for test in tests:
        test()

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
