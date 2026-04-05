import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC OMNISOURCE AI", layout="wide")

# 2. Configuración de la Inteligencia Artificial (Tu Llave ya está puesta)
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. Diseño de la Interfaz
st.markdown("<h1 style='text-align: center;'>🤖 HVAC AI: ASISTENTE EXPERTO ❄️</h1>", unsafe_content_allowed=True)
st.write("---")

# 4. Motor de Consulta
st.subheader("¿Qué problema presenta el equipo?")
pregunta = st.text_input("Describe la falla (Ej: El compresor se va a vacío, Error E1 Mirage, Motor no gira):")

if st.button("🧠 ANALIZAR CON IA"):
    if pregunta:
        with st.spinner("Consultando base de datos de ingeniería..."):
            try:
                # Instrucción maestra para que la IA no invente y sea técnica
                instruccion = f"""
                Actúa como un Ingeniero Senior en Refrigeración y HVAC. 
                Responde a la siguiente consulta técnica de forma detallada y profesional.
                Usa siempre pasos numerados (1, 2, 3...) para el diagnóstico.
                Si mencionas presiones, especifica el tipo de refrigerante (R410A o R22).
                Consulta: {pregunta}
                """
                
                response = model.generate_content(instruccion)
                
                st.success("### 🛠️ DIAGNÓSTICO Y PASO A PASO:")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Error de conexión con la IA: {e}")
    else:
        st.warning("Por favor, escribe la falla para poder ayudarte.")

# 5. Tablas de Referencia (Apoyo Visual y Técnico)
st.write("---")
st.subheader("📊 BIBLIOTECA DE CONSULTA RÁPIDA")

tab1, tab2, tab3 = st.tabs(["🌡️ Presión/Temp", "🔌 Electricidad", "🌡️ Sensores"])

with tab1:
    st.write("**Relación P/T (R-410A) en Succión**")
    st.table({
        "Temp. Ambiente": ["25°C", "30°C", "35°C", "40°C"],
        "Presión Baja (PSI)": ["115 - 118", "122 - 130", "135 - 145", "150 - 160"]
    })

with tab2:
    st.write("**Identificación de Bobinas de Compresor**")
    st.info("Regla: Resistencia R-S = (C-R) + (C-S). Si no suma, la bobina está recalentada.")

with tab3:
    st.write("**Tabla de Sensores kΩ**")
    st.table({
        "Temp": ["20°C", "25°C", "30°C"],
        "10kΩ": ["12.1", "10.0", "8.3"],
        "5kΩ": ["6.1", "5.0", "4.1"]
    })
    
