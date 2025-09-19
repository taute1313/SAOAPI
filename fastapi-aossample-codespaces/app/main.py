from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/healthz")
async def healthz():
    return {"status": "ok", "env": settings.env}

app.include_router(api_router)
