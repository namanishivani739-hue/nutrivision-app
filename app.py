import streamlit as st
import joblib
import numpy as np

# Load ML model
model = joblib.load("nutrition_model.pkl")

st.title("AI-Based Child Nutrition Prediction App")
st.write("Enter the child details below to predict nutrition status.")

age = st.number_input("Age (months)", 0, 60)
weight = st.number_input("Weight (kg)", 1.0, 30.0)
height = st.number_input("Height (cm)", 30.0, 150.0)

if st.button("Predict"):

    input_data = np.array([[age, weight, height]])
    prediction = model.predict(input_data)

    # ML prediction + severe check
    if weight < 5:
        result = "Severe Malnutrition"
    elif weight < 10:
        result = "Under Nutrition"
    else:
        result = "Normal Nutrition"

    st.success(f"Prediction: {result}")
