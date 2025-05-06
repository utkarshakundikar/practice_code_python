# Python Program to Check Whether a Number is Even or Odd

# ----------------------------
# Method 1: Using Brute Force
# ----------------------------
num1 = int(input("Method 1 - Enter a number: "))

if num1 % 2 == 0:
    print("Method 1: The number is Even.")
else:
    print("Method 1: The number is Odd.")

# ----------------------------
# Method 2: Using Ternary Operator
# ----------------------------
num2 = int(input("Method 2 - Enter a number: "))

# Ternary operator: one-liner conditional
print("Method 2: The number is Even." if num2 % 2 == 0 else "Method 2: The number is Odd.")

# ----------------------------
# Method 3: Using Bitwise Operator
# ----------------------------
num3 = int(input("Method 3 - Enter a number: "))

# Bitwise AND with 1 gives 0 for even numbers, 1 for odd numbers
if num3 & 1:
    print("Method 3: The number is Odd.")
else:
    print("Method 3: The number is Even.")
