import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.model import load_model
import numpy as np

st.title("🏡 Real Estate Price Predictor")

model = load_model("models/real_estate_model.pkl")

sqft = st.number_input("Enter area (in sqft):", 500, 10000, 1500)

if st.button("Predict"):
    prediction = model.predict(np.array([[sqft]]))
    st.success(f"Predicted price: ${prediction[0]:,.2f}")
