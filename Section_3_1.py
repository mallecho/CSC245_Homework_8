import pandas as pd

# Create Series
exam_scores = pd.Series([88, 95, 70, 85, 92],
                        index=["Alice", "Bob", "Charlie", "David", "Eva"])

# Find the top scorer
top_scorer = exam_scores.idxmax()

# Find all students scoring above the mean
mean_score = exam_scores.mean()
above_mean = exam_scores[exam_scores > mean_score]

print("Top Scorer:", top_scorer)
print("Above Mean:\n", above_mean)

# Create DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 21, 19, 22, 20],
    "Score": [88, 95, 70, 85, 92],
    "Passed": [True, True, False, True, True]
}
df = pd.DataFrame(data)

# Data types of each column
data_types = df.dtypes

# Summary statistics
summary_stats = df.describe(include='all')  # Include all column types

print("Data Types:\n", data_types)
print("\nSummary Statistics:\n", summary_stats)

# Load CSV into DataFrame
df_from_csv = pd.read_csv("top_scorer.csv")  # Replace with your actual file path

# Display first and last 5 rows
print("First 5 Rows:\n", df_from_csv.head())
print("\nLast 5 Rows:\n", df_from_csv.tail())

# Show .info() and .describe()
print("\nInfo:\n")
df_from_csv.info()
print("\nDescribe:\n", df_from_csv.describe(include='all'))

# Load the CSV file into a DataFrame
df_csv = pd.read_csv("top_scorer.csv")

# Display the first and last 5 rows
print("First 5 Rows:\n", df_csv.head())
print("\nLast 5 Rows:\n", df_csv.tail())

# Show .info() and .describe()
print("\nInfo:\n")
df_csv.info()
print("\nDescribe:\n", df_csv.describe(include='all'))

# Create a Series with datetime indices
date_range = pd.date_range(start="2025-01-01", periods=10, freq='D')
scores = [85.5, 92.0, 78.0, 90.5, 88.5, 75.0, 82.0, 88.0, 68.5, 91.0]
time_series = pd.Series(scores, index=date_range)

# Slice the series using index-based access
sliced_series = time_series["2025-01-03":"2025-01-06"]

print("Sliced Series:\n", sliced_series)

# Create two Series with non-aligned indices
series1 = pd.Series([85, 92, 78], index=["Alice", "Bob", "Charlie"])
series2 = pd.Series([90, 88, 75], index=["Bob", "Eva", "Fiona"])

# Perform arithmetic operation
result = series1 + series2

print("Result of Arithmetic:\n", result)

#Pandas aligns the indices before computing
#Since Bob appears in both series, his numbers were added,
#which is why in the output, Bob has the 182.0 number
#while the others have NaN,not a number, since
#they don't have matching indices

