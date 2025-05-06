# Python Program to Reverse a List Using Slicing

# Sample list
numbers = [10, 20, 30, 40, 50]

# Reverse the list using slicing
reversed_list = numbers[::-1]

# Output the result
print("Original list:", numbers)
print("Reversed list:", reversed_list)

# -----------------------------------------
# Explanation:
# -----------------------------------------
# 1. The list `numbers` contains a sequence of elements.
#
# 2. The slicing expression `numbers[::-1]` works as follows:
#    - The format is [start:stop:step]
#    - Leaving `start` and `stop` empty means the slice will include the entire list.
#    - `step = -1` means move through the list in reverse order.
#
# 3. So the result is a new list with elements from the original list in reverse.
#
# Output:
# Original list: [10, 20, 30, 40, 50]
# Reversed list: [50, 40, 30, 20, 10]
