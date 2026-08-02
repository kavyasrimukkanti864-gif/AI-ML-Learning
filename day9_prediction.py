import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("===== Day 9 - Prediction =====")

# Load dataset
data = pd.read_csv("student_marks.csv")

# Features and Target
X = data[["Hours"]]
y = data["Marks"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Predict new values
new_students = pd.DataFrame({
    "Hours":[3.5,5,7.5,9]
})

predictions = model.predict(new_students)

print("\nPredictions")

for hour, mark in zip(new_students["Hours"], predictions):
    print(f"Study Hours: {hour} --> Predicted Marks: {mark:.2f}")

print("\n===== Day 9 Completed Successfully =====")