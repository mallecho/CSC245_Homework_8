import pandas as pd

# 1. Create a Series with a custom index and show that Index objects are immutable.
custom_index = pd.Index(['A', 'B', 'C'])
s = pd.Series([1, 2, 3], index=custom_index)
print("Custom Series:")
print(s)

# Attempt to modify the index to show immutability.
try:
    s.index[0] = 'Z'
except TypeError as e:
    print("\nIndex objects are immutable:", e)

# 2. Generate a hierarchical (MultiIndex) for a Series and access subsets using multiple levels.
tuples = [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
multi_index = pd.MultiIndex.from_tuples(tuples, names=['Letter', 'Number'])
s_multi = pd.Series([100, 200, 300, 400], index=multi_index)
print("\nHierarchical (MultiIndex) Series:")
print(s_multi)

# Accessing a subset: all data for Letter 'A'
print("\nSubset for 'Letter' A:")
print(s_multi.loc['A'])

# 3. Create a DataFrame with a MultiIndex on rows, then perform .swaplevel() and .sort_index().
arrays = [['X', 'X', 'Y', 'Y'], ['a', 'b', 'a', 'b']]
multi_index_df = pd.MultiIndex.from_arrays(arrays, names=['Upper', 'Lower'])
df_multi = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=multi_index_df)
print("\nOriginal MultiIndex DataFrame:")
print(df_multi)

# Swap the levels of the MultiIndex.
df_swapped = df_multi.swaplevel('Upper', 'Lower')
print("\nDataFrame after swaplevel:")
print(df_swapped)

# Sort the DataFrame by index.
df_sorted = df_swapped.sort_index()
print("\nDataFrame after sort_index:")
print(df_sorted)

# 4. Reset and set index on a DataFrame, demonstrating the effects of 'drop' and 'inplace'.
# Reset the index: current MultiIndex becomes columns.
df_reset = df_multi.reset_index()
print("\nDataFrame after reset_index:")
print(df_reset)

# Set a new index ('Lower') with drop=True and modify it inplace.
df_reset.set_index('Lower', inplace=True, drop=True)
print("\nDataFrame after set_index('Lower', drop=True, inplace=True):")
print(df_reset)

# 5. Demonstrate arithmetic between DataFrames with mismatched indices.
df1 = pd.DataFrame({'A': [1, 2]}, index=['x', 'y'])
df2 = pd.DataFrame({'A': [10, 20]}, index=['y', 'z'])
result = df1 + df2
print("\nArithmetic result of DataFrames with mismatched indices:")
print(result)
