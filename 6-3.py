#Palindrome Checker

text = input("Enter a word: ")

if text == text[::-1]:
    print(" It's a palindrome!")
else:
    print(" It's not a palindrome.")
