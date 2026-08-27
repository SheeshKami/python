"""
01 - Variables

A variable is a name that refers to a value in memory.

Syntax:
    variable_name = value

Python is dynamically typed — no need to declare the type.
"""

# ============================================================
# 1. STRINGS
# ============================================================

first_name = "Mridul"
food = "pasta"
email = "mridulbud@gmail.com"

print(first_name)                    # Mridul
print("first_name")                  # first_name (just text)
print("Hi", first_name)              # Hi Mridul

# f-string
print(f"Hi {first_name}, your favorite food is {food}")


# ============================================================
# 2. INTEGERS
# ============================================================

age = 17
year = 2026

print(age)
print(f"You are {age} years old.")


# ============================================================
# 3. FLOATS
# ============================================================

price = 9.99
height = 5.11

print(price)
print(f"The price is ${price}")


# ============================================================
# 4. BOOLEANS
# ============================================================

is_student = True
is_adult = False

print(is_student)

if is_adult:
    print("This person is an adult.")
else:
    print("This person is not an adult.")


# ============================================================
# 5. CHECKING DATA TYPES
# ============================================================

print(type(first_name))   # <class 'str'>
print(type(age))          # <class 'int'>
print(type(price))        # <class 'float'>
print(type(is_student))   # <class 'bool'>


# ============================================================
# 6. MULTIPLE ASSIGNMENT
# ============================================================

name, age, city = "Mridul", 17, "Gurugram"

print(name)
print(age)
print(city)


# ============================================================
# 7. CONSTANTS
# ============================================================

# Python has no true constants.
# UPPERCASE is just a convention: "don't change this".

PI = 3.14159
MAX_USERS = 100


# ============================================================
# QUICK NOTES
# ============================================================

"""
Common built-in types:

str   -> "Hello"
int   -> 17
float -> 9.99
bool  -> True / False

Useful:
    type(value)

Important:
    "17"  -> str
    17    -> int
    17.0  -> float

Dynamically typed:
    age = 17
    age = "seventeen"   # completely fine
"""