import streamlit as st

# 1. Configuración de Pantalla (Sin CSS personalizado para evitar errores)
st.set_page_config(page_title="HVAC OMNISOURCE", layout="wide")

# 2. Barra Lateral de Navegación
st.sidebar.title("📁 BIBLIOTECA TÉCNICA")
opcion = st.sidebar.radio("SELECCIONE MÓDULO:", 
    ["🔍 Diagnóstico de Fallas", "🔌 Datos de Compresores", "🌀 Motores Ventiladores", "🌡️ Tabla de Sensores", "📋 Reporte de Campo"])

# --- ÁREA PRINCIPAL ---
st.title(f"🛠️ {opcion}")

if opcion == "🔍 Diagnóstico de Fallas":
    st.header("Buscador de Códigos")
    busqueda = st.text_input("Escribe Marca y Código (Ej: Mirage E1)").lower()
    
    if "mirage" in busqueda and "e1" in busqueda:
        st.success("✅ MIRAGE E1: Error de comunicación. Revisar cable de señal (S) y voltajes entre N y S.")
    elif "mirage" in busqueda and "e0" in busqueda:
        st.success("✅ MIRAGE E0: Error de EEPROM. Resetear equipo o cambiar tarjeta principal.")
    elif "midea" in busqueda and "ec" in busqueda:
        st.success("✅ MIDEA EC: Fuga de gas detectada. El equipo se protege por baja presión.")
    elif "comfort fresh" in busqueda and "e1" in busqueda:
        st.success("✅ COMFORT FRESH E1: Falla en sensor de aire ambiental (10k).")
    elif busqueda != "":
        st.warning("No hay resultados exactos. Intenta con otra palabra.")

elif opcion == "🔌 Datos de Compresores":
    st.header("⚡ Capacitores y Amperajes")
    st.write("**Tabla de referencia rápida:**")
    st.table({
        "BTU": ["9,000", "12,000", "18,000", "24,000"],
        "Capacitor (uF)": ["25-30", "30-35", "35-45", "50-60"],
        "Amperaje (RLA)": ["4.0 A", "6.0 A", "9.0 A", "12.0 A"]
    })
    st.info("Recordatorio: La bobina de ARRANQUE (S) siempre tiene mayor resistencia que la de MARCHA (R).")

elif opcion == "🌀 Motores Ventiladores":
    st.header("🌀 Diagnóstico de Motores")
    st.write("1. **Motor PSC (3 cables):** Blanco (C), Negro (M), Rojo (A).")
    st.write("2. **Motor PG (5 cables):** Sensor Hall incluido. Si el motor gira un poco y se detiene, el sensor Hall está abierto.")
    st.write("3. **Medición:** Los valores deben estar entre 150 y 500 Ohms.")

elif opcion == "🌡️ Tabla de Sensores":
    st.header("🌡️ Tabla kΩ vs Temperatura")
    st.write("Valores típicos para Mirage, Midea y Comfort Fresh:")
    st.table({
        "Temperatura": ["15°C", "20°C", "25°C", "30°C"],
        "Sensor 10k": ["14.7 kΩ", "12.1 kΩ", "10.0 kΩ", "8.3 kΩ"],
        "Sensor 5k": ["7.3 kΩ", "6.0 kΩ", "5.0 kΩ", "4.1 kΩ"]
    })

elif opcion == "📋 Reporte de Campo":
    st.header("📝 Captura de Datos")
    v = st.number_input("Voltaje medido (V)", 0.0)
    a = st.number_input("Amperaje medido (A)", 0.0)
    if st.button("Guardar Diagnóstico"):
        st.success("Datos analizados. Si el amperaje es mayor al RLA, revisa el capacitor.")
        
