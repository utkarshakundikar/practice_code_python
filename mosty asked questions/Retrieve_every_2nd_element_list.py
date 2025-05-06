# Python Program to Retrieve Every 2nd Element in a List

# Sample list
numbers = [10, 20, 30, 40, 50, 60, 70]

# Retrieve every 2nd element using slicing
every_second = numbers[1::2]

# Output the result
print("Original list:", numbers)
print("Every 2nd element:", every_second)

# -----------------------------------------
# Explanation:
# -----------------------------------------
# 1. The list `numbers` contains a sequence of integers.
#
# 2. The expression `numbers[1::2]` uses slicing with the format:
#    list[start:stop:step]
#    - `start=1` → Start from index 1 (second element, which is 20).
#    - `stop` is left empty → Go till the end of the list.
#    - `step=2` → Take every 2nd element.
#
# 3. So it picks elements at indices: 1, 3, 5 → which are 20, 40, 60.
#
# 4. The result is a new list containing every second element from the original list.
#
# Output:
# Original list: [10, 20, 30, 40, 50, 60, 70]
# Every 2nd element: [20, 40, 60]
