
import streamlit as st
import pickle

# Load model
with open("apps/model/student_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Student Performance Prediction")

studytime = st.slider("Study Time", 1, 4)
absences = st.slider("Absences", 0, 30)
g1 = st.slider("G1 Grade", 0, 20)
g2 = st.slider("G2 Grade", 0, 20)

if st.button("Predict"):
    prediction = model.predict([[studytime, absences, g1, g2]])
    st.success(f"Predicted Final Grade: {prediction[0]:.2f}")
