import streamlit as st
import joblib
import numpy as np
import pickle

st.title("Churn Prediction Using Streamlit")
st.write("This app predicts the churn of a customer using machine learning using Logistic Regression.")

#Load both the models
model=joblib.load('../Models/regress_model.pkl')
#Using the random forest model
st.markdown("Enter the user details to check for churns")
# Collect user data
gender=st.selectbox("Gender",["Male","Female"])
senior_citizen=st.selectbox("Senior Citizen",["Yes","No"])
partner=st.selectbox("Partner",["Yes","No"])
dependents=st.selectbox("Dependents",["Yes","No"])
tenure=st.slider("Tenure",0,500,25)
months=st.slider("Number of months with the company",0,500,25)
phone_service=st.selectbox("Phone Service",["Yes","No"])
lines=st.selectbox("Multiple Lines",["Yes","No"])
internet_service=st.selectbox("Internet Service",["DSL","Fiber optic","No"])
backup=st.selectbox("Online Backup",["Yes","No"])
device_protection=st.selectbox("Device Protection",["Yes","No"])
tech_support=st.selectbox("Tech Support",["Yes","No"])
streaming_tv=st.selectbox("Streaming TV",["Yes","No"])
streaming_movies=st.selectbox("Streaming Movies",["Yes","No"])
security=st.selectbox("Online Security",["Yes","No"])
contract_type=st.selectbox("Contract Type",["Month-to-month","One year","Two year"])
billing=st.selectbox("Paperless Billing",["Yes","No"])
payment=st.selectbox("Payment Method",["Electronic check","Mailed check","Bank transfer","Credit card"])
monthly_charges=st.slider("Monthly Charges",0.0,100.0,25.0)
total_charges=st.slider("Total Charges",0.0,10000.0,25.0)
#Encode the categorical inputs
gender_encoded=0 if gender=='male' else 1
senior_citizen_encoded=0 if senior_citizen=='yes' else 1
partner_encoded=0 if partner=='yes' else 1
dependents_encoded=0 if dependents=='yes' else 1
security_encoded=0 if security=='yes' else 2
contract_type_encoded=0 if contract_type=='month-to-month' else 1
billing_encoded=0 if billing=='yes' else 1
payment_encoded=0 if payment=='electronic check' else 1
phone_service_encoded=0 if phone_service=='yes' else 1
lines_encoded=0 if lines=='yes' else 1
security_encoded=0 if security=='yes' else 1
internet_service_encoded=0 if internet_service=='dsl' else 1
backup_encoded=0 if backup=='yes' else 1
device_protection_encoded=0 if device_protection=='yes' else 1
tech_support_encoded=0 if tech_support=='yes' else 1
streaming_tv_encoded=0 if streaming_tv=='yes' else 1
streaming_movies_encoded=0 if streaming_movies=='yes' else 1
# Creating the array
features=np.array([gender_encoded,senior_citizen_encoded,partner_encoded,dependents_encoded,phone_service_encoded,contract_type_encoded,lines_encoded,security_encoded,billing_encoded,payment_encoded,monthly_charges,total_charges,internet_service_encoded,backup_encoded,device_protection_encoded,tech_support_encoded,streaming_tv_encoded,streaming_movies_encoded,months])
features=features.reshape(1,-1)
# Predict
if st.button("Predict"):
    prediction=model.predict(features)
    if prediction[0]==1:
        st.success("🎉 This customer **would have churned!**")
    else:
        st.error("💀 This customer **would not have churned.**")