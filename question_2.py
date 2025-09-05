import re # Import the regular expressions module to help with cleaning the text.

def find_palindromes(text):
  # regex function finds all sequence of word characters   
  # \b ensures we match whole words only.
  words = re.findall(r'\b\w+\b', text.lower())

  #identifying palindromes
  palindromes = []
  for word in words:

    if word == word[::-1]:
      palindromes.append(word)

  #returns unique palindromes
  return list(set(palindromes))

if __name__ == "__main__":
  try:
    paragraph = input("Enter a paragraph (up to 100 words): ")

    #word count check
    if len(paragraph.split()) > 100:
        print("Error: The paragraph exceeds the 100-word limit.")
    else:

        found_palindromes = find_palindromes(paragraph)


        if found_palindromes:
          print("\nThe palindromes are:")
          # Sort the list for consistent output.
          for palindrome in sorted(found_palindromes):
            print(palindrome)
        else:
          # If the list is empty, no palindromes were found.
          print("0")

  except end:
      pass

