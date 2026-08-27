"""
04 - Input

input() receives data from the user.

Important:
    input() ALWAYS returns a string (str).

Convert with int() / float() when you need numbers.

Coding platforms:
    stdin  = input given to the program
    stdout = output the program prints
"""

# ============================================================
# 1. BASIC INPUT
# ============================================================

name = input("Enter your name: ")
print(f"Hello, {name}!")


# ============================================================
# 2. INPUT IS ALWAYS A STRING
# ============================================================

age = input("Enter your age: ")
print(age)
print(type(age))            # <class 'str'>


# ============================================================
# 3. INTEGER INPUT
# ============================================================

age = int(input("Enter your age: "))
print(f"You are {age} years old.")
print(type(age))            # <class 'int'>


# ============================================================
# 4. FLOAT INPUT
# ============================================================

price = float(input("Enter the price: "))
print(f"The price is ₹{price}")
print(type(price))          # <class 'float'>


# ============================================================
# 5. MULTIPLE INPUTS
# ============================================================

first_name = input("First name: ")
last_name = input("Last name: ")
print(f"Full name: {first_name} {last_name}")


# ============================================================
# 6. split()
# ============================================================

# splits on whitespace by default
first_name, last_name = input("Enter full name: ").split()
print(f"Hello, {first_name} {last_name}")


# ============================================================
# 7. MULTIPLE INTEGERS
# ============================================================

a, b = map(int, input("Enter two numbers: ").split())
print(a + b)


# ============================================================
# 8. MULTIPLE FLOATS
# ============================================================

x, y = map(float, input("Enter two decimals: ").split())
print(x + y)


# ============================================================
# 9. LIST OF INTEGERS
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)


# ============================================================
# 10. STDIN / STDOUT
# ============================================================

# input() reads from stdin
# print() writes to stdout

age = int(input())
print(age + 1)


# ============================================================
# 11. CODING-PLATFORM STYLE
# ============================================================

# Online judges hate prompts. Keep it clean:

n = int(input())
print(n * 2)

# Avoid:
# n = int(input("Enter n: "))


# ============================================================
# 12. MULTIPLE LINES
# ============================================================

n = int(input())
for _ in range(n):
    value = input()
    print(value)


# ============================================================
# 13. PRACTICAL EXAMPLE
# ============================================================

name = input("Name: ")
age = int(input("Age: "))
marks = float(input("Marks: "))
print(f"{name} is {age} years old and scored {marks}.")


# ============================================================
# QUICK NOTES
# ============================================================

"""
input()                     → always str
int(input())                → integer
float(input())              → float

.split()                    → list of strings
map(int, ...)               → apply int to each item
list(map(int, input().split())) → list of ints

Competitive style:
    n = int(input())
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))

No prompts on online judges.
"""