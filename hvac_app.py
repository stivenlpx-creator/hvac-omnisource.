import streamlit as st
import google.generativeai as genai

# 1. Configuración
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. IA con tu Key
API_KEY = "AIzaSyC0-1YsWu9A_xwMu-UflXzkZrn-IFk9Wf0"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de sistema: {e}")

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
                response = model.generate_content(pregunta)
                st.info(response.text)
            except Exception as e:
                st.error(f"Error de comunicación: {e}")

# PESTAÑAS (Calculadoras e Información)
st.divider()
t1, t2 = st.tabs(["🧮 Cálculos de Eficiencia", "🌡️ Gases"])

with t1:
    st.subheader("Eficiencia (Valores Enteros)")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Sobrecalentamiento (SH)**")
        ts = st.number_input("Temp Succión (°C)", value=10, step=1)
        pb = st.number_input("Presión Baja (PSI)", value=118, step=1)
        sh = int(round(ts - ((pb / 10) - 7)))
        st.metric("SH", f"{sh} °C")
        if 4 <= sh <= 7: st.success("✅ Eficiente (Ideal: 4-7°C)")
        else: st.warning("⚠️ Fuera de rango")

    with c2:
        st.write("**Subenfriamiento (SC)**")
        tl = st.number_input("Temp Líquido (°C)", value=32, step=1)
        pa = st.number_input("Presión Alta (PSI)", value=320, step=1)
        sc = int(round(((pa / 10) + 6) - tl))
        st.metric("SC", f"{sc} °C")
        if 5 <= sc <= 8: st.success("✅ Eficiente (Ideal: 5-8°C)")
        else: st.warning("⚠️ Fuera de rango")
