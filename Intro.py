"""
Portafolio de Aplicaciones de IA — Miguel Ruiz
Bitácora con las apps de Streamlit hechas en clase.
Paleta: azul petróleo + terracota + ámbar.
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
    _icon = "📊"
st.set_page_config(
    page_title="Portafolio · Miguel Ruiz",
    page_icon=_icon,
    layout="wide",
)


def html(codigo):
    """Muestra HTML/CSS. Usa st.html (Streamlit nuevo) y si no existe, st.markdown."""
    if hasattr(st, "html"):
        st.html(codigo)
    else:
        st.markdown(codigo, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOTO DE PERFIL (en el repo con este nombre)
# La app la endereza, la recorta en cuadrado y la pone en círculo.
# ─────────────────────────────────────────────
FOTO = "FotoPerfil.jpeg"


@st.cache_data
def foto_base64(ruta):
    if not os.path.exists(ruta):
        return None
    try:
        img = Image.open(ruta)
        img = ImageOps.exif_transpose(img).convert("RGB")
        img = ImageOps.fit(img, (600, 600), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=88)
        return base64.b64encode(buf.getvalue()).decode()
    except Exception:
        return None


foto = foto_base64(FOTO)


def foto_html(tam, borde=4):
    """Círculo con la foto (o el logo MR si la foto no carga)."""
    if foto:
        return (f'<img src="data:image/jpeg;base64,{foto}" '
                f'style="width:{tam}px; height:{tam}px; border-radius:50%; object-fit:cover; '
                f'border:{borde}px solid #1d3f4e; box-shadow:0 0 0 2px #e07a5f, '
                f'0 12px 30px rgba(0,0,0,0.35); display:block; margin:0 auto;">')
    return (f'<div style="width:{tam}px; height:{tam}px; margin:0 auto; border-radius:50%; '
            f'background:linear-gradient(135deg,#1d3f4e,#24485a); border:2px solid #e07a5f; '
            f'display:flex; align-items:center; justify-content:center; '
            f'font-family:Montserrat,sans-serif; font-weight:800; color:#f2cc8f; '
            f'font-size:{tam // 3}px;">MR</div>')


# ─────────────────────────────────────────────
# MIS PROYECTOS  (edita aquí nombres, textos o links)
# ─────────────────────────────────────────────
proyectos = [
    {
        "nombre": "Mi Primera App",
        "emoji": "🚀",
        "categoria": "Inicio",
        "descripcion": "El punto de partida de todo este camino: mi primera aplicación en Streamlit.",
        "link": "https://ejfbdohiqmyjutvlcdpnlv.streamlit.app/",
    },
    {
        "nombre": "Texto a Audio",
        "emoji": "🔊",
        "categoria": "Voz",
        "descripcion": "Escribe cualquier texto y escúchalo convertido en voz con un solo clic.",
        "link": "https://textoaaudio90909090.streamlit.app/",
    },
    {
        "nombre": "Reconocimiento de Objetos (YOLO)",
        "emoji": "🔍",
        "categoria": "Visión",
        "descripcion": "Detecta y señala los objetos que aparecen en una foto usando YOLOv5.",
        "link": "https://yolov5-909090.streamlit.app/",
    },
    {
        "nombre": "Traductor de Voz",
        "emoji": "🌍",
        "categoria": "Voz",
        "descripcion": "Habla o escribe y traduce tus palabras a otro idioma en segundos.",
        "link": "https://traductor-09090.streamlit.app/",
    },
    {
        "nombre": "Análisis de Datos",
        "emoji": "📊",
        "categoria": "Datos",
        "descripcion": "Carga un CSV o Excel y hazle preguntas sobre tus datos usando IA.",
        "link": "https://dataagent-0809.streamlit.app/",
    },
    {
        "nombre": "Chat con PDF",
        "emoji": "📄",
        "categoria": "Texto",
        "descripcion": "Sube un PDF y hazle preguntas sobre su contenido (RAG).",
        "link": "https://chatpdf909.streamlit.app/",
    },
    {
        "nombre": "Análisis de Imagen",
        "emoji": "🖼️",
        "categoria": "Visión",
        "descripcion": "Analiza una imagen con GPT-4o y describe lo que hay en ella.",
        "link": "https://vision2-0909.streamlit.app/",
    },
    {
        "nombre": "OCR + Audio",
        "emoji": "🎧",
        "categoria": "Voz",
        "descripcion": "Lee el texto de una imagen, lo traduce y además te lo dice en voz alta.",
        "link": "https://ocr-audio-dobai8kn64czzbuavjqojz.streamlit.app/",
    },
    {
        "nombre": "Reconocimiento de Caracteres (OCR)",
        "emoji": "🔤",
        "categoria": "Visión",
        "descripcion": "Toma una foto y extrae el texto que aparece en ella para copiarlo.",
        "link": "https://ixw43qkktp7a2ecnrxjm4v.streamlit.app/",
    },
    {
        "nombre": "Word Cloud",
        "emoji": "☁️",
        "categoria": "Texto",
        "descripcion": "Convierte un texto en una nube donde las palabras más repetidas brillan más.",
        "link": "https://wordcloud-0909.streamlit.app/",
    },
    {
        "nombre": "Análisis de Sentimientos",
        "emoji": "💬",
        "categoria": "Texto",
        "descripcion": "Descubre si un texto transmite un sentimiento positivo, negativo o neutral.",
        "link": "https://sentimenta-9a0909.streamlit.app/",
    },
    # ── PENDIENTES: pega tu link de Streamlit cuando despliegues cada una ──
    {
        "nombre": "Entrenando Modelos (Teachable Machine)",
        "emoji": "🤖",
        "categoria": "Visión",
        "descripcion": "Reconoce imágenes con un modelo entrenado en Teachable Machine.",
        "link": "",
    },
    {
        "nombre": "Transcriptor Audio y Video",
        "emoji": "🎬",
        "categoria": "Voz",
        "descripcion": "Realiza transcripciones automáticas de archivos de audio y video.",
        "link": "",
    },
    {
        "nombre": "TF-IDF",
        "emoji": "📚",
        "categoria": "Texto",
        "descripcion": "Encuentra las palabras más importantes dentro de un grupo de textos.",
        "link": "",
    },
    {
        "nombre": "Predicción de Números (MNIST)",
        "emoji": "🔢",
        "categoria": "Visión",
        "descripcion": "Escribe un número a mano y un modelo entrenado con MNIST lo adivina.",
        "link": "",
    },
    {
        "nombre": "App Multipágina",
        "emoji": "🗂️",
        "categoria": "Inicio",
        "descripcion": "Una app con varias páginas y menú lateral para navegar entre ellas.",
        "link": "",
    },
]

CATEGORIAS = {
    "Todas":  "✨",
    "Inicio": "🚀",
    "Texto":  "📝",
    "Voz":    "🎙️",
    "Visión": "👁️",
    "Datos":  "📊",
}


# ─────────────────────────────────────────────
# ESTILOS · azul petróleo, terracota y ámbar
# ─────────────────────────────────────────────
html("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

    :root {
        --fondo:    #14303d;
        --sup:      #1d3f4e;
        --sup2:     #24485a;
        --terra:    #e07a5f;
        --terra2:   #c9583c;
        --ambar:    #f2cc8f;
        --texto:    #e8eef0;
        --texto2:   #a9c0ca;
        --borde:    rgba(242,204,143,0.15);
    }

    .stApp, .stApp p, .stApp label, .stApp input, .stApp button, .stApp li {
        font-family: 'Inter', sans-serif;
    }
    .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
        font-family: 'Montserrat', sans-serif !important;
        color: var(--terra) !important;
        font-weight: 700 !important;
    }
    .stApp {
        background:
            radial-gradient(circle at 0% 0%, #1b3a4b 0%, transparent 40%),
            radial-gradient(circle at 100% 20%, #1a3947 0%, transparent 42%),
            #14303d;
    }
    p, li, label { color: var(--texto2); }

    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stToolbar"] { right: 1rem; }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #12272f !important;
        border-right: 1px solid var(--borde);
    }
    [data-testid="stSidebar"] * { color: var(--texto) !important; }
    [data-testid="stSidebar"] h3 {
        font-family: 'Montserrat', sans-serif !important;
        font-size: 0.72rem !important;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        color: var(--ambar) !important;
    }

    /* Tarjetas (st.container con borde) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid var(--borde) !important;
        border-radius: 20px !important;
        background: var(--sup);
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 36px rgba(0,0,0,0.38);
        border-color: rgba(224,122,95,0.55) !important;
    }

    /* Botones de link */
    [data-testid="stLinkButton"] a, .stLinkButton a {
        background: linear-gradient(135deg, #e07a5f, #c9583c) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 999px !important;
        font-weight: 600 !important;
        letter-spacing: 0.4px;
        transition: all 0.25s ease !important;
    }
    [data-testid="stLinkButton"] a:hover, .stLinkButton a:hover {
        background: linear-gradient(135deg, #f2cc8f, #e07a5f) !important;
        color: #14303d !important;
        transform: scale(1.02);
    }

    /* Filtro de categorías */
    [data-testid="stRadio"] [role="radiogroup"] {
        gap: 10px;
        justify-content: center;
        flex-wrap: wrap;
    }
    [data-testid="stRadio"] [role="radiogroup"] label {
        background: var(--sup);
        border: 1px solid var(--borde);
        border-radius: 999px;
        padding: 6px 16px;
        transition: all 0.2s;
    }
    [data-testid="stRadio"] [role="radiogroup"] label:hover {
        background: var(--sup2);
        border-color: var(--terra);
    }

    /* Portada */
    .portada {
        background: linear-gradient(135deg, #1d3f4e 0%, #1a3947 55%, #163340 100%);
        border: 1px solid var(--borde);
        border-radius: 32px;
        padding: 52px 40px 44px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 18px 48px rgba(0,0,0,0.33);
        font-family: 'Inter', sans-serif;
    }
    .portada::before, .portada::after {
        content: "";
        position: absolute;
        border-radius: 50%;
        filter: blur(2px);
    }
    .portada::before {
        width: 260px; height: 260px;
        background: rgba(224,122,95,0.22);
        top: -90px; left: -70px;
    }
    .portada::after {
        width: 220px; height: 220px;
        background: rgba(242,204,143,0.15);
        bottom: -90px; right: -50px;
    }
    .portada .marco {
        position: relative;
        z-index: 2;
        width: fit-content;
        margin: 0 auto 18px;
        animation: aparecer 0.8s ease;
    }
    @keyframes aparecer {
        from { opacity: 0; transform: scale(0.9); }
        to   { opacity: 1; transform: scale(1); }
    }
    .portada .sobre {
        position: relative;
        font-size: 0.72rem;
        letter-spacing: 5px;
        text-transform: uppercase;
        color: var(--texto2);
    }
    .portada .firma {
        position: relative;
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 3.4rem;
        line-height: 1.05;
        color: var(--ambar);
        margin: 12px 0 0;
        letter-spacing: 1px;
    }
    .portada .firma span { color: var(--terra); }
    .portada .titulo {
        position: relative;
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: var(--texto2);
        margin-top: 6px;
    }
    .portada .linea {
        position: relative;
        width: 90px;
        height: 2px;
        margin: 18px auto;
        background: linear-gradient(90deg, transparent, var(--terra), transparent);
    }
    .portada p {
        position: relative;
        color: var(--texto);
        max-width: 580px;
        margin: 0 auto;
        font-size: 0.98rem;
        line-height: 1.7;
    }
    .deco {
        position: absolute;
        font-size: 1.4rem;
        opacity: 0.7;
        animation: flotar 5s ease-in-out infinite;
        z-index: 1;
    }
    @keyframes flotar {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50%      { transform: translateY(-10px) rotate(8deg); }
    }

    /* Mini stats */
    .stats {
        display: flex;
        gap: 14px;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 22px;
    }
    .stat {
        background: var(--sup);
        border: 1px solid var(--borde);
        border-radius: 18px;
        padding: 14px 26px;
        text-align: center;
        min-width: 130px;
    }
    .stat b {
        display: block;
        font-family: 'Montserrat', sans-serif;
        font-size: 2rem;
        color: var(--terra);
        line-height: 1;
    }
    .stat span {
        font-size: 0.72rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: var(--texto2);
    }

    /* Título de sección */
    .seccion {
        text-align: center;
        margin: 36px 0 6px;
    }
    .seccion .mini {
        font-size: 0.7rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: var(--ambar);
    }
    .seccion h2 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        font-size: 2rem;
        color: var(--terra);
        margin: 4px 0 0;
    }

    /* Contenido de cada tarjeta */
    .card { font-family: 'Inter', sans-serif; padding: 4px 4px 0; }
    .card .arriba {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .card .num {
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        font-size: 0.95rem;
        color: var(--texto2);
    }
    .card .chip {
        background: var(--sup2);
        color: var(--ambar);
        border-radius: 999px;
        padding: 3px 12px;
        font-size: 0.7rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-weight: 600;
        border: 1px solid var(--borde);
    }
    .card .icono {
        width: 64px; height: 64px;
        margin: 16px 0 12px;
        border-radius: 50%;
        background: linear-gradient(135deg, #24485a, #1d3f4e);
        border: 1px solid var(--borde);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.9rem;
    }
    .card .nombre {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.15rem;
        font-weight: 700;
        color: var(--texto);
        line-height: 1.2;
        min-height: 2.9rem;
    }
    .card .desc {
        color: var(--texto2);
        font-size: 0.88rem;
        line-height: 1.55;
        margin-top: 8px;
        min-height: 62px;
    }

    .footer {
        text-align: center;
        margin-top: 42px;
    }
    .footer .firma {
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        font-size: 1.4rem;
        color: var(--terra);
    }
    .footer p {
        font-size: 0.76rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: var(--texto2);
        margin: 0;
    }
</style>
""")


# ─────────────────────────────────────────────
# PANEL LATERAL
# ─────────────────────────────────────────────
with st.sidebar:
    html(f"""
    <div style="text-align:center; padding-top:10px;">
        {foto_html(110, 3)}
        <div style="font-family:'Montserrat',sans-serif; font-weight:800; font-size:1.5rem; color:#f2cc8f; margin-top:12px;">
            Miguel Ruiz
        </div>
        <div style="font-size:0.72rem; letter-spacing:3px; text-transform:uppercase; color:#a9c0ca;">
            Portafolio de clase
        </div>
    </div>
    """)
    st.divider()

    st.markdown("### Sobre este portafolio")
    st.caption(
        "Aquí reúno las aplicaciones de Inteligencia Artificial que desarrollé "
        "en clase con Python y Streamlit, una por una."
    )

    st.divider()
    st.markdown("### Índice")
    for i, p in enumerate(proyectos, start=1):
        if p["link"]:
            st.markdown(f"{p['emoji']} [{i:02d} · {p['nombre']}]({p['link']})")
        else:
            st.markdown(f"{p['emoji']} {i:02d} · {p['nombre']} *(pronto)*")


# ─────────────────────────────────────────────
# PORTADA
# ─────────────────────────────────────────────
total = len(proyectos)
listas = sum(1 for p in proyectos if p["link"])
n_vision = sum(p["categoria"] == "Visión" for p in proyectos)
n_texto = sum(p["categoria"] == "Texto" for p in proyectos)

html(f"""
<div class="portada">
    <span class="deco" style="top:26px; left:40px;">🤖</span>
    <span class="deco" style="top:44px; right:56px; animation-delay:1.3s;">⚡</span>
    <span class="deco" style="bottom:30px; left:14%; animation-delay:2.1s;">📊</span>
    <span class="deco" style="bottom:34px; right:16%; animation-delay:1.7s;">✨</span>

    <div class="marco">{foto_html(170, 5)}</div>
    <div class="sobre">Portafolio de clase</div>
    <div class="firma">Miguel <span>Ruiz</span></div>
    <div class="titulo">Aplicaciones de Inteligencia Artificial</div>
    <div class="linea"></div>
    <p>Una colección de las aplicaciones que construí en clase con Python y Streamlit.
       Cada tarjeta es un proyecto: ábrelo y pruébalo.</p>
</div>

<div class="stats">
    <div class="stat"><b>{total}</b><span>Proyectos</span></div>
    <div class="stat"><b>{listas}</b><span>En línea</span></div>
    <div class="stat"><b>{n_vision}</b><span>Visión</span></div>
    <div class="stat"><b>{n_texto}</b><span>Texto</span></div>
</div>

<div class="seccion">
    <div class="mini">mis creaciones</div>
    <h2>Proyectos del curso</h2>
</div>
""")


# ─────────────────────────────────────────────
# FILTRO
# ─────────────────────────────────────────────
filtro = st.radio(
    "Filtrar",
    list(CATEGORIAS.keys()),
    format_func=lambda c: f"{CATEGORIAS[c]} {c}",
    horizontal=True,
    label_visibility="collapsed",
)

visibles = [(i, p) for i, p in enumerate(proyectos, start=1)
            if filtro == "Todas" or p["categoria"] == filtro]

st.write("")


# ─────────────────────────────────────────────
# TARJETAS (3 por fila)
# ─────────────────────────────────────────────
POR_FILA = 3
for inicio in range(0, len(visibles), POR_FILA):
    cols = st.columns(POR_FILA, gap="medium")
    for col, (num, p) in zip(cols, visibles[inicio:inicio + POR_FILA]):
        with col:
            with st.container(border=True):
                html(f"""
                <div class="card">
                    <div class="arriba">
                        <span class="num">N.º {num:02d}</span>
                        <span class="chip">{p['categoria']}</span>
                    </div>
                    <div class="icono">{p['emoji']}</div>
                    <div class="nombre">{p['nombre']}</div>
                    <div class="desc">{p['descripcion']}</div>
                </div>
                """)
                if p["link"]:
                    st.link_button("Abrir proyecto ↗", p["link"], use_container_width=True)
                else:
                    st.button("🔗 Próximamente", key=f"pend_{num}",
                              disabled=True, use_container_width=True)


# ─────────────────────────────────────────────
# PIE
# ─────────────────────────────────────────────
html("""
<div class="footer">
    <div class="firma">Miguel Ruiz</div>
    <p>hecho con python y streamlit</p>
</div>
""")
