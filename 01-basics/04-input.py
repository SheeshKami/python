"""
04 - Input

input() is used to receive data from the user.

Important:
    input() ALWAYS returns a string (str).

For numbers, convert the input using int() or float().

In coding platforms:
    stdin  = input provided to the program
    stdout = output produced by the program
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
print(type(age))            # str


# ============================================================
# 3. INTEGER INPUT
# ============================================================

age = int(input("Enter your age: "))

print(f"You are {age} years old.")
print(type(age))            # int


# ============================================================
# 4. FLOAT INPUT
# ============================================================

price = float(input("Enter the price: "))

print(f"The price is ₹{price}")
print(type(price))          # float


# ============================================================
# 5. MULTIPLE INPUTS
# ============================================================

first_name = input("First name: ")
last_name = input("Last name: ")

print(f"Full name: {first_name} {last_name}")


# ============================================================
# 6. split()
# ============================================================

# split() separates a string into parts using whitespace by default.

first_name, last_name = input("Enter your full name: ").split()

print(f"Hello, {first_name} {last_name}")


# Example:
#
# Input:
# Rohit Sharma
#
# Result:
# first_name = "Rohit"
# last_name  = "Sharma"


# ============================================================
# 7. MULTIPLE INTEGER INPUTS
# ============================================================

# map() applies int() to every value produced by split().

a, b = map(int, input("Enter two numbers: ").split())

print(a + b)


# Example:
#
# Input:
# 10 20
#
# a = 10
# b = 20
#
# Output:
# 30


# ============================================================
# 8. MULTIPLE FLOAT INPUTS
# ============================================================

x, y = map(float, input("Enter two decimal numbers: ").split())

print(x + y)


# ============================================================
# 9. INPUT AS A LIST OF INTEGERS
# ============================================================

numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)

# Input:
# 10 20 30 40
#
# Output:
# [10, 20, 30, 40]


# ============================================================
# 10. STDIN AND STDOUT
# ============================================================

# stdin = Standard Input
# stdout = Standard Output

# input() reads from stdin.
# print() writes to stdout.

age = int(input())

print(age + 1)


# On HackerRank / other coding platforms:
#
# stdin  -> test data given to your program
# stdout -> answer printed by your program


# ============================================================
# 11. CODING PLATFORM STYLE INPUT
# ============================================================

# Competitive programming usually avoids prompts.

# Good:
n = int(input())
print(n * 2)

# Avoid:
# n = int(input("Enter n: "))

# Why?
# Online judges provide their own input and compare your
# stdout with the expected output.


# ============================================================
# 12. READING MULTIPLE LINES
# ============================================================

n = int(input())

for _ in range(n):
    value = input()
    print(value)


# Example input:
#
# 3
# Apple
# Banana
# Mango
#
# Output:
#
# Apple
# Banana
# Mango


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
input()
    -> reads input
    -> always returns str

int(input())
    -> integer input

float(input())
    -> floating-point input

.split()
    -> separates a string into parts

map(function, iterable)
    -> applies a function to every item

list(map(int, input().split()))
    -> reads multiple integers into a list

stdin
    -> standard input

stdout
    -> standard output

For competitive programming:

    n = int(input())

    a, b = map(int, input().split())

    arr = list(map(int, input().split()))

Avoid prompts such as:

    input("Enter number: ")

when submitting to an online judge.
"""