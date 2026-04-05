import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de la IA (Nueva Llave Aplicada)
API_KEY = "AIzaSyC0-1YsWu9A_xwMu-UflXzkZrn-IFk9Wf0"

try:
    genai.configure(api_key=API_KEY)
    # Usamos la configuración de modelo estándar para Gemini 1.5 Flash
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de configuración: {e}")

# 3. Interfaz Profesional
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR CENTRAL CON IA
st.header("🔍 Asistente Técnico IA")
pregunta = st.text_input("Consulta técnica:", placeholder="Ej: ¿Cómo diagnosticar una obstrucción en el capilar?")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta:
        with st.spinner("🧠 Conectando con el cerebro de ingeniería..."):
            try:
                # Prompt directo para respuesta técnica
                response = model.generate_content(f"Eres un experto Ingeniero HVAC. Da diagnóstico técnico paso a paso para: {pregunta}")
                if response.text:
                    st.success("### 🛠️ DIAGNÓSTICO SUGERIDO:")
                    st.markdown(response.text)
                else:
                    st.warning("No se recibió respuesta. Intenta reformular la pregunta.")
            except Exception as e:
                st.error("⚠️ Error de API: Es posible que la llave necesite unos minutos para activarse en el servidor de Google.")
                st.write(f"Detalle técnico: {e}")

# PESTAÑAS DE HERRAMIENTAS
st.divider()
t1, t2, t3 = st.tabs(["🧮 Cálculos de Eficiencia", "🌡️ Enciclopedia de Gases", "🛡️ Seguridad"])

with t1:
    st.subheader("Cálculos en Tiempo Real (Valores Enteros)")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Sobrecalentamiento (Superheat)**")
        ts = st.number_input("Temp Succión (°C)", value=10, step=1, key="ts_final")
        pb = st.number_input("Presión Baja (PSI)", value=118, step=1, key="pb_final")
        # Cálculo SH (R410A aprox)
        sh = int(round(ts - ((pb / 10) - 7)))
        st.metric("SH", f"{sh} °C")
        if 4 <= sh <= 7:
            st.success("✅ Eficiente (Ideal: 4 a 7 °C)")
        else:
            st.warning("⚠️ Fuera de rango óptimo (Ajustar carga)")

    with c2:
        st.write("**Subenfriamiento (Subcooling)**")
        tl = st.number_input("Temp Líquido (°C)", value=32, step=1, key="tl_final")
        pa = st.number_input("Presión Alta (PSI)", value=320, step=1, key="pa_final")
        # Cálculo SC (R410A aprox)
        sc = int(round(((pa / 10) + 6) - tl))
        st.metric("SC", f"{sc} °C")
        if 5 <= sc <= 8:
            st.success("✅ Eficiente (Ideal: 5 a 8 °C)")
        else:
            st.warning("⚠️ Fuera de rango óptimo (Revisar condensación)")

with t2:
    st.subheader("Buscador de Refrigerantes y Tips")
    gas = st.selectbox("Seleccione el gas:", ["R-410A", "R-22", "R-32", "R-134a", "R-404A", "R-407C", "R-507", "R-600a", "R-290", "R-1234yf"])
    if gas == "R-410A": st.info("**Tips R-410A:** Carga LÍQUIDO. Succión: 115-145 PSI. Aceite POE.")
    elif gas == "R-22": st.warning("**Tips R-22:** Carga Gas/Líquido. Succión: 60-75 PSI. Aceite Mineral.")
    elif gas == "R-32": st.error("**Tips R-32:** Inflamable A2L. Succión: 120-155 PSI. Carga líquida.")
    elif gas == "R-134a": st.success("**Tips R-134a:** Automotriz/Comercial. Succión: 20-35 PSI.")
    elif gas == "R-404A": st.write("**Tips R-404A:** Baja temp. Carga LÍQUIDO. Succión: 15-60 PSI.")
    elif gas == "R-407C": st.info("**Tips R-407C:** Reemplazo R-22. Carga LÍQUIDO. Glide térmico alto.")
    elif gas == "R-507": st.write("**Tips R-507:** Congelación. Carga LÍQUIDO. Azeotrópico.")
    elif gas == "R-600a": st.error("**Tips R-600a:** Isobutano. Inflamable. Carga por peso exacto.")
    elif gas == "R-290": st.error("**Tips R-290:** Propano. Alta eficiencia. Muy inflamable.")
    elif gas == "R-1234yf": st.success("**Tips R-1234yf:** Ecológico auto. Bajo GWP. Inflamable A2L.")

with t3:
    st.subheader("Protocolos de Seguridad")
    st.error("⚠️ PROHIBIDO usar oxígeno para presurizar (Explosión).")
    st.warning("⚠️ Nitrógeno seco: Use siempre regulador de doble etapa.")
