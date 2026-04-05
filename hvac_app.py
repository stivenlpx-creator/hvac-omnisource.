import streamlit as st

# 1. Configuración de Pantalla
st.set_page_config(page_title="HVAC OMNISOURCE PRO", layout="wide")

# Cabecera Simple con Logo
st.markdown("<h1 style='text-align: center;'>❄️ HVAC MASTER 🛠️</h1>", unsafe_content_allowed=True)

# 2. MOTOR DE BÚSQUEDA
st.write("---")
busqueda = st.text_input("Ingrese Marca y Código (Ej: Mirage E1, Midea EC):", placeholder="Escriba aquí...")

# Botón de búsqueda (Sin CSS complejo para evitar errores)
if st.button("✅ INICIAR DIAGNÓSTICO"):
    if busqueda:
        query = busqueda.lower()
        
        # --- BASE DE DATOS DE FALLAS ---
        
        # MIRAGE
        if "mirage" in query:
            if "e1" in query or "comunicacion" in query:
                st.info("### 🛠️ PASO A PASO: MIRAGE E1 (Comunicación)")
                st.write("1. **Reset:** Apagar breaker 5 minutos.")
                st.write("2. **Cableado:** Revisar continuidad en cable de señal 'S'.")
                st.write("3. **Voltaje:** Medir DC entre N y S (debe oscilar 15-70V).")
                st.write("4. **Placa:** Si el voltaje es fijo 0V o 80V, una tarjeta falló.")
            elif "e0" in query or "eeprom" in query:
                st.error("### 🛠️ PASO A PASO: MIRAGE E0 (EEPROM)")
                st.write("1. **Causa:** Desprogramación de memoria interna.")
                st.write("2. **Acción:** Revisar voltajes de entrada estables.")
                st.write("3. **Solución:** Reemplazar tarjeta del evaporador.")

        # MIDEA
        elif "midea" in query:
            if "ec" in query or "fuga" in query:
                st.warning("### 🛠️ PASO A PASO: MIDEA EC (Fuga Detectada)")
                st.write("1. **Carga:** Verificar si hay rastro de aceite en tuercas.")
                st.write("2. **Presión:** Si es R410A y marca menos de 100 PSI, falta gas.")
                st.write("3. **Prueba:** Presurizar con nitrógeno a 350 PSI.")
                st.write("4. **Carga:** Hacer vacío de 500 micrones y cargar por peso.")
            elif "el" in query:
                st.write("### 🛠️ PASO A PASO: MIDEA EL (Falla Sensor)")
                st.write("1. **Medición:** Revisar sensor de aire (10k).")

        # COMFORT FRESH
        elif "comfort" in query:
            if "e1" in query or "sensor" in query:
                st.info("### 🛠️ PASO A PASO: COMFORT FRESH E1 (Sensor Aire)")
                st.write("1. **Prueba:** Medir resistencia del sensor (10k a 25°C).")
                st.write("2. **Placa:** Limpiar terminales con limpia-contactos.")

        # FALLAS COMUNES DE COMPRESORES
        elif "
        
