import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Student Performance Predictor")

st.title("🎓 Student Performance Predictor")

st.write("Predict the final student grade using Machine Learning")

# Load model
with open("model/student_model.pkl", "rb") as f:
    model = pickle.load(f)

# Inputs
studytime = st.slider("Study Time", 1, 4, 2)
absences = st.slider("Absences", 0, 30, 5)
g1 = st.slider("G1 Grade", 0, 20, 10)
g2 = st.slider("G2 Grade", 0, 20, 10)

if st.button("Predict Final Grade"):
    
    data = pd.DataFrame([[studytime, absences, g1, g2]],
                        columns=["studytime","absences","G1","G2"])

    prediction = model.predict(data)

    st.success(f"Predicted Final Grade: {round(prediction[0],2)}")