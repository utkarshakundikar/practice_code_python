# Python Program to Count Vowels and Consonants in a String

# Get input from the user
input_string = input("Enter a string: ")

# Convert the string to lowercase for uniform comparison
input_string = input_string.lower()

# Define vowel characters
vowels = "aeiou"

# Initialize counters
vowel_count = 0
consonant_count = 0

# Loop through each character in the string
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Display the results
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
