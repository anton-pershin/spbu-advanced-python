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
        if not isinstance(self.task_id, str) or not self.task_id:
            raise ValueError("task_id must be a non-empty string")
        if not isinstance(self.duration, int) or isinstance(self.duration, bool) or self.duration <= 0:
            raise ValueError("duration must be a positive integer")
        if len(set(self.deps)) != len(self.deps):
            raise ValueError("deps must not contain duplicates")
        if self.task_id in self.deps:
            raise ValueError("task must not depend on itself")


Predicate = Callable[[Task], bool]
TaskKey = Callable[[Task], object]


def parse_task(payload: TaskPayload) -> Task:
    task_id = payload.get("id")
    duration = payload.get("duration")
    deps = payload.get("deps")

    if not isinstance(task_id, str) or not task_id:
        raise ValueError("task id must be a non-empty string")
    if not isinstance(duration, int) or isinstance(duration, bool) or duration <= 0:
        raise ValueError("duration must be a positive integer")
    if not isinstance(deps, list):
        raise ValueError("deps must be a list")
    if any(not isinstance(dep, str) or not dep for dep in deps):
        raise ValueError("each dependency must be a non-empty string")

    return Task(task_id=task_id, duration=duration, deps=tuple(deps))


def parse_tasks(payloads: Iterable[TaskPayload]) -> list[Task]:
    tasks = [parse_task(payload) for payload in payloads]
    ids = [task.task_id for task in tasks]
    if len(set(ids)) != len(ids):
        raise ValueError("task ids must be unique")
    return tasks
