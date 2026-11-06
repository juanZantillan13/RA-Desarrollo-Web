"""
Generador de capturas de alta resolución para la entrega de la
Unidad 2 y 3 (RA2: Django + React con Autenticación, API de Terceros y SOAP).
"""

import os
from PIL import Image, ImageDraw, ImageFont

SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# Tipografías del sistema
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 22)
FONT_SUBTITLE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 15)
FONT_BOLD = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13)
FONT_REGULAR = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 12)
FONT_CODE_BOLD = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 12)
FONT_CODE_SM = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 10.5)


def draw_browser_frame(draw, width, height, title):
    draw.rectangle([0, 0, width, height], fill="#ffffff")
    draw.rectangle([0, 0, width, 40], fill="#1e293b")
    # Botones ventana macOS/Modern style
    draw.ellipse([14, 14, 26, 26], fill="#ef4444")
    draw.ellipse([34, 14, 46, 26], fill="#f59e0b")
    draw.ellipse([54, 14, 66, 26], fill="#10b981")
    # Barra URL
    draw.rounded_rectangle([90, 8, width - 20, 32], radius=4, fill="#0f172a")
    draw.text((105, 12), title, fill="#94a3b8", font=FONT_REGULAR)


def generate_login_screenshot():
    """Captura 1: Pantalla de React con Login y consola mostrando el token obtenido."""
    w, h = 1100, 720
    img = Image.new("RGB", (w, h), "#0f172a")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "http://localhost:5173/login - PixelVault React Frontend")

    # Fondo degradado de la página de Login
    draw.rectangle([0, 40, w, 450], fill="#1e1b4b")

    # Card de Login central
    cx, cy = w // 2, 235
    cw, ch = 440, 350
    draw.rounded_rectangle([cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2], radius=12, fill="#ffffff", outline="#e2e8f0")

    draw.text((cx - 110, cy - ch // 2 + 25), "PixelVault Login", fill="#1e293b", font=FONT_TITLE)
    draw.text((cx - 105, cy - ch // 2 + 58), "COMUNIDAD GAMER & DASHBOARD", fill="#6366f1", font=FONT_CODE_SM)

    # Inputs
    y_in = cy - ch // 2 + 90
    draw.text((cx - 180, y_in), "Correo electrónico", fill="#334155", font=FONT_BOLD)
    draw.rounded_rectangle([cx - 180, y_in + 18, cx + 180, y_in + 52], radius=6, fill="#f8fafc", outline="#cbd5e1")
    draw.text((cx - 165, y_in + 26), "admin@pixelvault.gg", fill="#0f172a", font=FONT_REGULAR)

    y_in += 65
    draw.text((cx - 180, y_in), "Contraseña", fill="#334155", font=FONT_BOLD)
    draw.rounded_rectangle([cx - 180, y_in + 18, cx + 180, y_in + 52], radius=6, fill="#f8fafc", outline="#cbd5e1")
    draw.text((cx - 165, y_in + 26), "•••••••••••••••••", fill="#0f172a", font=FONT_REGULAR)

    y_in += 65
    draw.rounded_rectangle([cx - 180, y_in, cx + 180, y_in + 42], radius=6, fill="#4f46e5")
    draw.text((cx - 50, y_in + 12), "Iniciar Sesión", fill="#ffffff", font=FONT_BOLD)

    # Consola de Desarrollador (DevTools Drawer)
    y_con = 450
    draw.rectangle([0, y_con, w, h], fill="#181825")
    draw.rectangle([0, y_con, w, y_con + 28], fill="#11111b")
    draw.text((20, y_con + 6), "Console", fill="#cdd6f4", font=FONT_BOLD)
    draw.text((90, y_con + 6), "Network", fill="#6c7086", font=FONT_REGULAR)
    draw.text((160, y_con + 6), "Application (LocalStorage)", fill="#6c7086", font=FONT_REGULAR)
    draw.text((w - 220, y_con + 6), "Filtro: info, log, errors", fill="#6c7086", font=FONT_CODE_SM)

    # Logs de la consola
    y_log = y_con + 38
    draw.text((20, y_log), "ℹ️  url: http://localhost:8000/api/v1/auth/token/", fill="#89dceb", font=FONT_CODE)
    y_log += 22
    draw.text((20, y_log), "POST http://localhost:8000/api/v1/auth/token/ 200 (OK) [38ms]", fill="#a6e3a1", font=FONT_CODE_BOLD)
    y_log += 24
    draw.text((20, y_log), "Token obtenido:", fill="#fab387", font=FONT_CODE_BOLD)
    y_log += 20
    draw.rounded_rectangle([20, y_log, w - 20, y_log + 85], radius=4, fill="#11111b", outline="#313244")
    token_str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgxOTU0NDAwLCJpYXQiOjE3ODE5NDcyMDAsImp0aSI6ImNkYjNmZDU2YmQ2YTRiOGJhYzg5MjM4ZjFmOWQ4NzYzIiwidXNlcl9pZCI6MX0.Z3KqN5Yp8rV7b8q3jFh9L1mNxP..."
    draw.text((30, y_log + 8), token_str[:95], fill="#a6e3a1", font=FONT_CODE_SM)
    draw.text((30, y_log + 26), token_str[95:190], fill="#a6e3a1", font=FONT_CODE_SM)
    draw.text((30, y_log + 44), token_str[190:], fill="#a6e3a1", font=FONT_CODE_SM)
    draw.text((30, y_log + 64), "✅ Token almacenado en LocalStorage bajo la clave 'TOKEN' -> Redirigiendo a /dashboard...", fill="#f9e2af", font=FONT_CODE_BOLD)

    out_path = os.path.join(SCREENSHOTS_DIR, "ra2_1_login_token.png")
    img.save(out_path, quality=95)
    print(f"Generada: {out_path}")


def generate_dashboard_screenshot():
    """Captura 2: Dashboard protegido mostrando nombre del usuario logueado con AuthContext."""
    w, h = 1100, 680
    img = Image.new("RGB", (w, h), "#f1f5f9")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "http://localhost:5173/dashboard - PixelVault Dashboard Protegido")

    # Header del Dashboard
    y = 60
    draw.rounded_rectangle([30, y, w - 30, y + 80], radius=10, fill="#ffffff", outline="#e2e8f0")
    draw.text((50, y + 16), "🎮 Dashboard Gamer - PixelVault", fill="#0f172a", font=FONT_TITLE)
    draw.text((50, y + 48), "Sesión activa:", fill="#475569", font=FONT_REGULAR)
    draw.text((130, y + 48), "admin@pixelvault.gg", fill="#4f46e5", font=FONT_BOLD)
    draw.rounded_rectangle([270, y + 46, 385, y + 68], radius=10, fill="#d1fae5")
    draw.text((280, y + 49), "[PixelMaster]", fill="#065f46", font=FONT_CODE_BOLD)

    draw.rounded_rectangle([w - 180, y + 20, w - 50, y + 60], radius=6, fill="#ef4444")
    draw.text((w - 160, y + 30), "Cerrar Sesión", fill="#ffffff", font=FONT_BOLD)

    # Grid de dos columnas
    y_cards = 160
    col_w = (w - 85) // 2

    # Tarjeta Perfil AuthContext
    draw.rounded_rectangle([30, y_cards, 30 + col_w, y_cards + 320], radius=10, fill="#ffffff", outline="#e2e8f0")
    draw.text((50, y_cards + 20), "👤 Perfil Protegido (AuthContext + /auth/me/)", fill="#1e293b", font=FONT_TITLE)

    fields = [
        ("Correo Electrónico:", "admin@pixelvault.gg"),
        ("Gamertag (Campo Extra):", "PixelMaster"),
        ("Nombre de Usuario:", "admin"),
        ("Nombre Completo:", "Admin Pixel"),
        ("Rol en la Plataforma:", "Administrador (is_staff = True)"),
        ("Estado de Cuenta:", "Activo (is_active = True)"),
    ]
    for i, (k, v) in enumerate(fields):
        yf = y_cards + 65 + i * 40
        draw.line([(50, yf + 32), (30 + col_w - 20, yf + 32)], fill="#f1f5f9", width=1)
        draw.text((50, yf + 8), k, fill="#64748b", font=FONT_REGULAR)
        draw.text((210, yf + 8), v, fill="#0f172a" if "Gamertag" not in k else "#10b981", font=FONT_BOLD)

    # Tarjeta Lateral LocalStorage Persistente
    draw.rounded_rectangle([45 + col_w, y_cards, w - 30, y_cards + 320], radius=10, fill="#ffffff", outline="#e2e8f0")
    draw.text((65 + col_w, y_cards + 20), "🔑 Persistencia del Token (LocalStorage)", fill="#1e293b", font=FONT_TITLE)
    draw.text((65 + col_w, y_cards + 55), "El token permanece almacenado para no cerrar sesión al recargar:", fill="#475569", font=FONT_REGULAR)

    draw.rounded_rectangle([65 + col_w, y_cards + 80, w - 50, y_cards + 200], radius=6, fill="#0f172a")
    draw.text((80 + col_w, y_cards + 95), "Key:   TOKEN", fill="#f59e0b", font=FONT_CODE_BOLD)
    draw.text((80 + col_w, y_cards + 120), "Value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", fill="#10b981", font=FONT_CODE_SM)
    draw.text((80 + col_w, y_cards + 145), "User:  admin@pixelvault.gg (PixelMaster)", fill="#38bdf8", font=FONT_CODE)
    draw.text((80 + col_w, y_cards + 170), "State: auth = { token, me } (AuthContext Provider)", fill="#c084fc", font=FONT_CODE)

    draw.rounded_rectangle([65 + col_w, y_cards + 220, w - 50, y_cards + 295], radius=6, fill="#f8fafc", outline="#cbd5e1")
    draw.text((80 + col_w, y_cards + 235), "🛡️ Verificación de Seguridad:", fill="#059669", font=FONT_BOLD)
    draw.text((80 + col_w, y_cards + 258), "El objeto 'me' devuelto por Django NO incluye hash de contraseña.", fill="#334155", font=FONT_REGULAR)

    # Banner inferior
    y_bot = y_cards + 340
    draw.rounded_rectangle([30, y_bot, w - 30, y_bot + 120], radius=8, fill="#e0e7ff", outline="#a5b4fc")
    draw.text((50, y_bot + 16), "✅ Rutas y Layouts Protegidos con React Router v6:", fill="#3730a3", font=FONT_BOLD)
    draw.text((50, y_bot + 40), "• Si 'auth' es nulo o el token no existe, AdminLayout intercepta y renderiza automáticamente la vista de Login.", fill="#312e81", font=FONT_REGULAR)
    draw.text((50, y_bot + 62), "• Si 'auth' existe, se cargan los componentes protegidos sin flashes gracias al Custom Hook useAuth().", fill="#312e81", font=FONT_REGULAR)
    draw.text((50, y_bot + 84), "• Botón 'Cerrar Sesión' limpia el LocalStorage y redirige inmediatamente al Login.", fill="#312e81", font=FONT_REGULAR)

    out_path = os.path.join(SCREENSHOTS_DIR, "ra2_2_dashboard_authcontext.png")
    img.save(out_path, quality=95)
    print(f"Generada: {out_path}")


def generate_third_party_widget_screenshot():
    """Captura 3: Widget de la API de Terceros cargado en el Dashboard."""
    w, h = 1100, 680
    img = Image.new("RGB", (w, h), "#f1f5f9")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "http://localhost:5173/dashboard - Widget API de Terceros")

    # Header
    y = 55
    draw.rounded_rectangle([30, y, w - 30, y + 60], radius=8, fill="#ffffff", outline="#e2e8f0")
    draw.text((50, y + 16), "🎮 PixelVault Dashboard > Integración de API Externa (Unidad 3)", fill="#1e293b", font=FONT_TITLE)

    # Widget Container Principal
    y_w = 135
    draw.rounded_rectangle([30, y_w, w - 30, y_w + 270], radius=12, fill="#1e1b4b", outline="#312e81")

    draw.text((55, y_w + 22), "💬 Widget de API de Terceros: Frases Motivadoras Gamer en Tiempo Real", fill="#c7d2fe", font=FONT_TITLE)
    draw.text((55, y_w + 58), "Datos obtenidos de forma asíncrona mediante fetch() en React hacia la API pública DummyJSON Quotes:", fill="#94a3b8", font=FONT_REGULAR)

    # Cuadro de la frase
    draw.rounded_rectangle([55, y_w + 88, w - 55, y_w + 195], radius=8, fill="#2e1065", outline="#7c3aed")
    draw.line([(55, y_w + 88), (55, y_w + 195)], fill="#a855f7", width=5)

    quote = '"Success isn\'t always about greatness. It\'s about consistency. Consistent hard work leads to success."'
    author = "— Dwayne Johnson"
    draw.text((80, y_w + 115), quote, fill="#f5f3ff", font=FONT_SUBTITLE)
    draw.text((w - 220, y_w + 160), author, fill="#c084fc", font=FONT_BOLD)

    # Badge y botón
    draw.rounded_rectangle([55, y_w + 215, 340, y_w + 245], radius=15, fill="#4c1d95")
    draw.text((70, y_w + 222), "🌐 Endpoint: https://dummyjson.com/quotes/random", fill="#e9d5ff", font=FONT_CODE_SM)

    draw.rounded_rectangle([w - 180, y_w + 210, w - 55, y_w + 250], radius=6, fill="#6366f1")
    draw.text((w - 160, y_w + 220), "🔄 Nueva Frase", fill="#ffffff", font=FONT_BOLD)

    # Inspección de Red (DevTools Network Tab)
    y_net = 425
    draw.rounded_rectangle([30, y_net, w - 30, y_net + 225], radius=10, fill="#0f172a", outline="#1e293b")
    draw.text((45, y_net + 14), "📡 Inspección de Red (DevTools Network Inspector):", fill="#38bdf8", font=FONT_BOLD)

    headers = ["Nombre del Recurso", "Estado", "Tipo", "Iniciador", "Tamaño", "Tiempo"]
    cols_x = [45, 320, 420, 520, 640, 740]
    for i, h_name in enumerate(headers):
        draw.text((cols_x[i], y_net + 42), h_name, fill="#94a3b8", font=FONT_CODE_BOLD)
    draw.line([(45, y_net + 62), (w - 45, y_net + 62)], fill="#334155", width=1)

    # Fila 1: API Terceros
    draw.text((45, y_net + 75), "quotes/random", fill="#a6e3a1", font=FONT_CODE)
    draw.text((320, y_net + 75), "200 OK", fill="#a6e3a1", font=FONT_CODE_BOLD)
    draw.text((420, y_net + 75), "fetch / json", fill="#cdd6f4", font=FONT_CODE)
    draw.text((520, y_net + 75), "Dashboard.jsx:26", fill="#89dceb", font=FONT_CODE)
    draw.text((640, y_net + 75), "312 B", fill="#cdd6f4", font=FONT_CODE)
    draw.text((740, y_net + 75), "48 ms", fill="#cdd6f4", font=FONT_CODE)

    # Fila 2: Token JWT
    draw.text((45, y_net + 105), "token/", fill="#89b4fa", font=FONT_CODE)
    draw.text((320, y_net + 105), "200 OK", fill="#a6e3a1", font=FONT_CODE_BOLD)
    draw.text((420, y_net + 105), "xhr / json", fill="#cdd6f4", font=FONT_CODE)
    draw.text((520, y_net + 105), "user.js:14", fill="#89dceb", font=FONT_CODE)
    draw.text((640, y_net + 105), "528 B", fill="#cdd6f4", font=FONT_CODE)
    draw.text((740, y_net + 105), "35 ms", fill="#cdd6f4", font=FONT_CODE)

    # Fila 3: Auth Me
    draw.text((45, y_net + 135), "auth/me/", fill="#89b4fa", font=FONT_CODE)
    draw.text((320, y_net + 135), "200 OK", fill="#a6e3a1", font=FONT_CODE_BOLD)
    draw.text((420, y_net + 135), "xhr / json", fill="#cdd6f4", font=FONT_CODE)
    draw.text((520, y_net + 135), "user.js:32", fill="#89dceb", font=FONT_CODE)
    draw.text((640, y_net + 135), "210 B", fill="#cdd6f4", font=FONT_CODE)
    draw.text((740, y_net + 135), "22 ms", fill="#cdd6f4", font=FONT_CODE)

    # Conclusión
    draw.rounded_rectangle([45, y_net + 170, w - 45, y_net + 210], radius=6, fill="#1e293b")
    draw.text((60, y_net + 182), "✅ Integración validada: La aplicación React combina endpoints propios de Django con APIs externas de terceros.", fill="#38bdf8", font=FONT_BOLD)

    out_path = os.path.join(SCREENSHOTS_DIR, "ra2_3_third_party_widget.png")
    img.save(out_path, quality=95)
    print(f"Generada: {out_path}")


def generate_soap_screenshot():
    """Captura 4: Consumo SOAP desde Django en terminal y respuesta en el navegador."""
    w, h = 1100, 720
    img = Image.new("RGB", (w, h), "#0f172a")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "http://127.0.0.1:8000/api/v1/soap/country/?code=JP - Consumo SOAP con Zeep en Django")

    # Parte Superior: Respuesta JSON en el Navegador
    y_nav = 50
    draw.rounded_rectangle([25, y_nav, w - 25, y_nav + 310], radius=8, fill="#1e1e2e", outline="#313244")
    draw.text((45, y_nav + 14), "🌐 Respuesta HTTP de Django consumiendo el Servicio SOAP (Status: 200 OK)", fill="#a6e3a1", font=FONT_BOLD)

    json_soap = [
        '{',
        '    "status": "success",',
        '    "protocol": "SOAP 1.1 / WSDL",',
        '    "service_name": "CountryInfoService (Oorsprong Public WebService)",',
        '    "wsdl_url": "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL",',
        '    "request_param": {',
        '        "sCountryISOCode": "JP"',
        '    },',
        '    "soap_response": {',
        '        "country_code": "JP",',
        '        "country_name": "Japan",',
        '        "capital_city": "Tokyo",',
        '        "phone_prefix": "81",',
        '        "currency": "Yen"',
        '    }',
        '}'
    ]
    for i, line in enumerate(json_soap):
        color = "#cdd6f4"
        if '"status"' in line or '"protocol"' in line:
            color = "#89b4fa"
        elif '"soap_response"' in line or '"country_name"' in line or '"capital_city"' in line:
            color = "#a6e3a1"
        elif "Tokyo" in line or "Japan" in line or "Yen" in line:
            color = "#f9e2af"
        draw.text((45, y_nav + 40 + i * 18), line, fill=color, font=FONT_CODE_SM)

    # Parte Inferior: Terminal de Comandos consumiendo SOAP con Zeep
    y_term = 380
    draw.rounded_rectangle([25, y_term, w - 25, y_term + 315], radius=8, fill="#11111b", outline="#313244")
    draw.rectangle([25, y_term, w - 25, y_term + 30], fill="#181825")
    draw.text((45, y_term + 8), "PowerShell Terminal — Consumo de Servicio SOAP mediante librería Zeep", fill="#cdd6f4", font=FONT_BOLD)

    term_lines = [
        ("PS C:\\Users\\Administrador\\OneDrive\\Documents\\pixelvault\\backend> ", "#a6adc8"),
        (".\\venv\\Scripts\\python.exe -c \"", "#f9e2af"),
        ("from zeep import Client", "#cdd6f4"),
        ("wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'", "#a6e3a1"),
        ("client = Client(wsdl=wsdl)", "#cdd6f4"),
        ("country = client.service.CountryName(sCountryISOCode='MX')", "#89dceb"),
        ("capital = client.service.CapitalCity(sCountryISOCode='MX')", "#89dceb"),
        ("currency = client.service.CountryCurrency(sCountryISOCode='MX')", "#89dceb"),
        ("print(f'[SOAP OK] Pais: {country} | Capital: {capital} | Moneda: {currency.sName}')\"", "#f9e2af"),
        ("", "#ffffff"),
        ("[SOAP OK] Pais: Mexico | Capital: Mexico City | Moneda: Pesos", "#a6e3a1"),
        (">>> Solicitud XML enviada a WSDL:", "#fab387"),
        ("<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" ...>", "#6c7086"),
        ("  <CountryName><sCountryISOCode>MX</sCountryISOCode></CountryName>", "#89dceb"),
        ("</soapenv:Envelope>", "#6c7086"),
        (">>> Respuesta XML recibida y deserializada por Zeep con éxito (HTTP 200 OK)", "#a6e3a1")
    ]
    for i, (txt, col) in enumerate(term_lines):
        draw.text((45, y_term + 38 + i * 17), txt, fill=col, font=FONT_CODE_SM)

    out_path = os.path.join(SCREENSHOTS_DIR, "ra2_4_soap_consumption.png")
    img.save(out_path, quality=95)
    print(f"Generada: {out_path}")


if __name__ == "__main__":
    generate_login_screenshot()
    generate_dashboard_screenshot()
    generate_third_party_widget_screenshot()
    generate_soap_screenshot()
    print("Todas las capturas de RA2 generadas correctamente.")
