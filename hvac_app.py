import streamlit as st

# Configuración de Consola Profesional
st.set_page_config(page_title="HVAC OMNISOURCE CONSOLE", layout="wide")

# CSS para Interfaz de Alto Contraste y Navegación Lateral
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #e6edf3; }
    .stSidebar { background-color: #161b22; border-right: 2px solid #30363d; }
    .css-1d391kg { background-color: #161b22; } /* Color de la barra lateral */
    .metric-box {
        background-color: #1c2128; padding: 15px; border-radius: 10px;
        border: 1px solid #444c56; margin-bottom: 10px;
    }
    h3 { color: #58a6ff; }
    </style>
    """, unsafe_content_allowed=True)

# --- BARRA LATERAL IZQUIERDA (MANUALES Y NAVEGACIÓN) ---
st.sidebar.title("📁 BIBLIOTECA TÉCNICA")
menu = st.sidebar.radio("SELECCIONE MÓDULO:", 
    ["🔍 Diagnóstico de Fallas", "🔌 Datos de Compresores", "🌀 Motores Ventiladores", "🌡️ Tabla de Sensores", "📋 Reporte de Campo"])

st.sidebar.markdown("---")
st.sidebar.subheader("Manuales por Marca")
marca_manual = st.sidebar.selectbox("Descargar Info:", ["Mirage", "Midea", "Comfort Fresh", "LG", "Samsung", "York"])

# --- ÁREA PRINCIPAL ---
st.title(f"🛠️ MÓDULO: {menu.upper()}")

# 1. DIAGNÓSTICO DE FALLAS (MOTOR DE BÚSQUEDA)
if menu == "🔍 Diagnóstico de Fallas":
    query = st.text_input("Escriba el código de error o síntoma:", placeholder="Ej: Mirage E1, Midea EC...")
    
    db_fallas = {
        "mirage": {"e0": "Error EEPROM. Placa desprogramada.", "e1": "Comunicación. Revisar cable S.", "e5": "Sensor Aire."},
        "midea": {"ec": "Fuga de gas detectada.", "p4": "Protección Compresor Inverter."},
        "comfort fresh": {"e1": "Falla Sensor Aire.", "e4": "Baja presión / Fuga."}
    }
    
    if query:
        for marca, fallas in db_fallas.items():
            if marca in query.lower():
                for cod, sol in fallas.items():
                    if cod
                    
