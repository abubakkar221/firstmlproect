import streamlit as st
import joblib
import numpy as np

st.title("Linear Regression Web Application")

model = joblib.load("linear_marks_model.pkl")

x = st.number_input("Enter value")

if st.button("Predict"):
    y = model.predict(np.array([[x]]))
    st.success(f"Prediction: {y[0]}")
