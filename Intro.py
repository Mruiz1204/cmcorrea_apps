"""
Portafolio editorial — Miguel Ruiz
Aplicaciones de IA hechas en clase con Streamlit.
Concepto: revista / editorial · jerarquía asimétrica.
"""

import os
import io
import base64
import streamlit as st
from PIL import Image, ImageOps


# ─────────────────────────────────────────────
# CONFIGURACIÓN
# ─────────────────────────────────────────────
try:
    _icon = Image.open('logo_mr.png')
except Exception:
    _icon = "▣"
st.set_page_config(page_title="Miguel Ruiz — Portafolio", page_icon=_icon, layout="wide")


def html(codigo):
    if hasattr(st, "html"):
        st.html(codigo)
    else:
        st.markdown(codigo, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOTO (marco rectangular editorial, no círculo)
# ─────────────────────────────────────────────
FOTO = "FotoPerfil.jpeg"


@st.cache_data
def foto_base64(ruta):
    if not os.path.exists(ruta):
        return None
    try:
        img = Image.open(ruta)
        img = ImageOps.exif_transpose(img).convert("RGB")
        img = ImageOps.fit(img, (640, 800), Image.Resampling.LANCZOS)  # proporción editorial 4:5
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=90)
        return base64.b64encode(buf.getvalue()).decode()
    except Exception:
        return None


foto = foto_base64(FOTO)


# ─────────────────────────────────────────────
# PROYECTOS
# ─────────────────────────────────────────────
proyectos = [
    {"n": "Análisis de Imagen", "cat": "Visión", "txt": "Interpreta una fotografía con GPT-4o y la describe con lenguaje natural.", "link": "https://vision2-0909.streamlit.app/"},
    {"n": "Reconocimiento de Objetos", "cat": "Visión", "txt": "Detección de objetos en imágenes mediante el modelo YOLOv5.", "link": "https://yolov5-909090.streamlit.app/"},
    {"n": "Reconocimiento de Caracteres", "cat": "Visión", "txt": "Extrae el texto contenido en una fotografía (OCR) para copiarlo.", "link": "https://ixw43qkktp7a2ecnrxjm4v.streamlit.app/"},
    {"n": "Chat con PDF", "cat": "Texto", "txt": "Formula preguntas sobre un documento PDF mediante recuperación aumentada (RAG).", "link": "https://chatpdf909.streamlit.app/"},
    {"n": "Word Cloud", "cat": "Texto", "txt": "Visualiza la frecuencia léxica de un texto como una nube de palabras.", "link": "https://wordcloud-0909.streamlit.app/"},
    {"n": "Análisis de Sentimientos", "cat": "Texto", "txt": "Clasifica la polaridad de un texto: positivo, negativo o neutral.", "link": "https://sentimenta-9a0909.streamlit.app/"},
    {"n": "Texto a Audio", "cat": "Voz", "txt": "Convierte cualquier texto escrito en voz sintetizada.", "link": "https://textoaaudio90909090.streamlit.app/"},
    {"n": "Traductor de Voz", "cat": "Voz", "txt": "Captura la voz, la traduce a otro idioma y la reproduce en audio.", "link": "https://traductor-09090.streamlit.app/"},
    {"n": "OCR con Audio", "cat": "Voz", "txt": "Lee el texto de una imagen, lo traduce y lo narra en voz alta.", "link": "https://ocr-audio-dobai8kn64czzbuavjqojz.streamlit.app/"},
    {"n": "Análisis de Datos", "cat": "Datos", "txt": "Carga un CSV o Excel y consulta tus datos con un asistente de IA.", "link": "https://dataagent-0809.streamlit.app/"},
    {"n": "Mi Primera App", "cat": "Inicio", "txt": "El punto de partida de este recorrido por Streamlit.", "link": "https://ejfbdohiqmyjutvlcdpnlv.streamlit.app/"},
    {"n": "Entrenando Modelos", "cat": "Visión", "txt": "Clasificación de imágenes con un modelo entrenado en Teachable Machine.", "link": ""},
    {"n": "Transcriptor de Audio y Video", "cat": "Voz", "txt": "Transcribe automáticamente el contenido de archivos de audio y video.", "link": ""},
    {"n": "TF-IDF", "cat": "Texto", "txt": "Identifica los términos más relevantes dentro de un conjunto de textos.", "link": ""},
    {"n": "Predicción de Números", "cat": "Visión", "txt": "Reconoce dígitos manuscritos con un modelo entrenado sobre MNIST.", "link": ""},
    {"n": "Aplicación Multipágina", "cat": "Inicio", "txt": "Navegación entre múltiples páginas con menú lateral.", "link": ""},
]


# ─────────────────────────────────────────────
# ESTILO EDITORIAL
# ─────────────────────────────────────────────
html("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,500&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    :root {
        --bg:     #11272f;
        --panel:  #16323c;
        --line:   rgba(242,204,143,0.18);
        --terra:  #e3785c;
        --ambar:  #f2cc8f;
        --ink:    #eef3f4;
        --mute:   #90a9b2;
    }

    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stToolbar"] { right: 1rem; }
    [data-testid="stSidebar"] { display: none; }
    .block-container { padding-top: 2.2rem !important; max-width: 1180px; }

    .stApp {
        background: var(--bg);
        color: var(--ink);
        font-family: 'Space Grotesk', sans-serif;
    }

    /* ───── Barra superior tipo cabecera de revista ───── */
    .masthead {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-top: 2px solid var(--terra);
        border-bottom: 1px solid var(--line);
        padding: 14px 2px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: var(--mute);
    }
    .masthead .mid { color: var(--ambar); }

    /* ───── HERO asimétrico ───── */
    .hero {
        display: grid;
        grid-template-columns: 1.5fr 1fr;
        gap: 40px;
        align-items: end;
        padding: 46px 0 34px;
        border-bottom: 1px solid var(--line);
    }
    .hero .edicion {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: var(--terra);
        margin-bottom: 10px;
    }
    .hero h1 {
        font-family: 'Fraunces', serif;
        font-weight: 600;
        font-size: clamp(3rem, 7vw, 6.4rem);
        line-height: 0.92;
        color: var(--ink);
        margin: 0;
    }
    .hero h1 em {
        font-style: italic;
        color: var(--terra);
    }
    .hero .lede {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.02rem;
        line-height: 1.65;
        color: var(--mute);
        max-width: 440px;
        margin-top: 20px;
    }
    .hero .retrato {
        justify-self: end;
    }
    .hero .retrato img {
        width: 100%;
        max-width: 280px;
        aspect-ratio: 4/5;
        object-fit: cover;
        border-radius: 4px;
        filter: grayscale(18%) contrast(1.05);
        border: 1px solid var(--line);
        box-shadow: -18px 18px 0 rgba(227,120,92,0.18);
    }
    .hero .retrato .pie {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: var(--mute);
        margin-top: 10px;
        text-align: right;
    }

    /* ───── Encabezado de sección ───── */
    .sec {
        display: flex;
        align-items: baseline;
        gap: 18px;
        margin: 54px 0 8px;
        border-bottom: 1px solid var(--line);
        padding-bottom: 8px;
    }
    .sec .rom {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        color: var(--terra);
        letter-spacing: 1px;
    }
    .sec h2 {
        font-family: 'Fraunces', serif;
        font-style: italic;
        font-weight: 500;
        font-size: 2rem;
        color: var(--ambar);
        margin: 0;
    }
    .sec .cuenta {
        margin-left: auto;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        color: var(--mute);
        letter-spacing: 1px;
    }

    /* ───── Entrada de proyecto: fila editorial ───── */
    .obra {
        display: grid;
        grid-template-columns: 70px 1fr auto;
        gap: 22px;
        align-items: center;
        padding: 22px 6px;
        border-bottom: 1px solid var(--line);
        transition: background 0.25s ease, padding-left 0.25s ease;
    }
    .obra:hover {
        background: var(--panel);
        padding-left: 18px;
    }
    .obra .idx {
        font-family: 'Fraunces', serif;
        font-size: 2.4rem;
        font-weight: 600;
        color: var(--terra);
        line-height: 1;
        opacity: 0.85;
    }
    .obra .cuerpo .nom {
        font-family: 'Fraunces', serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--ink);
        line-height: 1.1;
    }
    .obra .cuerpo .dsc {
        font-size: 0.92rem;
        color: var(--mute);
        line-height: 1.55;
        margin-top: 5px;
        max-width: 620px;
    }
    .obra .cuerpo .tag {
        display: inline-block;
        margin-top: 9px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.64rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: var(--ambar);
        border: 1px solid var(--line);
        border-radius: 2px;
        padding: 2px 8px;
    }

    /* ───── Botones de link (lado derecho de cada obra) ───── */
    [data-testid="stLinkButton"] a, .stLinkButton a {
        background: transparent !important;
        color: var(--terra) !important;
        border: 1px solid var(--terra) !important;
        border-radius: 2px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.74rem !important;
        letter-spacing: 1px !important;
        text-transform: uppercase;
        padding: 8px 18px !important;
        transition: all 0.2s ease !important;
    }
    [data-testid="stLinkButton"] a:hover, .stLinkButton a:hover {
        background: var(--terra) !important;
        color: var(--bg) !important;
    }
    .stButton > button {
        background: transparent !important;
        color: var(--mute) !important;
        border: 1px dashed var(--line) !important;
        border-radius: 2px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.74rem !important;
        letter-spacing: 1px !important;
        text-transform: uppercase;
    }

    .colofon {
        margin-top: 64px;
        padding: 26px 0;
        border-top: 2px solid var(--terra);
        display: flex;
        justify-content: space-between;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: var(--mute);
    }

    @media (max-width: 820px) {
        .hero { grid-template-columns: 1fr; }
        .hero .retrato { justify-self: start; margin-top: 24px; }
        .obra { grid-template-columns: 48px 1fr; }
        .obra .acc { grid-column: 2; }
    }
</style>
""")


# ─────────────────────────────────────────────
# MASTHEAD + HERO
# ─────────────────────────────────────────────
total = len(proyectos)
online = sum(1 for p in proyectos if p["link"])

retrato = (f'<img src="data:image/jpeg;base64,{foto}">' if foto
           else '<div style="width:100%;max-width:280px;aspect-ratio:4/5;background:#16323c;'
                'border:1px solid var(--line);display:flex;align-items:center;justify-content:center;'
                'font-family:Space Grotesk;font-weight:700;color:#f2cc8f;font-size:3rem;border-radius:4px;">MR</div>')

html(f"""
<div class="masthead">
    <span>Miguel Ruiz</span>
    <span class="mid">Inteligencia Artificial · Streamlit</span>
    <span>Nº 01 / {total:02d}</span>
</div>

<div class="hero">
    <div>
        <div class="edicion">Portafolio — Edición de clase</div>
        <h1>Aplicaciones<br>de <em>IA</em>.</h1>
        <div class="lede">
            Una recopilación de los proyectos que construí en clase con Python y Streamlit:
            visión por computadora, procesamiento de texto, voz y análisis de datos.
            {online} de {total} proyectos están en línea; el resto, en producción.
        </div>
    </div>
    <div class="retrato">
        {retrato}
        <div class="pie">Miguel Ruiz — Autor</div>
    </div>
</div>
""")


# ─────────────────────────────────────────────
# PROYECTOS AGRUPADOS POR SECCIÓN
# ─────────────────────────────────────────────
ORDEN = ["Inicio", "Visión", "Texto", "Voz", "Datos"]
ROMANOS = {"Inicio": "I", "Visión": "II", "Texto": "III", "Voz": "IV", "Datos": "V"}

contador = 0
for cat in ORDEN:
    delcat = [p for p in proyectos if p["cat"] == cat]
    if not delcat:
        continue

    html(f"""
    <div class="sec">
        <span class="rom">{ROMANOS.get(cat, '·')}</span>
        <h2>{cat}</h2>
        <span class="cuenta">{len(delcat):02d} proyecto(s)</span>
    </div>
    """)

    for p in delcat:
        contador += 1
        c_txt, c_acc = st.columns([0.80, 0.20], gap="small")
        with c_txt:
            html(f"""
            <div class="obra" style="border:none; padding-bottom:0;">
                <div class="idx">{contador:02d}</div>
                <div class="cuerpo">
                    <div class="nom">{p['n']}</div>
                    <div class="dsc">{p['txt']}</div>
                    <span class="tag">{p['cat']}</span>
                </div>
            </div>
            """)
        with c_acc:
            st.write("")
            if p["link"]:
                st.link_button("Ver ↗", p["link"], use_container_width=True)
            else:
                st.button("En proceso", key=f"p{contador}", disabled=True, use_container_width=True)
        html('<div style="border-bottom:1px solid var(--line);"></div>')


# ─────────────────────────────────────────────
# COLOFÓN
# ─────────────────────────────────────────────
html(f"""
<div class="colofon">
    <span>© Miguel Ruiz</span>
    <span>{total:02d} proyectos · Python + Streamlit</span>
    <span>Fin de la edición</span>
</div>
""")
