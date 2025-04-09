import pandas as pd
import numpy as np

# 1. Reindex a Series to include additional indices and fill missing values using fill_value and method.
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
new_index_series = ['a', 'b', 'c', 'd', 'e']

# Filling missing indices with a fixed fill_value.
s_reindexed_fill = s.reindex(new_index_series, fill_value=0)

# Filling missing values using forward fill.
s_reindexed_ffill = s.reindex(new_index_series, method='ffill')

print("Original Series:")
print(s)
print("\nSeries reindexed with fill_value=0:")
print(s_reindexed_fill)
print("\nSeries reindexed with forward fill (ffill):")
print(s_reindexed_ffill)

# 2. Reindex a DataFrame's rows and columns and analyze the shape and null values.
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])
new_rows = ['w', 'x', 'y', 'z', 'v']
new_cols = ['A', 'B', 'C']

df_reindexed = df.reindex(index=new_rows, columns=new_cols)

print("\nOriginal DataFrame:")
print(df)
print("\nDataFrame after reindexing rows and columns:")
print(df_reindexed)
print("\nShape of reindexed DataFrame:", df_reindexed.shape)
print("\nNull value check in reindexed DataFrame:")
print(df_reindexed.isnull())

# 3. Simulate a time series with missing dates. Use reindex() and interpolate() to fill gaps.
# Create a full time series
date_range_full = pd.date_range(start="2025-01-01", periods=10, freq='D')
ts_full = pd.Series(range(10), index=date_range_full)

# Simulate missing dates by dropping some dates.
ts_missing = ts_full.drop(ts_full.index[[2, 5, 7]])
print("\nTime series with missing dates:")
print(ts_missing)

# Reindex to the full date range (introducing NaN for missing dates)
ts_reindexed = ts_missing.reindex(date_range_full)
print("\nTime series reindexed (with NaN for missing dates):")
print(ts_reindexed)

# Interpolate to fill the gaps using linear interpolation.
ts_interpolated = ts_reindexed.interpolate(method='linear')
print("\nTime series after interpolation:")
print(ts_interpolated)


# 4. Write a function that reindexes a Series/DataFrame to a desired index with a selected method.
def custom_reindex(data, new_index, method=None, fill_value=None):
    """
    Reindex a Series or DataFrame to the new index with optional fill method or fill_value.

    Parameters:
      data      : Series or DataFrame to reindex.
      new_index : The desired new index.
      method    : Method for filling missing values (e.g., 'ffill' or 'bfill').
      fill_value: Static value to fill missing entries if method is None.

    Returns:
      The reindexed data.
    """
    return data.reindex(new_index, method=method, fill_value=fill_value)


# Example usage on a Series:
s_custom = custom_reindex(s, new_index_series, fill_value=-1)
print("\nCustom reindexed Series with fill_value = -1:")
print(s_custom)

# 5. Compare reindex() with sort_index() and sort_values() using sample data.
# Create an unsorted sample Series.
unsorted_series = pd.Series([3, 1, 2], index=['b', 'a', 'c'])

# Use reindex() to order according to a specified index.
ordered_series = unsorted_series.reindex(['a', 'b', 'c'])
# Sort the Series by index.
sorted_by_index = unsorted_series.sort_index()
# Sort the Series by its values.
sorted_by_values = unsorted_series.sort_values()

print("\nUnsorted Series:")
print(unsorted_series)
print("\nSeries reindexed to order ['a','b','c']:")
print(ordered_series)
print("\nSeries sorted by index:")
print(sorted_by_index)
print("\nSeries sorted by values:")
print(sorted_by_values)
