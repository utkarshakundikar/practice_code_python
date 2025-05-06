# -----------------------------------------
# EXPLANATIONS:
# -----------------------------------------

# ✅ What is a dictionary?
# A dictionary in Python is an unordered collection of key-value pairs.
# Example: {"name": "Alice", "age": 30}
# You access values by keys, e.g., person["name"] returns "Alice".

# ✅ What is a lambda function?
# A lambda is an anonymous (nameless) function defined using the `lambda` keyword.
# Syntax: lambda arguments: expression
# Example: lambda x: x['age'] means:
#          - Take input x (which is a dictionary),
#          - Return the value of the 'age' key from it.

# ✅ What is the `sorted()` function?
# `sorted()` is a built-in Python function that returns a new sorted list from any iterable.
# It does not change the original list.
# Syntax: sorted(iterable, key=..., reverse=...)
# The `key` argument lets you specify a function to extract the value to sort by.

# -----------------------------------------
# CODE: Sort a List of Dictionaries by a Specific Key
# -----------------------------------------

# Sample list of dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort by the 'age' key using lambda
sorted_people = sorted(people, key=lambda x: x['age'])

# Output the sorted list
print("Sorted list by age:")
for person in sorted_people:
    print(person)

# -----------------------------------------
# How it works:
# -----------------------------------------
# 1. `people` is a list where each item is a dictionary with 'name' and 'age'.
# 2. `sorted()` takes this list and uses `lambda x: x['age']` to extract the age for sorting.
#    So it compares 30, 25, and 35 — and sorts accordingly.
# 3. The result is a new list (`sorted_people`) sorted by increasing age.
# 4. The original `people` list is unchanged.
