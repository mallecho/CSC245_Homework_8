import pandas as pd
import numpy as np

# Create a DataFrame with intentional NaN values.
df = pd.DataFrame({
    'A': [1, np.nan, 3, 4],
    'B': [np.nan, 2, np.nan, 5],
    'C': [1, 2, 3, np.nan]
})
print("Initial DataFrame:")
print(df)

# Locate missing and non-missing values.
print("\nMissing values (isnull):")
print(df.isnull())
print("\nNon-missing values (notnull):")
print(df.notnull())

# Drop rows with any missing data.
df_drop_rows = df.dropna()
print("\nAfter dropping rows with any NaNs:")
print(df_drop_rows)

# Drop columns that do not have at least 3 non-null values.
df_drop_cols = df.dropna(axis=1, thresh=3)
print("\nAfter dropping columns with less than 3 non-null values:")
print(df_drop_cols)

# Fill missing data using a constant value.
df_fill_const = df.fillna(0)
print("\nAfter filling NaNs with constant 0:")
print(df_fill_const)

# Fill missing data using forward-fill.
df_ffill = df.ffill()
print("\nAfter forward-fill (using .ffill()):")
print(df_ffill)

# Fill missing data using backward-fill.
df_bfill = df.bfill()
print("\nAfter backward-fill (using .bfill()):")
print(df_bfill)

# Create and interpolate a time series with missing dates.
ts = pd.Series(
    [1, np.nan, 3, np.nan, 5],
    index=pd.date_range("2025-01-01", periods=5)
)
print("\nTime series with gaps:")
print(ts)
ts_interp = ts.interpolate(method='linear')
print("\nAfter interpolation:")
print(ts_interp)


# Reusable cleaning pipeline function
def clean_missing_data(df, fill_value=None, method=None, drop_threshold=0):
    """
    Cleans missing values in a DataFrame.

    Parameters:
      df            : Input DataFrame.
      fill_value    : Constant value to fill NaNs (if provided).
      method        : 'ffill' or 'bfill' for a filling method.
      drop_threshold: Drop rows with non-null count less than this threshold.

    Returns:
      Cleaned DataFrame.
    """
    cleaned = df.copy()
    if drop_threshold > 0:
        cleaned = cleaned.dropna(thresh=drop_threshold, axis=0)
    if fill_value is not None:
        cleaned = cleaned.fillna(fill_value)
    elif method == 'ffill':
        cleaned = cleaned.ffill()
    elif method == 'bfill':
        cleaned = cleaned.bfill()
    return cleaned


# Apply the cleaning pipeline.
cleaned_df = clean_missing_data(df, fill_value=99, drop_threshold=2)
print("\nCleaned DataFrame using the cleaning pipeline:")
print(cleaned_df)
