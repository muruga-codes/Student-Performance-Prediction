import streamlit as st
import pickle
import pandas as pd

st.title("🎓 Student Performance Predictor")

# Load model
with open("model/student_model.pkl", "rb") as f:
    model = pickle.load(f)

# Inputs
studytime = st.slider("Study Time", 1, 4, 2)
absences = st.slider("Absences", 0, 30, 5)
g1 = st.slider("G1 Grade", 0, 20, 10)
g2 = st.slider("G2 Grade", 0, 20, 10)

# Prediction
if st.button("Predict Final Grade"):
    
    data = pd.DataFrame([[studytime, absences, g1, g2]],
                        columns=["studytime","absences","G1","G2"])

    prediction = model.predict(data)
    st.success(f"Predicted Final Grade: {round(prediction[0],2)}")

# 👉 ADD HERE (Feature Importance Section)

st.subheader("📊 Feature Importance")

# Example values (or load from model)
features = pd.DataFrame({
    "Feature": ["G2", "G1", "studytime", "absences"],
    "Importance": [0.4, 0.3, 0.2, 0.1]
})

st.bar_chart(features.set_index("Feature"))