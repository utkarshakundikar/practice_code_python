# Python Program to Get the Last 3 Elements of a List Using Slicing

# Sample list
numbers = [5, 10, 15, 20, 25, 30, 35]

# Get the last 3 elements using slicing
last_three = numbers[-3:]

# Output the result
print("Original list:", numbers)
print("Last 3 elements:", last_three)

# -----------------------------------------
# Explanation:
# -----------------------------------------
# 1. The list `numbers` contains a sequence of integers.
#
# 2. The slicing expression `numbers[-3:]` means:
#    - `-3` is the start index, counting from the end (negative indices count from the right).
#    - It starts from the third-to-last element.
#    - No end index is specified, so it goes to the end of the list.
#
# 3. This retrieves the last 3 elements: 25, 30, and 35.
#
# Output:
# Original list: [5, 10, 15, 20, 25, 30, 35]
# Last 3 elements: [25, 30, 35]
