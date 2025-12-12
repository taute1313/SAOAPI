from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# --- MODELO DE DATOS ACTUALIZADO ---
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = ""  # <--- NUEVO CAMPO
    priority: str = "Media"
    completed: bool = False

# Base de datos simulada en memoria
tasks_db = []
current_id = 1

# Servir archivos estáticos (el frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    # Intenta buscar index.html en static, si no está, busca en la raíz
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html")
    return {"message": "Por favor, crea la carpeta 'static' y pon 'index.html' dentro."}

# --- API ENDPOINTS ---

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks_db

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    global current_id
    task.id = current_id
    current_id += 1
    tasks_db.append(task)
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    global tasks_db
    tasks_db = [t for t in tasks_db if t.id != task_id]
    return {"message": "Tarea eliminada"}

@app.put("/tasks/{task_id}/complete")
async def complete_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            task.completed = not task.completed
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
