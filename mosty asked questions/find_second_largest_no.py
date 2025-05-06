# Function to find the second largest number in a list
def find_second_largest(nums):
    # Remove duplicates by converting list to a set
    unique_nums = list(set(nums))

    # Check if there are at least two unique values
    if len(unique_nums) < 2:
        return None  # Not enough unique values to find second largest

    # Sort the list in descending order
    unique_nums.sort(reverse=True)

    # Return the second element — which is the second largest
    return unique_nums[1]

# Example usage
numbers = [12, 45, 2, 41, 31, 10, 45]
result = find_second_largest(numbers)

if result is not None:
    print(f"The second largest number is: {result}")
else:
    print("List does not have enough unique numbers to find a second largest.")

# -----------------------------------------
# Explanation:
# -----------------------------------------
# 1. The function `find_second_largest` takes a list of numbers as input.
# 2. `set(nums)` is used to remove duplicate values, because if the largest
#    number appears more than once, we still want the second *distinct* largest.
# 3. We convert the set back to a list so we can sort it.
# 4. We check if there are at least two unique numbers — otherwise, return `None`.
# 5. `sort(reverse=True)` sorts the list in descending order (largest to smallest).
# 6. The second element of the sorted list (`unique_nums[1]`) is returned as the result.
# 7. In the main block, the function is called, and we print the result if valid.

# Example:
# Input: [12, 45, 2, 41, 31, 10, 45]
# Unique values: [2, 10, 12, 31, 41, 45]
# Sorted: [45, 41, 31, 12, 10, 2]
# Output: 41 (second largest)
