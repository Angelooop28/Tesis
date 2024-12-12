import React from 'react';
import { Link } from 'react-router-dom';

function Welcome() {
  return (
    <div className="welcome">
      <h1>Bienvenido a MySite</h1>
      <p>Por favor, inicia sesión o regístrate para continuar.</p>
      <Link to="/login">Iniciar Sesión</Link> | <Link to="/register">Registrarse</Link>
    </div>
  );
}

export default Welcome;
