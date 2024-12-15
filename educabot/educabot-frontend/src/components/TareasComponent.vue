<template>
    <div>
      <h2>Tareas</h2>
      <ul>
        <li v-for="tarea in tareas" :key="tarea.id">
          {{ tarea.titulo }} - {{ tarea.descripcion }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        tareas: [],
      };
    },
    async created() {
      try {
        const response = await axios.get('http://localhost:5000/tareas', {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
        });
        this.tareas = response.data;
      } catch (error) {
        alert('Error al cargar tareas');
      }
    },
  };
  </script>
  