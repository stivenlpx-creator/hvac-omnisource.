import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="HVAC PRO", layout="wide")

# Llave de API (Recuerda protegerla después con st.secrets)
API_KEY = "AIzaSyC0-1YsWu9A_xwMu-UflXzkZrn-IFk9Wf0"

# Configuración global de la IA
genai.configure(api_key=API_KEY)

st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte OMNISOURCE")

# Buscador
pregunta = st.text_input("Consulta técnica:", placeholder="Ej: Equipo LG no enfría")

if st.button("ANALIZAR CON IA"):
    if pregunta:
        with st.spinner("🧠 Consultando cerebro de IA..."):
            try:
                # Se utiliza gemini-1.5-flash por ser más estable y rápido
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Opcional: Puedes agregar un "prompt" de sistema para que sea más técnico
                prompt_ingeniero = f"Actúa como un experto en refrigeración y HVAC. Responde a lo siguiente: {pregunta}"
                
                response = model.generate_content(prompt_ingeniero)
                
                st.success("### DIAGNÓSTICO:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error detectado: {e}")
                st.info("Sugerencia: Verifica que tu API Key esté activa y que la librería 'google-generativeai' esté actualizada.")
    else:
        st.warning("Por favor, ingresa una consulta.")

# Calculadoras (Enteros)
st.divider()
st.subheader("🧮 Eficiencia (Valores Enteros)")
c1, c2 = st.columns(2)

with c1:
    ts = st.number_input("Temp Succión (°C)", value=10, step=1)
    pb = st.number_input("Presión Baja (PSI)", value=118, step=1)
    # Cálculo de Superheat (SH) simplificado
    # Nota: Esta es una fórmula aproximada para R410A
    sh = int(round(ts - ((pb / 10) - 7)))
    st.metric("SH (Sobrecalentamiento)", f"{sh} °C")
    if 4 <= sh <= 7: 
        st.success("✅ Eficiente")
    else: 
        st.warning("⚠️ Ajustar Carga")

with c2:
    tl = st.number_input("Temp Líquido (°C)", value=32, step=1)
    pa = st.number_input("Presión Alta (PSI)", value=320, step=1)
    # Cálculo de Subcooling (SC) simplificado
    sc = int(round(((pa / 10) + 6) - tl))
    st.metric("SC (Subenfriamiento)", f"{sc} °C")
    if 5 <= sc <= 8: 
        st.success("✅ Eficiente")
    else: 
        st.warning("⚠️ Revisar Condensación")
