# Python Program to Check if a String is a Palindrome

# ----------------------------
# What is a Palindrome?
# ----------------------------
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
# Examples of palindromes: "madam", "racecar", "nurses run"

# Get input from the user
input_string = input("Enter a string: ")

# Preprocess the string:
# 1. Remove spaces using replace()
# 2. Convert to lowercase using lower()
processed_string = input_string.replace(" ", "").lower()

# Check if the processed string is equal to its reverse using slicing
if processed_string == processed_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
