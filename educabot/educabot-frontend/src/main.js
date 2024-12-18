import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// Creación de la aplicación con router
const app = createApp(App);

// Configuración del router
app.use(router);

// Montar la aplicación en el elemento con id #app
app.mount('#app');
