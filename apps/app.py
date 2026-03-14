import streamlit as st
import pickle
import pandas as pd

with open("apps/model/student_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Student Performance Predictor")

studytime = st.slider("Study Time", 1, 4)
absences = st.slider("Absences", 0, 30)
g1 = st.slider("G1 Grade", 0, 20)
g2 = st.slider("G2 Grade", 0, 20)

if st.button("Predict"):

    input_data = pd.DataFrame(
        [[studytime, absences, g1, g2]],
        columns=["studytime","absences","G1","G2"]
    )

    prediction = model.predict(input_data)

    st.success(f"Predicted Final Grade: {prediction[0]:.2f}")
st.sidebar.title("Project Info")
st.sidebar.write("Student Performance ML Project")