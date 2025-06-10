import streamlit as st
import pickle
import numpy as np


# 🏥 Título e introducción
st.set_page_config(page_title="Evaluador de Riesgo de Diabetes", page_icon="🏥")


# Autores del proyecto
st.markdown("""

<div style="background-color:#e0f7fa; padding:16px; border-radius:10px; border: 1px solid #b2ebf2;"> <h4 style="color:#00796b;">👨‍💻 <b>Autores del Proyecto</b></h4> <ul> <li><b>Carlos Alex Macias</b> <span style="color:#555;">(Código: 22500208)</span></li> <li><b>Juan Camilo Peña</b> <span style="color:#555;">(Código: 22501426)</span></li> </ul> </div> """, unsafe_allow_html=True)

st.title("Evaluador de Riesgo de Diabetes")
st.markdown("""
Esta aplicación estima el **riesgo de que una persona presente signos asociados a diabetes**
basándose en datos de salud y estilo de vida recopilados por los CDC (BRFSS 2015).

> **Importante:** Esta herramienta **no reemplaza un diagnóstico médico**. Si obtienes un riesgo alto,
consulta con un profesional de la salud.
""")

# 🔎 Cargar el modelo
with open('modelo_random_forest.pkl', 'rb') as file:
    model = pickle.load(file)

# ⚖️ Crear formulario de entrada
st.sidebar.header("Ingrese los datos del paciente")
def bool_to_binary(respuesta):
    return 1 if respuesta == "Sí" else 0

# 🏋️ Calcular BMI desde altura y peso
peso = st.sidebar.number_input("Peso (kg)", min_value=30.0, max_value=200.0, value=70.0)
altura = st.sidebar.number_input("Altura (cm)", min_value=100.0, max_value=220.0, value=170.0)
BMI = round(peso / (altura / 100) ** 2, 2)
st.sidebar.markdown(f"**IMC calculado:** {BMI}")

# Entradas booleanas convertidas a binario
HighBP = bool_to_binary(st.sidebar.selectbox("¿Presión arterial alta?", ["No", "Sí"]))
HighChol = bool_to_binary(st.sidebar.selectbox("¿Colesterol alto?", ["No", "Sí"]))
CholCheck = bool_to_binary(st.sidebar.selectbox("¿Se ha revisado el colesterol recientemente?", ["No", "Sí"]))
Stroke = bool_to_binary(st.sidebar.selectbox("¿Ha sufrido un ACV (derrame cerebral)?", ["No", "Sí"]))
HeartDiseaseorAttack = bool_to_binary(st.sidebar.selectbox("¿Tiene enfermedad cardíaca o ha sufrido un infarto?", ["No", "Sí"]))
PhysActivity = bool_to_binary(st.sidebar.selectbox("¿Realiza actividad física regularmente?", ["No", "Sí"]))
DiffWalk = bool_to_binary(st.sidebar.selectbox("¿Tiene dificultad para caminar o subir escaleras?", ["No", "Sí"]))

# Salud general y días no saludables
GenHlth = st.sidebar.slider("Estado general de salud (1=Excelente, 5=Malo)", 1, 5, 3)
MentHlth = st.sidebar.slider("Días con salud mental no buena (0-30)", 0, 30, 0)
PhysHlth = st.sidebar.slider("Días con salud física no buena (0-30)", 0, 30, 0)

# 📅 Edad como número => clasificación
edad_valor = st.sidebar.number_input("Edad (años)", min_value=18, max_value=100, value=35)
if edad_valor < 25:
    Age = 1
elif edad_valor < 30:
    Age = 2
elif edad_valor < 35:
    Age = 3
elif edad_valor < 40:
    Age = 4
elif edad_valor < 45:
    Age = 5
elif edad_valor < 50:
    Age = 6
elif edad_valor < 55:
    Age = 7
elif edad_valor < 60:
    Age = 8
elif edad_valor < 65:
    Age = 9
elif edad_valor < 70:
    Age = 10
elif edad_valor < 75:
    Age = 11
elif edad_valor < 80:
    Age = 12
else:
    Age = 13

# 🎓 Nivel educativo (1=menor, 6=posgrado)
ed_level = st.sidebar.selectbox("Nivel educativo", [
    "Primaria incompleta", "Primaria completa", "Secundaria", "Técnico", "Universitario", "Posgrado"])
Education = ["Primaria incompleta", "Primaria completa", "Secundaria", "Técnico", "Universitario", "Posgrado"].index(ed_level) + 1

# 💼 Nivel de ingresos (1=bajo, 8=alto)
income_level = st.sidebar.selectbox("Nivel de ingresos", [
    "<10k", "10k-15k", "15k-20k", "20k-25k", "25k-35k", "35k-50k", "50k-75k", ">75k"])
Income = ["<10k", "10k-15k", "15k-20k", "20k-25k", "25k-35k", "35k-50k", "50k-75k", ">75k"].index(income_level) + 1

# 👥 Organizar los datos
input_data = np.array([[
    HighBP, HighChol, CholCheck, BMI, Stroke, HeartDiseaseorAttack,
    PhysActivity, GenHlth, MentHlth, PhysHlth,
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
