import streamlit as st

# 1. Configuración de Pantalla
st.set_page_config(page_title="HVAC AI OMNISOURCE", layout="wide")

st.title("🤖 HVAC AI: ASISTENTE EXPERTO")
st.write("Consulta fallas de Mirage, Midea, Comfort Fresh y Sistemas Centrales")

# 2. Entrada de lenguaje natural
st.write("---")
pregunta = st.text_input("¿Qué está pasando con el equipo?", placeholder="Ej: 'El compresor se calienta y se apaga' o 'Error E1'")

if st.button("🧠 ANALIZAR FALLA"):
    if pregunta:
        p = pregunta.lower()
        
        # --- LÓGICA DE IA POR SÍNTOMAS ---

        if "agua" in p or "gotea" in p or "tira" in p:
            st.info("### 💧 DIAGNÓSTICO: DRENAJE OBSTRUIDO / CONGELAMIENTO")
            st.write("1. **Nivel:** Verifique que el evaporador tenga una ligera inclinación hacia el desagüe.")
            st.write("2. **Limpieza:** Sople la manguera de drenaje; suele acumular biopelícula (lodo).")
            st.write("3. **Falta de Gas:** Si el serpentín tiene hielo, el agua no cae a la bandeja. Revise presiones.")

        elif "vacio" in p or "succion baja" in p:
            st.error("### 📉 DIAGNÓSTICO: OBSTRUCCIÓN EN EL CICLO")
            st.write("1. **VXT/Capilar:** Si se va a vacío, hay un tapón mecánico o humedad congelada.")
            st.write("2. **Filtro:** Toque el filtro deshidratador. Si hay diferencia de temperatura entre entrada y salida, está tapado.")
            st.write("3. **Procedimiento:** Recupere gas, limpie con 141b/Nitrógeno y cambie el elemento de expansión.")

        elif "no enfría" in p or "poco frio" in p:
            st.warning("### 🌡️ DIAGNÓSTICO: BAJO RENDIMIENTO TÉRMICO")
            st.write("1. **Capacitor de Fan:** Si el ventilador exterior gira lento, el calor no sale y el compresor no rinde.")
            st.write("2. **Compresor:** Si las presiones están igualadas (ej. 150 PSI en alta y baja) con el equipo prendido, las válvulas del compresor fallaron.")
            st.write("3. **Sensores:** Un sensor desvalorizado puede hacer que el equipo corte por 'congelamiento' falso.")

        elif "e1" in p or "comunicacion" in p:
            st.error("### 📡 DIAGNÓSTICO: ERROR DE COMUNICACIÓN (E1/CH05)")
            st.write("1. **Voltaje S-N:** Mida voltaje DC. Debe ser errático (saltando entre 20V y 70V).")
            st.write("2. **Borneras:** El 90% de las veces es un cable sulfatado o flojo en la unidad exterior.")

        elif "no arranca" in p or "zumba" in p:
            st.error("### ⚡ DIAGNÓSTICO: FALLA ELÉCTRICA DE ARRANQUE")
            st.write("1. **Capacitor de Marcha:** Mida capacitancia. Si está seco, el motor solo vibrará.")
            st.write("2. **Bobinas:** Verifique C-R-S. Si alguna borna da 'OL', el compresor está abierto.")

        else:
            st.warning("No estoy seguro. Intenta ser más específico o escribe el código de error.")

# --- TABLAS TÉCNICAS PARA LA IA ---
st.write("---")
with st.expander("📊 BASES DE DATOS DE INGENIERÍA"):
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Relación Presión/Temperatura (R-410A)**")
        st.table({"Ambiente": ["25°C", "35°C", "45°C"], "Baja (PSI)": ["115", "138", "165"]})
    with col2:
        st.write("**Resistencia Sensores kΩ**")
        st.table({"Temp": ["20°C", "25°C", "30°C"], "10k": ["12.1", "10.0", "8.3"]})
