import streamlit as st
from PIL import Image

# =========================================================
#  Portafolio de Aplicaciones de IA — Miguel Ruiz
#  Paleta: azul petróleo / terracota / ámbar
# =========================================================
try:
    _icon = Image.open('logo_mr.png')
except Exception:
    _icon = "📄"
st.set_page_config(page_title="Portafolio IA · Miguel Ruiz", page_icon=_icon, layout="wide")

# ---- Estilo personalizado ----
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&family=Inter:wght@300;400;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #1b3a4b 0%, #14303d 100%);
        color: #e8eef0;
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stToolbar"] { right: 1rem; }
    h1, h2, h3 { font-family: 'Montserrat', sans-serif; color: #e07a5f; }
    section[data-testid="stSidebar"] { background: #12272f; }

    .firma {
        font-family: 'Montserrat', sans-serif;
        font-weight: 800;
        font-size: 3rem;
        color: #f2cc8f;
        text-align: center;
        margin-bottom: 0;
        letter-spacing: 1px;
    }
    .subtitulo {
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: #e8eef0;
        margin-top: 0;
    }
    .tarjeta {
        background: #1d3f4e;
        border: 1px solid rgba(242,204,143,0.15);
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 18px;
        box-shadow: 0 6px 22px rgba(0,0,0,0.25);
        transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
    }
    .tarjeta:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.33);
        border-color: rgba(224,122,95,0.5);
    }
    a { color: #e07a5f !important; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- Encabezado tipo portafolio ----
st.markdown('<p class="firma">MIGUEL RUIZ</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Portafolio de Aplicaciones de Inteligencia Artificial</p>', unsafe_allow_html=True)
st.divider()

with st.sidebar:
    st.markdown('<p class="firma" style="font-size:1.8rem;">Miguel Ruiz</p>', unsafe_allow_html=True)
    st.subheader("Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos. "
        "Aquí reúno mis versiones personalizadas de cada ejercicio."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("Mis ejercicios prácticos")
st.write(f"Material de referencia del curso: [Enlace]({url_ia})")

# =========================================================
#  LINKS — actualiza aquí la URL propia de cada app cuando
#  la despliegues en tu Streamlit Cloud.
#  (Mientras no tengas la tuya, queda la original del curso.)
# =========================================================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader("🔊 Conversión de texto a voz")
    st.image(Image.open('txt_to_audio2.png'), width=190)
    st.write("Convierte cualquier texto en audio con un clic.")
    url = "https://imultimod.streamlit.app/"   # TODO: reemplazar por tu URL (fork IMM1)
    st.write(f"Abrir app: [Enlace]({url})")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader("🔍 Reconocimiento de Objetos")
    st.image(Image.open('txt_to_audio.png'), width=200)
    st.write("Detecta objetos en imágenes con YOLO.")
    url = "https://yolov5cmc.streamlit.app/"   # TODO: reemplazar por tu URL
    st.write(f"Abrir app: [Enlace]({url})")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader("🤖 Entrenando Modelos")
    st.image(Image.open('OIG5.jpg'), width=200)
    st.write("Usa tu propio modelo entrenado.")
    url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"   # TODO: reemplazar por tu URL
    st.write(f"Abrir app: [Enlace]({url})")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader("🎤 Conversión de voz a texto")
    st.image(Image.open('OIG8.jpg'), width=200)
    st.write("Transcribe tu voz a texto fácilmente.")
    url = "https://traductorw.streamlit.app/"   # TODO: reemplazar por tu URL
    st.write(f"Abrir app: [Enlace]({url})")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader("📊 Análisis de Datos")
    st.image(Image.open('data_analisis.png'), width=190)
    st.write("Analiza datos usando agentes de IA.")
    url = "https://dataagente.streamlit.app/"   # TODO: reemplazar por tu URL
    st.write(f"Abrir app: [Enlace]({url})")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader("🎬 Transcriptor Audio y Video")
    st.image(Image.open('OIG3.jpg'), width=200)
    st.write("Realiza transcripciones de audio y video.")
    url = "https://transcript-whisper.streamlit.app/"   # TODO: reemplazar por tu URL
    st.write(f"Abrir app: [Enlace]({url})")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader("📄 Generación en Contexto (RAG)")
    st.image(Image.open('Chat_pdf.png'), width=190)
    st.write("Chatea con tus documentos PDF (RAG).")
    url = "https://chatpdf-cc.streamlit.app/"   # TODO: reemplazar por tu URL (fork chat_pdf)
    st.write(f"Abrir app: [Enlace]({url})")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader("🖼️ Análisis de Imagen")
    st.image(Image.open('OIG4.jpg'), width=200)
    st.write("Analiza imágenes con Vision GPT-4o.")
    url = "https://vision2-gpt4o.streamlit.app/"   # TODO: reemplazar por tu URL
    st.write(f"Abrir app: [Enlace]({url})")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader("🔌 Sistema Ciberfísico")
    st.image(Image.open('OIG6.jpg'), width=200)
    st.write("Interacción de la IA con el mundo físico.")
    url = "https://vision2-gpt4o.streamlit.app/"   # TODO: reemplazar por tu URL
    st.write(f"Abrir app: [Enlace]({url})")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.markdown(
    '<p style="text-align:center; font-family:\'Montserrat\', sans-serif; font-weight:600; '
    'font-size:1.1rem; color:#f2cc8f;">Desarrollado por Miguel Ruiz</p>',
    unsafe_allow_html=True,
)
