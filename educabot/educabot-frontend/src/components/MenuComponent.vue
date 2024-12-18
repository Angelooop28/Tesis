<template>
  <div class="menu-component">
    <!-- Botón para abrir/cerrar el menú -->
    <button class="toggle-menu" @click="toggleMenu" aria-label="Abrir menú de accesibilidad">
      <img src="@/assets/accessibility-icon.svg" alt="Accesibilidad" />
    </button>

    <!-- Menú de accesibilidad -->
    <div v-if="isMenuOpen" class="menu">
      <h3>Herramientas de accesibilidad</h3>
      <ul>
        <li @click="increaseFont">🔍 <span>Aumentar texto</span></li>
        <li @click="decreaseFont">🔍 <span>Disminuir texto</span></li>
        <li @click="toggleGrayscale">⚪ <span>Escala de grises</span></li>
        <li @click="applyHighContrast">🌓 <span>Alto contraste</span></li>
        <li @click="applyNegativeContrast">🌑 <span>Contraste negativo</span></li>
        <li @click="resetAccessibility">🔄 <span>Restablecer</span></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "MenuComponent",
  data() {
    return {
      isMenuOpen: false, // Controla si el menú está abierto o cerrado
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    increaseFont() {
      document.body.style.fontSize = "larger";
    },
    decreaseFont() {
      document.body.style.fontSize = "smaller";
    },
    toggleGrayscale() {
      const currentFilter = document.body.style.filter;
      document.body.style.filter =
        currentFilter === "grayscale(100%)" ? "none" : "grayscale(100%)";
    },
    applyHighContrast() {
      document.body.style.backgroundColor = "#000";
      document.body.style.color = "#ff0";
    },
    applyNegativeContrast() {
      document.body.style.backgroundColor = "#000";
      document.body.style.color = "#fff";
    },
    resetAccessibility() {
      document.body.style.fontSize = "";
      document.body.style.filter = "";
      document.body.style.backgroundColor = "";
      document.body.style.color = "";
    },
  },
};
</script>

<style scoped>
.menu-component {
  position: fixed;
  bottom: 20px; /* Lo deja en la parte inferior */
  left: 20px;   /* Lo deja en la parte izquierda */
  z-index: 1000; /* Se asegura de estar por encima de otros elementos */
}

.toggle-menu {
  background-color: #007bff;
  border: none;
  padding: 10px;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.toggle-menu img {
  width: 30px;
  height: 30px;
}

.menu {
  background-color: #ffffff; /* Fondo blanco */
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 15px;
  width: 220px;
}

.menu h3 {
  font-size: 18px;
  margin-bottom: 10px;
  color: #000; /* Letras negras */
}

.menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu ul li {
  padding: 8px;
  cursor: pointer;
  font-size: 14px;
  color: #000; /* Letras negras */
  transition: background-color 0.3s ease;
  display: flex;
  align-items: center;
}

.menu ul li span {
  margin-left: 5px; /* Espacio para el ícono */
}

.menu ul li:hover {
  background-color: #f0f0f0; /* Fondo al pasar el ratón */
}
</style>
