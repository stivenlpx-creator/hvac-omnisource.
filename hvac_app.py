import streamlit as st

# 1. Titulo y Logo
st.title("❄️ HVAC MASTER PRO")
st.write("Soporte Técnico: Mirage, Midea, Comfort Fresh")

# 2. Barra de Búsqueda
st.write("---")
busqueda = st.text_input("Escriba la marca y el código (Ej: Mirage E1)")

# 3. Botón de Búsqueda
if st.button("BUSCAR DIAGNÓSTICO"):
    q = busqueda.lower()
    
    if "mirage" in q and "e1" in q:
        st.info("✅ MIRAGE E1: FALLA DE COMUNICACIÓN")
        st.write("1. Apagar el equipo 5 minutos.")
        st.write("2. Revisar que el cable de señal 'S' esté firme.")
        st.write("3. Medir voltaje DC entre N y S (debe oscilar 15-70V).")
        st.write("4. Si el voltaje es fijo (0V o 80V), una tarjeta está dañada.")
        
    elif "mirage" in q and "e0" in q:
        st.error("✅ MIRAGE E0: ERROR DE EEPROM")
        st.write("1. La placa perdió su programación.")
        st.write("2. Revisar que el voltaje de entrada sea estable.")
        st.write("3. Si persiste, se debe cambiar la tarjeta del evaporador.")

    elif "midea" in q and "ec" in query:
        st.warning("✅ MIDEA EC: FUGA DE GAS")
        st.write("1. El sensor detectó falta de refrigerante.")
        st.write("2. Buscar manchas de aceite en las conexiones.")
        st.write("3. Presurizar con nitrógeno a 350 PSI.")
        st.write("4. Hacer vacío y cargar gas por peso.")

    elif "comfort" in q and "e1" in q:
        st.info("✅ COMFORT FRESH E1: SENSOR DE AIRE")
        st.write("1. Desconectar el sensor de la placa.")
        st.write("2. Medir con multímetro (debe dar 10k ohms a 25°C).")
        st.write("3. Si marca 0 o infinito, reemplazar el sensor.")

    elif "compresor" in q:
        st.info("✅ FALLA DE COMPRESOR")
        st.write("1. Revisar si el capacitor está inflado.")
        st.write("2. Medir continuidad en las 3 terminales (C, R, S).")
        st.write("3. Verificar que el protector térmico no esté abierto.")

    else:
        st.warning("No se encontró el código. Intente con: Mirage E1")

# 4. Tabla de Sensores
st.write("---")
st.write("**TABLA DE SENSORES (kΩ):**")
st.table({
    "Temp": ["20°C", "25°C", "30°C"],
    "10kΩ": ["12.1", "10.0", "8.3"],
    "5kΩ": ["6.0", "5.0", "4.1"]
})
