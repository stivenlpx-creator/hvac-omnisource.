import streamlit as st

# Configuración Pro
st.set_page_config(page_title="HVAC OMNISOURCE ELITE", layout="wide")

# CSS para que se vea como una App nativa y profesional
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: white; }
    .stButton>button {
        height: 4em; font-size: 18px; font-weight: bold;
        background-color: #1f6feb; color: white; border-radius: 10px;
    }
    .stTextInput>div>div>input { font-size: 20px; background-color: #161b22; color: white; }
    .status-box {
        padding: 20px; border-radius: 10px; border-left: 8px solid #238636;
        background-color: #161b22; margin-bottom: 15px;
    }
    </style>
    """, unsafe_content_allowed=True)

st.title("❄️ HVAC OMNISOURCE ELITE v3.0")
st.subheader("Manual Maestro de Diagnóstico y Reparación")

# --- BASE DE DATOS MAESTRA ---
db = {
    "mirage": {
        "e0": "ERROR PARAMETRO EEPROM: La memoria de la placa se desprogramó. Intentar reset (5 min apagado) o cambiar PCB.",
        "e1": "ERROR COMUNICACIÓN: Revisar cable de señal (S). Medir voltaje DC entre S y N (debe oscilar).",
        "e3": "FAN INTERIOR: Motor bloqueado o sensor Hall dañado.",
        "p4": "COMPRESOR: Alta temperatura. Revisar capacitor de ventilador exterior o suciedad extrema."
    },
    "midea": {
        "ec": "DETECCIÓN FUGA: El equipo detectó falta de refrigerante por temperatura de tubería. ¡No recargar sin buscar fuga!",
        "e1": "COMUNICACIÓN: Error de datos entre tarjetas. Revisar cableado y bornes sulfatados.",
        "p0": "PROTECCIÓN IPM: Corto circuito en compresor o falla en el módulo de potencia de la placa."
    },
    "comfort fresh": {
        "e1": "SENSOR AMBIENTE: Sensor de aire abierto o en corto (Medir 10kΩ).",
        "e2": "SENSOR TUBERÍA: Sensor de pozo dañado (Medir 10kΩ o 5kΩ según modelo).",
        "e4": "PROTECCIÓN SISTEMA: Presión anormal o falta de refrigerante."
    }
}

# --- BUSCADOR POR SÍNTOMA ---
st.markdown("### 🔍 Buscador de Soluciones")
query = st.text_input("Escribe el error o síntoma (ej: 'Mirage E1' o 'Fuga')").lower()

if query:
    match = False
    for marca in db:
        if marca in query:
            for cod, sol in db[marca].items():
                if cod in query:
                    st.markdown(f"<div class='status-box'><b>✅ {marca.upper()} - {cod.upper()}:</b><br>{sol}</div>", unsafe_content_allowed=True)
                    match = True
    if not match:
        st.warning("Sin coincidencia exacta. Prueba solo con el código (ej: 'E1').")

# --- SECCIONES DE INGENIERÍA ---
st.markdown("---")
tab1, tab2, tab3 = st.tabs(["📊 TABLA DE SENSORES", "⚡ DIAGRAMAS", "🧪 PRESIONES"])

with tab1:
    st.write("### Valores de Resistencia (kΩ) vs Temperatura")
    st.table({
        "Temp (°C)": ["15°C", "20°C", "25°C", "30°C"],
        "Sensor 5k": ["7.3", "6.0", "5.0", "4.1"],
        "Sensor 10k": ["14.6", "12.0", "10.0", "8.2"],
        "Sensor 15k": ["22.0", "18.1", "15.0", "12.4"]
    })

with tab2:
    st.write("### Identificación de Componentes")
    opcion = st.selectbox("Diagrama:", ["Compresor Monofásico", "Placa Inverter", "Ciclo de Gas"])
    
    if "Monofásico" in opcion:
        st.image("https://images.tcdn.com.br/img/editor/up/632121/Esquema_Eletrico_Ar_Condicionado.jpg")
        st.info("Mide Continuidad: C-R + C-S = R-S. Si no da exacto, bobina abierta.")
    elif "Inverter" in opcion:
        st.write("Puntos de prueba IPM: Mide resistencia entre U-V, V-W, W-U (deben ser idénticas).")

with tab3:
    st.write("### Carga de Gas por Presión (Guía Rápida)")
    st.table({
        "Gas": ["R-22", "R-410A", "R-32"],
        "Succión (PSI)": ["60 - 75", "110 - 130", "120 - 140"],
        "Líquido (PSI)": ["250 - 300", "450 - 500", "480 - 550"]
    })
    
