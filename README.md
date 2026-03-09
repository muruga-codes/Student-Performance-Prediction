🎓 Student Performance Prediction (Machine Learning Project)

 📌 Project Overview

This project predicts a student's **final grade (G3)** based on academic and behavioral factors using **Machine Learning**.
The goal is to help identify patterns in student performance and build a model that can estimate final outcomes from previous grades and study habits.

The model is trained using the **Student Performance Dataset** and deployed as an **interactive web application using Streamlit**.

🚀 Features

* Data preprocessing and feature selection
* Machine Learning model training using **Random Forest Regressor**
* Model serialization using **Pickle**
* Interactive **Streamlit Web App**
* Real-time prediction of student performance

🧠 Machine Learning Workflow

1. Data Loading and Exploration
2. Feature Selection
3. Train-Test Split
4. Model Training (Random Forest Regressor)
5. Model Evaluation
6. Model Saving (`.pkl`)
7. Web App Integration using Streamlit

 📊 Dataset Information

The dataset contains student academic records and demographic information.

Key features used in this project:

| Feature    | Description                   |
| ---------- | ----------------------------- |
| Study Time | Weekly study time             |
| Absences   | Number of school absences     |
| G1         | First period grade            |
| G2         | Second period grade           |
| G3         | Final grade (Target variable) |

Dataset Source: **UCI Machine Learning Repository – Student Performance Dataset**


🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* Pickle

 📂 Project Structure

Student-Performance-Prediction
│
├── data
│   └── student-mat.csv
│
├── notebooks
│   └── model_training.ipynb
│
├── apps
│   └── app.py
│
├── model
│   └── student_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/student-performance-prediction.git

Navigate to the project folder:

cd student-performance-prediction
Install dependencies:

pip install -r requirements.txt

▶️ Running the Application

Run the Streamlit application:

streamlit run apps/app.py

The application will open in your browser at:

http://localhost:8501

🖥️ Web Application

The Streamlit application allows users to input:

* Study Time
* Absences
* G1 Grade
* G2 Grade

The trained model then predicts the final student grade (G3).

📈 Model Used

Random Forest Regressor

Why Random Forest?

* Handles non-linear relationships well
* Robust against overfitting
* Performs well with tabular datasets

🔮 Future Improvements

* Add more input features
* Perform hyperparameter tuning
* Add model evaluation metrics
* Deploy the application online
* Build a more advanced dashboard UI

🌍 Deployment (Optional)

This project can be deployed using:

* Streamlit Cloud
* Hugging Face Spaces
* Docker
* AWS / Azure

👨‍💻 Author

Muruganantham

Aspiring Machine Learning Engineer building projects and sharing progress publicly.


⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork the project
📢 Share it with others


📜 License

This project is open-source and available under the **MIT License**.
