import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de la IA (Modelo de última generación)
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# 3. Interfaz Profesional
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR CENTRAL CON IA
st.header("🔍 Asistente Técnico IA")
pregunta = st.text_input("Describa el síntoma o consulta técnica:", placeholder="Ej: ¿Por qué un sistema R-410A se va a vacío con amperaje bajo?")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta:
        with st.spinner("🧠 IA Procesando..."):
            try:
                res = model.generate_content(f"Eres experto HVAC Senior. Responde con pasos técnicos numerados a: {pregunta}")
                st.info(res.text)
            except Exception as e:
                st.error(f"Error de conexión: {e}. Verifique su conexión o intente otra pregunta.")

# PESTAÑAS DE HERRAMIENTAS ACTUALIZADAS
st.divider()
t1, t2, t3 = st.tabs(["🧮 Calculadoras P/T", "🌡️ Enciclopedia de Refrigerantes", "🛡️ Seguridad"])

with t1:
    st.subheader("Cálculo de Superheat / Subcooling")
    c1, esp, c2 = st.columns([2, 1, 2])
    with c1:
        ts = st.number_input("Temp. Tubería Succión (°C)", value=12.0)
        pb = st.number_input("Presión de Baja (PSI)", value=118.0)
        # Cálculo SH aproximado R410A
        sh = ts - ((pb / 10) - 38)
        st.metric("Sobrecalentamiento", f"{sh:.1f} °C", delta="Ideal: 4-7°C")
    with c2:
        tl = st.number_input("Temp. Tubería Líquido (°C)", value=35.0)
        pa = st.number_input("Presión de Alta (PSI)", value=320.0)
        # Cálculo SC aproximado R410A
        sc = ((pa / 10) - 1) - tl
        st.metric("Subenfriamiento", f"{sc:.1f} °C", delta="Ideal: 5-8°C")

with t2:
    st.subheader("Guía de Presiones y Gases")
    
    refrig = st.selectbox("Seleccione Refrigerante para ver datos:", 
                         ["R-410A", "R-22", "R-32", "R-134a", "R-404A"])
    
    if refrig == "R-410A":
        st.write("**Uso:** Aire acondicionado moderno e Inverter.")
        st.write("**Presión Succión Típica:** 115 - 145 PSI.")
        st.write("**Aceite:** POE (Polioester).")
        st.info("💡 Mezcla azeotrópica: Se debe cargar siempre en fase LÍQUIDA.")
    
    elif refrig == "R-22":
        st.write("**Uso:** Equipos antiguos (en fase de salida).")
        st.write("**Presión Succión Típica:** 60 - 75 PSI.")
        st.write("**Aceite:** Mineral.")
        st.warning("⚠️ Dañino para la capa de ozono. No mezclar con aceites sintéticos.")

    elif refrig == "R-32":
        st.write("**Uso:** Nueva generación Inverter de alta eficiencia.")
        st.write("**Presión Succión Típica:** 120 - 155 PSI.")
        st.write("**Clasificación:** A2L (Ligeramente inflamable).")
        st.error("⚠️ Requiere herramientas antichispa y bomba de vacío certificada.")

    elif refrig == "R-134a":
        st.write("**Uso:** Refrigeración comercial y automotriz.")
        st.write("**Presión Succión Típica:** 20 - 35 PSI (depende de la aplicación).")
        st.write("**Aceite:** PAG / POE.")

    elif refrig == "R-404A":
        st.write("**Uso:** Baja y media temperatura (Congeladores).")
        st.write("**Presión Succión Típica:** 45 - 65 PSI (Media) / 15 - 25 PSI (Baja).")

with t3:
    st.subheader("Seguridad y Manejo Químico")
    st.write("1. **Nitrógeno:** Nunca presurice sin regulador. Límite seguro para evaporadoras: 150-250 PSI.")
    st.write("2. **Oxígeno:** PROHIBIDO su uso en limpieza o presurización (Riesgo de explosión térmica).")
    st.write("3. **EPP:** El uso de guantes es vital para evitar quemaduras por expansión de refrigerante líquido.")
