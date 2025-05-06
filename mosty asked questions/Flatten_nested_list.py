# Python Program to Flatten a Nested List

# Sample nested list
nested_list = [[1, 2], [3, 4], [5]]

# -----------------------------------------
# Method 1: Using List Comprehension
# -----------------------------------------
# Flattening the nested list into a single-level list
flat_list_comprehension = [item for sublist in nested_list for item in sublist]

# Output for method 1
print("Method 1: Using List Comprehension")
print(f"Original nested list: {nested_list}")
print(f"Flattened list: {flat_list_comprehension}")

# Explanation:
# - The outer loop: `for sublist in nested_list` iterates over each inner list.
# - The inner loop: `for item in sublist` iterates over each item in that sublist.
# - All items are collected into a single flat list.
# - Example: [[1, 2], [3, 4], [5]] → [1, 2, 3, 4, 5]

print("\n" + "-"*50 + "\n")

# -----------------------------------------
# Method 2: Using Normal For Loop
# -----------------------------------------
# Initialize an empty list to hold flattened values
flat_list_loop = []

# Loop through each sublist
for sublist in nested_list:
    # Loop through each item in the sublist
    for item in sublist:
        flat_list_loop.append(item)

# Output for method 2
print("Method 2: Using Normal For Loop")
print(f"Original nested list: {nested_list}")
print(f"Flattened list: {flat_list_loop}")

# Explanation:
# - Start with an empty list.
# - Loop through each sublist, then through each item.
# - Append each item to the result list.
# - This produces the same output as the list comprehension method.
