import streamlit as st

# 1. Configuración de Pantalla
st.set_page_config(page_title="HVAC OMNISOURCE PRO", layout="wide")

# 2. Encabezado
st.title("❄️ HVAC MASTER PRO - SOPORTE TÉCNICO")
st.write("Manual de Campo: Mirage, Midea, Comfort Fresh y Genéricos")

# 3. Motor de Búsqueda Inteligente
st.write("---")
busqueda = st.text_input("¿Qué falla o código presenta el equipo?", placeholder="Ej: Mirage E1, Midea EC, Falla Compresor...")

if st.button("🔍 INICIAR DIAGNÓSTICO"):
    if busqueda:
        q = busqueda.lower()
        
        # --- SECCIÓN MIRAGE ---
        if "mirage" in q:
            if "e1" in q or "comunicacion" in q:
                st.info("### ✅ MIRAGE E1: ERROR DE COMUNICACIÓN")
                st.write("1. **Voltaje N-S:** Mide voltaje DC entre Neutro y Señal. Debe oscilar entre 20V y 70V DC.")
                st.write("2. **Cableado:** Verifica que el cable de señal sea calibre 14 o 16 AWG, sin empalmes ni humedad.")
                st.write("3. **Prueba de Tarjeta:** Si el voltaje es fijo (0V o 80V), la tarjeta emisora (Evaporador) está dañada.")
            elif "e0" in q or "eeprom" in q:
                st.error("### ✅ MIRAGE E0: ERROR DE EEPROM")
                st.write("1. **Causa:** Desprogramación del chip de memoria en la placa.")
                st.write("2. **Acción:** Apagar breaker 10 min. Si no borra, reemplazar tarjeta de evaporador.")
            elif "e3" in q or "ventilador" in q:
                st.warning("### ✅ MIRAGE E3: FALLA MOTOR EVAPORADOR")
                st.write("1. **Giro:** Verifica si el rodamiento está pegado.")
                st.write("2. **Sensor Hall:** Revisa el conector pequeño de 3 cables en la placa.")

        # --- SECCIÓN MIDEA ---
        elif "midea" in q:
            if "ec" in q or "fuga" in q:
                st.error("### ✅ MIDEA EC: DETECCIÓN DE FUGA")
                st.write("1. **Lógica:** El equipo detecta que el serpentín no enfría tras 10 min de marcha.")
                st.write("2. **Aceite:** Busca manchas en las tuercas (flare) de la unidad exterior.")
                st.write("3. **Presión:** R-410A debe estar entre 110-130 PSI. Si está bajo 80 PSI, busca el poro.")
            elif "p4" in q or "ipm" in q:
                st.error("### ✅ MIDEA P4: FALLA MÓDULO IPM")
                st.write("1. **Compresor:** Mide que las 3 bornas no estén aterrizadas a tierra.")
                st.write("2. **Pasta Térmica:** Revisa si el disipador de la placa exterior está seco.")

        # --- SECCIÓN COMFORT FRESH ---
        elif "comfort" in q:
            if "e1" in q or "sensor" in q:
                st.info("### ✅ COMFORT FRESH E1: SENSOR DE AIRE")
                st.write("1. **Valor:** Sensor de 10kΩ. Medir resistencia desconectado.")
                st.write("2. **Tabla:** A 25°C debe dar 10k. A 30°C debe dar 8k aprox.")
            elif "e4" in q:
                st.warning("### ✅ COMFORT FRESH E4: PROTECCIÓN DE SISTEMA")
                st.write("1. **Causa:** Presión anormal o falta de gas. Revisar capacitor de ventilador exterior.")

        # --- FALLAS DE COMPRESOR Y ELÉCTRICA ---
        elif "compresor" in q or "capacitor" in q:
            st.info("### ✅ DIAGNÓSTICO DE ARRANQUE")
            st.write("1. **Capacitor:** Si el compresor zumba y no arranca, cambia el capacitor.")
            st.write("2. **Relación Bobinas:** C a R (Baja), C a S (Media), R a S (Suma de ambas).")
            st.write("3. **Amperaje:** Si el RLA supera el valor de placa, el compresor está sufriendo mecánicamente.")

        else:
            st.warning("⚠️ No encontré esa falla exacta. Intenta buscar por código (ej: E1, EC, E0).")

# --- TABLAS TÉCNICAS (SIEMPRE VISIBLES) ---
st.write("---")
st.subheader("📊 INFORMACIÓN TÉCNICA DE REFERENCIA")
col1, col2 = st.columns(2)

with col1:
    st.write("**Resistencia de Sensores (kΩ)**")
    st.table({
        "Temperatura": ["20°C", "25°C", "30°C"],
        "Sensor 10k": ["12.1", "10.0", "8.3"],
        "Sensor 5k": ["6.1", "5.0", "4.1"]
    })

with col2:
    st.write("**Presiones de Trabajo (PSI)**")
    st.table({
        "Gas": ["R-22", "R-410A", "R-32"],
        "Succión (Baja)": ["65", "120", "130"],
        "Descarga (Alta)": ["250", "450", "480"]
    })
    
