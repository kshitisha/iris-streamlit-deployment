import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load("svm_model.pkl")
scaler = joblib.load("scaler.pkl")


st.title("iris flower prediction app by Kshitisha")

st.markdown("predict the iris species using sepal and petal measurements.")

st.sidebar.header("input features")

def get_input():
    sepal_length = st.sidebar.slider("Sepal Length", 4.0, 8.0, 5.8)
    sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.5, 3.0)
    petal_length = st.sidebar.slider("Petal Length", 1.0, 7.0, 4.35)
    petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 1.3)

    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    return pd.DataFrame(data, index=[0])

    return pd.DataFrame(data, index=[0])

input_df = get_input()
st.subheader("input Data")
st.write(input_df)

scaled_input = scaler.transform(input_df)
prediction = model.predict(scaled_input)

#output
st.subheader("prediction")
st.success(f"Predicted Iris Species: **{prediction[0]}**")
st.subheader("feature breakdown")
st.bar_chart(input_df.T)
