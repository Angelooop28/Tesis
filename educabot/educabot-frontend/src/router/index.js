import { createRouter, createWebHistory } from "vue-router";
import HomeComponent from "../components/HomeComponent.vue";
import LoginComponent from "../components/LoginComponent.vue";
import RegisterComponent from "../components/RegisterComponent.vue";
import DashboardEstudiantes from "../components/DashboardEstudiantes.vue";
import DashboardDocentes from "../components/DashboardDocentes.vue";
import CalificacionesComponent from "../components/CalificacionesComponent.vue";
import TareasComponent from "../components/TareasComponent.vue";
import SubirTareaComponent from "../components/SubirTareaComponent.vue";
import ChatbotComponent from "../components/ChatbotComponent.vue";
import ContactComponent from "../components/ContactComponent.vue";
import CursosComponent from "../components/CursosComponent.vue";
import CursoDetalleComponent from "../components/CursoDetalleComponent.vue";

const routes = [
  { path: "/", component: HomeComponent },
  { path: "/login", component: LoginComponent },
  { path: "/register", component: RegisterComponent },
  {
    path: "/dashboard-estudiantes",
    component: DashboardEstudiantes,
    meta: { requiresAuth: true, rol: "estudiante" },
  },
  {
    path: "/dashboard-docentes",
    component: DashboardDocentes,
    meta: { requiresAuth: true, rol: "docente" },
  },
  {
    path: "/calificaciones",
    component: CalificacionesComponent,
    meta: { requiresAuth: true, rol: "estudiante" },
  },
  {
    path: "/tareas",
    component: TareasComponent,
    meta: { requiresAuth: true },
  },
  {
    path: "/subir-tarea",
    component: SubirTareaComponent,
    meta: { requiresAuth: true, rol: "docente" },
  },
  { path: "/chatbot", component: ChatbotComponent },
  { path: "/contact", component: ContactComponent },
  {
    path: "/cursos",
    component: CursosComponent,
    meta: { requiresAuth: true },
  },
  {
    path: "/cursos/:id",
    component: CursoDetalleComponent,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");
  const rol = localStorage.getItem("rol");

  if (to.meta.requiresAuth) {
    if (!token) {
      next("/login");
    } else if (to.meta.rol && to.meta.rol !== rol) {
      next("/");
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
