# 🚀 Guía rápida para ejecutar el proyecto en GitHub Codespaces

## 🧭 1️⃣ Abrir el proyecto en Codespaces
1. Entra a tu repositorio en GitHub.  
2. Haz clic en **Code → Codespaces → Create codespace on main**.  
3. Se abrirá un entorno VS Code completo en el navegador.

---

## ⚙️ 2️⃣ Activar el entorno virtual
En la terminal del Codespace, ejecuta:


python -m venv .venv
source .venv/bin/activate

## 📦 Instalar dependencias
pip install -r requirements.txt


## ▶️  Ejecutar la API
uvicorn app.main:app --host 0.0.0.0 --port 8000

## 📘 Probar la API en Swagger
/docs

## 🧪 Ejecutar tests automáticos
pytest -v

```bash

