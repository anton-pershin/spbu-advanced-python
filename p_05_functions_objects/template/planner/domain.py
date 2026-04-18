from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Mapping

TaskPayload = Mapping[str, object]


@dataclass(frozen=True)
class Task:
    task_id: str
    duration: int
    deps: tuple[str, ...]

    def __post_init__(self) -> None:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


Predicate = Callable[[Task], bool]
TaskKey = Callable[[Task], object]


def parse_task(payload: TaskPayload) -> Task:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError


def parse_tasks(payloads: Iterable[TaskPayload]) -> list[Task]:
    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################
    raise NotImplementedError
