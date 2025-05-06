# Python Program to Compress a String
# Example: "aaabbcccc" => "a3b2c4"

def compress_string(s):
    if not s:
        return ""

    compressed = ""
    count = 1  # Initialize count for first character

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1  # Same character, increment count
        else:
            # Append current character and its count to result
            compressed += s[i - 1] + str(count)
            count = 1  # Reset count for the new character

    # Append the last character and its count
    compressed += s[-1] + str(count)

    return compressed

# Input from the user
input_string = input("Enter a string to compress: ")
compressed = compress_string(input_string)
print(f"Compressed string: {compressed}")

# -----------------------------------------
# Explanation:
# -----------------------------------------
# 1. We check if the input string is empty; if so, return an empty string.
# 2. We initialize an empty result string `compressed` and a `count` variable to 1.
# 3. We loop through the string starting from index 1:
#    - If the current character matches the previous one, we increment `count`.
#    - If it doesn't match, we append the previous character and its count to the result string,
#      then reset `count` to 1 for the new character.
# 4. After the loop, we must append the last character and its count (since it won't be handled inside the loop).
# 5. The final result is returned and printed.

# Example:
# Input: "aaabbcccc"
# Output: "a3b2c4"
