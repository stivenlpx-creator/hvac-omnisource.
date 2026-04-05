import streamlit as st

# 1. Configuración de Pantalla
st.set_page_config(page_title="HVAC OMNISOURCE", layout="wide")

# --- BARRA LATERAL (BIBLIOTECA) ---
st.sidebar.title("📁 BIBLIOTECA TÉCNICA")
modulo = st.sidebar.radio("IR A:", 
    ["🔍 BUSCADOR DE FALLAS", "🔌 DATOS COMPRESORES", "🌀 MOTORES Y VENTILACIÓN", "🌡️ TABLA DE SENSORES"])

st.sidebar.markdown("---")
st.sidebar.write("**Capacitores Sugeridos:**")
st.sidebar.code("12k BTU: 35uF\n18k BTU: 45uF\n24k BTU: 60uF")

# --- ÁREA PRINCIPAL ---

if modulo == "🔍 BUSCADOR DE FALLAS":
    st.title("🔍 Asistente de Diagnóstico")
    st.write("Escribe la falla, el código o la marca para obtener el paso a paso.")
    
    # BARRA DE BÚSQUEDA INTELIGENTE
    busqueda = st.text_input("¿Qué problema tiene el equipo?", placeholder="Ej: Mirage E1, Midea fuga, Comfort Fresh sensor...")

    if busqueda:
        query = busqueda.lower()
        
        # LÓGICA DE RESPUESTAS PASO A PASO
        if "mirage" in query and "e1" in query:
            st.info("### 🛠️ PASO A PASO: MIRAGE E1 (Comunicación)")
            st.write("1. **Corte Energía:** Apague el equipo 5 minutos para resetear memoria.")
            st.write("2. **Verifique Cableado:** Revise que el cable de señal (S) no tenga empalmes.")
            st.write("3. **Prueba de Voltaje:** Mida voltaje DC entre N y S. Debe oscilar entre 15V y 70V.")
            st.write("4. **Veredicto:** Si el voltaje es fijo (0V o 80V), una de las tarjetas está dañada.")

        elif "midea" in query and "ec" in query:
            st.info("### 🛠️ PASO A PASO: MIDEA EC (Fuga de Gas)")
            st.write("1. **Carga Térmica:** Verifique si el equipo enfría algo o nada.")
            st.write("2. **Inspección:** Busque manchas de aceite en las tuercas de la unidad exterior.")
            st.write("3. **Presurización:** Recupere el gas restante y meta 350 PSI de Nitrógeno.")
            st.write("4. **Corrección:** Suelde la fuga, haga vacío profundo y cargue por peso.")

        elif "sensor" in query or "e1" in query or "e2" in query:
            st.info("### 🛠️ PASO A PASO: FALLA DE SENSORES")
            st.write("1. **Desconecte:** Retire el sensor de la placa electrónica.")
            st.write("2. **Mida Resistencia:** Use el multímetro en escala de kΩ.")
            st.write("3. **Compare:** Revise la tabla de sensores (en el menú lateral) según la temperatura.")
            st.write("4. **Sustituya:** Si el valor es 0 (corto) o infinito (abierto), cambie el sensor.")

        else:
            st.warning("⚠️ No encontré esa falla específica. Intenta escribir 'Marca + Código' (ej: Mirage E1).")

elif modulo == "🔌 DATOS COMPRESORES":
    st.title("🔌 Datos de Compresores y Bobinas")
    st.subheader("Identificación de Bornes (C, R, S)")
    st.write("Para identificar las bobinas si los cables están sueltos:")
    st.write("1. **Mida los 3 bornes:** Encontrará 3 lecturas diferentes.")
    st.write("2. **Lectura Mayor:** Es la suma de Marcha y Arranque (R + S).")
    st.write("3. **Lectura Menor:** Es la bobina de Marcha (C a R).")
    st.write("4. **Lectura Media:** Es la bobina de Arranque (C a S).")
    st.image("https://iaq.com.au/wp-content/uploads/2019/04/Compressor-Terminals.jpg", caption="Identificación de terminales de compresor")

elif modulo == "🌡️ TABLA DE SENSORES":
    st.title("🌡️ Tabla de Valores de Sensores")
    st.write("Valores de resistencia a temperatura ambiente:")
    tabla_data = {
        "Temp. Ambiente": ["15°C", "20°C", "25°C", "30°C"],
        "Sensor 10kΩ": ["14.7 kΩ", "12.1 kΩ", "10.0 kΩ", "8.3 kΩ"],
        "Sensor 5kΩ": ["7.3 kΩ", "6.0 kΩ", "5.0 kΩ", "4.1 kΩ"]
    }
    st.table(tabla_data)
    
