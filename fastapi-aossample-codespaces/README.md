# fastapi-aossample (Codespaces Ready)

Plantilla sencilla para crear APIs con FastAPI (CRUD de Item), lista para GitHub Codespaces.

## Ejecutar en Codespaces
1. Crea un Codespace: Code → Codespaces → Create codespace on main.
2. Activa el entorno y ejecuta:
```bash
source .venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
3. Abre el puerto 8000 en el navegador (se abrirá solo).

## Local
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# → http://127.0.0.1:8000/docs
```
