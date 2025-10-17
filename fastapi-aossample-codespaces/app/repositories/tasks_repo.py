from typing import Dict, List, Optional
from uuid import UUID
from app.schemas.task import Task, TaskCreate, TaskUpdate

class TasksRepository:
    def __init__(self):
        self._tasks: Dict[UUID, Task] = {}

    def list(self, skip: int = 0, limit: int = 50,
             completed: Optional[bool] = None, q: Optional[str] = None) -> List[Task]:
        values = list(self._tasks.values())
        if completed is not None:
            values = [t for t in values if t.completed == completed]
        if q:
            ql = q.lower()
            values = [t for t in values if ql in t.title.lower() or (t.description and ql in t.description.lower())]
        return values[skip: skip + limit]

    def get(self, task_id: UUID) -> Optional[Task]:
        return self._tasks.get(task_id)

    def create(self, data: TaskCreate) -> Task:
        task = Task(**data.model_dump())
        self._tasks[task.id] = task
        return task

    def replace(self, task_id: UUID, data: Task) -> Task:
        self._tasks[task_id] = data
        return data

    def update(self, task_id: UUID, data: TaskUpdate) -> Optional[Task]:
        current = self._tasks.get(task_id)
        if not current:
            return None
        updated = current.model_copy(update={k: v for k, v in data.model_dump(exclude_unset=True).items()})
        self._tasks[task_id] = updated
        return updated

    def delete(self, task_id: UUID) -> bool:
        return self._tasks.pop(task_id, None) is not None

repo = TasksRepository()
