
# 🩺 Evaluador de Riesgo de Diabetes con Machine Learning

Este proyecto implementa un sistema de predicción de riesgo de diabetes utilizando algoritmos de Machine Learning y una interfaz web con Streamlit. El modelo ha sido entrenado con datos del BRFSS 2015 (CDC) y busca identificar personas con alta probabilidad de desarrollar diabetes, basándose en datos clínicos, demográficos y de estilo de vida.

---

## 📦 Contenido del Repositorio

- `app.py` — Aplicación Streamlit para predicción interactiva.
- `modelo_random_forest.pkl` — Modelo Random Forest entrenado y preprocesado con pipeline.
- `requirements.txt` — Librerías necesarias para ejecutar el proyecto en local o en la nube.
- `notebooks/` — Contiene los notebooks del análisis exploratorio (EDA), ajuste de hiperparámetros y entrenamiento de modelos.

---

## 🧪 Dataset Utilizado

- **Fuente**: [CDC BRFSS 2015](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)
- **Variables**: Estado de salud, presión arterial, colesterol, IMC, edad, nivel educativo, nivel de ingresos, entre otros.
- **Target**: `Diabetes_binary` (0 = No tiene diabetes, 1 = Tiene diabetes)

---

## ⚙️ Modelos Entrenados

- Regresión Logística (con y sin balanceo de clases)
- Random Forest (modelo seleccionado final)
- XGBoost (modelo competitivo)

Se aplicaron técnicas como:
- `class_weight='balanced'`
- `SMOTE`, `NearMiss`, `RandomOverSampler`
- Ajuste de hiperparámetros con `RandomizedSearchCV`

---

## Enlace a los notebooks en google colab
https://drive.google.com/drive/folders/1pSKcMJvg2Zy6ukXCXYS30mcRllxGPz1J?usp=sharing

## 🚀 Cómo Ejecutar

1. Clona el repositorio:
```bash
git clone https://github.com/registel/proyecto_final_ML.git
cd proyecto_final_ML
```

2. Instala dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la app:
```bash
streamlit run app.py
```

---

## 🌐 Aplicación en Línea

La aplicación está desplegada y disponible públicamente en:

🔗 [Streamlit App — Proyecto Final ML](https://proyectofinalml-izxj6pyn34xb9idctwqrwx.streamlit.app/)

---

## 📊 Visualización de Resultados

La app calcula el IMC a partir de altura y peso, solicita respuestas tipo **Sí/No**, y adapta edad, educación e ingresos al formato del modelo.

Devuelve una probabilidad estimada de riesgo de diabetes acompañada de un mensaje de recomendación.

---

## 👨‍💻 Autores

- **Carlos Alex Macias** — Código: 22500208  
- **Juan Camilo Peña** — Código: 22501426

Proyecto desarrollado como parte del curso **Machine Learning** para la Maestría en Inteligencia Artificial y Ciencia de Datos.

---

## 📄 Licencia

MIT
