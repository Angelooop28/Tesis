<template>
  <div class="dashboard-container">
    <!-- Encabezado -->
    <header class="header">
      <h1>Educabot - Panel de Docentes</h1>
      <button @click="logout" class="btn-logout">Cerrar Sesión</button>
    </header>

    <!-- Contenido Principal -->
    <div class="main-content">
      <!-- Agregar Tareas -->
      <section class="card">
        <h2>Agregar Tareas</h2>
        <div class="form-group">
          <label for="materia">Materia:</label>
          <select v-model="nuevaTarea.id_asignatura" class="form-control">
            <option v-for="materia in materias" :key="materia.id" :value="materia.id">
              {{ materia.nombre }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="titulo">Título de la Tarea:</label>
          <input v-model="nuevaTarea.titulo" type="text" placeholder="Título" class="form-control" />
        </div>
        <div class="form-group">
          <label for="descripcion">Descripción:</label>
          <input v-model="nuevaTarea.descripcion" type="text" placeholder="Descripción" class="form-control" />
        </div>
        <div class="form-group">
          <label for="fecha">Fecha de Entrega:</label>
          <input v-model="nuevaTarea.fecha_entrega" type="date" class="form-control" />
        </div>
        <button @click="agregarTarea" class="btn-submit">Agregar Tarea</button>
      </section>

      <!-- Registrar Asistencia -->
      <section class="card">
        <h2>Registrar Asistencia</h2>
        <div class="form-group">
          <label for="id_estudiante">ID Estudiante:</label>
          <input v-model="asistencia.id_estudiante" type="text" placeholder="ID Estudiante" class="form-control" />
        </div>
        <div class="form-group">
          <label for="fecha">Fecha:</label>
          <input v-model="asistencia.fecha" type="date" class="form-control" />
        </div>
        <div class="form-group">
          <label for="estado">Estado (Presente/Ausente):</label>
          <input v-model="asistencia.estado" type="text" placeholder="Estado" class="form-control" />
        </div>
        <button @click="registrarAsistencia" class="btn-submit">Registrar Asistencia</button>
      </section>

      <!-- Ingresar Calificaciones -->
      <section class="card">
        <h2>Ingresar Calificaciones</h2>
        <div class="form-group">
          <label for="id_estudiante">ID Estudiante:</label>
          <input v-model="calificacion.id_estudiante" type="text" placeholder="ID Estudiante" class="form-control" />
        </div>
        <div class="form-group">
          <label for="materia">Materia:</label>
          <select v-model="calificacion.id_asignatura" class="form-control">
            <option v-for="materia in materias" :key="materia.id" :value="materia.id">
              {{ materia.nombre }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="nota">Calificación:</label>
          <input v-model="calificacion.nota" type="number" min="0" max="10" placeholder="Nota" class="form-control" />
        </div>
        <div class="form-group">
          <label for="fecha">Fecha:</label>
          <input v-model="calificacion.fecha" type="date" class="form-control" />
        </div>
        <button @click="ingresarCalificacion" class="btn-submit">Ingresar Calificación</button>
      </section>
    </div>
  </div>
</template>

<script>
import { agregarTarea, registrarAsistencia, ingresarCalificacion } from '@/services/api';

export default {
  data() {
    return {
      materias: [
        { id: 1, nombre: "Matemáticas" },
        { id: 2, nombre: "Ciencias" },
        { id: 3, nombre: "Lenguaje" },
      ],
      nuevaTarea: { id_asignatura: '', titulo: '', descripcion: '', fecha_entrega: '' },
      asistencia: { id_estudiante: '', fecha: '', estado: '' },
      calificacion: { id_estudiante: '', id_asignatura: '', nota: '', fecha: '' },
    };
  },
  methods: {
    async agregarTarea() {
      if (!this.nuevaTarea.id_asignatura || !this.nuevaTarea.titulo || !this.nuevaTarea.fecha_entrega) {
        alert("Por favor, completa todos los campos.");
        return;
      }
      const response = await agregarTarea(this.nuevaTarea);
      console.log(response);
      alert("Tarea agregada con éxito.");
    },
    async registrarAsistencia() {
      if (!this.asistencia.id_estudiante || !this.asistencia.fecha || !this.asistencia.estado) {
        alert("Por favor, completa todos los campos.");
        return;
      }
      const response = await registrarAsistencia(this.asistencia);
      console.log(response);
      alert("Asistencia registrada con éxito.");
    },
    async ingresarCalificacion() {
      if (!this.calificacion.id_estudiante || !this.calificacion.id_asignatura || !this.calificacion.nota) {
        alert("Por favor, completa todos los campos correctamente.");
        return;
      }
      const response = await ingresarCalificacion(this.calificacion);
      console.log(response);
      alert("Calificación ingresada con éxito.");
    },
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/login");
    },
  },
};
</script>

<style scoped>
.dashboard-container {
  font-family: Arial, sans-serif;
  background: linear-gradient(135deg, #e0f2ff, #78c0e0);
  min-height: 100vh;
  padding: 20px;
}

.header {
  background-color: #ffffff;
  color: #004aad;
  padding: 15px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-radius: 10px;
  margin-bottom: 20px;
}

.btn-logout {
  background-color: #dc3545;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.main-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.card {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 10px;
}

.form-control {
  width: 100%;
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.btn-submit {
  width: 100%;
  padding: 10px;
  background-color: #28a745;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
}

.btn-submit:hover {
  background-color: #218838;
}
</style>
 