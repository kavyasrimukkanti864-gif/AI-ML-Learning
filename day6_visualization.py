import pandas as pd
import matplotlib.pyplot as plt

print("===== Day 6 - Data Visualization =====")

# Load dataset
data = pd.read_csv("clean_student_scores.csv")

print("\nDataset Preview:")
print(data.head())

# -------------------------
# Line Chart
# -------------------------
plt.figure(figsize=(8,5))
plt.plot(data["Name"], data["Math"], marker="o")
plt.title("Math Scores")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line_chart.png", dpi=300)
plt.show()

# -------------------------
# Bar Chart
# -------------------------
plt.figure(figsize=(8,5))
plt.bar(data["Name"], data["Science"])
plt.title("Science Scores")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png", dpi=300)
plt.show()

# -------------------------
# Scatter Plot
# -------------------------
plt.figure(figsize=(6,5))
plt.scatter(data["Math"], data["Science"])
plt.title("Math vs Science")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.tight_layout()
plt.savefig("scatter_plot.png", dpi=300)
plt.show()

print("\nDay 6 Completed Successfully!")


