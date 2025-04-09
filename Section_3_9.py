import pandas as pd

# Concatenate Series along different axes
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

# Concatenate Series along rows (axis=0)
cat_series = pd.concat([s1, s2])
print("Concatenated Series (axis=0):")
print(cat_series, "\n")

# Concatenate Series along columns (axis=1)
cat_series_axis1 = pd.concat([s1, s2], axis=1)
print("Concatenated Series (axis=1):")
print(cat_series_axis1, "\n")


# Use keys= and names= parameters for hierarchical indexing during concatenation
cat_with_keys = pd.concat([s1, s2], keys=["first", "second"], names=["Group"])
print("Concatenated Series with keys and group name:")
print(cat_with_keys, "\n")


# Append rows to a DataFrame using pd.concat() (instead of .append())
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5], 'B': [6]})
appended_df = pd.concat([df1, df2], ignore_index=True)
print("Appended DataFrame using pd.concat():")
print(appended_df, "\n")


# Concatenate DataFrames with overlapping and non-overlapping columns
df3 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df4 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]})
cat_overlap = pd.concat([df3, df4], ignore_index=True)
print("Concatenated DataFrames with overlapping/non-overlapping columns:")
print(cat_overlap, "\n")


# Function to combine a list of DataFrames and clean resulting index/columns
def combine_and_clean(df_list, reset=True):
    """
    Combines a list of DataFrames using pd.concat.
    Optionally resets the index for a clean result.
    """
    combined = pd.concat(df_list)
    if reset:
        combined = combined.reset_index(drop=True)
    return combined

# Demonstrate the combine_and_clean function
df_a = pd.DataFrame({'X': [10, 20]})
df_b = pd.DataFrame({'X': [30, 40]})
df_c = pd.DataFrame({'X': [50, 60]})
cleaned_combined = combine_and_clean([df_a, df_b, df_c])
print("Combined and cleaned DataFrame:")
print(cleaned_combined)
