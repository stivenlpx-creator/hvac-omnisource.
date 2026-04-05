import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="HVAC PRO", layout="wide")

# Llave que probamos y funciona
API_KEY = "AIzaSyC0-1YsWu9A_xwMu-UflXzkZrn-IFk9Wf0"

# Inicializar IA
try:
    genai.configure(api_key=API_KEY)
    # Usamos el modelo más moderno pero de forma simplificada
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de sistema: {e}")

st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte OMNISOURCE")

# Buscador
pregunta = st.text_input("Consulta técnica:", placeholder="Ej: R410A")

if st.button("ANALIZAR CON IA"):
    if pregunta:
        with st.spinner("🧠 Consultando..."):
            try:
                response = model.generate_content(pregunta)
                st.success("### DIAGNÓSTICO:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

# Calculadoras (Enteros)
st.divider()
st.subheader("🧮 Eficiencia (Valores Enteros)")
c1, c2 = st.columns(2)

with c1:
    ts = st.number_input("Temp Succión (°C)", value=10, step=1)
    pb = st.number_input("Presión Baja (PSI)", value=118, step=1)
    sh = int(round(ts - ((pb / 10) - 7)))
    st.metric("SH", f"{sh} °C")
    if 4 <= sh <= 7: st.success("✅ Eficiente")
    else: st.warning("⚠️ Ajustar")

with c2:
    tl = st.number_input("Temp Líquido (°C)", value=32, step=1)
    pa = st.number_input("Presión Alta (PSI)", value=320, step=1)
    sc = int(round(((pa / 10) + 6) - tl))
    st.metric("SC", f"{sc} °C")
    if 5 <= sc <= 8: st.success("✅ Eficiente")
    else: st.warning("⚠️ Revisar")
