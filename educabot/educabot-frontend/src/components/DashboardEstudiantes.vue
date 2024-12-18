<template>
  <div class="dashboard-container">
    <!-- Menú de accesibilidad -->
    <MenuComponent class="accessibility-menu" />

    <!-- Encabezado -->
    <header class="header">
      <h1>Educabot - Panel de Estudiantes</h1>
      <button @click="logout" class="btn-logout">Cerrar Sesión</button>
    </header>

    <!-- Contenido Principal -->
    <div class="main-content">
      <!-- Materias Matriculadas -->
      <section class="card">
        <h2>Materias Matriculadas</h2>
        <ul v-if="materias.length > 0">
          <li v-for="materia in materias" :key="materia.id">{{ materia.nombre }}</li>
        </ul>
        <p v-else>No estás matriculado en ninguna materia.</p>
      </section>

      <!-- Tareas Pendientes -->
      <section class="card">
        <h2>Tareas Pendientes</h2>
        <p v-if="tareas.length === 0" class="no-tareas">No tienes tareas pendientes.</p>
        <ul v-else>
          <li v-for="tarea in tareas" :key="tarea.id">
            <strong>{{ tarea.materia }}:</strong> {{ tarea.titulo }} - {{ tarea.fechaEntrega }}
          </li>
        </ul>
      </section>

      <!-- Subir Tarea -->
      <section class="card subir-tarea">
        <h2>Subir Tarea</h2>
        <div class="form-group">
          <label for="materia-select">Selecciona la materia:</label>
          <select v-model="materiaSeleccionada" id="materia-select" class="form-control">
            <option v-for="materia in materias" :key="materia.id" :value="materia.nombre">
              {{ materia.nombre }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="archivo">Selecciona el archivo (PDF):</label>
          <input type="file" id="archivo" @change="subirArchivo" accept="application/pdf" class="file-input" />
        </div>
        <button @click="enviarTarea" class="btn-submit">Subir Archivo</button>
      </section>

      <!-- Asistencia -->
      <section class="card">
        <h2>Asistencia</h2>
        <p>Asistencias: <strong>{{ asistencia.asistencias }}</strong> / {{ asistencia.total }}</p>
      </section>

      <!-- Calificaciones -->
      <section class="card">
        <h2>Calificaciones</h2>
        <ul v-if="calificaciones.length > 0">
          <li v-for="nota in calificaciones" :key="nota.materia">
            {{ nota.materia }}: <strong>{{ nota.nota }}</strong>
          </li>
        </ul>
        <p v-else>No hay calificaciones disponibles.</p>
      </section>

      <!-- Chatbot -->
      <section class="card chatbot">
        <h2>Chatbot</h2>
        <div class="form-group">
          <label for="mensaje">Escribe tu duda:</label>
          <textarea v-model="mensajeChat" id="mensaje" placeholder="Escribe tu duda..." class="chat-input"></textarea>
        </div>
        <button @click="enviarMensaje" class="btn-chat">Enviar</button>
        <p v-if="respuestaChat" class="chat-response">{{ respuestaChat }}</p>
      </section>
    </div>
  </div>
</template>

<script>
import MenuComponent from "./MenuComponent.vue";

export default {
  components: {
    MenuComponent,
  },
  data() {
    return {
      tareas: [],
      asistencia: { asistencias: 0, total: 0 },
      calificaciones: [],
      materias: [],
      materiaSeleccionada: "",
      mensajeChat: "",
      respuestaChat: "",
      archivo: null,
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/");
      location.reload();
    },
    async fetchData() {
      const token = localStorage.getItem("token");
      const headers = { Authorization: `Bearer ${token}` };

      this.tareas = await fetch("/api/tareas", { headers }).then((res) => res.json());
      this.asistencia = await fetch("/api/asistencia", { headers }).then((res) => res.json());
      this.calificaciones = await fetch("/api/calificaciones", { headers }).then((res) => res.json());
      this.materias = await fetch("/api/materias", { headers }).then((res) => res.json());
    },
    subirArchivo(event) {
      this.archivo = event.target.files[0];
    },
    async enviarTarea() {
      if (!this.materiaSeleccionada) {
        alert("Por favor selecciona una materia.");
        return;
      }

      const formData = new FormData();
      formData.append("archivo", this.archivo);
      formData.append("materia", this.materiaSeleccionada);

      const token = localStorage.getItem("token");
      await fetch("/api/subir-tarea", {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
        body: formData,
      });

      alert(`Tarea de ${this.materiaSeleccionada} subida con éxito`);
    },
    async enviarMensaje() {
      const response = await fetch("/api/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensaje: this.mensajeChat }),
      });
      const data = await response.json();
      this.respuestaChat = data.respuesta;
    },
  },
  mounted() {
    this.fetchData();
  },
};
</script>

<style scoped>
.dashboard-container {
  font-family: 'Arial', sans-serif;
  background: linear-gradient(135deg, #e0f2ff, #78c0e0);
  min-height: 100vh;
  padding: 20px;
  color: #333;
  position: relative;
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
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
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

.form-control,
.file-input,
.chat-input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.btn-submit,
.btn-chat {
  width: 100%;
  padding: 10px;
  background-color: #28a745;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
}

.chat-response {
  margin-top: 10px;
  font-weight: bold;
  color: #004aad;
}

.accessibility-menu {
  position: fixed;
  bottom: 20px;
  left: 20px;
}
</style>
