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
    {"n": "Análisis de Imagen", "cat": "Visión", "ic": "🖼", "txt": "Interpreta una fotografía con GPT-4o y la describe con lenguaje natural.", "link": "https://vision2-0909.streamlit.app/"},
    {"n": "Reconocimiento de Objetos", "cat": "Visión", "ic": "🎯", "txt": "Detección de objetos en imágenes mediante el modelo YOLOv5.", "link": "https://yolov5-909090.streamlit.app/"},
    {"n": "Reconocimiento de Caracteres", "cat": "Visión", "ic": "🔤", "txt": "Extrae el texto contenido en una fotografía (OCR) para copiarlo.", "link": "https://ixw43qkktp7a2ecnrxjm4v.streamlit.app/"},
    {"n": "Chat con PDF", "cat": "Texto", "ic": "📄", "txt": "Formula preguntas sobre un documento PDF mediante recuperación aumentada (RAG).", "link": "https://chatpdf909.streamlit.app/"},
    {"n": "Word Cloud", "cat": "Texto", "ic": "☁", "txt": "Visualiza la frecuencia léxica de un texto como una nube de palabras.", "link": "https://wordcloud-0909.streamlit.app/"},
    {"n": "Análisis de Sentimientos", "cat": "Texto", "ic": "💬", "txt": "Clasifica la polaridad de un texto: positivo, negativo o neutral.", "link": "https://sentimenta-9a0909.streamlit.app/"},
    {"n": "Texto a Audio", "cat": "Voz", "ic": "🔊", "txt": "Convierte cualquier texto escrito en voz sintetizada.", "link": "https://textoaaudio90909090.streamlit.app/"},
    {"n": "Traductor de Voz", "cat": "Voz", "ic": "🌐", "txt": "Captura la voz, la traduce a otro idioma y la reproduce en audio.", "link": "https://traductor-09090.streamlit.app/"},
    {"n": "OCR con Audio", "cat": "Voz", "ic": "🎧", "txt": "Lee el texto de una imagen, lo traduce y lo narra en voz alta.", "link": "https://ocr-audio-dobai8kn64czzbuavjqojz.streamlit.app/"},
    {"n": "Análisis de Datos", "cat": "Datos", "ic": "📊", "txt": "Carga un CSV o Excel y consulta tus datos con un asistente de IA.", "link": "https://dataagent-0809.streamlit.app/"},
    {"n": "Mi Primera App", "cat": "Inicio", "ic": "🚀", "txt": "El punto de partida de este recorrido por Streamlit.", "link": "https://ejfbdohiqmyjutvlcdpnlv.streamlit.app/"},
    {"n": "Entrenando Modelos", "cat": "Visión", "ic": "🧠", "txt": "Clasificación de imágenes con un modelo entrenado en Teachable Machine.", "link": ""},
    {"n": "Transcriptor de Audio y Video", "cat": "Voz", "ic": "🎬", "txt": "Transcribe automáticamente el contenido de archivos de audio y video.", "link": ""},
    {"n": "TF-IDF", "cat": "Texto", "ic": "📚", "txt": "Identifica los términos más relevantes dentro de un conjunto de textos.", "link": ""},
    {"n": "Predicción de Números", "cat": "Visión", "ic": "🔢", "txt": "Reconoce dígitos manuscritos con un modelo entrenado sobre MNIST.", "link": ""},
    {"n": "Aplicación Multipágina", "cat": "Inicio", "ic": "🗂", "txt": "Navegación entre múltiples páginas con menú lateral.", "link": ""},
]

# Color de acento por categoría (dentro de la familia de la marca)
COLOR_CAT = {
    "Inicio": "#f2cc8f",   # ámbar
    "Visión": "#e3785c",   # terracota
    "Texto":  "#7bb0a8",   # verde agua apagado
    "Voz":    "#c58fb0",   # malva apagado
    "Datos":  "#8fb3d9",   # azul claro
}


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

    /* ───── Tarjeta de proyecto (box) ───── */
    .obra {
        display: grid;
        grid-template-columns: 96px 1fr;
        gap: 18px;
        align-items: stretch;
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 14px;
        overflow: hidden;
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        height: 100%;
    }
    .obra:hover {
        transform: translateY(-5px);
        box-shadow: 0 16px 34px rgba(0,0,0,0.4);
        border-color: var(--cat);
    }
    /* Miniatura de color con el ícono (la identidad visual de cada app) */
    .obra .mini {
        background:
            radial-gradient(circle at 30% 25%, rgba(255,255,255,0.14), transparent 60%),
            var(--cat);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.3rem;
        position: relative;
    }
    .obra .mini .numero {
        position: absolute;
        top: 6px; left: 8px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.62rem;
        color: rgba(17,39,47,0.75);
        font-weight: 600;
    }
    .obra .cuerpo {
        padding: 16px 16px 14px 2px;
        display: flex;
        flex-direction: column;
    }
    .obra .cuerpo .tag {
        align-self: flex-start;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.6rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: var(--cat);
        border: 1px solid var(--cat);
        border-radius: 999px;
        padding: 2px 10px;
        margin-bottom: 8px;
    }
    .obra .cuerpo .nom {
        font-family: 'Fraunces', serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--ink);
        line-height: 1.12;
    }
    .obra .cuerpo .dsc {
        font-size: 0.85rem;
        color: var(--mute);
        line-height: 1.5;
        margin-top: 6px;
    }

    /* ───── Botones ───── */
    [data-testid="stLinkButton"] a, .stLinkButton a {
        background: transparent !important;
        color: var(--terra) !important;
        border: 1px solid var(--terra) !important;
        border-radius: 999px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.72rem !important;
        letter-spacing: 1px !important;
        text-transform: uppercase;
        padding: 7px 16px !important;
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
        border-radius: 999px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.72rem !important;
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
# FILTRO POR CATEGORÍA
# ─────────────────────────────────────────────
html("""
<div class="sec">
    <span class="rom">—</span>
    <h2>Proyectos</h2>
    <span class="cuenta">filtra por categoría</span>
</div>
""")

CATS = ["Todas", "Inicio", "Visión", "Texto", "Voz", "Datos"]
filtro = st.radio("Filtrar", CATS, horizontal=True, label_visibility="collapsed")

visibles = [(i, p) for i, p in enumerate(proyectos, start=1)
            if filtro == "Todas" or p["cat"] == filtro]

st.write("")


# ─────────────────────────────────────────────
# TARJETAS (2 por fila, cada una con su miniatura de color)
# ─────────────────────────────────────────────
POR_FILA = 2
for inicio in range(0, len(visibles), POR_FILA):
    cols = st.columns(POR_FILA, gap="medium")
    for col, (num, p) in zip(cols, visibles[inicio:inicio + POR_FILA]):
        color = COLOR_CAT.get(p["cat"], "#e3785c")
        with col:
            html(f"""
            <div class="obra" style="--cat:{color};">
                <div class="mini">
                    <span class="numero">{num:02d}</span>
                    {p['ic']}
                </div>
                <div class="cuerpo">
                    <span class="tag">{p['cat']}</span>
                    <div class="nom">{p['n']}</div>
                    <div class="dsc">{p['txt']}</div>
                </div>
            </div>
            """)
            if p["link"]:
                st.link_button("Abrir proyecto ↗", p["link"], use_container_width=True)
            else:
                st.button("En proceso", key=f"p{num}", disabled=True, use_container_width=True)
            st.write("")


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
