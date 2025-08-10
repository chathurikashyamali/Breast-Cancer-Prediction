import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model & scaler
model = joblib.load("breast_cancer_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🔬 Breast Cancer Diagnosis Prediction")
st.write("Enter tumor measurements to predict if malignant or benign.")

# Input fields
feature_names = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean',
    'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se',
    'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se',
    'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst',
    'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst',
    'concavity_worst', 'concave points_worst', 'symmetry_worst',
    'fractal_dimension_worst'
]

user_input = []
for feature in feature_names:
    val = st.number_input(f"{feature}", min_value=0.0, format="%.5f")
    user_input.append(val)

if st.button("Predict"):
    # Convert to array
    features_array = np.array(user_input).reshape(1, -1)
    # Scale
    features_scaled = scaler.transform(features_array)
    # Predict
    prediction = model.predict(features_scaled)[0]

    if prediction == 1:
        st.success("✅ Benign (Non-cancerous)")
    else:
        st.error("⚠️ Malignant (Cancerous)")

st.caption("Disclaimer: This tool is for educational purposes only and not for medical diagnosis.")