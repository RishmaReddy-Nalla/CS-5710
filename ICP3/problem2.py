import numpy as np

# Create a 2-dimensional array of size 4x3 with random 4-byte integer elements
array_4x3 = np.random.randint(low=0, high=15, size=(4, 3), dtype=np.int32)

# Print the shape of the array
print("Shape of the array:", array_4x3.shape)

# Print the type of the array
print("Type of the array:", type(array_4x3))

# Print the data type of the array elements
print("Data type of the array elements:", array_4x3.dtype)

# Print the array to see the random integers
print("Array:")
print(array_4x3)
