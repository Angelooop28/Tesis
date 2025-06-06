const API_URL = 'http://localhost:5000/api';

// Agregar Tarea
export const agregarTarea = async (tarea) => {
    const response = await fetch(`${API_URL}/tareas`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(tarea),
    });
    return await response.json();
};

// Registrar Asistencia
export const registrarAsistencia = async (asistencia) => {
    const response = await fetch(`${API_URL}/asistencias`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(asistencia),
    });
    return await response.json();
};

// Ingresar Calificación
export const ingresarCalificacion = async (calificacion) => {
    const response = await fetch(`${API_URL}/calificaciones`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(calificacion),
    });
    return await response.json();
};
