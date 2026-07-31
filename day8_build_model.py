import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

print("===== Day 8 - Build the Model =====")

# Load dataset
data = pd.read_csv("student_marks.csv")

print("\nDataset:")
print(data)

# Features and Target
X = data[["Hours"]]
y = data["Marks"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Predictions
predictions = model.predict(X_test)

print("\nPredictions:")
print(predictions)

# Predict New Value
new_student = pd.DataFrame({"Hours": [7.5]})

predicted_marks = model.predict(new_student)

print("\nPredicted Marks for 7.5 Study Hours:")
print(predicted_marks[0])

# Model Evaluation
print("\nMean Absolute Error:")
print(mean_absolute_error(y_test, predictions))

print("\nR² Score:")
print(r2_score(y_test, predictions))

# Plot
plt.figure(figsize=(6,4))

plt.scatter(X, y, label="Actual Data")

plt.plot(X, model.predict(X), color="red", label="Regression Line")

plt.title("Linear Regression Model")

plt.xlabel("Hours Studied")

plt.ylabel("Marks")

plt.legend()

plt.tight_layout()

plt.savefig("linear_regression_model.png", dpi=300)

plt.show()

print("\n===== Day 8 Completed Successfully =====")