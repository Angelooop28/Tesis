<template>
  <div class="dashboard-container">
    <!-- Encabezado -->
    <header class="header">
      <h1>Educabot - Panel de Administración</h1>
      <button @click="logout" class="btn-logout">Cerrar Sesión</button>
    </header>

    <div class="main-content">
      <!-- Usuarios -->
      <section class="card">
        <h2>Usuarios Registrados</h2>
        <ul v-if="usuarios.length">
          <li v-for="usuario in usuarios" :key="usuario.id">
            👤 {{ usuario.nombre }} <small>({{ usuario.rol }})</small>
          </li>
        </ul>
        <p v-else>No hay usuarios registrados.</p>
      </section>

      <!-- Crear/Editar tarea -->
      <section class="card">
        <h2>{{ formulario.id ? "Editar Tarea" : "Crear Nueva Tarea" }}</h2>
        <form @submit.prevent="crearTarea">
          <div class="form-group">
            <label>Materia:</label>
            <select v-model="formulario.id_materia" class="form-control" required>
              <option disabled value="">Seleccione una materia</option>
              <option v-for="m in materias" :key="m.id" :value="m.id">{{ m.nombre }}</option>
            </select>
          </div>
          <div class="form-group">
            <label>Título:</label>
            <input v-model="formulario.titulo" class="form-control" required />
          </div>
          <div class="form-group">
            <label>Descripción:</label>
            <textarea v-model="formulario.descripcion" class="form-control" required></textarea>
          </div>
          <div class="form-group">
            <label>Fecha de Vencimiento:</label>
            <input type="date" v-model="formulario.fecha_vencimiento" class="form-control" required />
          </div>
          <button type="submit" class="btn-submit">
            {{ formulario.id ? 'Actualizar Tarea' : 'Crear Tarea' }}
          </button>
          <button v-if="formulario.id" type="button" @click="cancelarEdicion" class="btn-secondary">
            Cancelar
          </button>
          <p v-if="mensaje" class="success-msg">{{ mensaje }}</p>
          <p v-if="error" class="error-msg">{{ error }}</p>
        </form>
      </section>

      <!-- Lista de tareas -->
      <section class="card">
        <h2>Tareas Actuales</h2>
        <ul v-if="tareas.length">
          <li v-for="tarea in tareas" :key="tarea.id">
            📌 <strong>{{ tarea.titulo }}</strong> - {{ tarea.materia }}
            <br />
            <small>Vence: {{ tarea.fecha_entrega }}</small>
            <div class="btn-group">
              <button @click="seleccionarTarea(tarea)">Editar</button>
              <button @click="eliminarTarea(tarea.id)" class="btn-danger">Eliminar</button>
            </div>
          </li>
        </ul>
        <p v-else>No hay tareas registradas.</p>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: "DashboardAdmin",
  data() {
    return {
      usuarios: [],
      tareas: [],
      materias: [],
      mensaje: "",
      error: "",
      formulario: {
        id: null,
        id_materia: "",
        titulo: "",
        descripcion: "",
        fecha_vencimiento: ""
      }
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/login");
    },
    async fetchDashboardData() {
      const token = localStorage.getItem("token");
      try {
        const res = await fetch("http://127.0.0.1:5000/api/dashboard-admin", {
          headers: { Authorization: `Bearer ${token}` }
        });
        const data = await res.json();
        this.usuarios = data.usuarios || [];
        this.tareas = data.tareas || [];
        this.materias = data.asignaturas || [];
      } catch (e) {
        console.error("Error al cargar datos del panel admin:", e);
      }
    },
    cancelarEdicion() {
      this.formulario = {
        id: null,
        id_materia: "",
        titulo: "",
        descripcion: "",
        fecha_vencimiento: ""
      };
      this.mensaje = "";
      this.error = "";
    },
    seleccionarTarea(tarea) {
      const materiaSeleccionada = this.materias.find(m => m.nombre === tarea.materia);
      this.formulario = {
        id: tarea.id,
        id_materia: materiaSeleccionada ? materiaSeleccionada.id : "",
        titulo: tarea.titulo,
        descripcion: tarea.descripcion,
        fecha_vencimiento: tarea.fecha_entrega
      };
    },
    async crearTarea() {
      const token = localStorage.getItem("token");
      const url = this.formulario.id
        ? `http://127.0.0.1:5000/api/tareas/editar/${this.formulario.id}`
        : "http://127.0.0.1:5000/api/tareas/agregar";
      const method = this.formulario.id ? "PUT" : "POST";

      try {
        const res = await fetch(url, {
          method,
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
          },
          body: JSON.stringify(this.formulario)
        });
        const data = await res.json();
        if (res.ok) {
          this.mensaje = data.mensaje;
          this.cancelarEdicion();
          this.fetchDashboardData();
        } else {
          this.error = data.mensaje || "Error al procesar tarea.";
        }
      } catch (e) {
        this.error = "Error de conexión con el servidor.";
      }
    },
    async eliminarTarea(id) {
      const token = localStorage.getItem("token");
      try {
        const res = await fetch(`http://127.0.0.1:5000/api/tareas/eliminar/${id}`, {
          method: "DELETE",
          headers: { Authorization: `Bearer ${token}` }
        });
        const data = await res.json();
        this.mensaje = data.mensaje;
        this.fetchDashboardData();
      } catch (e) {
        console.error("Error al eliminar tarea:", e);
      }
    }
  },
  mounted() {
    this.fetchDashboardData();
  }
};
</script>

<style scoped>
.dashboard-container {
  font-family: "Arial", sans-serif;
  background: linear-gradient(135deg, #e0f2ff, #78c0e0);
  min-height: 100vh;
  padding: 20px;
  color: #333;
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
.form-control {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
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
.btn-secondary {
  background-color: #6c757d;
  color: white;
  margin-top: 10px;
  width: 100%;
  padding: 10px;
  border-radius: 5px;
}
.btn-danger {
  background-color: #dc3545;
  color: white;
  padding: 6px 10px;
  border: none;
  border-radius: 4px;
  margin-top: 5px;
}
.success-msg {
  color: green;
  margin-top: 10px;
}
.error-msg {
  color: red;
  margin-top: 10px;
}
</style>
