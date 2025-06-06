<template>
<<<<<<< HEAD:educabot/educabot-frontend/src/components/comunes/ChatbotComponent.vue
  <div class="chatbot">
    <label for="pregunta">Escribe tu duda:</label>
    <input v-model="pregunta" @keyup.enter="enviarPregunta" id="pregunta" class="chat-input" />
    <button @click="enviarPregunta" class="btn-chat">Enviar</button>
    <p class="chat-response" v-if="respuesta">🤖 {{ respuesta }}</p>
    <p v-if="error" class="chat-error">❌ {{ error }}</p>
=======
  <div class="chatbot-container">
    <h1>Chatbot</h1>
    <textarea
      v-model="pregunta"
      placeholder="Escribe tu duda..."
    ></textarea>
    <button @click="enviarMensaje" :disabled="cargando">
      {{ cargando ? "Enviando..." : "Enviar" }}
    </button>
    <p v-if="respuesta" class="respuesta">
      <strong>Respuesta del Chatbot:</strong> {{ respuesta }}
    </p>
    <p v-if="error" class="error">{{ error }}</p>
    <div v-if="cargando" class="loading">Procesando...</div>
>>>>>>> parent of 9dbd3cc (avance 4):educabot/educabot-frontend/src/components/ChatbotComponent.vue
  </div>
</template>

<script>
export default {
  data() {
    return {
<<<<<<< HEAD:educabot/educabot-frontend/src/components/comunes/ChatbotComponent.vue
      pregunta: "",
      respuesta: "",
      error: "",
    };
  },
  methods: {
    async enviarPregunta() {
      if (!this.pregunta.trim()) return;
      this.error = "";
=======
      pregunta: "", // Contenido del textarea
      respuesta: "", // Respuesta del chatbot
      cargando: false, // Estado de carga
      error: null, // Mensaje de error
    };
  },
  methods: {
    async enviarMensaje() {
      if (!this.pregunta.trim()) {
        this.error = "Por favor, escribe una pregunta.";
        return;
      }

      // Estado inicial
      this.cargando = true;
      this.error = null;
>>>>>>> parent of 9dbd3cc (avance 4):educabot/educabot-frontend/src/components/ChatbotComponent.vue
      this.respuesta = "";
      try {
<<<<<<< HEAD:educabot/educabot-frontend/src/components/comunes/ChatbotComponent.vue
        const token = localStorage.getItem("token");
        const res = await fetch("http://127.0.0.1:5000/api/chatbot/chat", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
=======
        // Usa una URL base dinámica
        const apiUrl = import.meta.env.VITE_API_URL || "http://127.0.0.1:5000";
        const response = await fetch(`${apiUrl}/api/chatbot/chat`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
>>>>>>> parent of 9dbd3cc (avance 4):educabot/educabot-frontend/src/components/ChatbotComponent.vue
          },
          body: JSON.stringify({ pregunta: this.pregunta }),
        });
        const data = await res.json();
        if (res.ok) {
          this.respuesta = data.respuesta;
        } else {
          this.error = data.mensaje || "Error al comunicarse con el chatbot";
        }
      } catch (err) {
        this.error = "Servidor no disponible";
      }
    },
  },
};
</script>

<style scoped>
<<<<<<< HEAD:educabot/educabot-frontend/src/components/comunes/ChatbotComponent.vue
.chatbot {
  margin-top: 15px;
}
.chat-input {
  width: 100%;
  padding: 8px;
  margin-bottom: 5px;
}
.btn-chat {
  background-color: #004aad;
=======
.chatbot-container {
  border: 1px solid #ccc;
  padding: 15px;
  border-radius: 5px;
  background-color: #f9f9f9;
  max-width: 600px;
  margin: auto;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

textarea {
  width: 100%;
  height: 100px;
  margin-bottom: 10px;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: none;
  outline: none;
  transition: border-color 0.3s;
}

textarea:focus {
  border-color: #28a745;
}

button {
  padding: 10px 20px;
  background-color: #28a745;
>>>>>>> parent of 9dbd3cc (avance 4):educabot/educabot-frontend/src/components/ChatbotComponent.vue
  color: white;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}
<<<<<<< HEAD:educabot/educabot-frontend/src/components/comunes/ChatbotComponent.vue
.chat-response {
  color: #1d3557;
  font-weight: bold;
}
.chat-error {
  color: red;
  margin-top: 5px;
}
</style>
=======

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.respuesta {
  margin-top: 20px;
  font-size: 16px;
  color: #333;
  white-space: pre-wrap;
}

.error {
  margin-top: 20px;
  color: red;
  font-size: 16px;
}

.loading {
  margin-top: 20px;
  font-size: 16px;
  color: #28a745;
  font-weight: bold;
}
</style>
>>>>>>> parent of 9dbd3cc (avance 4):educabot/educabot-frontend/src/components/ChatbotComponent.vue
