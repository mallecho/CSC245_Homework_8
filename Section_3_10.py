import pandas as pd

# --- One-to-One Merge ---
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value2': [4, 5, 6]})
one_to_one = pd.merge(df1, df2, on='key')
print("One-to-One Merge:\n", one_to_one, "\n")

# --- Many-to-One Merge ---
df3 = pd.DataFrame({
    'dept': ['Sales', 'Sales', 'HR', 'HR', 'IT'],
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
})
df4 = pd.DataFrame({
    'dept': ['Sales', 'HR', 'IT'],
    'manager': ['Marry', 'John', 'Alice']
})
many_to_one = pd.merge(df3, df4, on='dept')
print("Many-to-One Merge:\n", many_to_one, "\n")

# --- Many-to-Many Merge ---
df5 = pd.DataFrame({'key': ['X', 'X', 'Y'], 'left_val': [10, 20, 30]})
df6 = pd.DataFrame({'key': ['X', 'X', 'Z'], 'right_val': [100, 200, 300]})
many_to_many = pd.merge(df5, df6, on='key', how='inner')
print("Many-to-Many Merge:\n", many_to_many, "\n")

# --- Using on=, left_on=, right_on=, and suffixes= ---
df_left = pd.DataFrame({'l_key': ['K0', 'K1', 'K2'], 'shared': [1, 2, 3]})
df_right = pd.DataFrame({'r_key': ['K0', 'K1', 'K2'], 'shared': [4, 5, 6]})
merge_diff_keys = pd.merge(df_left, df_right, left_on='l_key', right_on='r_key',
                           suffixes=('_L', '_R'))
print("Merge with different key names and suffixes:\n", merge_diff_keys, "\n")

# --- Joining on Indexes ---
df_index1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
df_index2 = pd.DataFrame({'B': [4, 5]}, index=['b', 'c'])
join_left = df_index1.join(df_index2, how='left')
join_right = df_index1.join(df_index2, how='right')
join_outer = df_index1.join(df_index2, how='outer')
print("Join on Index (left join):\n", join_left, "\n")
print("Join on Index (right join):\n", join_right, "\n")
print("Join on Index (outer join):\n", join_outer, "\n")

# --- Merging Three or More DataFrames with indicator ---
df7 = pd.DataFrame({'key': ['A', 'B'], 'val1': [10, 20]})
df8 = pd.DataFrame({'key': ['B', 'C'], 'val2': [30, 40]})
df9 = pd.DataFrame({'key': ['B', 'D'], 'val3': [50, 60]})

# First merge of df7 and df8 with indicator
merge_78 = pd.merge(df7, df8, on='key', how='outer', indicator=True)
print("Merge of df7 and df8 (with indicator):\n", merge_78, "\n")

# Drop the indicator column to avoid conflict
merge_78_clean = merge_78.drop(columns='_merge')

# Merge the cleaned result with df9; indicator will now work without conflict.
merge_all = pd.merge(merge_78_clean, df9, on='key', how='outer', indicator=True)
print("Merge of three DataFrames (with indicator):\n", merge_all)
