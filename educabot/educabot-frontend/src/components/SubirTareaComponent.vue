<template>
    <form @submit.prevent="subirTarea">
      <h2>Subir Tarea</h2>
      <input v-model="titulo" type="text" placeholder="Título" />
      <textarea v-model="descripcion" placeholder="Descripción"></textarea>
      <button type="submit">Subir</button>
    </form>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        titulo: '',
        descripcion: '',
      };
    },
    methods: {
      async subirTarea() {
        try {
          await axios.post(
            'http://localhost:5000/tareas',
            { titulo: this.titulo, descripcion: this.descripcion },
            { headers: { Authorization: `Bearer ${localStorage.getItem('token')}` } }
          );
          alert('Tarea subida exitosamente');
        } catch (error) {
          alert('Error al subir tarea');
        }
      },
    },
  };
  </script>
  