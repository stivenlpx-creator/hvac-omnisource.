import streamlit as st
import google.generativeai as genai

# 1. Configuración de la Aplicación
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# Estilo CSS para Interfaz Profesional Oscura
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    h1 { color: #00e5ff; text-align: center; font-weight: bold; }
    .stButton > button {
        background-color: #00c853 !important;
        color: white !important;
        height: 3.5em !important;
        width: 100% !important;
        font-size: 20px !important;
        border-radius: 12px !important;
    }
    .stTextInput > div > div > input {
        background-color: #1c1f26;
        color: white;
        border: 2px solid #00e5ff;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_content_allowed=True)

# 2. Configuración de IA
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# --- ENCABEZADO ---
st.markdown("<h1>⚡ HVAC PRO DIAGNOSTIC ❄️</h1>", unsafe_content_allowed=True)
st.write("---")

# --- BUSCADOR CENTRAL ---
col_c1, col_c2, col_c3 = st.columns([1, 3, 1])
with col_c2:
    pregunta = st.text_input("", placeholder="🔍 Describa la falla (Ej: Mirage E1 o Compresor a vacío)...")
    if st.button("INICIAR DIAGNÓSTICO CON IA"):
        if pregunta:
            with st.spinner("🧠 Analizando con IA..."):
                try:
                    prompt = f"Actúa como Ingeniero Senior HVAC. Da pasos numerados y técnicos a: {pregunta}"
                    response = model.generate_content(prompt)
                    st.info(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")

# --- SUB-APARTADOS (Pestañas) ---
st.write("---")
tab1, tab2, tab3, tab4 = st.tabs(["🧮 Calculadoras", "🔌 Diagramas", "🌡️ Tabla P-T", "🛡️ Seguridad"])

with tab1:
    st.subheader("Calculadoras de Ingeniería")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Sobrecalentamiento (Superheat)**")
        t_suc = st.number_input("Temp. Succión (°C)", value=12.0)
        p_baja = st.number_input("Presión Baja (PSI)", value=120.0)
        # Cálculo simplificado R410A
        sh = t_suc - ((p_baja / 10) - 38)
        st.metric("Superheat", f"{sh:.1f} °C")
    with c2:
        st.write("**Subenfriamiento (Subcooling)**")
        t_liq = st.number_input("Temp. Líquido (°C)", value=35.0)
        p_alta = st.number_input("Presión Alta (PSI)", value=320.0)
        sc = ((p_alta / 10) - 1) - t_liq
        st.metric("Subcooling", f"{sc:.1f} °C")

with tab2:
    st.subheader("Diagramas Eléctricos de Control")
    st.write("1. **Sistemas On-Off:** Control por contactor 24V/220V.")
    st.write("2. **Sistemas Inverter:** Comunicación por bus de datos (Señal S).")
    st.info("💡 En Inverter, mide voltaje DC entre N y S; debe oscilar si hay comunicación.")

with tab3:
    st.subheader("Tabla Presión-Temperatura (P-T)")
    st.table({
        "Refrigerante": ["R-410A", "R-22", "R-134a", "R-32"],
        "Baja (PSI) @ 5°C": ["118", "58", "31", "125"],
        "Alta (PSI) @ 45°C": ["375", "240", "168", "390"]
    })

with tab4:
    st.subheader("Buenas Prácticas y Seguridad")
    st.error("1. Nunca presurice con Oxígeno (Explosión). Use Nitrógeno con regulador.")
    st.warning("2. Use EPP: Gafas y guantes al manipular refrigerante líquido.")
    st.write("3. Manejo de R-32: Es ligeramente inflamable (A2L). Evite chispas.")
    
