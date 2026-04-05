import streamlit as st

# Configuración básica sin errores
st.set_page_config(page_title="HVAC OMNISOURCE PRO", layout="wide")

st.title("🛠️ HVAC OMNISOURCE PRO")
st.markdown("### Terminal de Diagnóstico Universal")

# --- BASE DE DATOS EXPANDIDA ---
base_datos = {
    "samsung": {
        "e1": "FALLA: Sensor Ambiente. Medir 10kΩ. Revisar conector.",
        "e5": "FALLA: Comunicación. Revisar cable señal (L-N-S).",
        "p4": "FALLA: Sobrecarga Compresor. Limpiar condensadora."
    },
    "lg": {
        "ch01": "FALLA: Sensor interior. Revisar termistor.",
        "ch05": "FALLA: Error Comunicación. Revisar voltajes DC.",
        "ch61": "FALLA: Alta temperatura. Limpiar serpentín."
    },
    "midea": {
        "e1": "FALLA: Error comunicación unidades. Revisar cableado.",
        "ec": "FALLA: Fuga de gas. El sensor detectó baja presión.",
        "e3": "FALLA: Velocidad ventilador interior fuera de control."
    },
    "mirage": {
        "e0": "FALLA: Error de parámetro en EEPROM (Placa dañada).",
        "e1": "FALLA: Error de comunicación interior/exterior.",
        "p4": "FALLA: Protección de temperatura del compresor."
    },
    "comfort fresh": {
        "e1": "FALLA: Sensor de aire ambiente interior.",
        "e2": "FALLA: Sensor de tubería (evaporador).",
        "e4": "FALLA: Protección de alta presión o falta de refrigerante."
    },
    "carrier": {
        "e1": "FALLA: Alta presión. Limpiar filtros y ventilador.",
        "e3": "FALLA: Baja presión. Posible fuga."
    }
}

# --- BUSCADOR ---
st.info("Escribe el error o la marca abajo (Ejemplo: 'E1', 'Midea', 'Fuga')")
pregunta = st.text_input("🔍 CONSULTA TÉCNICA:", "").lower()

if pregunta:
    encontrado = False
    for marca, fallas in base_datos.items():
        if marca in pregunta:
            st.write(f"### 📋 Listado rápido para {marca.upper()}:")
            st.json(fallas)
            encontrado = True
        for cod, sol in fallas.items():
            if cod in pregunta:
                st.success(f"✅ {marca.upper()} - {cod.upper()}: {sol}")
                encontrado = True
    if not encontrado:
        st.warning("No encontrado. Intenta con 'Mirage' o 'E1'.")

# --- CAJONES DE DIAGNÓSTICO ---
st.markdown("---")
st.header("📂 MANUALES RÁPIDOS")
marca_sel = st.selectbox("Seleccione Marca:", ["Seleccione...", "Mirage", "Midea", "Comfort Fresh", "LG", "Samsung"])

if marca_sel != "Seleccione...":
    st.subheader(f"Guía de campo: {marca_sel}")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Paso 1: Eléctrico**")
        st.write("- Revisar capacitor y contactor.")
        st.write("- Medir continuidad en bobinas C-R-S.")
        
    with col2:
        st.write("**Paso 2: Refrigeración**")
        st.write("- Presión R410A: 110-140 PSI.")
        st.write("- Presión R22: 60-75 PSI.")
        
