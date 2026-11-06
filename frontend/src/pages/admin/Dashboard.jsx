import React, { useState, useEffect } from "react";
import { Button, Loader } from "semantic-ui-react";
import { useAuth } from "../../hooks/useAuth";

export function Dashboard() {
  const { logout, auth } = useAuth();
  const user = auth?.me;

  // Estado para el widget de API de terceros (Parte 2: Unidad 3)
  const [thirdPartyData, setThirdPartyData] = useState(null);
  const [loadingApi, setLoadingApi] = useState(true);
  const [apiError, setApiError] = useState(null);

  // Función para consumir API de terceros gratuita usando fetch
  const fetchThirdPartyQuote = async () => {
    setLoadingApi(true);
    setApiError(null);
    try {
      const response = await fetch("https://dummyjson.com/quotes/random");
      if (!response.ok) {
        throw new Error("Respuesta no satisfactoria de la API externa");
      }
      const data = await response.json();
      setThirdPartyData(data);
    } catch (err) {
      console.error("Error al consultar API externa:", err);
      // Fallback temático en caso de no tener conexión a internet
      setThirdPartyData({
        quote: "No importa qué tan difícil sea el juego, un verdadero gamer nunca se rinde.",
        author: "PixelVault Master",
      });
    } finally {
      setLoadingApi(false);
    }
  };

  useEffect(() => {
    fetchThirdPartyQuote();
  }, []);

  return (
    <div className="dashboard-container">
      {/* Encabezado del Dashboard */}
      <div className="dashboard-header">
        <div className="header-info">
          <h1>🎮 Dashboard Gamer - PixelVault</h1>
          <div className="user-badge">
            Sesión activa: <strong>{user?.email}</strong>{" "}
            {user?.gamertag && (
              <span style={{ color: "#10b981", marginLeft: "6px" }}>
                [{user.gamertag}]
              </span>
            )}
          </div>
        </div>
        <Button
          color="red"
          content="Cerrar Sesión"
          icon="sign-out"
          onClick={logout}
        />
      </div>

      <div className="dashboard-grid">
        {/* Tarjeta 1: Perfil del Usuario Protegido (AuthContext + Django /auth/me/) */}
        <div className="card-box">
          <h3>
            <i className="user circle icon" style={{ color: "#6366f1" }}></i>
            Datos del Usuario Autenticado (AuthContext)
          </h3>
          <ul className="user-details-list">
            <li>
              <span className="label">Correo Electrónico:</span>
              <span className="val">{user?.email || "No disponible"}</span>
            </li>
            <li>
              <span className="label">Gamertag (Campo Extra):</span>
              <span className="val" style={{ color: "#10b981" }}>
                {user?.gamertag || "Sin Gamertag asignado"}
              </span>
            </li>
            <li>
              <span className="label">Nombre de Usuario:</span>
              <span className="val">{user?.username || "N/A"}</span>
            </li>
            <li>
              <span className="label">Nombre Completo:</span>
              <span className="val">
                {`${user?.first_name || ""} ${user?.last_name || ""}`.trim() ||
                  "Sin nombre registrado"}
              </span>
            </li>
            <li>
              <span className="label">Rol en Plataforma:</span>
              <span className="val">
                {user?.is_staff ? "Administrador (Staff)" : "Jugador (Gamer)"}
              </span>
            </li>
            <li>
              <span className="label">Estado de Cuenta:</span>
              <span className="val" style={{ color: user?.is_active ? "#10b981" : "#ef4444" }}>
                {user?.is_active ? "Activo" : "Inactivo"}
              </span>
            </li>
          </ul>
        </div>

        {/* Tarjeta 2: Widget de API de Terceros (Parte 2 de la Práctica) */}
        <div className="third-party-widget">
          <h3>
            <i className="quote left icon"></i>
            Widget de API de Terceros (Frase Motivadora Gamer)
          </h3>
          <p style={{ color: "#e0e7ff", fontSize: "13px" }}>
            Datos consumidos en tiempo real mediante <code>fetch()</code> desde la API externa gratuita{" "}
            <strong>DummyJSON Quotes API</strong>.
          </p>

          {loadingApi ? (
            <div style={{ padding: "30px 0", textAlign: "center" }}>
              <Loader active inline="centered" inverted content="Consultando API de terceros..." />
            </div>
          ) : (
            <>
              <div className="quote-box">
                <div className="quote-text">"{thirdPartyData?.quote}"</div>
                <div className="quote-author">— {thirdPartyData?.author}</div>
              </div>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <span className="api-badge">API Externa: https://dummyjson.com/quotes/random</span>
                <Button
                  size="mini"
                  inverted
                  icon="refresh"
                  content="Nueva Frase"
                  onClick={fetchThirdPartyQuote}
                />
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
