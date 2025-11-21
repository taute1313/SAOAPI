# 🚀 Guía rápida para ejecutar el proyecto en GitHub Codespaces

## 🧭 1️⃣ Abrir el proyecto en Codespaces
1. Entra a tu repositorio en GitHub.  
2. Haz clic en **Code → Codespaces → Create codespace on main**.  
3. Se abrirá un entorno VS Code completo en el navegador.

---

## ⚙️ 2️⃣ Activar el entorno virtual
En la terminal del Codespace, ejecuta:

```bash
python -m venv .venv
source .venv/bin/activate

## 📦 3️⃣ Instalar dependencias
pip install -r requirements.txt


## ▶️ 4️⃣ Ejecutar la API
uvicorn app.main:app --host 0.0.0.0 --port 8000

## 📘 6️⃣ Probar la API en Swagger
/docs

## 🧪 7️⃣ Ejecutar tests automáticos
pytest -v
