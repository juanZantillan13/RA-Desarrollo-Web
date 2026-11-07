"""
Generador del Documento PDF Oficial de Entrega para:
RA2 Django + React con Autenticación y APIs (Unidades 2 y 3)
Manual Páginas 13 a 35 + API de Terceros + Consumo SOAP.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, Table, TableStyle, PageBreak
)
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "..", "screenshots")
PDF_OUTPUT_PATH = os.path.join(BASE_DIR, "..", "Reporte_RA2_Django_React_SOAP.pdf")
PDF_COPY_OLD = os.path.join(BASE_DIR, "..", "Reporte_Proyecto_PixelVault_Django.pdf")
PDF_ROOT_COPY = os.path.join(BASE_DIR, "..", "..", "Reporte_RA2_Django_React_SOAP.pdf")


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#334155"))
        self.drawString(36, 762, "RA2 DJANGO + REACT CON AUTENTICACIÓN, API DE TERCEROS Y SOAP (UNIDADES 2 Y 3)")
        self.setFont("Helvetica", 8)
        self.drawRightString(576, 762, "PixelVault Gaming Platform • Manual Págs. 13-35")
        self.setStrokeColor(colors.HexColor("#cbd5e0"))
        self.setLineWidth(0.5)
        self.line(36, 756, 576, 756)

        self.line(36, 42, 576, 42)
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(36, 30, "Repositorio GitHub: https://github.com/juanZantillan13/RA-Desarrollo-Web")
        self.drawRightString(576, 30, f"Página {self._pageNumber} de {page_count}")
        self.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        PDF_OUTPUT_PATH,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=48,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#4f46e5"),
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#1e293b"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#334155")
    )

    story = []

    # ==========================
    # PÁGINA 1: PORTADA Y METADATOS
    # ==========================
    story.append(Paragraph("🎮 RA2 Django + React con Autenticación y APIs", title_style))
    story.append(Paragraph("Cierre de Unidades 2 y 3 — Manual Páginas 13 a 35 + API de Terceros + SOAP", subtitle_style))

    meta_data = [
        [
            Paragraph("<b>Proyecto:</b> PixelVault (Plataforma de Videojuegos)", body_style),
            Paragraph("<b>Materia:</b> Desarrollo Full Stack (DWI) / Web Services", body_style)
        ],
        [
            Paragraph("<b>Backend:</b> Django 6.1 • DRF 3.18 • SimpleJWT • Zeep (SOAP)", body_style),
            Paragraph("<b>Frontend:</b> React 18 • Vite • Semantic UI • Formik • SASS", body_style)
        ],
        [
            Paragraph("<b>Web Services:</b> Propio (/auth/me/) • SOAP (CountryInfo WSDL)", body_style),
            Paragraph("<b>API de Terceros:</b> DummyJSON Quotes API (en Dashboard)", body_style)
        ],
        [
            Paragraph("<b>Repositorio GitHub:</b> <font color='#2563eb'><u>https://github.com/juanZantillan13/RA-Desarrollo-Web</u></font>", body_style),
            Paragraph("<b>Estado de Entrega:</b> 100% Completo y Validado ✅", body_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    # Resumen técnico de requisitos
    story.append(Paragraph("1. Resumen de Requisitos Implementados", h1_style))
    resumen_text = (
        "• <b>Parte 1: Frontend en React (Manual Páginas 13 a 35):</b> Proyecto inicializado con Vite y React 18, "
        "configuración de Semantic UI React, SASS, sistema modular de rutas con React Router Dom v6 (AdminLayout, "
        "ClientLayout, CommonLayout), formulario de Login con Formik + Yup + Toastify conectado al backend de JWT, "
        "persistencia de sesión con AuthContext y useAuth en LocalStorage, y pantalla de Registro de nuevos usuarios.<br/>"
        "• <b>Parte 2: Integración de API de Terceros (Unidad 3):</b> En el Dashboard protegido se integró un widget "
        "que consume en tiempo real la API externa gratuita DummyJSON Quotes mediante <code>fetch()</code> asíncrono.<br/>"
        "• <b>Parte 3: Web Services Propios y Consumo SOAP (Unidad 3):</b> Web Service propio con datos protegidos "
        "(<code>/api/v1/auth/me/</code> con Bearer Token) y consumo de un Web Service SOAP público (CountryInfoService WSDL) "
        "en Django mediante la librería <code>zeep</code> a través del endpoint <code>/api/v1/soap/country/</code>."
    )
    story.append(Paragraph(resumen_text, body_style))
    story.append(Spacer(1, 8))

    # CAPTURA 1: LOGIN Y TOKEN
    story.append(Paragraph("Captura 1: Login Funcionando en React y Consola con Token JWT", h1_style))
    story.append(Paragraph(
        "Se observa el formulario de Login en React (<code>http://localhost:5173/login</code>). Al ingresar las credenciales, "
        "se efectúa la petición POST a <code>/api/v1/auth/token/</code>, obteniendo el token de acceso JWT (código 200 OK) "
        "el cual se imprime en la consola de desarrollador y se almacena en el LocalStorage para persistir la sesión.",
        body_style
    ))
    story.append(Spacer(1, 4))
    img1 = os.path.join(SCREENSHOTS_DIR, "ra2_1_login_token.png")
    if os.path.exists(img1):
        story.append(RLImage(img1, width=540, height=345))

    story.append(PageBreak())

    # ==========================
    # PÁGINA 2: DASHBOARD Y API TERCEROS
    # ==========================
    # CAPTURA 2: DASHBOARD PROTEGIDO
    story.append(Paragraph("Captura 2: Dashboard Protegido con Nombre de Usuario (AuthContext)", h1_style))
    story.append(Paragraph(
        "Ruta protegida <code>/dashboard</code> en React accesible únicamente para usuarios autenticados. "
        "Gracias al Custom Hook <code>useAuth()</code> y al <code>AuthProvider</code>, se muestran los datos personales "
        "recuperados desde el endpoint <code>/auth/me/</code> (correo: <b>admin@pixelvault.gg</b>, gamertag: <b>PixelMaster</b>, "
        "nombre: <b>Admin Pixel</b>), así como la persistencia de la clave <code>TOKEN</code> en LocalStorage.",
        body_style
    ))
    story.append(Spacer(1, 4))
    img2 = os.path.join(SCREENSHOTS_DIR, "ra2_2_dashboard_authcontext.png")
    if os.path.exists(img2):
        story.append(RLImage(img2, width=540, height=330))

    story.append(Spacer(1, 8))

    # CAPTURA 3: WIDGET API TERCEROS
    story.append(Paragraph("Captura 3: Widget de API de Terceros Consumido con fetch() en Dashboard", h1_style))
    story.append(Paragraph(
        "Integración de la Unidad 3: En el Dashboard se muestra la sección dinámica que consulta una frase motivadora gamer "
        "desde la API externa <code>https://dummyjson.com/quotes/random</code>. En la parte inferior se muestra la pestaña "
        "Network de las DevTools confirmando la petición <b>fetch / json con código 200 OK</b> conviviendo armónicamente con los endpoints de Django.",
        body_style
    ))
    story.append(Spacer(1, 4))
    img3 = os.path.join(SCREENSHOTS_DIR, "ra2_3_third_party_widget.png")
    if os.path.exists(img3):
        story.append(RLImage(img3, width=540, height=330))

    story.append(PageBreak())

    # ==========================
    # PÁGINA 3: CONSUMO SOAP Y CONCLUSIONES
    # ==========================
    # CAPTURA 4: CONSUMO SOAP CON ZEEP
    story.append(Paragraph("Captura 4: Consumo de Servicio SOAP Público en Django usando Zeep", h1_style))
    story.append(Paragraph(
        "Demostración de la Parte 3 (Unidad 3): Se implementó en Django el endpoint <code>/api/v1/soap/country/</code> "
        "que consume mediante la librería <code>zeep</code> el servicio SOAP público <b>CountryInfoService (WSDL)</b>. "
        "Arriba se observa la respuesta JSON devuelta por Django al navegador con los datos de Japón (Tokyo, Yen, código 81) "
        "y abajo la ejecución de prueba en la terminal de PowerShell consumiendo las operaciones SOAP con éxito.",
        body_style
    ))
    story.append(Spacer(1, 4))
    img4 = os.path.join(SCREENSHOTS_DIR, "ra2_4_soap_consumption.png")
    if os.path.exists(img4):
        story.append(RLImage(img4, width=540, height=345))

    story.append(Spacer(1, 10))

    # Conclusión
    concl_data = [
        [Paragraph("<b>Conclusión y Validación de la Entrega (Unidad 2 y 3):</b>", h1_style)],
        [Paragraph(
            "Se ha completado satisfactoriamente el ciclo full-stack del manual (páginas 13 a 35) y los requerimientos de la Unidad 3: "
            "Backend Django REST Framework + JWT, Frontend en React con Vite, rutas protegidas con AuthContext, consumo asíncrono "
            "de una API REST externa de terceros y consumo de un Web Service SOAP público con Zeep. El código completo y actualizado "
            "se encuentra disponible en el repositorio de GitHub: <b>https://github.com/juanZantillan13/RA-Desarrollo-Web</b>.",
            body_style
        )]
    ]
    t_concl = Table(concl_data, colWidths=[540])
    t_concl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f0fdf4")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#86efac")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_concl)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado: {PDF_OUTPUT_PATH}")

    import shutil
    shutil.copyfile(PDF_OUTPUT_PATH, PDF_COPY_OLD)
    shutil.copyfile(PDF_OUTPUT_PATH, PDF_ROOT_COPY)
    print("Copias del PDF actualizadas con éxito.")


if __name__ == "__main__":
    build_pdf()
