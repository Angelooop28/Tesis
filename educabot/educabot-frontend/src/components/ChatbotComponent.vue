<template>
    <div>
      <h2>Chatbot</h2>
      <textarea v-model="pregunta" placeholder="Escribe tu pregunta"></textarea>
      <button @click="enviarPregunta">Enviar</button>
      <p>{{ respuesta }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        pregunta: '',
        respuesta: '',
      };
    },
    methods: {
      async enviarPregunta() {
        try {
          const response = await axios.post('http://localhost:5000/chatbot', { pregunta: this.pregunta });
          this.respuesta = response.data.respuesta;
        } catch (error) {
          alert('Error al obtener respuesta del chatbot');
        }
      },
    },
  };
  </script>
  