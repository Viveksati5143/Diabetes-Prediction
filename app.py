import streamlit as st
import pickle
import numpy as np
import pandas as pd


model = pickle.load(open('model.pkl','rb'))

st.title("Diabetes Prediction System")

col1,col2,col3 = st.columns(3)
with col1:
    ip_Pregnancies=st.text_input('Enter No. of pregnancies: ')
with col2:
    ip_Glucose=st.text_input('Enter Glucose level: ')
with col3:
    ip_BloodPressure=st.text_input('Enter BloodPressure Level: ')
with col1:
    ip_SkinThickness=st.text_input('Enter SkinThickness: ')
with col2:
    ip_Insulin=st.text_input('Enter Insulin Level: ')
with col3:
    ip_BMI=st.text_input('Enter BMI : ')
with col1:
    ip_DiabetesPedigreeFunction=st.text_input('Enter DiabetesPedigreeFunction: ')
with col2:
    ip_Age=st.text_input('Enter Age: ')

res = ''

if st.button('Check Result'):
   diab_prediction =  model.predict([[ip_Pregnancies,ip_Glucose,ip_BloodPressure,ip_SkinThickness,ip_Insulin,ip_BMI,ip_DiabetesPedigreeFunction,ip_Age]])

   if(diab_prediction[0] == 0):
       res = 'The Person is Not Diabetic'
   else:
       res = 'Diabetic'

st.success(res)