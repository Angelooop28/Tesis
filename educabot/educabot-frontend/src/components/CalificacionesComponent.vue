<template>
    <div>
      <h2>Calificaciones</h2>
      <ul>
        <li v-for="calificacion in calificaciones" :key="calificacion.id">
          {{ calificacion.nombre }}: {{ calificacion.nota }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        calificaciones: [],
      };
    },
    async created() {
      try {
        const response = await axios.get('http://localhost:5000/calificaciones', {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
        });
        this.calificaciones = response.data;
      } catch (error) {
        alert('Error al cargar calificaciones');
      }
    },
  };
  </script>
  