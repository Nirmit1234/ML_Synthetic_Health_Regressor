import streamlit as st
import pickle
import numpy as np


with open('Synthetic_Health_model.pkl', 'rb') as file:
    model = pickle.load(file)


st.title("Synthetic Health Score Predictor")


age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
exercise = st.slider("Exercise Frequency (days per week)", 0, 7, 3)
diet_quality = st.number_input("Diet Quality (0-100)", min_value=0, max_value=100, value=50)
sleep_hours = st.number_input("Sleep Hours per Night", min_value=3.0, max_value=12.0, value=7.0)
smoking_status = st.selectbox("Smoking Status", ["Non-Smoker", "Smoker"])
alcohol_consumption = st.number_input("Alcohol Consumption (drinks per week)", min_value=0.0, max_value=50.0, value=2.0)


def encode_smoking(status):
    return 1 if status == "Smoker" else 0

smoking_status_encoded = encode_smoking(smoking_status)


if st.button("Predict Health Score"):
    features = np.array([[age, bmi, exercise, diet_quality, sleep_hours, smoking_status_encoded, alcohol_consumption]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Health Score: {prediction:.2f}")