word = input("Type a word ")

letters = sum(c.isalpha() for c in word)

print("The word has", letters, "letters")