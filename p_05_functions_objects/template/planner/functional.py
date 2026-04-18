from __future__ import annotations

from functools import reduce
from typing import Iterable

from .domain import Predicate, Task


def has_duration_at_least(min_duration: int, task: Task) -> bool:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def depends_on(dep_id: str, task: Task) -> bool:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def filter_tasks(tasks: Iterable[Task], predicate: Predicate) -> list[Task]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def select_tasks(tasks: Iterable[Task], predicates: Iterable[Predicate], *, mode: str = "all") -> list[Task]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def task_ids(tasks: Iterable[Task]) -> list[str]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def total_duration(tasks: Iterable[Task]) -> int:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def max_parallelism(layers: Iterable[Iterable[Task]]) -> int:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError
