# 📝 (FastAPI Tasks API)

## 1️⃣ Descripción general  
La API permite crear, listar, actualizar y eliminar tareas, y además cuenta con persistencia en un archivo JSON y un frontend sencillo en HTML para interactuar con ella.

---

## 2️⃣ Arquitectura del proyecto
El proyecto está organizado en módulos siguiendo una estructura clara:

- **app/main.py** → Inicializa FastAPI, monta `/static` y carga el frontend.
- **app/api/v1/** → Contiene los endpoints de la API.
- **app/schemas/** → Define los modelos de datos usando Pydantic.
- **app/repositories/** → Maneja la lógica CRUD y la persistencia en JSON.
- **app/static/** → Contiene el frontend `index.html`.
- **data/tasks.json** → Almacena las tareas creadas.

---

## 3️⃣ Sistema CRUD implementado
La API soporta:

- **POST /tasks** → Crear tareas  
- **GET /tasks** → Listar tareas (con filtros avanzados)  
- **PATCH /tasks/{id}** → Actualización parcial  
- **PUT /tasks/{id}** → Reemplazo total  
- **DELETE /tasks/{id}** → Eliminar tareas  
- **POST /tasks/complete_all** → Marcar todas como completadas  

---

## 4️⃣ Persistencia en JSON
Cada operación modifica un archivo `data/tasks.json`, lo que significa que:

- Las tareas **no se pierden** al reiniciar el servidor.
- Se recargan automáticamente al iniciar FastAPI.

Esto simula una base de datos ligera.


---

## 6️⃣ Frontend sencillo
Incluye una página HTML básica con:

- Formulario para crear tareas  
- Botón para recargar tareas  
- Listado dinámico extraído desde la API  

Esto hace más visual el funcionamiento.

---

## 7️⃣ Pruebas automáticas
El proyecto usa pytest para validar:

- La salud del servicio (`/healthz`)
- El flujo CRUD completo

Esto asegura estabilidad y correctitud.

---
