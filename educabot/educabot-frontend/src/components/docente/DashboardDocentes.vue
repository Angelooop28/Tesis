<template>
  <div class="dashboard-container">
    <header class="header">
      <h1>Educabot - Panel de Docentes</h1>
      <button @click="logout" class="btn-logout">Cerrar Sesión</button>
    </header>

    <div class="main-content">
      <!-- Materias asignadas -->
      <section class="card">
        <h2>Materias asignadas</h2>
        <ul v-if="materias.length > 0">
          <li v-for="materia in materias" :key="materia.id">{{ materia.nombre }}</li>
        </ul>
        <p v-else>No hay materias asignadas.</p>
      </section>

      <!-- Agregar Tarea -->
      <section class="card">
        <h2>Agregar Tarea</h2>
        <div class="form-group">
          <label>Materia:</label>
          <select v-model="tarea.id_asignatura" class="form-control">
            <option disabled value="">Seleccione una materia</option>
            <option v-for="materia in materias" :key="materia.id" :value="materia.id">
              {{ materia.nombre }}
            </option>
          </select>
        </div>
        <input v-model="tarea.titulo" type="text" placeholder="Título" class="form-control" />
        <input v-model="tarea.descripcion" type="text" placeholder="Descripción" class="form-control" />
        <input v-model="tarea.fecha_entrega" type="date" class="form-control" />
        <button @click="agregarTarea" class="btn-submit">Agregar Tarea</button>
      </section>

      <!-- Registrar Asistencia -->
      <section class="card">
        <h2>Registrar Asistencia</h2>
        <div class="form-group">
          <label>Materia:</label>
          <select v-model="asistencia.id_asignatura" class="form-control">
            <option disabled value="">Seleccione una materia</option>
            <option v-for="materia in materias" :key="materia.id" :value="materia.id">
              {{ materia.nombre }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label>Estudiante:</label>
          <select v-model="asistencia.id_estudiante" class="form-control">
            <option disabled value="">Seleccione un estudiante</option>
            <option v-for="e in estudiantesAsistencia" :key="e.id" :value="e.id">
              {{ e.nombre }}
            </option>
          </select>
        </div>
        <input v-model="asistencia.fecha" type="date" class="form-control" />
        <input v-model="asistencia.estado" placeholder="Presente / Ausente" class="form-control" />
        <button @click="registrarAsistencia" class="btn-submit">Registrar</button>
      </section>

      <!-- Registrar Calificaciones -->
      <section class="card">
        <h2>Registrar Calificaciones</h2>
        <div class="form-group">
          <label>Materia:</label>
          <select v-model="calificacion.id_asignatura" class="form-control">
            <option disabled value="">Seleccione una materia</option>
            <option v-for="materia in materias" :key="materia.id" :value="materia.id">
              {{ materia.nombre }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label>Estudiante:</label>
          <select v-model="calificacion.id_estudiante" class="form-control">
            <option disabled value="">Seleccione un estudiante</option>
            <option v-for="e in estudiantesCalificaciones" :key="e.id" :value="e.id">
              {{ e.nombre }}
            </option>
          </select>
        </div>
        <input v-model="calificacion.nota" type="number" min="0" max="10" placeholder="Nota" class="form-control" />
        <input v-model="calificacion.fecha" type="date" class="form-control" />
        <button @click="registrarCalificacion" class="btn-submit">Registrar</button>
      </section>

      <!-- Chatbot -->
      <section class="card">
        <ChatbotComponent />
      </section>
    </div>
  </div>
</template>

<script>
import ChatbotComponent from "@/components/comunes/ChatbotComponent.vue";

export default {
  components: { ChatbotComponent },
  data() {
    return {
      materias: [],
      tarea: { id_asignatura: "", titulo: "", descripcion: "", fecha_entrega: "" },
      asistencia: { id_estudiante: "", id_asignatura: "", fecha: "", estado: "" },
      calificacion: { id_estudiante: "", id_asignatura: "", nota: "", fecha: "" },
      estudiantesAsistencia: [],
      estudiantesCalificaciones: []
    };
  },
  watch: {
    "asistencia.id_asignatura"(idMateria) {
      const materia = this.materias.find(m => m.id == idMateria);
      this.estudiantesAsistencia = materia ? materia.estudiantes : [];
    },
    "calificacion.id_asignatura"(idMateria) {
      const materia = this.materias.find(m => m.id == idMateria);
      this.estudiantesCalificaciones = materia ? materia.estudiantes : [];
    }
  },
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push("/login");
    },
    async fetchData() {
      const token = localStorage.getItem("token");
      try {
        const res = await fetch("http://127.0.0.1:5000/api/dashboard-docentes", {
          headers: { Authorization: `Bearer ${token}` },
        });

        if (!res.ok) throw new Error("No se pudo cargar el dashboard");

        const data = await res.json();

        this.materias = Array.isArray(data.materias)
          ? data.materias.map((m) => ({
              id: m.id,
              nombre: m.nombre,
              estudiantes: Array.isArray(m.estudiantes) ? m.estudiantes : []
            }))
          : [];
      } catch (error) {
        console.error("❌ Error al cargar datos:", error);
        this.materias = [];
      }
    },
    async agregarTarea() {
      const token = localStorage.getItem("token");
      await fetch("http://127.0.0.1:5000/api/tareas/agregar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(this.tarea),
      });
      alert("✅ Tarea agregada con éxito");
      this.tarea = { id_asignatura: "", titulo: "", descripcion: "", fecha_entrega: "" };
    },
    async registrarAsistencia() {
      const token = localStorage.getItem("token");
      await fetch("http://127.0.0.1:5000/api/asistencias/agregar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(this.asistencia),
      });
      alert("📋 Asistencia registrada");
      this.asistencia = { id_estudiante: "", id_asignatura: "", fecha: "", estado: "" };
    },
    async registrarCalificacion() {
      const token = localStorage.getItem("token");
      await fetch("http://127.0.0.1:5000/api/calificaciones/agregar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(this.calificacion),
      });
      alert("✅ Calificación ingresada");
      this.calificacion = { id_estudiante: "", id_asignatura: "", nota: "", fecha: "" };
    }
  },
  mounted() {
    this.fetchData();
  }
};
</script>

<style scoped>
.dashboard-container {
  padding: 20px;
  background: #f0f8ff;
  min-height: 100vh;
  font-family: "Segoe UI", sans-serif;
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
</style>
