import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de la IA (CONEXIÓN SEGURA)
# Tu API Key: AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I
try:
    genai.configure(api_key="AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I")
    # Usamos 'gemini-1.5-flash' que es el modelo más compatible actualmente
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error en configuración de IA: {e}")

# 3. Interfaz Principal
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.divider()

# BUSCADOR CENTRAL CON IA
st.header("🔍 Asistente Técnico IA")
pregunta = st.text_input("Describa la falla o consulta:", placeholder="Ej: ¿Por qué el R-410A tiene alta presión de descarga y baja succión?")

if st.button("ANALIZAR CON IA", use_container_width=True):
    if pregunta:
        with st.spinner("🧠 Consultando base de datos de ingeniería..."):
            try:
                # Forzamos una respuesta técnica y estructurada
                prompt_ingenieria = f"Actúa como un Ingeniero Senior de HVAC. Proporciona un diagnóstico técnico paso a paso para el siguiente problema: {pregunta}"
                response = model.generate_content(prompt_ingenieria)
                
                if response.text:
                    st.success("### 🛠️ DIAGNÓSTICO SUGERIDO:")
                    st.markdown(response.text)
                else:
                    st.warning("La IA no devolvió datos. Intenta reformular la pregunta.")
            except Exception as e:
                st.error("⚠️ Error de comunicación con Google. Esto puede deberse a que la API Key aún se está activando o al límite de cuota gratuita.")
                st.info("Prueba preguntando algo más corto para verificar conexión.")

# PESTAÑAS DE HERRAMIENTAS
st.divider()
t1, t2, t3 = st.tabs(["🧮 Calculadoras P/T", "🌡️ Enciclopedia de Refrigerantes", "🛡️ Seguridad"])

with t1:
    st.subheader("Cálculo de Superheat / Subcooling")
    c1, esp, c2 = st.columns([2, 1, 2])
    with c1:
        ts = st.number_input("Temp. Tubería Succión (°C)", value=12.0, key="succion")
        pb = st.number_input("Presión de Baja (PSI) - R410A", value=118.0, key="baja")
        # Fórmula: Temperatura real - Temperatura saturada
        sh = ts - ((pb / 10) - 38)
        st.metric("Sobrecalentamiento (SH)", f"{sh:.1f} °C", delta="Ideal: 4 a 7°C")
    with c2:
        tl = st.number_input("Temp. Tubería Líquido (°C)", value=35.0, key="liquido")
        pa = st.number_input("Presión de Alta (PSI) - R410A", value=320.0, key="alta")
        # Fórmula: Temperatura saturada - Temperatura real
        sc = ((pa / 10) - 1) - tl
        st.metric("Subenfriamiento (SC)", f"{sc:.1f} °C", delta="Ideal: 5 a 8°C")

with t2:
    st.subheader("Guía Técnica de Refrigerantes")
    gas = st.selectbox("Seleccione el gas:", ["R-410A", "R-22", "R-32", "R-134a", "R-404A", "R-407C", "R-600a"])
    
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        if gas == "R-410A":
            st.info("**R-410A (Ecológico):** Mezcla de R-32 y R-125. Alta presión. Cargar solo en líquido.")
            st.write("- **Presión Succión:** 115-145 PSI")
            st.write("- **Presión Descarga:** 350-450 PSI")
        elif gas == "R-22":
            st.warning("**R-22 (HCFC):** En desuso. Carga en gas o líquido. Aceite Mineral.")
            st.write("- **Presión Succión:** 60-75 PSI")
        elif gas == "R-32":
            st.error("**R-32 (HFC):** Inflamable A2L. Muy eficiente. Requiere equipo antichispas.")
            st.write("- **Presión Succión:** 120-155 PSI")
    with col_info2:
        st.write("**Datos de Seguridad:**")
        if gas in ["R-32", "R-600a"]:
            st.error("⚠️ ALTA INFLAMABILIDAD. No soldar sin barrido de nitrógeno.")
        else:
            st.success("Baja toxicidad y no inflamable (A1).")

with t3:
    st.subheader("Protocolos de Seguridad")
    st.write("1. **Nitrógeno Seco:** Siempre use regulador de doble etapa.")
    st.write("2. **Vacío:** Mínimo 500 micrones para asegurar deshidratación.")
    st.write("3. **Sustancias:** Evite el contacto del R-141b con partes plásticas sensibles.")
