import streamlit as st

# 1. Configuración de Pantalla
st.set_page_config(page_title="HVAC OMNISOURCE TOTAL", layout="wide")

# 2. Encabezado con Estilo
st.markdown("<h1 style='text-align: center;'>❄️ HVAC MASTER: ENCICLOPEDIA TÉCNICA 🛠️</h1>", unsafe_content_allowed=True)
st.write("---")

# 3. Motor de Búsqueda Inteligente
busqueda = st.text_input("🔍 DESCRIBA LA FALLA O CÓDIGO:", placeholder="Ej: No enfría, Se va a vacío, E1, IPM, Compresor...")
btn_buscar = st.button("🚀 INICIAR DIAGNÓSTICO DE CAMPO")

if busqueda or btn_buscar:
    q = busqueda.lower()
    
    # --- SECCIÓN A: FALLAS MECÁNICAS Y DE CICLO ---
    
    if "vacio" in q or "se va a vacio" in q:
        st.error("### 🛠️ DIAGNÓSTICO: EL SISTEMA SE VA A VACÍO")
        st.write("1. **Obstrucción por Hielo:** Si el vacío es intermitente, hay humedad. Cambiar filtro y hacer vacío de 500 micrones.")
        st.write("2. **Filtro Tapado:** Si la entrada está caliente y la salida fría, el filtro deshidratador está obstruido.")
        st.write("3. **Capilar/VXT:** Si el evaporador solo congela el inicio, el elemento de expansión está semitapado.")
        st.write("4. **Válvulas:** Verifique que las válvulas de succión y líquido estén abiertas al 100%.")

    elif "no enfria" in q and "bien" in q:
        st.warning("### 🛠️ DIAGNÓSTICO: ARRANCA, PRESIONES BIEN, PERO NO ENFRÍA")
        st.write("1. **Compresor Descompresionado:** Mida el amperaje. Si es muy bajo (30-50% del RLA) y las presiones están casi igualadas, las válvulas internas del compresor no bombean.")
        st.write("2. **Válvula Inversora:** Si es bomba de calor, la válvula de 4 vías puede estar fugando internamente, mezclando succión con descarga.")
        st.write("3. **Cortocircuito de Aire:** Verifique que el aire caliente de la condensadora no esté recirculando hacia la entrada.")

    elif "no arranca" in q and "compresor" in q:
        st.error("### 🛠️ DIAGNÓSTICO: COMPRESOR NO ARRANCA")
        st.write("1. **Capacitor:** Si zumba, el capacitor de marcha está agotado. Probar con un 'Hard Start Kit' si el compresor está pegado.")
        st.write("2. **Protector Térmico:** Si el compresor está caliente y no marca continuidad, el térmico interno está abierto. Enfriar con agua/aire.")
        st.write("3. **Bobinado:** Mida continuidad C-R, C-S y R-S. La suma de C-R + C-S debe ser igual a R-S.")

    elif "ventilador" in q or "fan" in q:
        st.warning("### 🛠️ DIAGNÓSTICO: FALLA EN MOTOR VENTILADOR")
        st.write("1. **Mecánico:** Si el aspa está dura, los rodamientos/bujes están resecos. Cambiar motor.")
        st.write("2. **Eléctrico:** Revisar capacitor de fan (generalmente 1.5uF a 6uF).")
        st.write("3. **Electrónico:** En motores PG, medir 5V DC en el sensor Hall. Si no hay señal, el equipo se apaga por seguridad.")

    # --- SECCIÓN B: CÓDIGOS DE ERROR (MIRAGE, MIDEA, COMFORT) ---
    
    elif "e1" in q or "comunicacion" in q:
        st.info("### 🛠️ FALLA: ERROR DE COMUNICACIÓN (E1)")
        st.write("1. **Voltaje N-S:** Debe oscilar entre 15V y 70V DC. Si es fijo 0V o 80V, hay falla de placa.")
        st.write("2. **Cableado:** Revisar que el cable de señal no esté aterrizado o sulfatado.")

    elif "ec" in q or "fuga" in q:
        st.error("### 🛠️ FALLA: DETECCIÓN DE FUGA (EC)")
        st.write("1. **Causa:** El sensor de tubería no detecta enfriamiento tras 10 min de marcha.")
        st.write("2. **Acción:** Presurizar con Nitrógeno a 350 PSI. No cargar gas sin reparar la fuga.")

    else:
        st.warning("⚠️ No hay coincidencia exacta. Escriba: 'Vacío', 'IPM', 'E1', 'Sensor' o 'No enfría'.")

# --- TABLAS DE INGENIERÍA (SIEMPRE DISPONIBLES) ---
st.write("---")
st.subheader("📊 TABLAS DE REFERENCIA DE INGENIERÍA")

t1, t2, t3 = st.tabs(["🌡️ PRESIÓN / TEMPERATURA", "🔌 BOBINAS Y CAPACITORES", "🌡️ SENSORES kΩ"])

with t1:
    st.write("**Relación P/T para R-410A (Lecturas en Succión)**")
    st.table({
        "Temp. Exterior": ["25°C (77°F)", "30°C (86°F)", "35°C (95°F)", "40°C (104°F)"],
        "Presión Baja (PSI)": ["110 - 118", "122 - 130", "135 - 145", "150 - 160"],
        "Presión Alta (PSI)": ["310 - 330", "360 - 390", "420 - 460", "490 - 530"]
    })

with t2:
    st.write("**Datos de Compresores On-Off**")
    st.table({
        "Capacidad": ["12,000 BTU", "18,000 BTU", "24,000 BTU", "36,000 BTU"],
        "Capacitor": ["30 - 35 uF", "40 - 45 uF", "55 - 60 uF", "70 - 80 uF"],
        "Amperaje RLA": ["5.5 A", "8.2 A", "11.0 A", "16.0 A"]
    })

with t3:
    st.write("**Resistencia de Sensores (kΩ)**")
    st.table({
        "Temperatura": ["20°C", "25°C", "30°C", "35°C"],
        "Sensor 10kΩ": ["12.1", "10.0", "8.3", "6.9"],
        "Sensor 5kΩ": ["6.1", "5.0", "4.1", "3.4"]
    })
    
