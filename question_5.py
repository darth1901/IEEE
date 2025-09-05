
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
  num_points = 1000

  #generating the random numbers
  #a normal distribution has a mean of 0 and a standard deviation of 1.
  # np.random.randn() is a convenient function for this.
  random_values = np.random.randn(num_points)


  x_axis = np.arange(num_points)  
  plt.figure(figsize=(12, 7))
  plt.scatter(x_axis, random_values, alpha=0.7, edgecolors='b', s=30)

  plt.title('Scatter Plot of 1000 Random Numbers from a Normal Distribution', fontsize=16)
  plt.xlabel('Index', fontsize=12)
  plt.ylabel('Random Value', fontsize=12)

  plt.grid(True, linestyle='--', alpha=0.6)
  plt.show()


