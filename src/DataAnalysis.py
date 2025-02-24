import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import bootstrap

# Load dataset
file_path = "basic-questionnaire-study_all_tidy.csv"
df = pd.read_csv(file_path)

# Extract chart type from 'responseId'
df["chartType"] = df["responseId"].str.extract(r'(vertical_bar|horizontal_bar|reverse_bar)')

# Ensure necessary columns exist
if "answer" not in df.columns or "correctAnswer" not in df.columns or "chartType" not in df.columns:
    raise ValueError("Missing required columns: 'answer', 'correctAnswer', or 'chartType'.")

# Convert to numeric
df["answer"] = pd.to_numeric(df["answer"], errors="coerce")
df["correctAnswer"] = pd.to_numeric(df["correctAnswer"], errors="coerce")

# Calculate absolute error
df["Error"] = np.abs(df["answer"] - df["correctAnswer"])

# Calculate log2Error (Cleveland & McGill method)
df["log2Error"] = np.log2(df["Error"] + 1/8)
df.loc[df["Error"] == 0, "log2Error"] = 0  # Handling perfect matches

# Group by chart type and calculate mean log2Error
error_results = df.groupby("chartType")["log2Error"].mean()

# Bootstrap 95% confidence intervals for log2Error
def bootstrap_ci(data, n_resamples=1000):
    res = bootstrap((data.dropna(),), np.mean, n_resamples=n_resamples, confidence_level=0.95, method='percentile')
    return res.confidence_interval.low, res.confidence_interval.high

ci_intervals = df.groupby("chartType")["log2Error"].apply(bootstrap_ci)

# Extract lower and upper bounds
error_results = error_results.to_frame()
error_results["CI Lower"] = ci_intervals.apply(lambda x: x[0])
error_results["CI Upper"] = ci_intervals.apply(lambda x: x[1])

# Prepare error bars
yerr_values = np.vstack([
    error_results["log2Error"] - error_results["CI Lower"],
    error_results["CI Upper"] - error_results["log2Error"]
])

# Plot results with confidence intervals
plt.figure(figsize=(10, 6))
sns.barplot(x=error_results.index, y=error_results["log2Error"], hue=error_results.index, legend=False, palette="muted")
plt.errorbar(error_results.index, error_results["log2Error"], yerr=yerr_values, fmt='none', capsize=5, color='black')
plt.xlabel("Chart Type")
plt.ylabel("Average log2Error (Lower is Better)")
plt.title("Comparison of log2Error Across Chart Types with 95% Confidence Intervals")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save the plot
plt.savefig("Log2Error_Comparison.png", dpi=300, bbox_inches="tight")
plt.show()
