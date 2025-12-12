const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = 3000; // El puerto que usará el usuario
const FASTAPI_URL = 'http://127.0.0.1:8000/api/v1/tasks'; // Donde vive Python

app.use(cors());
app.use(express.json());

// 1️⃣ SERVIR EL FRONTEND (HTML)
// Le decimos a Node que sirva los archivos de la carpeta app/static
app.use(express.static(path.join(__dirname, 'app/static')));


// 2️⃣ RUTAS DE INTERMEDIACIÓN (PROXY)
// Cuando la web pida /api/v1/tasks, Node se lo pedirá a Python

// Helper para hacer las llamadas a Python
async function forwardRequest(method, path = '', body = null) {
    const options = {
        method: method,
        headers: { 'Content-Type': 'application/json' }
    };
    if (body) options.body = JSON.stringify(body);
    
    // fetch nativo de Node 18+
    const response = await fetch(`${FASTAPI_URL}${path}`, options);
    
    if (response.status === 204) return null; // Sin contenido (Delete)
    return await response.json();
}

// --- Endpoints Espejo ---

// GET: Listar
app.get('/api/v1/tasks', async (req, res) => {
    try {
        console.log('🔄 Intermediando GET tasks...');
        const data = await forwardRequest('GET');
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// POST: Crear
app.post('/api/v1/tasks', async (req, res) => {
    try {
        console.log('🔄 Intermediando POST task...');
        const data = await forwardRequest('POST', '', req.body);
        res.status(201).json(data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// PATCH: Actualizar
app.patch('/api/v1/tasks/:id', async (req, res) => {
    try {
        const { id } = req.params;
        console.log(`🔄 Intermediando PATCH task ${id}...`);
        const data = await forwardRequest('PATCH', `/${id}`, req.body);
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// DELETE: Borrar
app.delete('/api/v1/tasks/:id', async (req, res) => {
    try {
        const { id } = req.params;
        console.log(`🔄 Intermediando DELETE task ${id}...`);
        await forwardRequest('DELETE', `/${id}`);
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});


// Arrancar servidor
app.listen(PORT, () => {
    console.log(`\n🛡️  Middleware de seguridad activo en: http://localhost:${PORT}`);
    console.log(`🔗 Conectado internamente a FastAPI en: ${FASTAPI_URL}`);
});
