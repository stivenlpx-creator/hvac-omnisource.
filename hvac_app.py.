import streamlit as st

# Configuración de interfaz profesional
st.set_page_config(page_title="HVAC OmniSource v2.0", layout="wide")

# Estilos personalizados
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_content_allowed=True)

st.title("🛠️ HVAC-Master OmniSource")
st.write("Sistema Experto de Diagnóstico, Fallas y Corrección")

# --- BASE DE DATOS MAESTRA (MARCAS Y CÓDIGOS) ---
hvac_data = {
    "Samsung": {
        "E1": "Error de sensor de temperatura ambiente (Interior). Revisar sensor de 10kΩ.",
        "E5": "Error de comunicación entre unidades. Revisar cable de señal y voltajes DC.",
        "P4": "Protección de sobrecarga en el compresor Inverter."
    },
    "LG": {
        "CH01": "Sensor de aire interior abierto o en corto. Medir resistencia.",
        "CH05": "Fallo de comunicación persistente. Revisar cableado y placa exterior.",
        "CH61": "Alta temperatura en el condensador. Limpieza urgente requerida."
    },
    "Carrier / York": {
        "E1": "Protección por alta presión (Presostato abierto).",
        "E3": "Protección por baja presión (Falta de refrigerante o fuga).",
        "EC": "Detección de fuga de refrigerante por sensor de temperatura."
    },
    "Daikin": {
        "U4": "Error de transmisión entre unidad interior y exterior.",
        "L5": "Sobrecorriente instantánea en el compresor Inverter.",
        "E7": "Bloqueo del motor ventilador de la unidad exterior."
    },
    "Trane (Industrial/Paquetes)": {
        "ER01": "Falla en el encendido del quemador (Calefacción).",
        "SERVICE": "Falla en el sensor de flujo de aire (Ductos obstruidos).",
        "HI PRES": "Disparo de presostato de alta. Revisar ventilador condensador."
    },
    "Mitsubishi Electric": {
        "P1": "Error de sensor de entrada (Abierto/Corto).",
        "E6": "Falla de comunicación serie. Revisar placa de potencia."
    }
}

# --- BARRA LATERAL: SELECCIÓN DE MARCA ---
st.sidebar.header("⚙️ Configuración del Equipo")
marca_seleccionada = st.sidebar.selectbox("Seleccione la Marca del Equipo:", list(hvac_data.keys()))

menu = st.sidebar.radio("Módulo de Trabajo:", ["Buscador de Códigos", "Asistente de Diagnóstico", "Esquemas Técnicos"])

# --- MÓDULO 1: BUSCADOR DE CÓDIGOS ---
if menu == "Buscador de Códigos":
    st.subheader(f"🔍 Base de Datos: {marca_seleccionada}")
    codigo_input = st.text_input("Ingrese el código de error (ej: E1, CH05, U4):").upper()
    
    if codigo_input:
        if codigo_input in hvac_data[marca_seleccionada]:
            st.success(f"**DIAGNÓSTICO:** {hvac_data[marca_seleccionada][codigo_input]}")
            st.info("💡 **Acción recomendada:** Verificar voltajes y limpieza de contactos antes de reemplazar piezas.")
        else:
            st.warning("Código no encontrado en esta marca. Verifique el manual físico o pruebe con una marca genérica.")

# --- MÓDULO 2: ASISTENTE DE DIAGNÓSTICO (PASO A PASO) ---
elif menu == "Asistente de Diagnóstico":
    st.subheader(f"🤖 Protocolo de Reparación para {marca_seleccionada}")
    falla_tipo = st.selectbox("Tipo de Falla:", ["No Enfría", "Error de Comunicación", "Compresor no arranca"])
    
    if falla_tipo == "No Enfría":
        st.write("### Secuencia de Corrección:")
        st.step1 = st.checkbox("1. Limpieza de filtros y serpentines confirmada.")
        st.step2 = st.checkbox("2. Ventilador exterior girando correctamente.")
        if st.step2:
            st.write("**Siguiente paso:** Mida presiones de succión.")
            presion = st.number_input("Presión de Succión (PSI):", value=0)
            if presion > 0 and presion < 110:
                st.error("Diagnóstico: Falta de refrigerante. Busque fugas con nitrógeno.")

# --- MÓDULO 3: ESQUEMAS TÉCNICOS ---
elif menu == "Esquemas Técnicos":
    st.subheader(f"📄 Manual de Referencia Visual: {marca_seleccionada}")
    tipo_esquema = st.selectbox("Tipo de Diagrama:", ["Conexión Eléctrica Básica", "Circuito Inverter (PCB)", "Ciclo de Refrigeración"])
    
    if tipo_esquema == "Conexión Eléctrica Básica":
        st.image("https://via.placeholder.com/800x500.png?text=Diagrama+Electrico+General", caption="Diagrama de Interconexión")
    elif tipo_esquema == "Circuito Inverter (PCB)":
        st.image("https://via.placeholder.com/800x500.png?text=Esquema+Electronico+Inverter", caption="Puntos de prueba en Placa Electrónica")
