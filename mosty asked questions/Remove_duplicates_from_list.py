# Python Program to Remove Duplicates from a List

# Sample input list
input_list = input("Enter a list of elements separated by spaces: ").split()

# Convert list to a set to remove duplicates, then back to a list
unique_list = list(set(input_list))

# Optional: maintain the original order (since set() does not preserve order)
# Use dict.fromkeys() which preserves the first occurrence
ordered_unique_list = list(dict.fromkeys(input_list))

# Output
print(f"Original list: {input_list}")
print(f"Unique (unordered): {unique_list}")
print(f"Unique (ordered): {ordered_unique_list}")

# -----------------------------------------
# Explanation:
# -----------------------------------------
# 1. `input().split()` reads space-separated values and creates a list.
#    Example: "apple banana apple" => ['apple', 'banana', 'apple']
#
# 2. `set(input_list)` removes duplicates but may not preserve the original order.
#    Example: {'banana', 'apple'}
#
# 3. `dict.fromkeys(input_list)` removes duplicates **while keeping the first occurrence's order**,
#    because dictionaries (in Python 3.7+) maintain insertion order.
#
# 4. `list()` is used to convert the set or dictionary back to a list.
#
# So you get two results:
# - `unique_list`: unique elements, possibly unordered
# - `ordered_unique_list`: unique elements, in original order
