	
import numpy as np


if __name__ == "__main__":
  #create a 5x5 numpy matrix with random integers between 1 and 100.
  matrix = np.random.randint(1, 101, size=(5, 5))

	
  print(" Random 5x5 Matrix ")
  print(matrix)
  print("-" * 30)

  #Calculating and print the maximum, minimum, and mean.
  max_val = matrix.max()
  min_val = matrix.min()
  mean_val = matrix.mean()

  print(f"Maximum value: {max_val}")
  print(f"Minimum value: {min_val}")
  print(f"Mean value: {mean_val:.2f}") # Format mean to 2 decimal places.
  print("-" * 30)

  #normalisation
  # The formula for min-max normalization is (X - min(X)) / (max(X) - min(X)).
  # We add a small epsilon to the denominator to avoid division by zero if all elements are the same.
  normalized_matrix = (matrix - min_val) / ((max_val - min_val) + 1e-9)
  print("--- Normalized Matrix (values between 0 and 1) ---")
  print(normalized_matrix)
  print("-" * 30)

  #flattening
  flattened_array = matrix.flatten()

  #sorting the flattened array
  sorted_array = np.sort(flattened_array)
  print("--- Flattened and Sorted 1D Array ---")
  print(sorted_array)
  print("-" * 30)
