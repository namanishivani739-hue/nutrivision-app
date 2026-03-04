import streamlit as st
import joblib
import numpy as np

model = joblib.load("nutrition_model.pkl")

age = st.number_input("Age (months)")
weight = st.number_input("Weight (kg)")
height = st.number_input("Height (cm)")

if st.button("Predict"):
    input_data = np.array([[age, weight, height]])
    prediction = model.predict(input_data)
    st.success(f"Prediction: {prediction[0]}")
