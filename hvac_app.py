import streamlit as st

# 1. Configuración de Pantalla
st.set_page_config(page_title="HVAC OMNISOURCE", layout="wide")

# 2. Encabezado (Logo HVAC)
st.markdown("<h1 style='text-align: center;'>❄️ HVAC MASTER 🛠️</h1>", unsafe_content_allowed=True)
st.markdown("<p style='text-align: center;'>Soporte Técnico Mirage, Midea, Comfort Fresh</p>", unsafe_content_allowed=True)

# 3. Motor de Búsqueda
st.write("---")
busqueda = st.text_input("¿Qué falla presenta el equipo?", placeholder="Ej: Mirage E1, Midea EC, Falla Compresor...")

# Botón de Búsqueda (Verde)
if st.button("🟢 INICIAR DIAGNÓSTICO"):
    if busqueda:
        q = busqueda.lower()
        
        # --- Lógica de Diagnóstico Paso a Paso ---

        # FALLAS MIRAGE
        if "mirage" in q and "e1" in q:
            st.info("### ✅ PASO A PASO: MIRAGE E1 (Comunicación)")
            st.write("1. **Reset:** Apague el equipo desde el breaker por 5 minutos.")
            st.write("2. **Cables:** Revise que el cable de señal 'S' esté bien apretado en ambas borneras.")
            st.write("3. **Voltaje:** Mida voltaje DC entre N y S. Debe variar entre 15V y 70V DC.")
            st.write("4. **Veredicto:** Si el voltaje es fijo (0V u 80V), una tarjeta electrónica está dañada.")

        elif "mirage" in q and "e0" in q:
            st.error("### ✅ PASO A PASO: MIRAGE E0 (Error EEPROM)")
            st.write("1. **Definición:** La memoria de la placa principal se desprogramó.")
            st.write("2. **Acción:** Verifique si el voltaje de entrada es inestable.")
            st.write("3. **Solución:** Reemplace la tarjeta del evaporador.")

        # FALLAS MIDEA
        elif "midea" in q and "ec" in q:
            st.warning("### ✅ PASO A PASO: MIDEA EC (Fuga Detectada)")
            st.write("1. **Sensor:** El sensor de tubería detectó falta de gas.")
            st.write("2. **Revisión:** Busque manchas de aceite en las tuercas (flare).")
            st.write("3. **Prueba:** Presurice con nitrógeno a 350 PSI para buscar el poro.")
            st.write("4. **Carga:** Haga vacío profundo y cargue gas por peso.")

        # FALLAS COMFORT FRESH
        elif "comfort" in q and ("e1" in q or "sensor" in q):
            st.info("### ✅ PASO A PASO: COMFORT FRESH E1 (Sensor Aire)")
            st.write("1. **Prueba:** Desconecte el sensor y mídalo con multímetro.")
            st.write("2. **Valor:** Debe dar 10k ohms a una temperatura de 25°C.")
            st.write("3. **Acción:** Si marca 0 o infinito, cámbielo por uno nuevo.")

        # FALLAS DE COMPRESOR
        elif "compresor" in q:
            st.info("### ✅ DIAGNÓSTICO: FALLA DE COMPRESOR")
            st.write("1. **Capacitor:** Verifique si el capacitor de marcha está en rango.")
            st.write("2. **Bobinas:** Mida continuidad entre C-R, C-S y R-S.")
            st.write("3. **Inverter:** Si es Inverter, mida impedancia entre las fases U-V-W (deben ser iguales).")

        else:
            st.warning("⚠️ No encontré la falla exacta. Escriba 'Marca + Código' (ej: Mirage E1).")
    else:
        st.error("Escriba la falla en el cuadro arriba antes de presionar el botón.")

# 4. Tabla Técnica Fija
st.write("---")
with st.expander("📊 TABLA DE REFERENCIA SENSORES (kΩ)"):
    st.table({
        "Temp": ["15°C", "20°C", "25°C", "30°C"],
        "10kΩ": ["14.7", "12.1", "10.0", "8.3"],
        "5kΩ": ["7.3", "6.1", "5.0", "4.1"]
    })
    
