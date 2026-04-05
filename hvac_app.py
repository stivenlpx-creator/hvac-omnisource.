import streamlit as st
import google.generativeai as genai

# 1. Configuración de la Aplicación
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# Estilo CSS Avanzado para Interfaz Profesional
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #00e5ff; text-align: center; font-weight: bold; margin-bottom: 0px; }
    .stButton > button {
        background-color: #00c853 !important;
        color: white !important;
        height: 4em !important;
        width: 100% !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(0, 200, 83, 0.3);
    }
    .stTextInput > div > div > input {
        background-color: #1c1f26;
        color: white;
        border: 2px solid #00e5ff;
        border-radius: 12px;
        font-size: 18px;
        text-align: center;
    }
    .css-1kyx603 { border-radius: 15px; background-color: #1c1f26; padding: 20px; }
    </style>
    """, unsafe_content_allowed=True)

# 2. Configuración de IA
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# --- ENCABEZADO ---
st.markdown("<h1>⚡ HVAC PRO DIAGNOSTIC ❄️</h1>", unsafe_content_allowed=True)
st.markdown("<p style='text-align: center; color: #808495;'>Console de Ingeniería y Soporte con IA v3.0</p>", unsafe_content_allowed=True)

# --- SECCIÓN 1: BUSCADOR IA CENTRAL ---
st.write("---")
col_c1, col_c2, col_c3 = st.columns([1, 3, 1])
with col_c2:
    pregunta = st.text_input("", placeholder="🔍 Describa la falla o consulte un procedimiento...", key="main_search")
    btn_buscar = st.button("INICIAR DIAGNÓSTICO CON IA")

if btn_buscar and pregunta:
    with st.status("🧠 IA Analizando parámetros de ingeniería...", expanded=True) as status:
        try:
            prompt = f"Eres un Ingeniero HVAC Senior. Responde con pasos numerados y datos técnicos precisos a: {pregunta}"
            response = model.generate_content(prompt)
            st.info(response.text)
            status.update(label="✅ Análisis de IA Completado", state="complete")
        except Exception as e:
            st.error(f"Error: {e}")

# --- SECCIÓN 2: BIBLIOTECA DE HERRAMIENTAS (SUB-APARTADOS) ---
st.write("---")
tab_calc, tab_pt, tab_elec, tab_seg = st.tabs([
    "🧮 Calculadoras", "🌡️ Tabla P-T", "🔌 Diagramas Eléctricos", "🛡️ Seguridad y Química"
])

# --- SUB-APARTADO: CALCULADORAS ---
with tab_calc:
    col_sc, col_sh = st.columns(2)
    with col_sc:
        st.subheader("Subenfriamiento (Subcooling)")
        t_liq = st.number_input("Temp. Salida Condensador (°C)", value=35.0)
        p_alta = st.number_input("Presión de Alta (PSI) - R410A", value=320.0)
        # Temp saturada simple para R410A
        t_sat_alta = (p_alta / 10) - 1  # Estimación rápida
        sc = t_sat_alta - t_liq
        st.metric("Subcooling", f"{sc:.1f} °C", delta="Ideal: 5-8°C")
        
    with col_sh:
        st.subheader("Sobrecalentamiento (Superheat)")
        t_suc = st.number_input("Temp. Tubería Succión (°C)", value=12.0)
        p_baja = st.number_input("Presión de Baja (PSI) - R410A", value=120.0)
        t_sat_baja = (p_baja / 10) - 38 # Estimación rápida
        sh = t_suc - t_sat_baja
        st.metric("Superheat", f"{sh:.1f} °C", delta="Ideal: 4-7°C")

    st.write("---")
    st.subheader("🏠 Cálculo Térmico Rápido (BTU)")
    c1, c2, c3 = st.columns(3)
    largo = c1.number_input("Largo (m)", 1.0)
    ancho = c2.number_input("Ancho (m)", 1.0)
    personas = c3.number_input("Personas", 1)
    btu_total = (largo * ancho * 600) + (personas * 500)
    st.success(f"Carga Térmica Estimada: **{btu_total:,.0f} BTU/h**")

# --- SUB-APARTADO: TABLA P-T ---
with tab_pt:
    st.subheader("Relación Presión - Temperatura (Todos los Refrigerantes)")
    refrig = st.selectbox("Seleccione Refrigerante:", ["R-410A", "R-22", "R-32", "R-134a", "R-404A"])
    st.table({
        "Temp. Sat (°C)": ["-10", "0", "5", "10", "40", "45", "50"],
        f"Presión {refrig} (PSI)": [
            "81 / 43" if refrig=="R-410A" else "33 / 11",
            "101 / 57" if refrig=="R-410A" else "49 / 24",
            "118 / 68" if refrig=="R-410A" else "58 / 31",
            "138 / 81" if refrig=="R-410A" else "69 / 39",
            "334 / 210" if refrig=="R-410A" else "211 / 147",
            "375 / 239" if refrig=="R-410A" else "240 / 168",
            "420 / 270" if refrig=="R-410A" else "272 / 191"
        ]
    })

# --- SUB-APARTADO: DIAGRAMAS ELÉCTRICOS ---
with tab_elec:
    st.subheader("Esquemas de Control y Potencia")
    diag_tipo = st.radio("Nivel de Sistema:", ["Básico (On-Off)", "Complejo (Inverter/Centrales)"])
    if diag_tipo == "Básico (On-Off)":
        st.write("**Diagrama Típico:** Termostato (R, Y, G, W, C) -> Contactor -> Compresor.")
        st.info("💡 Mida continuidad en bobina de contactor (24V o 220V) antes de reemplazar.")
    else:
        st.write("**Diagrama Inverter:** Filtro EMI -> Rectificador -> IPM -> Compresor DC.")
        st.warning("⚠️ Nunca mida voltaje directo en las fases U-V-W con el compresor conectado si no tiene multímetro de alta frecuencia.")

# --- SUB-APARTADO: SEGURIDAD ---
with tab_seg:
    st.subheader("🛡️ Buenas Prácticas y Manejo Químico")
    st.write("1. **Gases Refrigerantes:** Nunca mezcle refrigerantes. El R-32 es A2L (Ligeramente inflamable).")
    st.write("2. **Nitrógeno:** Use siempre regulador de presión. Nunca presurice con Oxígeno (Riesgo de Explosión).")
    st.write("3. **Sustancias Químicas:** El 141b está siendo descontinuado; use agentes de limpieza biodegradables.")
    st.error("⚠️ Uso de EPP obligatorio: Guantes criogénicos y gafas de seguridad al manipular líquido.")
    
