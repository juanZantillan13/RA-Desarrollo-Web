import React from "react";
import { Link } from "react-router-dom";
import { Button } from "semantic-ui-react";

export function Error404() {
  return (
    <div style={{ textAlign: "center", padding: "80px 20px" }}>
      <h1 style={{ fontSize: "60px", color: "#6366f1" }}>404</h1>
      <h2>Página no encontrada</h2>
      <p style={{ color: "#64748b" }}>La ruta solicitada no existe en la plataforma PixelVault.</p>
      <Link to="/">
        <Button primary>Volver al Inicio</Button>
      </Link>
    </div>
  );
}
