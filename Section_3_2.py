import pandas as pd

# --- 1. Create a Custom DataFrame ---
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
    'Age': [23, 27, 22, 32, 29],
    'Score': [85.5, 92.0, 78.0, 90.5, 88.5]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# --- 2. Demonstrate the Difference Between .loc and .iloc ---
# .loc uses labels, while .iloc uses integer positions.
print("\nUsing .loc to get 'Score' of row with label 2 (third row):")
print(df.loc[2, 'Score'])  # Uses label/index 2

print("\nUsing .iloc to get 'Score' of the third row, third column:")
print(df.iloc[2, 2])  # Uses zero-based positional indexing

# 3. Filter Rows Using Conditional Logic
# Filter rows where Score > 85.
filtered_df = df[df['Score'] > 85]
print("\nRows where 'Score' > 85:")
print(filtered_df)

# 4. Create a Boolean Mask f

bool_mask = df[['Age', 'Score']] > 80
print("\nBoolean mask for elements in 'Age' and 'Score' > 80:")
print(bool_mask)

# 5. Chained Indexing Pitfalls and Using .copy() to avoid Them
# Chained indexing: filtering then selecting a column.
chained = df[df['Score'] > 85]['Score']
print("\nChained indexing result (before modification):")
print(chained)

# modify, first create an explicit copy.
chained_copy = chained.copy()
chained_copy[:] = 100
print("\nModified copy of chained result (all set to 100):")
print(chained_copy)

# The original DataFrame remains unchanged.
print("\nOriginal DataFrame remains unchanged:")
print(df)

# 6. Create a DataFrame with a Custom Index and Perform Row/Column Slicing
df2 = pd.DataFrame({
    'ID': ['A1', 'B2', 'C3', 'D4', 'E5'],
    'Score': [88, 92, 78, 95, 85],
    'Passed': [True, True, False, True, True]
})
df2.set_index('ID', inplace=True)
print("\nDataFrame with custom index:")
print(df2)

# Using .loc for label-based slicing (inclusive of endpoints).
print("\nUsing .loc to slice rows 'B2' to 'D4':")
print(df2.loc['B2':'D4'])

# Using .iloc for integer-based slicing (end index is exclusive).
print("\nUsing .iloc to slice rows 1 to 3:")
print(df2.iloc[1:4])
