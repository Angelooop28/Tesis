<template>
    <div class="curso-detalle">
      <h1>{{ curso.nombre }}</h1>
      <section>
        <h2>Calificaciones</h2>
        <ul>
          <li v-for="nota in calificaciones" :key="nota.id">
            {{ nota.materia }}: {{ nota.nota }}
          </li>
        </ul>
      </section>
  
      <section>
        <h2>Asistencia</h2>
        <p>{{ asistencia.asistencias }} asistencias de {{ asistencia.total }} clases.</p>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: "CursoDetalleComponent",
    data() {
      return {
        curso: {},
        calificaciones: [],
        asistencia: {},
      };
    },
    methods: {
      async fetchDetalle() {
        const token = localStorage.getItem("token");
        const cursoId = this.$route.params.id;
  
        // Obtener detalles del curso
        const cursoRes = await fetch(`/api/curso/${cursoId}`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.curso = await cursoRes.json();
  
        // Obtener calificaciones
        const calRes = await fetch(`/api/curso/${cursoId}/calificaciones`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.calificaciones = await calRes.json();
  
        // Obtener asistencia
        const asisRes = await fetch(`/api/curso/${cursoId}/asistencia`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.asistencia = await asisRes.json();
      },
    },
    mounted() {
      this.fetchDetalle();
    },
  };
  </script>
  
  <style scoped>
  .curso-detalle {
    padding: 20px;
  }
  
  section {
    margin-top: 20px;
  }
  </style>
  