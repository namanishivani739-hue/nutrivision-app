import streamlit as st

st.title("AI-Based Child Nutrition Prediction App")

st.write("Enter the child details below to predict nutrition status.")

age = st.number_input("Age (months)", 0, 60)
weight = st.number_input("Weight (kg)", 1.0, 30.0)
height = st.number_input("Height (cm)", 30.0, 150.0)

if st.button("Predict"):
    st.success("Prediction: Normal Nutrition (Demo Output)")
