import streamlit as st

# Configuración de página para entorno industrial
st.set_page_config(page_title="HVAC OMNISOURCE PRO", layout="wide")

# CSS Avanzado para Botones Táctiles y Cajones de Información
st.markdown("""
    <style>
    .stButton > button {
        height: 5em;
        width: 100%;
        font-size: 22px !important;
        font-weight: bold;
        background-color: #004a99;
        color: white;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    .stTextInput > div > div > input {
        font-size: 20px;
        height: 3em;
    }
    .cajon-info {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border-left: 10px solid #004a99;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_content_allowed=True)

st.title("🚀 HVAC OMNISOURCE: Terminal de Diagnóstico")

# --- MOTOR DE BÚSQUEDA INTELIGENTE ---
st.markdown("### 🔍 CONSULTA RÁPIDA (Falla o Código)")
pregunta = st.text_input("Ejemplo: 'E1', 'sensor', 'compresor caliente', 'comunicación'", "").lower()

# --- BASE DE DATOS ESTRUCTURADA ---
base_datos = {
    "samsung": {
        "e1": "FALLA: Sensor Ambiente. \n1. Medir sensor (10kΩ). \n2. Revisar conector en PCB. \n3. Reemplazar si el valor es ∞.",
        "e5": "FALLA: Comunicación. \n1. Medir voltaje DC entre 2 y 3. \n2. Revisar cable de señal apantallado. \n3. Verificar tierra física.",
        "compresor": "DIAGNÓSTICO: Si no arranca, medir IPM (U,V,W). Si se calienta, revisar carga de refrigerante."
    },
    "lg": {
        "ch01": "FALLA: Sensor aire interior. \n1. Revisar termistor. \n2. Limpiar contactos. \n3. Sustituir pieza.",
        "ch05": "FALLA: Error de comunicación serie. \n1. Revisar fase y neutro invertidos. \n2. Comprobar continuidad cable de datos.",
        "ruido": "DIAGNÓSTICO: Revisar rodamientos del motor blower o aspas del ventilador exterior."
    },
    "carrier": {
        "e1": "FALLA: Alta Presión. \n1. Limpiar condensador. \n2. Revisar capacitor del ventilador. \n3. Verificar presostato.",
        "ec": "FALLA: Fuga detectada. \n1. Recuperar gas. \n2. Presurizar con nitrógeno a 350 PSI. \n3. Buscar pompas con jabón."
    }
}

# --- LÓGICA DE RESPUESTA ---
if pregunta:
    encontrado = False
    for marca, fallas in base_datos.items():
        for clave, solucion in fallas.items():
            if clave in pregunta:
                st.markdown(f"<div class='cajon-info'><h3>✅ RESULTADO ({marca.upper()}):</h3><p style='font-size:18px;'>{solucion}</p></div>", unsafe_content_allowed=True)
                encontrado = True
    if not encontrado:
        st.warning("No hay una coincidencia exacta. Intenta con una sola palabra (ej: 'E1' o 'fuga').")

# --- SEGMENTACIÓN POR MARCAS (CAJONES TÉCNICOS) ---
st.markdown("---")
st.header("📂 MANUALES DE DIAGNÓSTICO POR MARCA")
marca_sel = st.selectbox("Seleccione para ver guía técnica completa:", ["Seleccione...", "Samsung", "LG", "Carrier", "Daikin", "Trane"])

if marca_sel != "Seleccione...":
    st.markdown(f"<div class='cajon-info'><h2>🛠️ Guía Paso a Paso: {marca_sel}</h2>", unsafe_content_allowed=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 1. Verificación Eléctrica")
        st.write("- Medir voltaje de entrada (L-N).")
        st.write("- Comprobar capacitores de marcha.")
        
    
    with col_b:
        st.write("### 2. Ciclo Frigorífico")
        st.write("- Presión Succión: 110-130 PSI (R410A).")
        st.write("- Salto térmico ideal: 12°C a 15°C.")
        

    st.write("### 3. Electrónica Avanzada")
    st.write("Si el equipo es Inverter, verifique los LEDs de la placa exterior antes de manipular.")
    
    st.markdown("</div>", unsafe_content_allowed=True)

# --- BOTONES DE HERRAMIENTAS RÁPIDAS ---
st.markdown("### 🧰 HERRAMIENTAS")
c1, c2 = st.columns(2)
with c1:
    if st.button("📊 TABLA PT (Presión-Temp)"):
        st.table({"Refrigerante": ["R22", "R410A", "R134a"], "Baja (PSI)": ["65", "120", "30"], "Alta (PSI)": ["250", "450", "150"]})
with c2:
    if st.button("🚑 SOPORTE DE EMERGENCIA"):
        st.error("LLAMANDO A INGENIERÍA... (Simulación)")
