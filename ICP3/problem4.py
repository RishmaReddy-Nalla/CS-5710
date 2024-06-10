import numpy as np

# Define the array
array = np.array([[0, 1, 2], 
                  [3, 4, 5]])

# Extract the diagonal elements
diagonal_elements = np.diag(array)
print(f"diagonal_elements: {diagonal_elements}")
# Compute the sum of the diagonal elements
sum_diagonal = np.sum(diagonal_elements)

# Print the sum of the diagonal elements
print("Sum of the diagonal elements:", sum_diagonal)
