from fastapi import APIRouter
from .endpoints import items

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(items.router)
