import streamlit as st
import google.generativeai as genai
import os

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. IA con tu nueva Key (Forzando Conexión v1)
API_KEY = "AIzaSyC0-1YsWu9A_xwMu-UflXzkZrn-IFk9Wf0"

try:
    # Forzamos la configuración limpia
    genai.configure(api_key=API_KEY)
    # Seleccionamos el modelo flash sin prefijos raros
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error de sistema: {e}")

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
                # Intento de llamada simplificada
                response = model.generate_content(pregunta)
                if response.text:
                    st.success("### 🛠️ DIAGNÓSTICO:")
                    st.info(response.text)
            except Exception as e:
                # Este bloque nos dirá la VERDAD de por qué no conecta
                st.error("⚠️ Error de conexión detectado.")
                st.write(f"Código de error Google: {e}")
                st.info("Si el error menciona 'API_KEY_INVALID', la llave se copió mal. Si menciona 'User location', es un bloqueo regional.")

# PESTAÑAS (Calculadoras - Siguen funcionando al 100%)
st.divider()
t1, t2 = st.tabs(["🧮 Cálculos de Eficiencia", "🌡️ Gases"])

with t1:
    st.subheader("Eficiencia (Valores Enteros)")
    c1, c2 = st.columns(2)
    with c1:
        ts = st.number_input("Temp Succión (°C)", value=10, step=1)
        pb = st.number_input("Presión Baja (PSI)", value=118, step=1)
        sh = int(round(ts - ((pb / 10) - 7)))
        st.metric("SH", f"{sh} °C")
        if 4 <= sh <= 7: st.success("✅ Eficiente (Ideal: 4-7°C)")
        else: st.warning("⚠️ Fuera de rango")

    with c2:
        tl = st.number_input("Temp Líquido (°C)", value=32, step=1)
        pa = st.number_input("Presión Alta (PSI)", value=320, step=1)
        sc = int(round(((pa / 10) + 6) - tl))
        st.metric("SC", f"{sc} °C")
        if 5 <= sc <= 8: st.success("✅ Eficiente (Ideal: 5-8°C)")
        else: st.warning("⚠️ Fuera de rango")

with t2:
    st.subheader("Tips de Refrigerantes")
    gas = st.selectbox("Seleccione:", ["R-410A", "R-22", "R-32", "R-134a", "R-404A"])
    if gas == "R-410A": st.info("Carga LÍQUIDO. Succión: 115-145 PSI. Aceite POE.")
