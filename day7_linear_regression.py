import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("===== Day 7 - Machine Learning Basics =====")

# Load dataset
data = pd.read_csv("student_marks.csv")
print("\nDataset:")
print(data)

# Input and Output
X = data[["Hours"]]
y = data["Marks"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

print("\nPredicted Marks:")
print(predictions)

# Predict new value
new_prediction = model.predict(pd.DataFrame({"Hours": [7.5]}))

print("\nPredicted Marks for 7.5 Study Hours:")
print(new_prediction)

print("\n===== Day 7 Completed Successfully =====")