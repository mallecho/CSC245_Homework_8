import numpy as np
import pandas as pd

# 1. Apply NumPy universal functions to a Series and observe index preservation.
s = pd.Series([0, 1, 2], index=['a', 'b', 'c'])
exp_s = np.exp(s)             # Applying np.exp: index is preserved.
log_s = np.log(s + 1)         # Using s+1 to avoid log(0) error.
print("Original Series:\n", s, "\n")
print("After np.exp (index preserved):\n", exp_s, "\n")
print("After np.log(s+1) (index preserved):\n", log_s, "\n")


# 2. Apply element-wise operations on two Series with partially overlapping indices.
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3], index=['b', 'c', 'd'])
result = s1 * s2
print("s1:\n", s1)
print("\ns2:\n", s2)
print("\nElement-wise multiplication (only overlapping indices computed):\n", result, "\n")
# Explanation: Only indices 'b' and 'c' exist in both Series. Unmatched indices yield NaN.


# 3. Use np.where on a Series for conditional vectorized logic.
s_cond = pd.Series([5, 15, 25, 35], index=list('abcd'))
# Vectorized condition: if value > 20, label as 'High', otherwise 'Low'
cond_result = pd.Series(np.where(s_cond > 20, 'High', 'Low'), index=s_cond.index)
print("Conditional np.where result on Series:\n", cond_result, "\n")


# 4. Create a function that applies a ufunc and returns a cleaned result.
def apply_ufunc_clean(series, func, fill_value=0):
    """
    Applies a ufunc to a Series after filling NaNs.
    Returns the resulting Series.
    """
    cleaned_series = series.fillna(fill_value)
    return func(cleaned_series)

s_with_nan = pd.Series([0, np.nan, 2, 3], index=['a','b','c','d'])
sqrt_result = apply_ufunc_clean(s_with_nan, np.sqrt, fill_value=0)
print("Series with NaNs:\n", s_with_nan)
print("\nResult after applying np.sqrt (with NaN filled by 0):\n", sqrt_result, "\n")


# 5. Compare element-wise operations on Series vs. NumPy arrays.
# Create two Series and their corresponding NumPy arrays.
s1 = pd.Series(np.random.rand(1000), index=range(1000))
s2 = pd.Series(np.random.rand(1000), index=range(1000))
array1 = s1.values
array2 = s2.values

# Element-wise addition on Series (retains index information)
series_sum = s1 + s2
# Element-wise addition on NumPy arrays (faster but without index labels)
array_sum = array1 + array2

print("First element of Series sum (with index):", series_sum.iloc[0])
print("First element of NumPy array sum:", array_sum[0])
print("\nType of Series result:", type(series_sum))
print("Type of NumPy array result:", type(array_sum))
