# Python Program to Find the Longest Substring Without Repeating Characters

def longest_unique_substring(s):
    start = 0  # Start index of current window
    max_len = 0  # Length of longest substring
    max_substr = ""  # The longest substring
    seen = {}  # Dictionary to store last seen index of characters

    for end in range(len(s)):
        if s[end] in seen and seen[s[end]] >= start:
            # If character is repeated and within the current window,
            # move the start pointer right after the previous occurrence
            start = seen[s[end]] + 1
        
        # Update the last seen index of the current character
        seen[s[end]] = end

        # Calculate current window length
        current_len = end - start + 1

        # Update max values if a longer unique substring is found
        if current_len > max_len:
            max_len = current_len
            max_substr = s[start:end+1]
    
    return max_substr

# Input from user
user_input = input("Enter a string: ")
result = longest_unique_substring(user_input)
print(f"Longest substring without repeating characters: '{result}'")

# -----------------------------------------
# Explanation:
# -----------------------------------------
# - We use a sliding window approach with two pointers: `start` and `end`.
# - `seen` is a dictionary that keeps track of the last index where each character was seen.
# - When we see a repeated character within the current window, we shift the `start` pointer.
# - We continuously update the longest substring when a longer one is found.
# - This algorithm runs in O(n) time, where n is the length of the string,
#   because each character is visited at most twice.
