import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("data/student-mat.csv", sep=";")

# Only 4 features used in app
X = df[["studytime", "absences", "G1", "G2"]]
y = df["G3"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save model
with open("model/student_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
print(model.feature_names_in_)