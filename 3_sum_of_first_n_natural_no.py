# Python Program to Find the Sum of First N Natural Numbers

# ----------------------------
# Method 1: Using for Loop
# ----------------------------
n1 = int(input("Method 1 - Enter a positive integer: "))
sum1 = 0
for i in range(1, n1 + 1):
    sum1 += i
print(f"Method 1: Sum of first {n1} natural numbers is {sum1}")

# ----------------------------
# Method 2: Using Formula for the Sum of Nth Term
# Formula: sum = n * (n + 1) / 2
# ----------------------------
n2 = int(input("Method 2 - Enter a positive integer: "))
sum2 = n2 * (n2 + 1) // 2
print(f"Method 2: Sum of first {n2} natural numbers is {sum2}")

# ----------------------------
# Method 3: Using Recursion
# ----------------------------
def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)

n3 = int(input("Method 3 - Enter a positive integer: "))
if n3 < 1:
    print("Method 3: Please enter a number greater than 0.")
else:
    sum3 = recursive_sum(n3)
    print(f"Method 3: Sum of first {n3} natural numbers is {sum3}")
