import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de la IA (Conexión Estabilizada)
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de configuración: {e}")

# 3. Interfaz Profesional
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR CENTRAL CON IA
st.header("🔍 Asistente Técnico IA")
pregunta = st.text_input("Consulta técnica:", placeholder="Ej: Pasos para diagnosticar un compresor en corto...")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta:
        with st.spinner("🧠 Consultando base de datos técnica..."):
            try:
                prompt = f"Eres un Ingeniero HVAC Senior. Responde con pasos numerados a: {pregunta}"
                response = model.generate_content(prompt)
                if response:
                    st.success("### 🛠️ DIAGNÓSTICO:")
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"⚠️ Error de conexión: {str(e)}")
                st.info("Asegúrate de que tu API Key de Google AI Studio esté activa.")

# PESTAÑAS DE HERRAMIENTAS
st.divider()
t1, t2, t3 = st.tabs(["🧮 Calculadoras P/T", "🌡️ Guía de Gases", "🛡️ Seguridad"])

with t1:
    st.subheader("Cálculos de Eficiencia (Valores Enteros)")
    c1, esp, c2 = st.columns([2, 1, 2])
    
    with c1:
        st.write("**Sobrecalentamiento (Superheat)**")
        ts = st.number_input("Temp. Succión (°C)", value=10, step=1, key="ts_int")
        pb = st.number_input("Presión de Baja (PSI)", value=118, step=1, key="pb_int")
        # Cálculo SH (R410A aprox)
        t_sat = (pb / 10) - 7
        sh = int(round(ts - t_sat))
        st.metric("Superheat (SH)", f"{sh} °C", delta="Ideal: 4 a 7°C")
        
    with c2:
        st.write("**Subenfriamiento (Subcooling)**")
        tl = st.number_input("Temp. Líquido (°C)", value=32, step=1, key="tl_int")
        pa = st.number_input("Presión de Alta (PSI)", value=320, step=1, key="pa_int")
        # Cálculo SC (R410A aprox)
        t_sat_alta = (pa / 10) + 6
        sc = int(round(t_sat_alta - tl))
        st.metric("Subcooling (SC)", f"{sc} °C", delta="Ideal: 5 a 8°C")

with t2:
    st.subheader("Buscador de Refrigerantes y Tips")
    gas = st.selectbox("Seleccione el refrigerante para ver tips:", 
                      ["R-410A", "R-22", "R-32", "R-134a", "R-404A"])
    
    if gas == "R-410A":
        st.info("**R-410A:** Carga en LÍQUIDO (Mezcla 50/50 R-32 y R-125). P. Succión: 115-145 PSI. Aceite: POE.")
    elif gas == "R-22":
        st.warning("**R-22:** Carga en GAS o LÍQUIDO. P. Succión: 60-75 PSI. Aceite: Mineral. *Dañino para el ozono.*")
    elif gas == "R-32":
        st.error("**R-32:** Altamente eficiente. Inflamable A2L. P. Succión: 120-155 PSI. Requiere equipo antichispas.")
    elif gas == "R-134a":
        st.success("**R-134a:** Uso automotriz/comercial. P. Succión: 20-35 PSI. No mezclar con R-12.")
    elif gas == "R-404A":
        st.write("**R-404A:** Baja temperatura. P. Succión: 15-65 PSI. Siempre cargar en líquido.")

with t3:
    st.subheader("Protocolos de Seguridad")
    st.error("⚠️ PROHIBIDO usar oxígeno (Riesgo de explosión térmica).")
    st.warning("⚠️ Nitrógeno seco: Use siempre regulador de doble etapa.")
