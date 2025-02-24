import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "basic-questionnaire-study_all_tidy.csv"
df = pd.read_csv(file_path)

# Extract chart type from 'responseId'
df["chartType"] = df["responseId"].str.extract(r'(vertical|horizontal|reverse)')

# Ensure necessary columns exist
if "answer" not in df.columns or "correctAnswer" not in df.columns or "chartType" not in df.columns:
    raise ValueError("Missing required columns: 'answer', 'correctAnswer', or 'chartType'.")

# Convert to numeric for comparison
df["answer"] = pd.to_numeric(df["answer"], errors="coerce")
df["correctAnswer"] = pd.to_numeric(df["correctAnswer"], errors="coerce")

# Create an accuracy column (1 if correct, 0 otherwise)
df["accuracy"] = (df["answer"] == df["correctAnswer"]).astype(int)

# Group by chart type and calculate mean accuracy
accuracy_results = df.groupby("chartType")["accuracy"].mean()

# Plot the results
plt.figure(figsize=(8, 5))
accuracy_results.sort_values().plot(kind="bar", color=["blue", "green", "red"])
plt.xlabel("Chart Type")
plt.ylabel("Accuracy (Proportion Correct)")
plt.title("Comparison of Answer Accuracy Across Chart Orientations")
plt.xticks(rotation=0)
plt.ylim(0, 1)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot
plt.show()
