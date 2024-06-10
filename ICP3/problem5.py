import numpy as np

# Define the original 3x2 array
array_3x2 = np.array([[1, 2], 
                      [3, 4], 
                      [5, 6]])

# Print the original array
print("Original 3x2 array:")
print(array_3x2)

# Reshape the array to 2x3
array_2x3 = array_3x2.reshape(2, 3)

# Print the reshaped array
print("Reshaped 2x3 array:")
print(array_2x3)
