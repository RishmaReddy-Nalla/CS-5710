import numpy as np

# Create a random vector of size 15 with integers in the range of 1 to 20
random_vector = np.random.randint(1, 21, size=15)
print(f"random vector of integers between 1-20:  {random_vector}")

# Reshape the vector to a 3x5 array
reshaped_array = random_vector.reshape(3, 5)

# Print the shape of the array
print("Shape of the array:", reshaped_array.shape)

# Replace the maximum value in each row by 0
for i in range(reshaped_array.shape[0]):
    max_index = np.argmax(reshaped_array[i])
    reshaped_array[i, max_index] = 0

# Print the modified array
print(f"Modified array:")
print(reshaped_array)
