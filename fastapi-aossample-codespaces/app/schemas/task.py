from typing import Optional, List
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import date

class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = None
    completed: bool = False
    due_date: Optional[date] = None
    tags: List[str] = []

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[date] = None
    tags: Optional[List[str]] = None

class Task(TaskBase):
    id: UUID = Field(default_factory=uuid4)
