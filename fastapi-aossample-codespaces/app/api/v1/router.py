from fastapi import APIRouter
from .endpoints import tasks

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(tasks.router)
