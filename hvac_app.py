import streamlit as st

# 1. Configuración de Pantalla
st.set_page_config(page_title="HVAC OMNISOURCE", layout="wide")

# 2. Estilo Visual
st.markdown("""
    <style>
    .main { background-color: #0b1016; color: white; }
    .stSidebar { background-color: #161b22; }
    .stAlert { background-color: #1c2128; border-radius: 10px; }
    </style>
    """, unsafe_content_allowed=True)

# --- BARRA LATERAL (MENÚ) ---
st.sidebar.title("📁 MENÚ TÉCNICO")
opcion = st.sidebar.selectbox("Seleccione Módulo:", 
    ["🔍 Diagnóstico de Fallas", "🔌 Datos de Compresores", "🌀 Motores Ventiladores", "🌡️ Tabla de Sensores", "📋 Reporte de Campo"])

st.sidebar.markdown("---")
st.sidebar.info("Marcas Soportadas: Mirage, Midea, Comfort Fresh, Samsung, LG.")

# --- CUERPO PRINCIPAL ---
st.title(f"🛠️ {opcion.upper()}")

if opcion == "🔍 Diagnóstico de Fallas":
    st.write("Escriba la marca y el código (Ej: Mirage E1)")
    busqueda = st.text_input("Consulta:").lower()
    
    # Lógica simplificada de búsqueda
    if "mirage" in busqueda and "e1" in busqueda:
        st.info("✅ MIRAGE E1: Error de comunicación. Revisar cable de señal (S) y voltajes entre N y S.")
    elif "mirage" in busqueda and "e0" in busqueda:
        st.info("✅ MIRAGE E0: Error de EEPROM. Resetear equipo o cambiar tarjeta principal.")
    elif "midea" in busqueda and "ec" in busqueda:
        st.info("✅ MIDEA EC: Fuga de gas detectada. El equipo se protege por baja presión.")
    elif "comfort fresh" in busqueda and "e1" in busqueda:
        st.info("✅ COMFORT FRESH E1: Falla en sensor de aire ambiental (10k).")
    elif busqueda == "":
        st.write("Esperando consulta...")
    else:
        st.warning("No hay coincidencia exacta. Intente: 'Marca + Código'.")

elif opcion == "🔌 Datos de Compresores":
    st.markdown("### ⚡ Capacitores y Bobinas")
    st.table({
        "Capacidad BTU": ["9,000", "12,000", "18,000", "24,000"],
        "Capacitor uF": ["25-30", "30-35", "35-45", "50-60"],
        "Amperaje RLA": ["4.0 A", "6.0 A", "9.0 A", "12.0 A"]
    })
    st.info("Identificación: C (Común), R (Marcha), S (Arranque). Resistencia R a S es la más alta.")

elif opcion == "🌀 Motores Ventiladores":
    st.write("### Diagnóstico de Motores PG y PSC")
    st.write("1. **Motor PSC:** 3 cables. Mida resistencia entre bobinas.")
    st.write("2. **Motor PG:** 5-6 cables. Incluye sensor Hall (Rojo, Negro, Blanco).")
    st.info("Si el motor gira y se detiene marcando error, el sensor Hall está dañado.")

elif opcion == "🌡️ Tabla de Sensores":
    st.write("### Tabla de Resistencia (kΩ) a 25°C")
    st.table({
        "Marca": ["Mirage / Midea", "LG / Samsung", "York / Carrier"],
        "Sensor Aire": ["10 kΩ", "10 kΩ", "5 kΩ / 10 kΩ"],
        "Sensor Pozo": ["10 kΩ", "5 kΩ", "10 kΩ"]
    })

elif opcion == "📋 Reporte de Campo":
    st.write("### 📝 Datos Tomados")
    v = st.number_input("Voltaje (V)", 0.0)
    a = st.number_input("Amperaje (A)", 0.0)
    if st.button("Analizar"):
        st.success("Datos registrados correctamente.")
        
