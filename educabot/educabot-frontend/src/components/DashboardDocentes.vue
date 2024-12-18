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
            <select v-model="materiaSeleccionada" class="form-control">
              <option v-for="materia in materias" :key="materia.id" :value="materia.nombre">
                {{ materia.nombre }}
              </option>
            </select>
          </div>
          <div class="form-group">
            <label for="titulo">Título de la Tarea:</label>
            <input v-model="tituloTarea" type="text" placeholder="Título" class="form-control" />
          </div>
          <div class="form-group">
            <label for="fecha">Fecha de Entrega:</label>
            <input v-model="fechaEntrega" type="date" class="form-control" />
          </div>
          <button @click="agregarTarea" class="btn-submit">Agregar Tarea</button>
        </section>
  
        <!-- Registrar Asistencia -->
        <section class="card">
          <h2>Registrar Asistencia</h2>
          <label for="asistencia">Total de Asistencias:</label>
          <input v-model="totalAsistencias" type="number" placeholder="Total de Asistencias" class="form-control" />
          <button @click="registrarAsistencia" class="btn-submit">Registrar Asistencia</button>
        </section>
  
        <!-- Ingresar Calificaciones -->
        <section class="card">
          <h2>Ingresar Calificaciones</h2>
          <label for="materia">Materia:</label>
          <select v-model="materiaSeleccionada" class="form-control">
            <option v-for="materia in materias" :key="materia.id" :value="materia.nombre">
              {{ materia.nombre }}
            </option>
          </select>
          <div class="form-group">
            <label for="nota">Calificación:</label>
            <input v-model="calificacion" type="number" min="0" max="10" placeholder="Nota" class="form-control" />
          </div>
          <button @click="agregarCalificacion" class="btn-submit">Agregar Calificación</button>
        </section>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        materias: [
          { id: 1, nombre: "Matemáticas" },
          { id: 2, nombre: "Ciencias" },
          { id: 3, nombre: "Lenguaje" },
        ],
        materiaSeleccionada: "",
        tituloTarea: "",
        fechaEntrega: "",
        totalAsistencias: 0,
        calificacion: 0,
      };
    },
    methods: {
      agregarTarea() {
        if (!this.materiaSeleccionada || !this.tituloTarea || !this.fechaEntrega) {
          alert("Por favor, completa todos los campos.");
          return;
        }
        console.log("Tarea agregada:", {
          materia: this.materiaSeleccionada,
          titulo: this.tituloTarea,
          fechaEntrega: this.fechaEntrega,
        });
        alert("Tarea agregada con éxito.");
      },
      registrarAsistencia() {
        if (!this.totalAsistencias) {
          alert("Por favor, ingresa el total de asistencias.");
          return;
        }
        console.log("Asistencia registrada:", this.totalAsistencias);
        alert("Asistencia registrada con éxito.");
      },
      agregarCalificacion() {
        if (!this.materiaSeleccionada || this.calificacion < 0 || this.calificacion > 10) {
          alert("Por favor, completa todos los campos correctamente.");
          return;
        }
        console.log("Calificación agregada:", {
          materia: this.materiaSeleccionada,
          calificacion: this.calificacion,
        });
        alert("Calificación agregada con éxito.");
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
  