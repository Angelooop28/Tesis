<template>
  <div class="home-container">
    <!-- Tarjeta central -->
    <div class="card">
      <!-- Izquierda: Información del software -->
      <div class="card-left">
        <img :src="logoImage" alt="Imagen ilustrativa de una maestra enseñando" class="logo" />
        <h2>La plataforma educativa más completa y accesible.</h2>
        <p>
          Innovamos para transformar la educación con tecnología inclusiva y accesible
          para todos los estudiantes.
        </p>
      </div>

      <!-- Derecha: Acceso a la plataforma -->
      <div class="card-right">
        <h2>Bienvenido a Educabot</h2>
        <p>Accede a la plataforma:</p>
        <div class="buttons-section">
          <button 
            class="btn btn-primary" 
            @click="navigateToLogin" 
            aria-label="Iniciar sesión en la plataforma">
            Iniciar Sesión
          </button>
          <button 
            class="btn btn-secondary" 
            @click="navigateToRegister" 
            aria-label="Registrarse en la plataforma">
            Registrarse
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import logoImage from "@/assets/images/logo.png"; // Ruta de la imagen

export default {
  data() {
    return {
      logoImage, // Imagen del logo o ilustrativa
    };
  },
  methods: {
    navigateToLogin() {
      this.$router.push("/login"); // Navega al login
    },
    navigateToRegister() {
      this.$router.push("/register"); // Navega al registro
    },
  },
};
</script>

<style scoped>
/* Fondo de la página */
.home-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #004aad, #78c0e0); /* Fondo degradado */
  font-family: 'Arial', sans-serif;
  color: #333333;
  padding: 20px;
}

/* Tarjeta central */
.card {
  display: flex;
  flex-direction: row;
  background: #ffffff;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  width: 80%;
  max-width: 900px;
  height: auto;
}

/* Sección izquierda de la tarjeta */
.card-left {
  flex: 1;
  background: #f5f5f5;
  padding: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.card-left h2 {
  color: #004aad;
  font-size: 24px; /* Texto más grande */
  margin: 20px 0 10px;
}

.card-left p {
  color: #666666;
  font-size: 18px; /* Texto más grande */
}

/* Imagen del logo redondeada */
.logo {
  max-width: 150px;
  margin-bottom: 20px;
  border-radius: 50%; /* Hace que la imagen sea redonda */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra para mejor diseño */
  object-fit: cover; /* Ajusta el contenido al círculo */
}

/* Sección derecha de la tarjeta */
.card-right {
  flex: 1;
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.card-right h2 {
  color: #333333; /* Contraste mejorado */
  font-size: 24px;
  margin-bottom: 10px;
}

.card-right p {
  color: #666666;
  font-size: 18px; /* Texto más grande */
  margin-bottom: 20px;
}

/* Botones */
.buttons-section {
  display: flex;
  flex-direction: column;
  gap: 20px; /* Espaciado mejorado */
}

.btn {
  padding: 15px 20px;
  font-size: 18px; /* Tamaño de texto accesible */
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.btn-primary {
  color: #ffffff;
  background-color: #004aad; /* Contraste fuerte */
}

.btn-primary:hover {
  background-color: #003580;
  transform: scale(1.05);
}

.btn-primary:focus {
  outline: 2px solid #78c0e0; /* Indicador visual de enfoque */
}

.btn-secondary {
  background-color: #f5f5f5;
  color: #004aad;
  border: 2px solid #004aad;
}

.btn-secondary:hover {
  background-color: #e6f4ff;
  transform: scale(1.05);
}

.btn-secondary:focus {
  outline: 2px solid #78c0e0; /* Indicador visual de enfoque */
}
</style>
