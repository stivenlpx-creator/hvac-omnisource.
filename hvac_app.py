import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="HVAC PRO", layout="wide")

# Llave de API
API_KEY = "AIzaSyC0-1YsWu9A_xwMu-UflXzkZrn-IFk9Wf0"

# Configuración de la IA
genai.configure(api_key=API_KEY)

st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte OMNISOURCE")

# Buscador
pregunta = st.text_input("Consulta técnica:", placeholder="Ej: Equipo LG no enfría")

if st.button("ANALIZAR CON IA"):
    if pregunta:
        with st.spinner("🧠 Consultando cerebro de IA..."):
            try:
                # CORRECCIÓN: Usar solo el nombre del modelo sin el prefijo 'models/'
                # Esto evita el error 404 en la mayoría de las versiones de la SDK
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                instruccion = f"Como experto en HVAC, analiza este problema: {pregunta}"
                response = model.generate_content(instruccion)
                
                st.success("### DIAGNÓSTICO:")
                st.write(response.text)
            except Exception as e:
                # Si el error persiste, intentamos una variante de nombre
                try:
                    model_alt = genai.GenerativeModel('gemini-pro')
                    response = model_alt.generate_content(pregunta)
                    st.success("### DIAGNÓSTICO (Nodo Alterno):")
                    st.write(response.text)
                except:
                    st.error(f"Error de conexión: {e}")
                    st.info("Recomendación: Actualiza la librería en tu terminal con: pip install -U google-generativeai")
    else:
        st.warning("Por favor, ingresa una consulta.")

# Calculadoras (Enteros)
st.divider()
st.subheader("🧮 Eficiencia (Valores Enteros)")
c1, c2 = st.columns(2)

with c1:
    ts = st.number_input("Temp Succión (°C)", value=10, step=1)
    pb = st.number_input("Presión Baja (PSI)", value=118, step=1)
    sh = int(round(ts - ((pb / 10) - 7)))
    st.metric("SH (Sobrecalentamiento)", f"{sh} °C")
    if 4 <= sh <= 7: 
        st.success("✅ Eficiente")
    else: 
        st.warning("⚠️ Ajustar Carga")

with c2:
    tl = st.number_input("Temp Líquido (°C)", value=32, step=1)
    pa = st.number_input("Presión Alta (PSI)", value=320, step=1)
    sc = int(round(((pa / 10) + 6) - tl))
    st.metric("SC (Subenfriamiento)", f"{sc} °C")
    if 5 <= sc <= 8: 
        st.success("✅ Eficiente")
    else: 
        st.warning("⚠️ Revisar Condensación")
