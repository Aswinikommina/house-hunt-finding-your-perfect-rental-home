import streamlit as st import pandas as pd from sklearn.linear_model
import LinearRegression import numpy as np

st.title(“House Hunt: Find Your Perfect Rental Home”)

Sample dataset

data = { “Area”: [500, 800, 1000, 1200, 1500], “Bedrooms”: [1, 2, 2, 3,
3], “Rent”: [8000, 12000, 15000, 20000, 25000] }

df = pd.DataFrame(data)

X = df[[“Area”, “Bedrooms”]] y = df[“Rent”]

model = LinearRegression() model.fit(X, y)

area = st.number_input(“Enter Area (sq ft):”) bedrooms =
st.number_input(“Enter Number of Bedrooms:”)

if st.button(“Predict Rent”): prediction = model.predict([[area,
bedrooms]]) st.success(f”Estimated Rent: ₹{int(prediction[0])}“)
