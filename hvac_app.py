import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de la IA
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Interfaz Limpia (Sin HTML para evitar errores)
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR CENTRAL
st.header("🔍 Buscador de Fallas con IA")
pregunta = st.text_input("Describe la falla del equipo:", placeholder="Ej: Compresor se va a vacío, error E1, capacitor seco...")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta:
        with st.spinner("🧠 IA Analizando parámetros..."):
            try:
                res = model.generate_content(f"Eres experto HVAC. Pasos numerados para: {pregunta}")
                st.info(res.text)
            except Exception as e:
                st.error(f"Error de conexión: {e}")

# PESTAÑAS DE HERRAMIENTAS
st.divider()
t1, t2, t3, t4 = st.tabs(["🧮 Cálculos", "🔌 Diagramas", "🌡️ Presión", "🛡️ Seguridad"])

with t1:
    st.subheader("Cálculos de Superheat y Carga")
    c1, col_espacio, c2 = st.columns([2, 1, 2])
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
    st.write("1. **Identificación de bornes:** Mida resistencia entre los 3 bornes.")
    st.write("2. **Motores PG:** Revisar sensor Hall (conector pequeño).")

with t3:
    st.subheader("Consultas de Presión")
    st.info("💡 Tip: En R-410A, 118 PSI es ideal para una evaporación de 4.5°C.")
    st.write("Consulte al buscador de IA arriba para refrigerantes específicos.")

with t4:
    st.subheader("Seguridad y Manejo Químico")
    st.error("⚠️ Nunca use Oxígeno para presurizar (Riesgo de explosión).")
    st.warning("⚠️ Use siempre gafas de seguridad y guantes.")
    
