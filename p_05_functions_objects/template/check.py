"""Lightweight checks (no pytest yet).

Run from repo root:

python -m p_05_functions_objects.template.check

The checks intentionally use only the public API:

from p_05_functions_objects.template.planner import ...
"""

from __future__ import annotations

from functools import partial

from p_05_functions_objects.template.planner import (
    Task,
    detect_cycle,
    execution_layers,
    filter_tasks,
    has_duration_at_least,
    depends_on,
    max_parallelism,
    parse_tasks,
    select_tasks,
    task_ids,
    topological_order,
    total_duration,
)


def _sample_payloads() -> list[dict[str, object]]:
    return [
        {"id": "parse", "duration": 2, "deps": []},
        {"id": "compile", "duration": 5, "deps": ["parse"]},
        {"id": "lint", "duration": 1, "deps": ["parse"]},
        {"id": "test", "duration": 3, "deps": ["compile"]},
        {"id": "report", "duration": 1, "deps": ["lint", "test"]},
    ]


def test_parse_tasks_and_invariants() -> None:
    tasks = parse_tasks(_sample_payloads())
    assert len(tasks) == 5
    assert tasks[0] == Task(task_id="parse", duration=2, deps=())

    try:
        parse_tasks(
            [
                {"id": "a", "duration": 1, "deps": []},
                {"id": "a", "duration": 2, "deps": []},
            ]
        )
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate task ids must be rejected")


def test_topological_order_with_default_and_custom_key() -> None:
    tasks = parse_tasks(_sample_payloads())

    default_order = topological_order(tasks)
    assert task_ids(default_order) == ["parse", "compile", "lint", "test", "report"]

    duration_order = topological_order(tasks, ready_key=lambda task: (task.duration, task.task_id))
    assert task_ids(duration_order) == ["parse", "lint", "compile", "test", "report"]


def test_execution_layers_and_parallelism() -> None:
    tasks = parse_tasks(_sample_payloads())
    layers = execution_layers(tasks)

    assert [[task.task_id for task in layer] for layer in layers] == [
        ["parse"],
        ["compile", "lint"],
        ["test"],
        ["report"],
    ]
    assert max_parallelism(layers) == 2


def test_cycle_detection() -> None:
    cyclic = parse_tasks(
        [
            {"id": "a", "duration": 1, "deps": ["c"]},
            {"id": "b", "duration": 1, "deps": ["a"]},
            {"id": "c", "duration": 1, "deps": ["b"]},
        ]
    )
    assert detect_cycle(cyclic) is True


def test_predicates_any_all_partial_and_reduce() -> None:
    tasks = parse_tasks(_sample_payloads())

    long_task = partial(has_duration_at_least, 3)
    depends_on_parse = partial(depends_on, "parse")

    filtered = filter_tasks(tasks, long_task)
    assert task_ids(filtered) == ["compile", "test"]

    any_selected = select_tasks(tasks, [long_task, depends_on_parse], mode="any")
    assert task_ids(any_selected) == ["compile", "lint", "test"]

    all_selected = select_tasks(tasks, [long_task, depends_on_parse], mode="all")
    assert task_ids(all_selected) == ["compile"]

    assert total_duration(filtered) == 8


def main() -> int:
    tests = [
        test_parse_tasks_and_invariants,
        test_topological_order_with_default_and_custom_key,
        test_execution_layers_and_parallelism,
        test_cycle_detection,
        test_predicates_any_all_partial_and_reduce,
    ]

    for t in tests:
        t()

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
