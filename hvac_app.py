import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC PRO", layout="wide")

# 2. IA con tu Key (La que probaste en la foto)
API_KEY = "AIzaSyC0-1YsWu9A_xwMu-UflXzkZrn-IFk9Wf0"

def conectar_ia():
    try:
        genai.configure(api_key=API_KEY)
        # Forzamos el modelo que te funcionó en el chat
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        return None

model = conectar_ia()

# 3. Interfaz
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR
st.header("🔍 Asistente Técnico IA")
pregunta = st.text_input("Consulta técnica:", placeholder="Ej: Pasos para probar un compresor aterrado")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta and model:
        with st.spinner("🧠 Consultando..."):
            try:
                # Quitamos cualquier filtro para que no bloquee la respuesta
                response = model.generate_content(pregunta)
                st.success("### 🛠️ DIAGNÓSTICO:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error de conexión: {e}")
                st.info("Intenta borrar la app en Streamlit Cloud y crearla de nuevo (Deploy) si el error persiste.")

# CALCULADORAS (Enteros y Eficiencia)
st.divider()
st.subheader("🧮 Eficiencia (Valores Enteros)")
c1, c2 = st.columns(2)

with c1:
    st.write("**Sobrecalentamiento (SH)**")
    ts = st.number_input("Temp Succión (°C)", value=10, step=1, key="ts_v")
    pb = st.number_input("Presión Baja (PSI)", value=118, step=1, key="pb_v")
    # Fórmula: Ts - ((Pb/10) - 7)
    sh = int(round(ts - ((pb / 10) - 7)))
    st.metric("SH", f"{sh} °C")
    if 4 <= sh <= 7: 
        st.success("✅ Eficiente (Ideal: 4-7°C)")
    else: 
        st.warning("⚠️ Fuera de rango")

with c2:
    st.write("**Subenfriamiento (SC)**")
    tl = st.number_input("Temp Líquido (°C)", value=32, step=1, key="tl_v")
    pa = st.number_input("Presión Alta (PSI)", value=320, step=1, key="pa_v")
    # Fórmula: ((Pa/10) + 6) - Tl
    sc = int(round(((pa / 10) + 6) - tl))
    st.metric("SC", f"{sc} °C")
    if 5 <= sc <= 8: 
        st.success("✅ Eficiente (Ideal: 5-8°C)")
    else: 
        st.warning("⚠️ Fuera de rango")
