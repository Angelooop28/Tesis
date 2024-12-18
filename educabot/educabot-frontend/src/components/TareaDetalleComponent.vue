<template>
    <div class="tarea-detalle">
      <h1>{{ tarea.titulo }}</h1>
      <p>Fecha de vencimiento: {{ tarea.fecha_vencimiento }}</p>
      <div>
        <h2>Subir Tarea</h2>
        <input type="file" @change="handleFile" accept="application/pdf" />
        <button @click="subirArchivo">Subir Archivo</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "TareaDetalleComponent",
    data() {
      return {
        tarea: {},
        archivo: null,
      };
    },
    methods: {
      async fetchTarea() {
        const id = this.$route.params.id;
        const token = localStorage.getItem("token");
        const response = await fetch(`/api/tareas/${id}`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.tarea = await response.json();
      },
      handleFile(event) {
        this.archivo = event.target.files[0];
      },
      async subirArchivo() {
        const formData = new FormData();
        formData.append("archivo", this.archivo);
  
        const token = localStorage.getItem("token");
        await fetch(`/api/tareas/${this.tarea.id}/subir`, {
          method: "POST",
          headers: { Authorization: `Bearer ${token}` },
          body: formData,
        });
        alert("Archivo subido con éxito");
      },
    },
    mounted() {
      this.fetchTarea();
    },
  };
  </script>
  
  <style scoped>
  .tarea-detalle {
    padding: 20px;
  }
  
  button {
    margin-top: 10px;
    padding: 5px 10px;
  }
  </style>
  