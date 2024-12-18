<template>
    <div class="tareas-container">
      <h1>Tareas Pendientes</h1>
      <ul>
        <li v-for="tarea in tareas" :key="tarea.id">
          {{ tarea.titulo }} - Vence el {{ tarea.fecha_vencimiento }}
          <button @click="verDetalle(tarea.id)">Ver Detalle</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "TareasComponent",
    data() {
      return {
        tareas: [],
      };
    },
    methods: {
      async fetchTareas() {
        const token = localStorage.getItem("token");
        const response = await fetch("/api/tareas", {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.tareas = await response.json();
      },
      verDetalle(id) {
        this.$router.push(`/tarea/${id}`);
      },
    },
    mounted() {
      this.fetchTareas();
    },
  };
  </script>
  
  <style scoped>
  button {
    margin-left: 10px;
    padding: 5px 10px;
  }
  </style>
  