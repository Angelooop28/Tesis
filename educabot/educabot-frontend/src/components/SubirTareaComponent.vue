<template>
    <div>
      <h1>Subir Tarea</h1>
      <input type="file" @change="handleFileUpload" />
      <button @click="enviarTarea">Subir</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "SubirTareaComponent",
    methods: {
      handleFileUpload(event) {
        console.log(event.target.files[0]);
      },
      enviarTarea() {
        alert("Tarea subida con éxito");
      },
    },
  };
  </script>
  