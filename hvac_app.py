import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de la IA con la Nueva API Key
API_KEY = "AIzaSyDlyLW--Tan3ObFrPurB-ycI-3hf_Mx00I"

try:
    genai.configure(api_key=API_KEY)
    # Usamos la ruta más estable para evitar errores 404
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de configuración: {e}")

# 3. Interfaz Profesional
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR CENTRAL CON IA
st.header("🔍 Asistente Técnico IA")
pregunta = st.text_input("Consulta técnica:", placeholder="Ej: ¿Cómo diagnosticar un compresor con válvulas descompresionadas?")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta:
        with st.spinner("🧠 Consultando base de datos técnica..."):
            try:
                # Instrucción maestra para la IA
                prompt = f"Eres un Ingeniero HVAC Senior. Responde de forma técnica, precisa y con pasos numerados a: {pregunta}"
                response = model.generate_content(prompt)
                if response:
                    st.success("### 🛠️ DIAGNÓSTICO:")
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"⚠️ Error de conexión: {str(e)}")
                st.info("Verifica que la API Key esté activa en Google AI Studio.")

# PESTAÑAS DE HERRAMIENTAS
st.divider()
t1, t2, t3 = st.tabs(["🧮 Calculadoras P/T", "🌡️ Enciclopedia de Gases", "🛡️ Seguridad"])

with t1:
    st.subheader("Cálculos de Eficiencia (Valores Enteros)")
    c1, esp, c2 = st.columns([2, 1, 2])
    
    with c1:
        st.write("**Sobrecalentamiento (Superheat)**")
        ts = st.number_input("Temp. Tubería Succión (°C)", value=10, step=1, key="ts_final")
        pb = st.number_input("Presión de Baja (PSI)", value=118, step=1, key="pb_final")
        # Cálculo SH (R410A aprox)
        t_sat = (pb / 10) - 7
        sh = int(round(ts - t_sat))
        st.metric("Superheat (SH)", f"{sh} °C", delta="Ideal: 4 a 7°C")
        
    with c2:
        st.write("**Subenfriamiento (Subcooling)**")
        tl = st.number_input("Temp. Tubería Líquido (°C)", value=32, step=1, key="tl_final")
        pa = st.number_input("Presión de Alta (PSI)", value=320, step=1, key="pa_final")
        # Cálculo SC (R410A aprox)
        t_sat_alta = (pa / 10) + 6
        sc = int(round(t_sat_alta - tl))
        st.metric("Subcooling (SC)", f"{sc} °C", delta="Ideal: 5 a 8°C")

with t2:
    st.subheader("Buscador de
