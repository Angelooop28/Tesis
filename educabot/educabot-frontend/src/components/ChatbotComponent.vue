<template>
    <div>
      <h1>Chatbot</h1>
      <textarea placeholder="Escribe tu duda..."></textarea>
      <button @click="enviarMensaje">Enviar</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "ChatbotComponent",
    methods: {
      enviarMensaje() {
        alert("Mensaje enviado al chatbot");
      },
    },
  };
  </script>
  