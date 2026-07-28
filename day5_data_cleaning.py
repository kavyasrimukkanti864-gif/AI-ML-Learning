import pandas as pd

print("===== Day 5 - Data Cleaning =====\n")

# Load dataset
data = pd.read_csv("student_scores.csv")

print("Original Dataset:\n")
print(data)

# Check missing values
print("\nMissing Values Count:")
print(data.isnull().sum())

# Fill missing values with column mean
data["Math"] = data["Math"].fillna(data["Math"].mean())
data["English"] = data["English"].fillna(data["English"].mean())

print("\nDataset After Filling Missing Values:\n")
print(data)

# Check duplicate rows
print("\nDuplicate Rows:")
print(data.duplicated())

print("\nNumber of Duplicate Rows:")
print(data.duplicated().sum())

# Remove duplicate rows
data = data.drop_duplicates()

print("\nDataset After Removing Duplicates:\n")
print(data)

# Dataset information
print("\nDataset Information:")
data.info()

# Statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Save cleaned dataset
data.to_csv("clean_student_scores.csv", index=False)

print("\nClean dataset saved as 'clean_student_scores.csv'")
print("\n===== Day 5 Completed Successfully =====")
