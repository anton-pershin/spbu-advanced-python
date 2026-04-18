from __future__ import annotations

from functools import reduce
from typing import Iterable

from .domain import Predicate, Task


def has_duration_at_least(min_duration: int, task: Task) -> bool:
    return task.duration >= min_duration


def depends_on(dep_id: str, task: Task) -> bool:
    return dep_id in task.deps


def filter_tasks(tasks: Iterable[Task], predicate: Predicate) -> list[Task]:
    return [task for task in tasks if predicate(task)]


def select_tasks(tasks: Iterable[Task], predicates: Iterable[Predicate], *, mode: str = "all") -> list[Task]:
    predicates_tuple = tuple(predicates)
    if mode not in {"all", "any"}:
        raise ValueError("mode must be 'all' or 'any'")

    if mode == "all":
        return [task for task in tasks if all(predicate(task) for predicate in predicates_tuple)]
    return [task for task in tasks if any(predicate(task) for predicate in predicates_tuple)]


def task_ids(tasks: Iterable[Task]) -> list[str]:
    return [task.task_id for task in tasks]


def total_duration(tasks: Iterable[Task]) -> int:
    return reduce(lambda acc, task: acc + task.duration, tasks, 0)


def max_parallelism(layers: Iterable[Iterable[Task]]) -> int:
    return max((len(tuple(layer)) for layer in layers), default=0)
