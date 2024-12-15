<template>
  <div>
    <h1>Bienvenido, {{ user.nombre }}</h1>
    <p>Rol: {{ user.rol }}</p>

    <nav>
      <ul>
        <li><router-link to="/calificaciones">Ver Calificaciones</router-link></li>
        <li><router-link to="/tareas">Ver Tareas</router-link></li>
        <li><router-link to="/subir-tarea">Subir Tarea</router-link></li>
        <li><router-link to="/chatbot">Chatbot</router-link></li>
      </ul>
    </nav>

    <button @click="logout">Cerrar Sesión</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      user: {
        nombre: "",
        rol: "",
      },
    };
  },
  methods: {
    async fetchUserData() {
      try {
        const token = localStorage.getItem("token");

        if (!token) {
          alert("No estás autenticado. Redirigiendo al inicio de sesión.");
          this.$router.push("/login");
          return;
        }

        const response = await axios.get("http://localhost:5000/api/auth/user", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        this.user = response.data.usuario;
      } catch (error) {
        console.error("Error al obtener los datos del usuario:", error.response?.data || error.message);
        alert("Hubo un problema al cargar los datos del usuario.");
        this.$router.push("/login");
      }
    },
    logout() {
      localStorage.removeItem("token"); // Elimina el token almacenado
      alert("Sesión cerrada. Redirigiendo al inicio.");
      this.$router.push("/login"); // Redirige al inicio de sesión
    },
  },
  mounted() {
    this.fetchUserData(); // Cargar los datos del usuario al montar el componente
  },
};
</script>
