import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/HomeComponent.vue";
import Login from "../components/LoginComponent.vue";
import Register from "../components/RegisterComponent.vue";
import Dashboard from "../components/DashboardComponent.vue";
import Calificaciones from "../components/CalificacionesComponent.vue";
import Tareas from "../components/TareasComponent.vue";
import SubirTarea from "../components/SubirTareaComponent.vue";
import Chatbot from "../components/ChatbotComponent.vue";
import Contact from "../components/ContactComponent.vue";
import About from "../components/AboutComponent.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  { path: "/dashboard", component: Dashboard, meta: { requiresAuth: true } },
  { path: "/calificaciones", component: Calificaciones, meta: { requiresAuth: true } },
  { path: "/tareas", component: Tareas, meta: { requiresAuth: true } },
  { path: "/subir-tarea", component: SubirTarea, meta: { requiresAuth: true } },
  { path: "/chatbot", component: Chatbot, meta: { requiresAuth: true } },
  { path: "/contact", component: Contact },
  { path: "/about", component: About },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Middleware para proteger rutas
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");

  if (to.matched.some((record) => record.meta.requiresAuth) && !token) {
    alert("Debes iniciar sesión para acceder a esta página");
    next("/login");
  } else {
    next();
  }
});

export default router;
