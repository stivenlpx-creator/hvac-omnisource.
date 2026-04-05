import streamlit as st
import google.generativeai as genai

# 1. Configuración de la App
st.set_page_config(page_title="HVAC Pro Diagnostic", layout="wide")

# 2. Configuración de Gemini IA
API_KEY = "AIzaSyACIqPCfjD54WS-XahDvT4zMppQQRu2w0I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. Interfaz de Usuario (Limpia para evitar errores)
st.title("⚡ HVAC PRO DIAGNOSTIC ❄️")
st.write("Soporte Técnico de Ingeniería - OMNISOURCE")
st.write("---")

# BUSCADOR CENTRAL
st.subheader("🔍 Buscador de Fallas con IA")
pregunta = st.text_input("Describa el problema del equipo:", placeholder="Ej: Compresor se va a vacío, error E1, capacitor seco...")

if st.button("ANALIZAR CON IA"):
    if pregunta:
        with st.spinner("Analizando información..."):
            try:
                res = model.generate_content(f"Actúa como Ingeniero Senior HVAC. Responde con pasos numerados a: {pregunta}")
                st.markdown("### 🛠️ Diagnóstico:")
                st.info(res.text)
            except Exception as e:
                st.error(f"Error de conexión: {e}")

# PESTAÑAS DE HERRAMIENTAS
st.write("---")
t1, t2, t3, t4 = st.tabs(["🧮 Cálculos", "🔌 Diagramas", "🌡️ Tabla P-T", "🛡️ Seguridad"])

with t1:
    st.subheader("Cálculos de Superheat y Carga")
    st.write("Use la IA en el buscador superior para calcular sobrecalentamiento rápido.")
    
with t2:
    st.subheader("Diagramas y Electricidad")
    st.write("1. **Identificación de Bobinas:** C-R-S.")
    st.write("2. **Motores PG:** Revisar sensor Hall (conector de 5 cables).")
    
with t3:
    st.subheader("Tabla Presión-Temperatura")
    st.table({
        "Refrigerante": ["R-410A", "R-22", "R-134a"],
        "Baja (PSI)": ["118", "58", "31"],
        "Alta (PSI)": ["375", "240", "168"]
    })
    
with t4:
    st.subheader("Seguridad y Manejo Químico")
    st.error("Uso de Nitrógeno con regulador obligatorio.")
    st.warning("EPP: Gafas y guantes para evitar quemaduras por refrigerante.")
    
