import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de la IA (Línea corregida para evitar error 404)
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"

try:
    genai.configure(api_key=API_KEY)
    # Cambiamos a 'models/gemini-1.5-flash' (Ruta completa para máxima compatibilidad)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de configuración: {e}")

# 3. Interfaz Profesional
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR CENTRAL
st.header("🔍 Asistente Técnico IA")
pregunta = st.text_input("Consulta técnica:", placeholder="Ej: Pasos para realizar vacío profundo...")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta:
        with st.spinner("🧠 Consultando base de datos técnica..."):
            try:
                # Instrucción para que la respuesta sea profesional
                prompt = f"Eres un Ingeniero HVAC Senior. Responde con pasos numerados a: {pregunta}"
                response = model.generate_content(prompt)
                
                if response:
                    st.success("### 🛠️ DIAGNÓSTICO:")
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"⚠️ Error de API (404/Conexión): {str(e)}")
                st.info("Si el error persiste, la API Key podría estar restringida en Google AI Studio.")

# PESTAÑAS DE HERRAMIENTAS (Fórmulas Corregidas)
st.divider()
t1, t2, t3 = st.tabs(["🧮 Calculadoras P/T", "🌡️ Datos de Gases", "🛡️ Seguridad"])

with t1:
    st.subheader("Cálculo de Superheat / Subcooling (R-410A)")
    c1, esp, c2 = st.columns([2, 1, 2])
    
    with c1:
        st.write("**Sobrecalentamiento (Superheat)**")
        ts = st.number_input("Temp. Tubería Succión (°C)", value=10.0, key="ts_fix")
        pb = st.number_input("Presión de Baja (PSI)", value=118.0, key="pb_fix")
        # Fórmula: Ts - T_sat (R410A a 118 PSI es aprox 4.5°C)
        t_sat = (pb / 10) - 7.3 # Estimación más precisa para R410A
        sh = ts - t_sat
        st.metric("Superheat (SH)", f"{sh:.1f} °C", delta="Ideal: 4 a 7°C")
        
    with c2:
        st.write("**Subenfriamiento (Subcooling)**")
        tl = st.number_input("Temp. Tubería Líquido (°C)", value=32.0, key="tl_fix")
        pa = st.number_input("Presión de Alta (PSI)", value=320.0, key="pa_fix")
        # T_sat a 320 PSI es aprox 38°C
        t_sat_alta = (pa / 10) + 6.0
        sc = t_sat_alta - tl
        st.metric("Subcooling (SC)", f"{sc:.1f} °C", delta="Ideal: 5 a 8°C")

with t2:
    st.subheader("Presiones de Trabajo (PSI)")
    st.table({
        "Refrigerante": ["R-410A", "R-22", "R-134a", "R-32", "R-404A"],
        "Baja (Promedio)": ["120", "65", "30", "125", "55"],
        "Alta (Promedio)": ["350", "250", "170", "380", "300"]
    })

with t3:
    st.subheader("Protocolos de Seguridad")
    st.error("1. PROHIBIDO usar oxígeno (Riesgo de explosión térmica).")
    st.warning("2. Nitrógeno seco: Use siempre regulador de doble etapa.")
