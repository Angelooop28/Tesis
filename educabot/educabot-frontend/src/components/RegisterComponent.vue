
<template>
  <div class="register-container">
    <div class="register-card">
      <h2>Registrarse en Educabot</h2>
      <p>Complete los datos para crear su cuenta</p>
      <form @submit.prevent="register">
        <input v-model="form.nombre" type="text" placeholder="Nombre" required />
        <input v-model="form.email" type="email" placeholder="Correo Electrónico" required />
        <input v-model="form.password" type="password" placeholder="Contraseña" required />
        <select v-model="form.rol" required>
          <option disabled value="">Seleccione un rol</option>
          <option value="estudiante">Estudiante</option>
          <option value="docente">Docente</option>
        </select>
        <button type="submit" class="btn-primary">Registrar</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        nombre: "",
        email: "",
        password: "",
        rol: "",
      },
    };
  },
  methods: {
    async register() {
      try {
        await axios.post("http://localhost:5000/api/auth/register", this.form);
        alert("Registro exitoso. Por favor, inicie sesión.");
        this.$router.push("/login");
      } catch (error) {
        alert(error.response?.data?.mensaje || "Error al registrarse");
      }
    },
  },
};
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #004aad, #78c0e0);
  font-family: "Arial", sans-serif;
}

.register-card {
  background-color: #ffffff;
  padding: 30px;
  border-radius: 15px;
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

input,
select {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 10px;
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
