import pandas as pd
import numpy as np

# Create a Pandas Series
series = pd.Series(['A', 'B', 'C', 'D', 'E'])

print("Original Pandas Series:")
print(series)

# Convert Series to NumPy Array
numpy_array = np.array(series)

print("\nConverted NumPy Array:")
print(numpy_array)

# Display data type
print("\nType of Series:", type(series))
print("Type of NumPy Array:", type(numpy_array))