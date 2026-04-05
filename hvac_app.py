import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de la IA
# IMPORTANTE: Si sigue fallando, genera una nueva API Key en https://aistudio.google.com/
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"

try:
    genai.configure(api_key=API_KEY)
    # Cambiamos a la versión más estable posible
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de configuración inicial: {e}")

# 3. Interfaz Profesional
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR CENTRAL
st.header("🔍 Asistente Técnico IA")
pregunta = st.text_input("Consulta técnica (Ej: ¿Cómo probar un compresor aterrizado?):", placeholder="Escriba aquí...")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta:
        with st.spinner("🧠 Consultando cerebro de ingeniería..."):
            try:
                # Instrucción maestra
                prompt = f"Eres un Ingeniero HVAC experto. Responde de forma técnica y con pasos numerados a: {pregunta}"
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("### 🛠️ DIAGNÓSTICO:")
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"⚠️ Error técnico de la API: {str(e)}")
                st.warning("Si el error persiste, genera una nueva API Key en Google AI Studio.")

# PESTAÑAS DE HERRAMIENTAS (Fórmulas Corregidas)
st.divider()
t1, t2, t3 = st.tabs(["🧮 Calculadoras P/T", "🌡️ Enciclopedia de Refrigerantes", "🛡️ Seguridad"])

with t1:
    st.subheader("Cálculo de Superheat / Subcooling (R-410A)")
    c1, esp, c2 = st.columns([2, 1, 2])
    
    with c1:
        st.write("**Sobrecalentamiento (Superheat)**")
        ts = st.number_input("Temp. Tubería Succión (°C)", value=10.0, key="succion_v2")
        pb = st.number_input("Presión de Baja (PSI)", value=120.0, key="baja_v2")
        # Fórmula mejorada: Temperatura real - Temperatura de saturación aproximada
        t_sat_baja = (pb / 10) - 38.5 
        sh = ts - t_sat_baja
        st.metric("Superheat (SH)", f"{sh:.1f} °C", delta="Ideal: 4 a 7°C")
        
    with c2:
        st.write("**Subenfriamiento (Subcooling)**")
        tl = st.number_input("Temp. Tubería Líquido (°C)", value=32.0, key="liquido_v2")
        pa = st.number_input("Presión de Alta (PSI)", value=320.0, key="alta_v2")
        # Fórmula mejorada: Temperatura de saturación aproximada - Temperatura real
        t_sat_alta = (pa / 10) + 2.0
        sc = t_sat_alta - tl
        st.metric("Subcooling (SC)", f"{sc:.1f} °C", delta="Ideal: 5 a 8°C")

with t2:
    st.subheader("Datos Técnicos por Gas")
    refrig = st.selectbox("Seleccione:", ["R-410A", "R-22", "R-32", "R-134a", "R-404A"])
    
    tablas_datos = {
        "R-410A": {"Succion": "115-145 PSI", "Descarga": "350-450 PSI", "Aceite": "Sintético (POE)"},
        "R-22": {"Succion": "60-75 PSI", "Descarga": "250-300 PSI", "Aceite": "Mineral (MO)"},
        "R-32": {"Succion": "120-155 PSI", "Descarga": "380-480 PSI", "Aceite": "Sintético (POE)"},
        "R-134a": {"Succion": "20-35 PSI", "Descarga": "150-200 PSI", "Aceite": "PAG/POE"},
        "R-404A": {"Succion": "15-65 PSI", "Descarga": "280-350 PSI", "Aceite": "Sintético (POE)"}
    }
    
    st.json(tablas_datos[refrig])
    st.info("Nota: Los valores varían según la temperatura ambiente y la carga térmica.")

with t3:
    st.subheader("Seguridad en el Sitio")
    st.error("1. PROHIBIDO usar aire o oxígeno para presurizar (Explosión).")
    st.warning("2. Use nitrógeno seco con regulador de doble etapa.")
    st.write("3. Mida el vacío con vacuómetro electrónico, no con manómetros de aguja.")
