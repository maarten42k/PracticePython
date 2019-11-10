word = input("Give me a word: ")
lower = word.lower()
if lower == lower[::-1]:
    print("This is a Palindrome!")
else:
    print("Nope, this is not a Palindrome!")
