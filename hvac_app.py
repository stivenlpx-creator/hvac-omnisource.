import streamlit as st

# 1. Configuración de Pantalla (Limpia para evitar errores)
st.set_page_config(page_title="HVAC OMNISOURCE", layout="wide")

# 2. Título de la Aplicación
st.title("❄️ HVAC MASTER: ENCICLOPEDIA TÉCNICA")
st.write("Guía Maestra de Diagnóstico para Técnicos de Campo")
st.write("---")

# 3. Motor de Búsqueda Inteligente
busqueda = st.text_input("🔍 DESCRIBA LA FALLA O CÓDIGO (Ej: Vacío, No arranca, E1, Fuga):")

if st.button("🚀 INICIAR DIAGNÓSTICO"):
    if busqueda:
        q = busqueda.lower()
        
        # --- BLOQUE DE FALLAS MECÁNICAS ---
        
        if "vacio" in q or "se va a vacio" in q:
            st.error("### 🛠️ DIAGNÓSTICO: EL SISTEMA SE VA A VACÍO")
            st.write("1. **Humedad:** Si el vacío es intermitente, hay agua en el sistema. Cambiar filtro y hacer vacío a 500 micrones.")
            st.write("2. **Obstrucción:** Verifique si el capilar o la válvula VXT están congelados por fuera.")
            st.write("3. **Filtro:** Si la entrada del filtro está caliente y la salida fría, está obstruido.")

        elif "no enfria" in q and ("arranca" in q or "bien" in q):
            st.warning("### 🛠️ DIAGNÓSTICO: ARRANCA PERO NO ENFRÍA (Presiones normales)")
            st.write("1. **Compresor Descompresionado:** Mida el amperaje. Si es muy bajo (menos del 50% del RLA) y las presiones están casi iguales, el compresor no bombea.")
            st.write("2. **Válvula 4 Vías:** Si es bomba de calor, puede estar fugando internamente, mezclando alta con baja.")
            st.write("3. **Intercambio:** Verifique que los serpentines no estén tapados de suciedad extrema.")

        elif "no arranca" in q and "compresor" in q:
            st.error("### 🛠️ DIAGNÓSTICO: EL COMPRESOR NO ARRANCA")
            st.write("1. **Capacitor:** Si zumba, cambie el capacitor de marcha. Pruebe con un Start Kit.")
            st.write("2. **Bobinas:** Mida continuidad C-R, C-S y R-S. La suma de C-R + C-S debe dar R-S.")
            st.write("3. **Térmico:** Si el compresor está hirviendo, espere a que enfríe para que el térmico interno cierre.")

        elif "ventilador" in q or "motor" in q:
            st.warning("### 🛠️ DIAGNÓSTICO: FALLA MOTOR VENTILADOR")
            st.write("1. **Capacitor:** Cambie el capacitor de fan (generalmente 1.5uF a 5uF).")
            st.write("2. **Rodamientos:** Gire el aspa con la mano; si está pesada, cambie el motor.")
            st.write("3. **Sensor Hall:** Si gira y se detiene rápido, el sensor de velocidad en la placa falló.")

        # --- BLOQUE DE CÓDIGOS DE MARCA ---
        
        elif "mirage" in q or "midea" in q or "comfort" in q:
            st.info("### 🛠️ CÓDIGOS DE ERROR")
            if "e1" in q: st.write("**E1:** Error de comunicación. Revisar cable de señal y voltajes DC (15-70V).")
            if "ec" in q: st.write("**EC:** Fuga detectada. Sensor de tubería detectó falta de gas.")
            if "e0" in q: st.write("**E0:** Error de memoria EEPROM. Placa dañada.")
        
        else:
            st.warning("⚠️ No encontré la falla exacta. Intente con: 'Vacío', 'Compresor no arranca' o 'E1'.")

# --- TABLAS TÉCNICAS (SIEMPRE VISIBLES ABAJO) ---
st.write("---")
st.subheader("📊 REFERENCIAS DE INGENIERÍA")

col1, col2 = st.columns(2)

with col1:
    st.write("**Relación Presión/Temperatura (R-410A)**")
    st.table({
        "Ambiente": ["25°C", "30°C", "35°C", "40°C"],
        "Baja (PSI)": ["115", "125", "135", "150"],
        "Alta (PSI)": ["320", "370", "430", "500"]
    })

with col2:
    st.write("**Resistencia de Sensores (kΩ)**")
    st.table({
        "Temp": ["20°C", "25°C", "30°C"],
        "10kΩ": ["12.1", "10.0", "8.3"],
        "5kΩ": ["6.1", "5.0", "4.1"]
    })
    
