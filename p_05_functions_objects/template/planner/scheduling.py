from __future__ import annotations

from collections import deque
from typing import Deque, Dict, Iterable, Set, Tuple

from .domain import Task, TaskKey


def build_dependency_maps(
    tasks: Iterable[Task],
) -> Tuple[Dict[str, Task], Dict[str, Set[str]], Dict[str, Set[str]]]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def topological_order(tasks: Iterable[Task], *, ready_key: TaskKey | None = None) -> list[Task]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def execution_layers(tasks: Iterable[Task], *, ready_key: TaskKey | None = None) -> list[list[Task]]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def detect_cycle(tasks: Iterable[Task]) -> bool:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError
