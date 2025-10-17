from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from uuid import UUID
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.repositories.tasks_repo import repo

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[Task])
async def list_tasks(skip: int = 0, limit: int = 50,
                     completed: Optional[bool] = None, q: Optional[str] = None):
    return repo.list(skip=skip, limit=limit, completed=completed, q=q)

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(payload: TaskCreate):
    return repo.create(payload)

@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: UUID):
    task = repo.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=Task)
async def replace_task(task_id: UUID, payload: Task):
    if task_id != payload.id:
        raise HTTPException(status_code=400, detail="Path id and body id mismatch")
    return repo.replace(task_id, payload)

@router.patch("/{task_id}", response_model=Task)
async def update_task(task_id: UUID, payload: TaskUpdate):
    updated = repo.update(task_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: UUID):
    deleted = repo.delete(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
