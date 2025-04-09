import pandas as pd
import numpy as np

# Create a MultiIndex DataFrame
index = pd.MultiIndex.from_product([['A', 'B'], [1, 2, 3]], names=['Letter', 'Number'])
df = pd.DataFrame(np.random.randint(10, 100, size=(6, 2)), index=index, columns=['Value1', 'Value2'])
print("MultiIndex DataFrame:")
print(df)

# Tuple-based indexing: select the row for ('A', 2)
print("\nTuple-based indexing (row ('A', 2)):")
print(df.loc[('A', 2)])

# Use stack() and unstack() to reshape the DataFrame
stacked = df.stack()
print("\nStacked DataFrame (Series):")
print(stacked)
unstacked = stacked.unstack()
print("\nUnstacked DataFrame (back to original):")
print(unstacked)

# Extract a cross-section from the MultiIndex with .xs()
xs_A = df.xs('A', level='Letter')
print("\nCross-section for Letter 'A':")
print(xs_A)

# Aggregate over a MultiIndex using groupby() with level specification (calculating mean)
grouped = df.groupby(level='Letter').mean()
print("\nAggregation (mean) by 'Letter':")
print(grouped)

# Rename the index axes and then flatten the MultiIndex
df_renamed = df.rename_axis(index={'Letter': 'Group', 'Number': 'Item'})
print("\nDataFrame with renamed index axes:")
print(df_renamed)
df_flat = df_renamed.reset_index()
print("\nFlattened DataFrame:")
print(df_flat)
