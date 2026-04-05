import streamlit as st
import google.generativeai as genai

# 1. Configuración
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. IA con tu nueva Key
API_KEY = "AIzaSyDlyLW--Tan3ObFrPurB-ycI-3hf_Mx00I"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de configuración: {e}")

# 3. Interfaz
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR
st.header("🔍 Asistente Técnico IA")
pregunta = st.text_input("Consulta técnica:", placeholder="Ej: Pasos para diagnosticar falla de vacío...")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta:
        with st.spinner("🧠 Analizando..."):
            try:
                res = model.generate_content(f"Ingeniero HVAC experto. Pasos numerados para: {pregunta}")
                st.info(res.text)
            except Exception as e:
                st.error(f"Error de API: {str(e)}")

# PESTAÑAS
st.divider()
t1, t2, t3 = st.tabs(["🧮 Cálculos", "🌡️ Gases", "🛡️ Seguridad"])

with t1:
    st.subheader("Eficiencia (Enteros)")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Sobrecalentamiento**")
        ts = st.number_input("Temp Succión (°C)", value=10, step=1)
        pb = st.number_input("Presión Baja (PSI)", value=118, step=1)
        sh = int(round(ts - ((pb / 10) - 7)))
        st.metric("SH", f"{sh} °C")
    with c2:
        st.write("**Subenfriamiento**")
        tl = st.number_input("Temp Líquido (°C)", value=32, step=1)
        pa = st.number_input("Presión Alta (PSI)", value=320, step=1)
        sc = int(round(((pa / 10) + 6) - tl))
        st.metric("SC", f"{sc} °C")

with t2:
    st.subheader("Guía de Refrigerantes")
    gas = st.selectbox("Refrigerante:", ["R-410A", "R-22", "R-32", "R-134a", "R-404A", "R-407C", "R-507", "R-600a", "R-290", "R-1234yf"])
    if gas == "R-410A": st.info("Carga LÍQUIDO. Succión: 115-145 PSI. Aceite POE.")
    elif gas == "R-22": st.warning("Carga Gas/Líquido. Succión: 60-75 PSI. Aceite Mineral.")
    elif gas == "R-32": st.error("Inflamable A2L. Succión: 120-155 PSI. Herramienta especial.")
    elif gas == "R-134a": st.success("Automotriz/Comercial. Succión: 20-35 PSI.")
    elif gas == "R-404A": st.write("Baja temp. Carga LÍQUIDO. Succión: 15-60 PSI.")
    elif gas == "R-407C": st.info("Reemplazo R-22. Carga LÍQUIDO. Glide alto.")
    elif gas == "R-507": st.write("Congelación. Carga LÍQUIDO. Reemplaza R-502.")
    elif gas == "R-600a": st.error("Isobutano. Inflamable. Carga por gramaje exacto.")
    elif gas == "R-290": st.error("Propano. Natural. Muy eficiente e inflamable.")
    elif gas == "R-1234yf": st.success("Nuevo estándar auto. Bajo GWP. A2L.")

with t3:
    st.subheader("Seguridad")
    st.error("⚠️ PROHIBIDO OXÍGENO para presurizar.")
    st.warning("⚠️ Nitrógeno: Siempre con regulador.")
