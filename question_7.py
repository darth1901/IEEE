if __name__ == "__main__":

  list1 = [3, 4, 5, 1, 4, 6, 1, 7, 7]
  list2 = [5, 8, 2, 9, 9, 4, 6, 3]

  print("--- Original Lists ---")
  print(f"List 1: {list1}")
  print(f"List 2: {list2}")
  print("-" * 30)

  #finding intersection
  set1 = set(list1)
  set2 = set(list2)
  intersection_set = set1 & set2

  #converting back to a list	
  intersection_list = list(intersection_set)

  print(intersection_list)
  print("-" * 30)

