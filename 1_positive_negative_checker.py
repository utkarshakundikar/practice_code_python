# Python Program to check if a Number Is Positive Or Negative using Multiple Methods

# ----------------------------
# Method 1: Using Brute Force
# ----------------------------
# Direct and simple use of if-elif-else structure

num1 = float(input("Method 1 - Enter a number: "))

if num1 > 0:
    print("Method 1: The number is positive.")
elif num1 < 0:
    print("Method 1: The number is negative.")
else:
    print("Method 1: The number is zero.")

# ----------------------------
# Method 2: Using Nested if-else
# ----------------------------
# Demonstrating logic with nested conditional statements

num2 = float(input("Method 2 - Enter a number: "))

if num2 >= 0:
    if num2 == 0:
        print("Method 2: The number is zero.")
    else:
        print("Method 2: The number is positive.")
else:
    print("Method 2: The number is negative.")

# ----------------------------
# Method 3: Using Ternary Operator
# ----------------------------
# A compact form of if-else in one line using conditional expressions

num3 = float(input("Method 3 - Enter a number: "))

# This line chooses the correct string based on the condition
result = "positive" if num3 > 0 else "negative" if num3 < 0 else "zero"
print(f"Method 3: The number is {result}.")
