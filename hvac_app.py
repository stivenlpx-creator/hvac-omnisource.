import streamlit as st

# 1. Configuración de Pantalla
st.set_page_config(page_title="HVAC OMNISOURCE PRO", layout="wide")

# Estilo para el botón verde y diseño limpio
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #28a745;
        color: white;
        height: 3em;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        border: none;
    }
    .stTextInput > div > div > input {
        font-size: 18px;
    }
    </style>
    """, unsafe_content_allowed=True)

# --- CABECERA CON LOGO TEXTUAL HVAC ---
st.markdown("<h1 style='text-align: center; color: #58a6ff;'>❄️ HVAC 🛠️</h1>", unsafe_content_allowed=True)
st.markdown("<h3 style='text-align: center;'>Terminal de Diagnóstico y Fallas Pro</h3>", unsafe_content_allowed=True)

# --- MOTOR DE BÚSQUEDA ---
st.write("---")
busqueda = st.text_input("Ingrese Marca, Código de Error o Síntoma:", placeholder="Ej: Mirage E1, Midea EC, Falla de compresor...")
boton_buscar = st.button("BUSCAR DIAGNÓSTICO")

if busqueda or boton_buscar:
    query = busqueda.lower()
    
    # --- BASE DE DATOS PROFUNDA ---
    
    # 1. MIRAGE
    if "mirage" in query:
        if "e1" in query or "comunicacion" in query:
            st.success("### ✅ DIAGNÓSTICO: MIRAGE E1 - ERROR DE COMUNICACIÓN")
            st.write("1. **Reset Eléctrico:** Desconecta el equipo 5 minutos.")
            st.write("2. **Cables de Señal:** Revisa el borne 'S' o '3' en ambas unidades. El cable debe ser continuo, sin empalmes.")
            st.write("3. **Prueba de Voltaje:** Con el equipo encendido, mide Voltaje DC entre el Neutro (N) y la Señal (S). Debe variar (oscilar) entre 15V y 70V DC.")
            st.write("4. **Veredicto:** Si el voltaje es fijo en 0V o 80V, la placa del evaporador o condensador está dañada.")
            st.image("https://iaq.com.au/wp-content/uploads/2019/04/Compressor-Terminals.jpg", caption="Verifique bornes de señal")
            
        elif "e0" in query or "eeprom" in query:
            st.error("### ✅ DIAGNÓSTICO: MIRAGE E0 - ERROR DE PARÁMETRO EEPROM")
            st.write("1. **Causa:** La memoria de la placa principal perdió su programación.")
            st.write("2. **Acción:** Apagar el interruptor principal (breaker) por 10 minutos.")
            st.write("3. **Revisión:** Verificar que no haya humedad o sulfatación en la placa.")
            st.write("4. **Solución:** Si el error persiste, se debe reemplazar la tarjeta electrónica del evaporador.")

    # 2. MIDEA
    elif "midea" in query:
        if "ec" in query or "fuga" in query:
            st.warning("### ✅ DIAGNÓSTICO: MIDEA EC - FUGA DE REFRIGERANTE")
            st.write("1. **Detección:** El sensor de tubería detectó una temperatura anormal por falta de gas.")
            st.write("2. **Búsqueda:** Revisa las tuercas de conexión (flare). Busca rastros de aceite.")
            st.write("3. **Prueba de Presión:** Si la presión es menor a 100 PSI (R410A), hay fuga.")
            st.write("4. **Solución:** Presuriza con Nitrógeno a 350 PSI para hallar el poro, suelda, haz vacío y carga por peso.")
            st.image("https://iaq.com.au/wp-content/uploads/2019/04/Refrigeration-Cycle.jpg", caption="Puntos de inspección de fuga")

    # 3. COMFORT FRESH
    elif "comfort" in query or "fresh" in query:
        if "e1" in query or "sensor" in query:
            st.info("### ✅ DIAGNÓSTICO: COMFORT FRESH E1 - SENSOR DE AIRE")
            st.write("1. **Medición:** Desconecta el sensor de la placa.")
            st.write("2. **Valor:** Debe medir 10 kΩ a una temperatura de 25°C.")
            st.write("3. **Prueba:** Si mide 0Ω (corto) o infinito (abierto), está dañado.")
            st.write("4. **Sustitución:** Reemplaza por un sensor original de 10k.")

    # 4. FALLAS GENÉRICAS (COMPRESOR / VENTILADOR)
    elif "compresor" in query:
        st.info("### 🛠️ DIAGNÓSTICO: EL COMPRESOR NO ARRANCA")
        st.write("1. **Capacitor:** Verifica si el capacitor de marcha está inflado o desvalorizado.")
        st.write("2. **Bobinas:** Mide continuidad entre C, R y S. (R a S debe ser la suma de C-R + C-S).")
        st.write("3. **Térmico:** Verifica que el protector térmico no esté abierto por exceso de calor.")
        st.write("4. **Inverter:** Si es Inverter, mide la impedancia entre las fases U-V-W. Deben ser idénticas.")

    else:
        st.warning("⚠️ No se encontró la falla exacta. Intenta con: 'Mirage E1', 'Midea EC', 'Compresor caliente'.")

# --- TABLAS DE APOYO VISUAL FIJAS ---
st.write("---")
with st.expander("📊 TABLA DE REFERENCIA DE SENSORES (kΩ)"):
    st.write("Valores para Mirage, Midea y Comfort Fresh:")
    st.table({
        "Temperatura": ["15°C", "20°C", "25°C", "30°C"],
        "Sensor 10kΩ": ["14.7 kΩ", "12.1 kΩ", "10.0 kΩ", "8.3 kΩ"],
        "Sensor 5kΩ": ["7.3 kΩ", "6.1 kΩ", "5.0 kΩ", "4.1 kΩ"]
    })
    
