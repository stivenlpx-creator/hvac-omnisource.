import streamlit as st
import google.generativeai as genai

# Configuración de la App
st.set_page_config(page_title="HVAC OMNISOURCE AI", layout="wide")

# CONFIGURACIÓN DE LA IA (Pega aquí tu llave cuando la tengas)
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I" 

if API_KEY != "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I":
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')

st.title("🤖 ASISTENTE HVAC CON IA")
st.write("Consulta cualquier falla, tabla o procedimiento técnico.")

# Barra de chat
user_input = st.text_input("Describe el problema del equipo (ej: 'El compresor calienta pero no arranca'):")

if st.button("PREGUNTAR A LA IA"):
    if API_KEY == "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I":
        st.error("⚠️ Error: Debes pegar tu API KEY en el código para que la IA funcione.")
    elif user_input:
        with st.spinner("La IA está analizando la falla..."):
            try:
                # Instrucción maestra para la IA
                contexto = f"Actúa como un ingeniero experto en refrigeración y HVAC. Responde de forma técnica pero fácil de entender, con pasos numerados (1, 2, 3). El técnico pregunta: {user_input}"
                response = model.generate_content(contexto)
                
                st.markdown("### 🛠️ Diagnóstico Sugerido:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Hubo un error con la IA: {e}")
    else:
        st.warning("Escribe algo para poder ayudarte.")

# Tablas de apoyo fijas (por si no hay internet estable)
st.write("---")
with st.expander("📊 TABLAS DE REFERENCIA RÁPIDA"):
    st.table({
        "R-410A Temp": ["25°C", "35°C", "45°C"],
        "Presión Baja (PSI)": ["118", "142", "168"],
        "Sensor 10kΩ": ["12.1k", "10.0k", "8.3k"]
    })
    
