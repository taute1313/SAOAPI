// Configuración base (según tu README y endpoints)
const BASE_URL = 'http://127.0.0.1:8000/api/v1/tasks';

/**
 * Helper para manejar las respuestas
 */
async function handleResponse(response) {
  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Error ${response.status}: ${errorText}`);
  }
  // Si la respuesta no tiene contenido (como en DELETE 204), retorna null
  if (response.status === 204) return null;
  return response.json();
}

/**
 * 1. LISTAR TAREAS (GET /)
 * Equivalente a loadTasks() en tu HTML
 */
async function getTasks() {
  console.log('🔄 Obteniendo lista de tareas...');
  try {
    const response = await fetch(`${BASE_URL}/`);
    const tasks = await handleResponse(response);
    console.log(`✅ Tareas encontradas: ${tasks.length}`);
    tasks.forEach(t => console.log(`   - [${t.priority}] ${t.title} (ID: ${t.id})`));
    return tasks;
  } catch (error) {
    console.error('❌ Error al obtener tareas:', error.message);
  }
}

/**
 * 2. CREAR TAREA (POST /)
 * Equivalente al formulario del HTML
 */
async function createTask(title, description = "", priority = "medium") {
  console.log(`\n➕ Creando tarea: "${title}"...`);
  const payload = {
    title: title,
    description: description,
    priority: priority,
    completed: false,
    tags: ["nodejs-client"]
  };

  try {
    const response = await fetch(`${BASE_URL}/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const newTask = await handleResponse(response);
    console.log(`✅ Tarea creada con éxito: ID ${newTask.id}`);
    return newTask;
  } catch (error) {
    console.error('❌ Error al crear tarea:', error.message);
  }
}

/**
 * 3. ACTUALIZAR TAREA (PATCH /{id})
 * Equivalente al botón "Completar" en tu HTML
 */
async function completeTask(taskId) {
  console.log(`\n✏️  Marcando tarea ${taskId} como completada...`);
  try {
    const response = await fetch(`${BASE_URL}/${taskId}`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ completed: true })
    });
    const updatedTask = await handleResponse(response);
    console.log(`✅ Tarea actualizada. Estado completed: ${updatedTask.completed}`);
    return updatedTask;
  } catch (error) {
    console.error('❌ Error al actualizar tarea:', error.message);
  }
}

/**
 * 4. ELIMINAR TAREA (DELETE /{id})
 * Equivalente al botón "Borrar" en tu HTML
 */
async function deleteTask(taskId) {
  console.log(`\n🗑️  Eliminando tarea ${taskId}...`);
  try {
    const response = await fetch(`${BASE_URL}/${taskId}`, {
      method: 'DELETE'
    });
    await handleResponse(response); // Espera confirmación 204
    console.log('✅ Tarea eliminada correctamente.');
  } catch (error) {
    console.error('❌ Error al eliminar tarea:', error.message);
  }
}

/**
 * FUNCIÓN PRINCIPAL DE EJECUCIÓN
 * Ejecuta un flujo completo de prueba.
 */
async function main() {
  console.log('🚀 Iniciando cliente Node.js para SAOAPI...\n');

  // 1. Listar lo que hay actualmente
  await getTasks();

  // 2. Crear una nueva tarea de prueba
  const newTask = await createTask("Aprender Node.js", "Script de prueba para la API", "high");

  if (newTask) {
    // 3. Listar de nuevo para ver la nueva tarea
    await getTasks();

    // 4. Marcarla como completada
    await completeTask(newTask.id);

    // 5. Eliminar la tarea creada (limpieza)
    await deleteTask(newTask.id);

    // 6. Verificar que se borró
    await getTasks();
  }
}

// Ejecutar el script
main();
