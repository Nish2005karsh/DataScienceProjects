import streamlit as st
import joblib
import numpy as np

st.title("🏠 House Price Prediction")

# Load model and scaler
model = joblib.load('../Models/house_price_model.pkl')
scaler = joblib.load('../Models/scaler.pkl')

# Input widgets
OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)
GrLivArea = st.number_input("Above Ground Living Area (sq ft)", 100, 10000, 1500)
GarageCars = st.slider("Garage Capacity (cars)", 0, 5, 1)
TotalBsmtSF = st.number_input("Basement Area (sq ft)", 0, 5000, 800)
FullBath = st.slider("Full Bathrooms", 0, 5, 1)
YearBuilt = st.number_input("Year Built", 1800, 2023, 2000)

# Prepare input
input_data = np.array([[OverallQual, GrLivArea, GarageCars, TotalBsmtSF, FullBath, YearBuilt]])
input_scaled = scaler.transform(input_data)

if st.button("Predict Price"):
    prediction = model.predict(input_scaled)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
