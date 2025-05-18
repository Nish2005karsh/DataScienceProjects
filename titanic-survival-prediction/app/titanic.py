import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load('../models/titanic_model.pkl')

st.title("🚢 Titanic Survival Predictor")

st.markdown("Fill in the passenger details below to predict survival.")

# Collect user input
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ['male', 'female'])
age = st.slider("Age", 0.42, 80.0, 25.0)
sibsp = st.number_input("Number of Siblings/Spouses Aboard", 0, 8, 0)
parch = st.number_input("Number of Parents/Children Aboard", 0, 6, 0)
fare = st.slider("Fare Paid", 0.0, 600.0, 32.0)
embarked = st.selectbox("Port of Embarkation", ['S', 'C', 'Q'])
# Encode categorical inputs
sex_encoded = 0 if sex == 'male' else 1
embarked_map = {'S': 2, 'C': 0, 'Q': 1}
embarked_encoded = embarked_map[embarked]
# Family Size Feature
family_size = sibsp + parch
# Create feature array
features = np.array([[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded, family_size]])
# Predict
if st.button("Predict"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.success("🎉 This passenger **would have survived!**")
    else:
        st.error("💀 This passenger **would not have survived.**")
