import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de la IA (Modelo Flash 1.5 - Más rápido y sin errores)
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Interfaz Profesional
st.markdown("<h1 style='text-align: center; color: #00e5ff;'>⚡ HVAC PRO DIAGNOSTIC ❄️</h1>", unsafe_content_allowed=True)
st.markdown("<p style='text-align: center; color: #808495;'>Soporte Técnico de Ingeniería - OMNISOURCE</p>", unsafe_content_allowed=True)
st.write("---")

# BUSCADOR CENTRAL CON IA
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.subheader("🔍 Buscador de Fallas con IA")
    pregunta = st.text_input("Describa el problema del equipo:", placeholder="Ej: Compresor se va a vacío, error E1, capacitor seco...")
    if st.button("ANALIZAR CON IA", use_container_width=True):
        if pregunta:
            with st.spinner("🧠 IA Analizando parámetros técnicos..."):
                try:
                    res = model.generate_content(f"Eres experto HVAC. Da diagnóstico paso a paso para: {pregunta}")
                    st.info(res.text)
                except Exception as e:
                    st.error(f"Error de conexión: {e}")

# PESTAÑAS DE HERRAMIENTAS (Información técnica sin tablas largas)
st.write("---")
t1, t2, t3, t4 = st.tabs(["🧮 Calculadoras", "🔌 Diagramas", "🌡️ Tabla P-T", "🛡️ Seguridad"])

with t1:
    st.subheader("Superheat / Subcooling")
    c1, c2 = st.columns(2)
    with c1:
        ts = st.number_input("Temp. Tubería Succión (°C)", value=12.0)
        pb = st.number_input("Presión de Baja (PSI)", value=120.0)
        # Cálculo SH para R410A
        sh = ts - ((pb / 10) - 38)
        st.metric("Sobrecalentamiento (SH)", f"{sh:.1f} °C", delta="Ideal: 4-7°C")
    with c2:
        tl = st.number_input("Temp. Tubería Líquido (°C)", value=35.0)
        pa = st.number_input("Presión de Alta (PSI)", value=320.0)
        sc = ((pa / 10) - 1) - tl
        st.metric("Subenfriamiento (SC)", f"{sc:.1f} °C", delta="Ideal: 5-8°C")

with t2:
    st.subheader("Esquemas y Electricidad")
    st.write("**Identificación de Compresor:**")
    st.write("Para determinar C, R y S, mida la resistencia entre los 3 bornes. La suma de las dos menores debe dar la mayor (R-S).")
    [attachment_0](attachment)
    st.write("**Motores Ventilador:**")
    st.write("En motores PG, verifique el conector pequeño de 3 o 5 cables (Sensor Hall) para señales de pulso de velocidad.")
    [attachment_1](attachment)

with t3:
    st.subheader("Relación Presión-Temperatura")
    st.write("Use el buscador superior para consultar presiones específicas de cualquier refrigerante (R-22, R-
    
