import streamlit as st
import numpy as np
import joblib

# ── Load model once ────────────────────────────────
@st.cache_resource



def load_model():
    return joblib.load('rf_model.pkl')
        
model = load_model()

# ── Page title ─────────────────────────────────────
st.title("❤️ Cardiovascular Risk Predictor")
st.write("Enter patient details to estimate cardiovascular disease risk.")

# ── Inputs in sidebar ──────────────────────────────
st.sidebar.header("Patient Details")
age    = st.sidebar.slider("Age",             10, 100, 45)
gender = st.sidebar.selectbox('Gender',options = [0,1],format_func=lambda x : 'Male' if x==1 else 'Female')
ap_hi  = st.sidebar.number_input("Systolic BP",  80, 250, 120)
ap_lo  = st.sidebar.number_input("Diastolic BP", 50, 150, 80)
chol   = st.sidebar.selectbox("Cholesterol, 1 = Yes, 0 = No",   [1,0])
glucose= st.sidebar.selectbox("Glucose, 1 = Yes, 0 = No",   [1,0])
smoke  = st.sidebar.selectbox("Smoker, 1 = Yes, 0 = No",        [0, 1])
alcohol  = st.sidebar.selectbox("Alcohol, 1 = Yes, 0 = No",   [1,0])
activity = st.sidebar.selectbox("Actitviy, 1 = Yes, 0 = No",   [1,0])
bmi = st.sidebar.number_input('BMI' , 10,50)

# ── Predict on button click ────────────────────────
if st.button("Predict Risk"):
    X = np.array([[age, gender,ap_hi, ap_lo, chol,glucose, smoke,alcohol,activity,bmi]])
    prob = model.predict_proba(X)[0][1]

    col1, col2 = st.columns(2)
    col1.metric("Risk Probability", f"{prob*100:.1f}%")
    col2.metric("Model Accuracy", ' = 76%')

    if   prob < 0.4: st.success("✅ Low Risk")
    elif prob < 0.7: st.warning("⚠️ Moderate Risk")
    else:            st.error  ("🚨 High Risk")

