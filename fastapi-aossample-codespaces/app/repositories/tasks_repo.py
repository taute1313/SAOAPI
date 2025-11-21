from typing import Dict, List, Optional
from uuid import UUID
from app.schemas.task import Task, TaskCreate, TaskUpdate
import json
from pathlib import Path

DATA_FILE = Path("data/tasks.json")


class TasksRepository:
    def __init__(self):
        self._tasks: Dict[UUID, Task] = {}
        self._load_from_file()

    # ---- Persistencia en JSON ----
    def _load_from_file(self) -> None:
        if not DATA_FILE.exists():
            return
        try:
            raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            for item in raw:
                task = Task(**item)
                self._tasks[task.id] = task
        except Exception as e:
            print(f"[WARN] No se pudo cargar {DATA_FILE}: {e}")

    def _save_to_file(self) -> None:
        try:
            # Convertimos los Task a dict (convertible a JSON)
            data = [t.model_dump() for t in self._tasks.values()]
            DATA_FILE.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
        except Exception as e:
            print(f"[WARN] No se pudo guardar en {DATA_FILE}: {e}")

    # ---- Métodos públicos ----
    def list(self, skip: int = 0, limit: int = 50,
             completed: Optional[bool] = None,
             q: Optional[str] = None,
             priority: Optional[str] = None) -> List[Task]:
        values = list(self._tasks.values())

        if completed is not None:
            values = [t for t in values if t.completed == completed]

        if priority is not None:
            values = [t for t in values if t.priority == priority]

        if q:
            q_low = q.lower()
            values = [
                t for t in values
                if q_low in t.title.lower()
                or (t.description and q_low in t.description.lower())
            ]

        return values[skip: skip + limit]

    def get(self, task_id: UUID) -> Optional[Task]:
        return self._tasks.get(task_id)

    def create(self, data: TaskCreate) -> Task:
        task = Task(**data.model_dump())
        self._tasks[task.id] = task
        self._save_to_file()
        return task

    def replace(self, task_id: UUID, data: Task) -> Task:
        self._tasks[task_id] = data
        self._save_to_file()
        return data

    def update(self, task_id: UUID, data: TaskUpdate) -> Optional[Task]:
        current = self._tasks.get(task_id)
        if not current:
            return None
        updated = current.model_copy(
            update={k: v for k, v in data.model_dump(exclude_unset=True).items()}
        )
        self._tasks[task_id] = updated
        self._save_to_file()
        return updated

    def delete(self, task_id: UUID) -> bool:
        deleted = self._tasks.pop(task_id, None) is not None
        if deleted:
            self._save_to_file()
        return deleted

    # Extra: marcar todas como completadas
    def complete_all(self) -> int:
        count = 0
        for task_id, task in list(self._tasks.items()):
            if not task.completed:
                updated = task.model_copy(update={"completed": True})
                self._tasks[task_id] = updated
                count += 1
        if count:
            self._save_to_file()
        return count


repo = TasksRepository()
