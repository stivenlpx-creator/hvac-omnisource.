import streamlit as st

# Configuración de Consola Profesional
st.set_page_config(page_title="HVAC OMNISOURCE CONSOLE", layout="wide")

# Estilo de interfaz industrial
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #e6edf3; }
    .stSidebar { background-color: #161b22; border-right: 2px solid #30363d; }
    h3 { color: #58a6ff; }
    .metric-card {
        background-color: #1c2128; padding: 15px; border-radius: 10px;
        border: 1px solid #444c56; margin-bottom: 10px;
    }
    </style>
    """, unsafe_content_allowed=True)

# --- BARRA LATERAL IZQUIERDA ---
st.sidebar.title("📁 BIBLIOTECA TÉCNICA")
menu = st.sidebar.radio("SELECCIONE MÓDULO:", 
    ["🔍 Diagnóstico de Fallas", "🔌 Datos de Compresores", "🌀 Motores Ventiladores", "🌡️ Tabla de Sensores", "📋 Reporte de Campo"])

st.sidebar.markdown("---")
st.sidebar.subheader("Manuales por Marca")
marca_manual = st.sidebar.selectbox("Info Rápida:", ["Mirage", "Midea", "Comfort Fresh", "LG", "Samsung"])

# --- ÁREA PRINCIPAL ---
st.title(f"🛠️ {menu.upper()}")

# 1. DIAGNÓSTICO DE FALLAS
if menu == "🔍 Diagnóstico de Fallas":
    st.write("Escriba el código de error o el síntoma para obtener el paso a paso.")
    query = st.text_input("Consulta técnica:", placeholder="Ej: Mirage E1, Midea EC...")
    
    db_fallas = {
        "mirage": {
            "e0": "1. Error EEPROM. \n2. Desenergizar 5 min. \n3. Si persiste, cambiar placa.",
            "e1": "1. Error Comunicación. \n2. Medir señal en borne S. \n3. Revisar neutro.",
            "e5": "1. Sensor de Aire (10k). \n2. Revisar resistencia."
        },
        "midea": {
            "ec": "1. Detección de Fuga. \n2. Verificar presión de gas. \n3. Buscar fuga en soldaduras.",
            "p4": "1. Protección Compresor Inverter. \n2. Revisar IPM."
        },
        "comfort fresh": {
            "e1": "1. Sensor de ambiente defectuoso. \n2. Medir 10k o 5k.",
            "e4": "1. Protección por baja presión o falta de refrigerante."
        }
    }
    
    if query:
        encontrado = False
        query_l = query.lower()
        for marca in db_fallas:
            if marca in query_l:
                for cod in db_fallas[marca]:
                    if cod in query_l:
                        st.info(f"### ✅ {marca.upper()} - {cod.upper()}\n{db_fallas[marca][cod]}")
                        encontrado = True
        if not encontrado:
            st.warning("No se encontró una coincidencia exacta. Pruebe con 'Marca + Código'.")

# 2. DATOS DE COMPRESORES
elif menu == "🔌 Datos de Compresores":
    st.markdown("### ⚡ Capacitores y Amperajes Sugeridos")
    st.table({
        "BTU": ["9k", "12k", "18k", "24k", "36k"],
        "Capacitor (µF)": ["25-30", "30-35", "35-45", "50-60", "70-80"],
        "Amperaje (RLA)": ["3.8A", "5.5A", "8.5A", "11.5A", "16.5A"]
    })
    st.info("**Bobinas:** Mida R-S (Suma total), C-R (Marcha), C-S (Arranque).")

# 3. MOTORES VENTILADORES
elif menu == "🌀 Motores Ventiladores":
    st.markdown("###
                
