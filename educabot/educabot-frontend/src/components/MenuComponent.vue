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
          <li @click="increaseFont">🔍 Aumentar texto</li>
          <li @click="decreaseFont">🔍 Disminuir texto</li>
          <li @click="toggleGrayscale">⚪ Escala de grises</li>
          <li @click="applyHighContrast">🌓 Alto contraste</li>
          <li @click="applyNegativeContrast">🌑 Contraste negativo</li>
          <li @click="resetAccessibility">🔄 Restablecer</li>
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
        this.isMenuOpen = !this.isMenuOpen; // Alternar el estado del menú
      },
      increaseFont() {
        document.body.style.fontSize = "larger"; // Aumentar el tamaño del texto
      },
      decreaseFont() {
        document.body.style.fontSize = "smaller"; // Disminuir el tamaño del texto
      },
      toggleGrayscale() {
        const currentFilter = document.body.style.filter;
        document.body.style.filter =
          currentFilter === "grayscale(100%)" ? "none" : "grayscale(100%)"; // Alternar escala de grises
      },
      applyHighContrast() {
        document.body.style.backgroundColor = "#000"; // Fondo negro
        document.body.style.color = "#ff0"; // Texto amarillo
      },
      applyNegativeContrast() {
        document.body.style.backgroundColor = "#000"; // Fondo negro
        document.body.style.color = "#fff"; // Texto blanco
      },
      resetAccessibility() {
        document.body.style.fontSize = ""; // Restablecer tamaño del texto
        document.body.style.filter = ""; // Restablecer escala de grises
        document.body.style.backgroundColor = ""; // Restablecer color de fondo
        document.body.style.color = ""; // Restablecer color de texto
      },
    },
  };
  </script>
  
  <style scoped>
  .menu-component {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
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
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 15px;
    margin-top: 10px;
    width: 220px;
  }
  
  .menu h3 {
    font-size: 18px;
    margin-bottom: 10px;
    color: #333;
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
    transition: background-color 0.3s ease;
  }
  
  .menu ul li:hover {
    background-color: #f0f0f0;
  }
  </style>
  