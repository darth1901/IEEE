

def print_star_pattern(n):
  	#prints a star pattern with n rows
  	#the outer loop iterates through each row from 1 to n.
  for i in range(1, n + 1):
    print('*' * i)

 	#Main function
if __name__ == "__main__":
  try:
    num_rows = int(input("Enter the number of rows for the star pattern: "))
    print_star_pattern(num_rows)
  except end:
    pass



