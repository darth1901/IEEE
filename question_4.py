import numpy as np
if __name__ == "__main__":

  np.random.seed(42)


  matrix = np.random.randint(1, 101, size=(5, 5))
  print(" Original 5x5 Matrix")
  print(matrix)


  #extraction by slicing
  # For a 5x5 matrix, the middle part starts at row index 1 and ends at 3,
  # and the same for columns (indices 1 to 3).
  middle_matrix = matrix[1:4, 1:4]
  print("\n Middle 3x3 Sub-Matrix")
  print(middle_matrix)


  first_row = middle_matrix[0, :]  # First row of the 3x3 matrix
  last_col = middle_matrix[:, 2]   # Last column of the 3x3 matrix

  print("\n Dot Product ")
  print(f"First row of 3x3 matrix: {first_row}")
  print(f"Last column of 3x3 matrix: {last_col}")


  dot_product = np.dot(first_row, last_col)
  print(f"Dot product: {dot_product}")


