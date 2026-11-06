import React from "react";
import { Link } from "react-router-dom";
import { Button } from "semantic-ui-react";

export function Home() {
  return (
    <div style={{ textAlign: "center", padding: "60px 20px" }}>
      <h1>🎮 Bienvenido a PixelVault</h1>
      <p style={{ color: "#64748b", fontSize: "16px" }}>
        Plataforma gamer full-stack con Django REST Framework y React.js
      </p>
      <div style={{ marginTop: "30px" }}>
        <Link to="/login">
          <Button primary size="large">Iniciar Sesión</Button>
        </Link>
        <Link to="/register" style={{ marginLeft: "15px" }}>
          <Button secondary size="large">Registrarse</Button>
        </Link>
      </div>
    </div>
  );
}
