import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Used Car Price Prediction", page_icon="🚗", layout="centered")
MODEL_PATH = "linear_regression_model.joblib"
model = joblib.load(MODEL_PATH)

st.title("🚗 Used Car Price Prediction")
st.write("Enter the details of a used car to estimate its selling price. This is an educational estimate, not a guaranteed market quote.")

with st.form("car_form"):
    name = st.text_input("Car name / model", "Maruti Swift Dzire VDI")
    c1, c2 = st.columns(2)
    with c1:
        year = st.number_input("Manufacturing year", min_value=1980, max_value=2026, value=2018, step=1)
        km_driven = st.number_input("Kilometres driven", min_value=0, max_value=3000000, value=60000, step=1000)
        fuel = st.selectbox("Fuel type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
        seller_type = st.selectbox("Seller type", ["Individual", "Dealer", "Trustmark Dealer"])
        transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    with c2:
        owner = st.selectbox("Owner history", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])
        mileage = st.number_input("Mileage (km/l or kg)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)
        engine = st.number_input("Engine capacity (cc)", min_value=0.0, max_value=10000.0, value=1200.0, step=50.0)
        max_power = st.number_input("Maximum power (bhp)", min_value=0.0, max_value=2000.0, value=80.0, step=1.0)
        seats = st.selectbox("Seats", [2, 4, 5, 6, 7, 8, 9, 10, 12, 14], index=2)
    submitted = st.form_submit_button("Predict estimated price")

if submitted:
    brand = str(name).strip().split()[0].title() if str(name).strip() else "Unknown"
    data = pd.DataFrame([{
        "car_age": 2026 - int(year),
        "km_driven": int(km_driven),
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "owner": owner,
        "mileage(km/ltr/kg)": float(mileage),
        "engine": float(engine),
        "max_power": float(max_power),
        "seats": float(seats),
        "brand": brand
    }])
    predicted_price = float(model.predict(data)[0])
    st.subheader("Estimated selling price")
    st.success(f"₹{max(0, predicted_price):,.0f}")
    st.caption("The estimate depends on the dataset and model. Actual prices vary with condition, location, service history and market demand.")
