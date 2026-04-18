from __future__ import annotations

from typing import Dict, Iterable, Set, Tuple

from .domain import Task, TaskKey


def build_dependency_maps(
    tasks: Iterable[Task],
) -> Tuple[Dict[str, Task], Dict[str, Set[str]], Dict[str, Set[str]]]:
    task_list = list(tasks)
    task_map = {task.task_id: task for task in task_list}
    if len(task_map) != len(task_list):
        raise ValueError("task ids must be unique")

    parents = {task.task_id: set(task.deps) for task in task_list}
    children = {task.task_id: set() for task in task_list}

    for task in task_list:
        for dep in task.deps:
            if dep not in task_map:
                raise ValueError(f"unknown dependency: {dep}")
            children[dep].add(task.task_id)

    return task_map, parents, children


def _effective_key(ready_key: TaskKey | None) -> TaskKey:
    if ready_key is None:
        return lambda task: task.task_id
    return ready_key


def topological_order(tasks: Iterable[Task], *, ready_key: TaskKey | None = None) -> list[Task]:
    task_map, parents, children = build_dependency_maps(tasks)
    indegree = {task_id: len(deps) for task_id, deps in parents.items()}
    key = _effective_key(ready_key)

    ready = [task_map[task_id] for task_id, degree in indegree.items() if degree == 0]
    order: list[Task] = []

    while ready:
        ready.sort(key=key)
        task = ready.pop(0)
        order.append(task)

        for child_id in sorted(children[task.task_id]):
            indegree[child_id] -= 1
            if indegree[child_id] == 0:
                ready.append(task_map[child_id])

    if len(order) != len(task_map):
        raise ValueError("dependency graph contains a cycle")

    return order


def execution_layers(tasks: Iterable[Task], *, ready_key: TaskKey | None = None) -> list[list[Task]]:
    task_map, parents, children = build_dependency_maps(tasks)
    indegree = {task_id: len(deps) for task_id, deps in parents.items()}
    key = _effective_key(ready_key)

    ready = [task_map[task_id] for task_id, degree in indegree.items() if degree == 0]
    layers: list[list[Task]] = []
    processed = 0

    while ready:
        current_layer = sorted(ready, key=key)
        layers.append(current_layer)
        processed += len(current_layer)
        ready = []

        for task in current_layer:
            for child_id in sorted(children[task.task_id]):
                indegree[child_id] -= 1
                if indegree[child_id] == 0:
                    ready.append(task_map[child_id])

    if processed != len(task_map):
        raise ValueError("dependency graph contains a cycle")

    return layers


def detect_cycle(tasks: Iterable[Task]) -> bool:
    try:
        topological_order(tasks)
    except ValueError:
        return True
    return False
