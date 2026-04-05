import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de la IA
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Interfaz Profesional
st.markdown("<h1 style='text-align: center; color: #00e5ff;'>⚡ HVAC PRO DIAGNOSTIC ❄️</h1>", unsafe_content_allowed=True)
st.write("---")

# BUSCADOR CENTRAL
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.subheader("🔍 Buscador de Fallas con IA")
    pregunta = st.text_input("Describa la falla:", placeholder="Ej: Compresor se va a vacío...")
    if st.button("ANALIZAR CON IA", use_container_width=True):
        if pregunta:
            with st.spinner("🧠 Analizando..."):
                try:
                    res = model.generate_content(f"Eres experto HVAC. Pasos numerados para: {pregunta}")
                    st.info(res.text)
                except Exception as e:
                    st.error(f"Error: {e}")

# PESTAÑAS DE HERRAMIENTAS
st.write("---")
t1, t2, t3, t4 = st.tabs(["🧮 Cálculos", "🔌 Diagramas", "🌡️ Presión", "🛡️ Seguridad"])

with t1:
    st.subheader("Superheat / Subcooling")
    c1, c2 = st.columns(2)
    with c1:
        ts = st.number_input("Temp. Succión (°C)", value=12.0)
        pb = st.number_input("Presión Baja (PSI)", value=120.0)
        sh = ts - ((pb / 10) - 38)
        st.metric("Sobrecalentamiento", f"{sh:.1f} °C")
    with c2:
        tl = st.number_input("Temp. Líquido (°C)", value=35.0)
        pa = st.number_input("Presión Alta (PSI)", value=320.0)
        sc = ((pa / 10) - 1) - tl
        st.metric("Subenfriamiento", f"{sc:.1f} °C")

with t2:
    st.subheader("Electricidad y Control")
    st.write("Mida resistencia entre bornes para hallar C, R y S.")
    st.write("C-R + C-S debe ser igual a R-S.")

with t3:
    st.subheader("Consultas de Presión")
    st.write("Use el buscador de arriba para consultar presiones de R-22, R-134a o R-404.")
    st.info("💡 Tip: En R-410A, 120 PSI equivale a aprox. 4°C de saturación.")

with t4:
    st.subheader("Seguridad")
    st.error("⚠️ Prohibido usar Oxígeno para presurizar.")
    st.warning("⚠️ Use regulador de Nitrógeno siempre.")
