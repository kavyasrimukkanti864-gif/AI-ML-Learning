import pandas as pd

print("===== Day 4 - Pandas Basics =====\n")

# Load the dataset
data = pd.read_csv("student_scores.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(data.head())

# Display the last 5 rows
print("\nLast 5 Rows:")
print(data.tail())

# Display dataset information
print("\nDataset Information:")
data.info()

# Display number of rows and columns
print("\nShape of Dataset:")
print(data.shape)

# Display column names
print("\nColumn Names:")
print(data.columns)

# Display statistical summary
print("\nStatistical Summary:")
print(data.describe())

print("\n===== Day 4 Completed Successfully =====")