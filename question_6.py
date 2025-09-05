import pprint #library for formatting

if __name__ == "__main__":
  #cutoff list
  cutoff_list = [
      ("Pilani", "CS", 327),
      ("Pilani", "Chemical", 240),
      ("Pilani", "M.Sc. Eco", 271),
      ("Pilani", "M.Sc. Bio", 236),
      ("Goa", "CS", 300),
      ("Goa", "Chemical", 220),
      ("Goa", "M.Sc. Eco", 259),
      ("Goa", "M.Sc. Bio", 217),
      ("Hyderabad", "CS", 307),
      ("Hyderabad", "Chemical", 220),
      ("Hyderabad", "M.Sc. Eco", 258),
      ("Hyderabad", "M.Sc. Bio", 216),
  ]

  print("Initial List of Tuples")
  # Use pprint to print the list, though standard print works fine too.
  pprint.pprint(cutoff_list)
  print("-" * 35)


  #converting to a nested dictionary
  cutoff_dict = {}
  for campus, branch, score in cutoff_list:
    if campus not in cutoff_dict:
      cutoff_dict[campus] = {}
    cutoff_dict[campus][branch] = score


  print("\n Converted Nested Dictionary ")
  pprint.pprint(cutoff_dict)
  print("-" * 35)

