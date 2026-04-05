import streamlit as st
import google.generativeai as genai

# 1. Configuración básica
st.set_page_config(page_title="HVAC Pro", layout="wide")

# 2. IA con tu Key
API_KEY = "AIzaSyC0-1YsWu9A_xwMu-UflXzkZrn-IFk9Wf0"

try:
    genai.configure(api_key=API_KEY)
    # Seleccionamos el modelo sin florituras para máxima compatibilidad
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de inicio: {e}")

# 3. Interfaz
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR
st.header("🔍 Asistente Técnico IA")
pregunta = st.text_input("Consulta técnica:", placeholder="Ej: R410A")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta:
        with st.spinner("🧠 Analizando..."):
            try:
                # Intento de respuesta directa
                response = model.generate_content(pregunta)
                st.success("### 🛠️ DIAGNÓSTICO:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error técnico: {e}")
                st.info("Si el error persiste tras borrar y recrear la app, la API Key podría estar bloqueada por Google.")

# CALCULADORAS
st.divider()
st.subheader("🧮 Eficiencia (Enteros)")
c1, c2 = st.columns(2)
with c1:
    ts = st.number_input("Temp Succión (°C)", value=10, step=1)
    pb = st.number_input("Presión Baja (PSI)", value=118, step=1)
    sh = int(round(ts - ((pb / 10) - 7)))
    st.metric("SH", f"{sh} °C")
    if 4 <= sh <= 7: st.success("✅ Eficiente (Ideal: 4-7°C)")
    else: st.warning("⚠️ Fuera de rango")

with c2:
    tl = st.number_input("Temp Líquido (°C)", value=32, step=1)
    pa = st.number_input("Presión Alta (PSI)", value=320, step=1)
    sc = int(round(((pa / 10) + 6) - tl))
    st.metric("SC", f"{sc} °C")
    if 5 <= sc <= 8: st.success("✅ Eficiente (Ideal: 5-8°C)")
    else: st.warning("⚠️ Fuera de rango")
