import numpy as np

# Define the square array
square_array = np.array([[3, -2], 
                         [1, 0]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(square_array)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Print the right eigenvectors
print("Right eigenvectors:")
print(eigenvectors)
