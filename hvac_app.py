import streamlit as st

# Configuración simplificada para evitar errores de estilo
st.set_page_config(page_title="HVAC Master OmniSource", layout="wide")

st.title("🛠️ HVAC-Master OmniSource")
st.write("Sistema de Diagnóstico y Fallas")

# --- BASE DE DATOS ---
hvac_data = {
    "Samsung": {"E1": "Error sensor temperatura ambiente. Revisar sensor 10kΩ.", "E5": "Error de comunicación. Revisar cables señal.", "P4": "Protección sobrecarga Inverter."},
    "LG": {"CH01": "Sensor aire interior abierto/corto.", "CH05": "Fallo comunicación. Revisar placa exterior.", "CH61": "Alta temperatura condensador. Limpiar serpentín."},
    "Carrier / York": {"E1": "Alta presión.", "E3": "Baja presión (Fuga).", "EC": "Detección de fuga."},
    "Daikin": {"U4": "Error transmisión unidades.", "L5": "Sobrecorriente compresor Inverter.", "E7": "Bloqueo motor ventilador exterior."},
    "Trane": {"ER01": "Falla encendido quemador.", "SERVICE": "Falla sensor flujo aire.", "HI PRES": "Disparo presostato alta."},
    "Mitsubishi": {"P1": "Error sensor entrada.", "E6": "Falla comunicación serie."}
}

# --- MENÚ ---
st.sidebar.header("Menú")
marca = st.sidebar.selectbox("Marca del Equipo:", list(hvac_data.keys()))
modo = st.sidebar.radio("Módulo:", ["Códigos de Error", "Ayuda Visual"])

if modo == "Códigos de Error":
    st.subheader(f"🔍 Códigos para {marca}")
    cod = st.text_input("Ingresa el código (ej: E1):").upper()
    if cod:
        if cod in hvac_data[marca]:
            st.success(f"**Resultado:** {hvac_data[marca][cod]}")
        else:
            st.warning("Código no encontrado.")

elif modo == "Ayuda Visual":
    st.subheader("⚡ Diagramas de Referencia")
    diag = st.selectbox("Elegir diagrama:", ["Esquema Eléctrico Condensadora", "Placa Electrónica Inverter", "Ciclo Refrigeración Industrial"])
    
    if diag == "Esquema Eléctrico Condensadora":
        st.write("Referencia de conexión de capacitor y compresor:")
        # Aquí la app cargará las imágenes de referencia
        
