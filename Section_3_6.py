import pandas as pd
import numpy as np

# Arithmetic Operations and Broadcasting
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Add a scalar to all elements
print("Scalar Broadcast:\n", df + 10)

# Broadcast a Series by columns
print("Column-wise Broadcast:\n", df + pd.Series({'A': 100, 'B': 200, 'C': 300}))

# Broadcast a Series by rows
print("Row-wise Broadcast:\n", df.add(pd.Series([10, 20, 30], index=df.index), axis=0))


# Safe Arithmetic with Fill Values
df1 = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})
df2 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})

# Using .add() with a fill_value to handle NaNs
print("Safe Addition:\n", df1.add(df2, fill_value=0))


# Row-wise and Column-wise Statistics
print("Row statistics (mean, sum):\n", df.agg(['mean', 'sum'], axis=1))
print("Column statistics (mean, sum):\n", df.agg(['mean', 'sum'], axis=0))
print("Row Means (via .apply()):\n", df.apply(np.mean, axis=1))


# Normalization Using Axis Parameters
# Normalize each row
row_norm = df.apply(lambda row: (row - row.mean()) / row.std(), axis=1)
# Normalize each column
col_norm = df.apply(lambda col: (col - col.mean()) / col.std(), axis=0)

print("Row-normalized DataFrame:\n", row_norm)
print("Column-normalized DataFrame:\n", col_norm)


# Standardization Function (z-score normalization)
def standardize(df):
    return (df - df.mean()) / df.std()

print("Standardized DataFrame:\n", standardize(df))
