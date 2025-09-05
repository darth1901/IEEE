# This program takes an integer n as input and prints a right-angled triangle star pattern.

def print_star_pattern(n):
  	#Prints a star pattern with n rows
  	# The outer loop iterates through each row from 1 to n.
  for i in range(1, n + 1):
    # The inner logic prints '*' i times for the current row.
    # The string multiplication operator '*' is used for this.
    print('*' * i)

 	#Main function
if __name__ == "__main__":
  try:
    # Get user input for the number of rows.
    num_rows = int(input("Enter the number of rows for the star pattern: "))
    # Call the function to print the pattern.
    print_star_pattern(num_rows)
  except end:
    pass

