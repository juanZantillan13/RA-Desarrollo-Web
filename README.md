# 🎮 PixelVault — Full Stack Django & React (RA2: Unidad 2 y 3)

Proyecto Full Stack integral para la plataforma de videojuegos y comunidad **PixelVault**, implementando un Backend en **Django REST Framework** con autenticación JWT y consumo SOAP, y un Frontend moderno en **React (Vite)** siguiendo las **páginas 13 a 35 del manual**.

🔗 **Repositorio Oficial de GitHub:** [https://github.com/juanZantillan13/Practica-4](https://github.com/juanZantillan13/Practica-4)

---

## 📋 Contenido de la Entrega

Este repositorio contiene la solución completa de las **Unidades 2 y 3**:

1. **Parte 1: Frontend en React (Manual Páginas 13 a 35):**
   - Inicialización del proyecto con **Vite** y **React 18** (`/frontend`).
   - Componentes y estilos con **Semantic UI React** y **SASS** (`App.scss`).
   - Sistema modular de rutas con **React Router Dom v6** (`AdminLayout`, `ClientLayout`, `CommonLayout`).
   - Pantalla de **Login** conectada al backend de JWT con validaciones en **Formik** y **Yup**, notificaciones en tiempo real con **React-Toastify**.
   - Contexto de usuario (`AuthContext`) y Custom Hook (`useAuth`) con persistencia en **LocalStorage** para mantener la sesión activa sin cierres al recargar.
   - Pantalla y lógica de **Registro de Nuevos Usuarios** conectada al endpoint de autoregistro.

2. **Parte 2: Integración de API de Terceros (Unidad 3):**
   - En el **Dashboard protegido**, se implementó un widget que consume de forma asíncrona mediante `fetch()` la API externa pública **DummyJSON Quotes API** (`https://dummyjson.com/quotes/random`), mostrando frases motivadoras para gamers con botón de recarga en tiempo real.

3. **Parte 3: Web Services Propios y Consumo SOAP (Unidad 3):**
   - **Web Service Propio:** Endpoint protegido `/api/v1/auth/me/` con `Bearer Token` que retorna los datos del usuario logueado (incluyendo el campo personalizado `gamertag`).
   - **Consumo SOAP:** Endpoint en Django `/api/v1/soap/country/?code=JP` que consume mediante la librería **`zeep`** el servicio SOAP público **CountryInfoService** (`http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL`).

4. **Documento PDF de Entrega:**
   - [`Reporte_RA2_Django_React_SOAP.pdf`](./Reporte_RA2_Django_React_SOAP.pdf) con las 4 evidencias fotográficas solicitadas (Login con token en consola, Dashboard protegido con AuthContext, Widget de API de Terceros, y Consumo SOAP en terminal y navegador).

---

## 📁 Estructura del Proyecto

```text
pixelvault/
├── .gitignore
├── requirements.txt
├── README.md
├── Reporte_RA2_Django_React_SOAP.pdf
├── screenshots/
│   ├── ra2_1_login_token.png
│   ├── ra2_2_dashboard_authcontext.png
│   ├── ra2_3_third_party_widget.png
│   └── ra2_4_soap_consumption.png
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── verify_tests.py
│   ├── generate_ra2_captures.py
│   ├── generate_pdf_report.py
│   ├── pixelvault/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── users/
│       ├── models.py
│       ├── admin.py
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
└── frontend/
    ├── package.json
    ├── vite.config.js
    ├── .env
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── App.scss
        ├── api/
        │   ├── token.js
        │   └── user.js
        ├── context/
        │   └── AuthContext.jsx
        ├── hooks/
        │   ├── useAuth.jsx
        │   └── useUser.jsx
        ├── layouts/
        │   ├── AdminLayout.jsx
        │   ├── ClientLayout.jsx
        │   ├── CommonLayout.jsx
        │   └── index.jsx
        ├── pages/
        │   ├── admin/
        │   │   └── Dashboard.jsx
        │   ├── client/
        │   │   └── Home.jsx
        │   └── common/
        │       ├── Login.jsx
        │       ├── Register.jsx
        │       └── Error404.jsx
        └── routes/
            ├── routes.admin.jsx
            ├── routes.client.jsx
            ├── routes.common.jsx
            ├── routes.js
            └── Navigation.jsx
```

---

## 🚀 Guía de Instalación y Ejecución

### 1. Clonar el Repositorio
```bash
git clone https://github.com/juanZantillan13/Practica-4.git
cd Practica-4
```

---

### 2. Ejecutar el Backend (Django)
```bash
cd backend

# Crear y activar entorno virtual
python -m venv venv
.\venv\Scripts\activate   # En Windows
# source venv/bin/activate  # En Linux / Mac

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# Iniciar servidor Django
python manage.py runserver
```
El Backend estará corriendo en `http://127.0.0.1:8000/`.
- **Swagger UI:** `http://127.0.0.1:8000/swagger/`
- **Django Admin:** `http://127.0.0.1:8000/admin/`
- **Endpoint SOAP:** `http://127.0.0.1:8000/api/v1/soap/country/?code=MX`

---

### 3. Ejecutar el Frontend (React + Vite)
En una nueva terminal:
```bash
cd frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo Vite
npm run dev
```
El Frontend estará corriendo en `http://localhost:5173/`.

---

## 👥 Cuentas de Prueba Pre-configuradas

| Usuario | Correo Electrónico | Contraseña | Gamertag | Rol |
|---|---|---|---|---|
| **Administrador** | `admin@pixelvault.gg` | `AdminPassword123!` | `PixelMaster` | Staff / Admin |
| **Gamer Cloud** | `cloud_strife@pixelvault.gg` | `OriginalPassword456!` | `BusterSword97` | Usuario regular |
| **Gamer Sephiroth** | `sephiroth@pixelvault.gg` | `MasamuneSword123!` | `OneWingedAngel` | Usuario registrado |

---

## 🧪 Pruebas Automatizadas

Para validar todos los endpoints de autenticación, tiempo de vida del token (2h), seguridad contra fugas de contraseña y el consumo SOAP:
```bash
cd backend
python verify_tests.py
```
Resultado esperado: `>>> TODAS LAS PRUEBAS Y CORRECCIONES PASARON AL 100% <<<`
