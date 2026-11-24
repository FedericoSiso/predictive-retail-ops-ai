import streamlit as st
import pandas as pd
import joblib

# Configuración visual de la página
st.set_page_config(page_title="Pronóstico de Ventas", layout="centered")

# Estilos CSS personalizados para un diseño minimalista y de alto contraste
st.markdown("""
    <style>
    /* Fondo principal gris oscuro */
    .stApp {
        background-color: #121212;
        color: #F8F9FA;
    }
    
    /* Títulos y textos principales en blanco puro / dorado */
    h1, h2, h3, h4, h5, h6, p, label {
        color: #F8F9FA !important;
        font-family: 'Inter', sans-serif;
    }
    
    h1 {
        color: #D4AF37 !important; /* Dorado elegante para el título */
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* Estilo de los inputs y selectboxes */
    .stSelectbox div[data-baseweb="select"], .stSlider div[data-baseweb="slider"] {
        background-color: #1E1E1E !important;
        border: 1px solid #333333;
        border-radius: 8px;
    }
    
    /* Color de acento para sliders y radio buttons (Verde Musgo) */
    div[data-baseweb="slider"] div[data-testid="stTickBar"] {
        background-color: #4A5D23 !important; /* Verde Musgo */
    }

    /* Botón principal */
    .stButton>button {
        background-color: #D4AF37; /* Dorado */
        color: #121212 !important;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    .stButton>button:hover {
        background-color: #F8F9FA;
        color: #121212 !important;
        transform: translateY(-2px);
    }

    /* Mensaje de éxito (Azul Oscuro / Azul Claro) */
    .stSuccess {
        background-color: #0A192F !important; /* Azul oscuro */
        color: #64FFDA !important; /* Azul claro / Cian para el texto */
        border: 1px solid #64FFDA;
        border-radius: 8px;
        font-weight: 500;
    }
    
    /* Separador sutil */
    hr {
        border-color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Asistente de Producción")
st.markdown("<p style='text-align: center; color: #888888 !important; margin-bottom: 3rem;'>Simulación de demanda basada en machine learning.</p>", unsafe_allow_html=True)

# 1. Cargar el modelo en caché para que no se recargue en cada clic
@st.cache_resource
def cargar_modelo():
    try:
        return joblib.load('modelo_cafe.joblib')
    except Exception as e:
        return None

modelo = cargar_modelo()

if modelo is None:
    st.error("No se pudo cargar el modelo. Asegúrate de haber ejecutado entrenar.py primero.")
else:
    # 2. Interfaz: Columnas con controles minimalistas
    st.markdown("### Parámetros de Simulación")
    st.write("") # Espaciador
    
    col1, padding, col2 = st.columns([10, 1, 10])

    with col1:
        dia = st.selectbox("Día de la semana", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        producto = st.selectbox("Producto", ['Croissant', 'Iced Coffee', 'Sandwich', 'Banana Bread', 'Hot Chocolate'])

    with col2:
        temp = st.slider("Temperatura Máxima (°C)", 5, 40, 20)
        
        # Uso de radio buttons horizontales para un look más limpio
        c1, c2 = st.columns(2)
        with c1:
            lluvia = st.radio("¿Lloverá?", ["No", "Sí"], horizontal=True)
        with c2:
            promo = st.radio("¿Hay Promoción?", ["No", "Sí"], horizontal=True)

    st.markdown("<hr style='margin-top: 2rem; margin-bottom: 2rem;'>", unsafe_allow_html=True)

    # 3. Lógica de predicción al presionar el botón
    if st.button("CALCULAR DEMANDA", use_container_width=True):
        
        # Formatear datos para el modelo
        input_df = pd.DataFrame([{
            'Dia_Semana': dia,
            'Temp_Max_C': temp,
            'Lluvia': 1 if lluvia == "Sí" else 0,
            'Promocion': 1 if promo == "Sí" else 0,
            'Producto': producto
        }])
        
        # Ejecutar predicción
        prediccion = modelo.predict(input_df)[0]
        
        # Mostrar resultado destacado
        st.success(f"Proyección óptima: **{int(prediccion)} unidades** de {producto}")