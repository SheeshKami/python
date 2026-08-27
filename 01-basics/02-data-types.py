"""
02 - Data Types

A data type tells Python what kind of value a variable holds.

Python is dynamically typed — no need to declare the type.

Common built-in types:

    str      -> text
    int      -> whole numbers
    float    -> decimals
    complex  -> complex numbers
    bool     -> True / False
    NoneType -> no value

    list     -> ordered, mutable
    tuple    -> ordered, immutable
    set      -> unordered, unique
    dict     -> key-value pairs
"""

# ============================================================
# 1. STRING (str)
# ============================================================

name = "Mridul"
message = 'Hello'

print(name)
print(type(name))       # <class 'str'>

# Anything inside quotes is a string
number = "17"           # still a string, not an int


# ============================================================
# 2. INTEGER (int)
# ============================================================

age = 17
year = 2026
negative = -10

print(age)
print(type(age))        # <class 'int'>


# ============================================================
# 3. FLOAT (float)
# ============================================================

price = 99.99
temp = 36.5

print(price)
print(type(price))      # <class 'float'>


# ============================================================
# 4. COMPLEX (complex)
# ============================================================

# Real + imaginary part (j for imaginary)
z = 3 + 4j

print(z)
print(type(z))          # <class 'complex'>


# ============================================================
# 5. BOOLEAN (bool)
# ============================================================

is_student = True
is_logged_in = False

print(is_student)
print(type(is_student)) # <class 'bool'>

if is_student:
    print("Student account")
else:
    print("Not a student account")


# ============================================================
# 6. NONE (NoneType)
# ============================================================

# Represents absence of a value
result = None

print(result)
print(type(result))     # <class 'NoneType'>

if result is None:
    print("No result available.")


# ============================================================
# 7. LIST
# ============================================================

# Ordered + mutable
subjects = ["Physics", "Chemistry", "Maths"]

print(subjects)
print(type(subjects))   # <class 'list'>

subjects.append("Computer Science")
print(subjects)


# ============================================================
# 8. TUPLE
# ============================================================

# Ordered + immutable
coordinates = (28.45, 77.03)

print(coordinates)
print(type(coordinates))    # <class 'tuple'>


# ============================================================
# 9. SET
# ============================================================

# Unordered + unique values only
numbers = {1, 2, 3, 3, 4}

print(numbers)              # {1, 2, 3, 4}
print(type(numbers))        # <class 'set'>


# ============================================================
# 10. DICTIONARY
# ============================================================

# Key : Value pairs
student = {
    "name": "Mridul",
    "age": 17,
    "grade": 12
}

print(student)
print(type(student))        # <class 'dict'>

print(student["name"])      # Mridul
print(student["age"])       # 17


# ============================================================
# 11. CHECKING TYPES
# ============================================================

x = 100

print(type(x))              # <class 'int'>
print(isinstance(x, int))   # True
print(isinstance(x, str))   # False


# ============================================================
# QUICK REFERENCE
# ============================================================

"""
str      -> "Hello"
int      -> 17
float    -> 17.5
complex  -> 3 + 4j
bool     -> True / False
None     -> no value

list     -> [1, 2, 3]
tuple    -> (1, 2, 3)
set      -> {1, 2, 3}
dict     -> {"name": "Mridul"}

Useful:
    type(x)
    isinstance(x, type)

Mutable:   list, set, dict
Immutable: str, int, float, bool, tuple, complex, None
"""