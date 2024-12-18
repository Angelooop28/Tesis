<template>
    <div class="cursos-container">
      <h1>Mis Cursos</h1>
      <div class="curso" v-for="curso in cursos" :key="curso.id">
        <button @click="verDetalle(curso.id)">
          {{ curso.nombre }}
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "CursosComponent",
    data() {
      return {
        cursos: [], // Lista de materias
      };
    },
    methods: {
      async fetchCursos() {
        const token = localStorage.getItem("token");
        const response = await fetch("/api/cursos", {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.cursos = await response.json();
      },
      verDetalle(id) {
        this.$router.push(`/curso/${id}`);
      },
    },
    mounted() {
      this.fetchCursos();
    },
  };
  </script>
  
  <style scoped>
  .cursos-container {
    padding: 20px;
  }
  
  .curso button {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    background-color: #f0f0f0;
    border: none;
    text-align: left;
    cursor: pointer;
  }
  
  .curso button:hover {
    background-color: #e0e0e0;
  }
  </style>
  