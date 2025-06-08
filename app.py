import streamlit as st
import pickle
import numpy as np

# 🏥 Título e introducción
st.set_page_config(page_title="Evaluador de Riesgo de Diabetes", page_icon="🏥")
st.title("Evaluador de Riesgo de Diabetes")
st.markdown("""
Esta aplicación estima el **riesgo de que una persona presente signos asociados a diabetes**
basándose en datos de salud y estilo de vida recopilados por los CDC (BRFSS 2015).

> **Importante:** Esta herramienta **no reemplaza un diagnóstico médico**. Si obtienes un riesgo alto,
consulta con un profesional de la salud.
""")

# 🔎 Cargar el modelo
with open('pipeline_random_forest.pkl', 'rb') as file:
    model = pickle.load(file)

# ⚖️ Crear formulario de entrada
st.sidebar.header("Ingrese los datos del paciente")
definir_entrada = lambda etiqueta, minimo, maximo, valor: st.sidebar.slider(etiqueta, minimo, maximo, valor)

HighBP = st.sidebar.selectbox("Presión Alta (HighBP)", [0, 1])
HighChol = st.sidebar.selectbox("Colesterol Alto (HighChol)", [0, 1])
CholCheck = st.sidebar.selectbox("Revisión de colesterol reciente (CholCheck)", [0, 1])
BMI = definir_entrada("IMC (BMI)", 12, 98, 25)
Stroke = st.sidebar.selectbox("Historial de ACV (Stroke)", [0, 1])
HeartDiseaseorAttack = st.sidebar.selectbox("Enfermedad Cardíaca o Infarto", [0, 1])
PhysActivity = st.sidebar.selectbox("Actividad física regular", [0, 1])
HvyAlcoholConsump = st.sidebar.selectbox("Consumo excesivo de alcohol", [0, 1])
GenHlth = definir_entrada("Estado general de salud (1=Excelente, 5=Malo)", 1, 5, 3)
MentHlth = definir_entrada("Días con salud mental no buena (0-30)", 0, 30, 0)
PhysHlth = definir_entrada("Días con salud física no buena (0-30)", 0, 30, 0)
DiffWalk = st.sidebar.selectbox("Dificultad para caminar o subir escaleras", [0, 1])
Age = definir_entrada("Grupo de edad (1-13)", 1, 13, 9)
Education = definir_entrada("Nivel de educación (1-6)", 1, 6, 4)
Income = definir_entrada("Nivel de ingresos (1-8)", 1, 8, 4)

# 👥 Organizar los datos
input_data = np.array([[
    HighBP, HighChol, CholCheck, BMI, Stroke, HeartDiseaseorAttack,
    PhysActivity, HvyAlcoholConsump, GenHlth, MentHlth, PhysHlth,
    DiffWalk, Age, Education, Income
]])

# 🔍 Ejecutar predicción
if st.sidebar.button("Evaluar Riesgo"):
    proba = model.predict_proba(input_data)[0][1]  # Probabilidad clase 1
    porcentaje = round(proba * 100, 2)

    st.subheader("Resultado de Evaluación")
    st.write(f"**Probabilidad estimada de diabetes: {porcentaje}%**")

    if proba >= 0.7:
        st.error("⚠️ Riesgo muy alto de diabetes. Consulte a un médico lo antes posible.")
    elif proba >= 0.5:
        st.warning("⚠️ Riesgo moderado. Se recomienda chequeo preventivo.")
    elif proba >= 0.3:
        st.info("🔎 Riesgo leve. Mantenga control y estilo de vida saludable.")
    else:
        st.success("✅ Riesgo bajo de diabetes.")

# 📊 Pie de página
st.markdown("""
<hr>
© Proyecto de Machine Learning – Predicción de Riesgo de Diabetes 
<br>
Desarrollado con fines educativos. Basado en datos BRFSS 2015 (CDC).
""", unsafe_allow_html=True)
