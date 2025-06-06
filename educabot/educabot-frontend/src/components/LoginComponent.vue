<template>
  <div class="login-container">
    <div class="login-card">
      <h2>Iniciar Sesión</h2>
      <p>Accede a la plataforma</p>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="email">Correo Electrónico</label>
          <input
            type="email"
            id="email"
            v-model="email"
            placeholder="Ingrese su correo electrónico"
            required
          />
        </div>
        <div class="form-group">
          <label for="password">Contraseña</label>
          <input
            type="password"
            id="password"
            v-model="password"
            placeholder="Ingrese su contraseña"
            required
          />
        </div>
        <button type="submit" class="btn-primary">ACCEDER</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginComponent",
  data() {
    return {
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch("http://127.0.0.1:5000/api/auth/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: this.email, password: this.password }),
        });

        const data = await response.json();
        if (response.ok) {
<<<<<<< HEAD:educabot/educabot-frontend/src/components/auth/RecuperarContrasena.vue
          this.mensaje = data.mensaje;
          this.error = "";

          // 🔁 Redirigir a login luego de 4 segundos
          setTimeout(() => {
            this.$router.push("/login");
          }, 4000);
=======
          // Guardar token y rol en localStorage
          localStorage.setItem("token", data.token);
          localStorage.setItem("rol", data.rol);

          // Redirección según el rol
          if (data.rol === "estudiante") {
            this.$router.push("/dashboard-estudiantes");
          } else if (data.rol === "docente") {
            this.$router.push("/dashboard-docentes");
          }
>>>>>>> parent of 9dbd3cc (avance 4):educabot/educabot-frontend/src/components/LoginComponent.vue
        } else {
          this.error = data.mensaje || "Error en la autenticación.";
        }
      } catch (error) {
        console.error("Error al iniciar sesión:", error);
        this.error = "Error del servidor.";
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #004aad, #78c0e0);
  font-family: "Arial", sans-serif;
}

.login-card {
  background-color: #ffffff;
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  text-align: center;
  width: 100%;
  max-width: 400px;
}

h2 {
  font-size: 2rem;
  color: #004aad;
}

p {
  color: #666666;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #333333;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 1rem;
}

.btn-primary {
  width: 100%;
  padding: 12px;
  font-size: 1rem;
  background-color: #004aad;
  color: #ffffff;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: transform 0.3s, background-color 0.3s;
}

.btn-primary:hover {
  background-color: #003580;
  transform: scale(1.05);
}
</style>
