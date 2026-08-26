"""
02 - Data Types

A data type tells Python what kind of value a variable contains.

Python is dynamically typed, so we don't have to declare the
data type when creating a variable.

Common built-in data types:

    str      -> text
    int      -> whole numbers
    float    -> decimal numbers
    complex  -> complex numbers
    bool     -> True / False
    NoneType -> no value

    list     -> ordered, mutable collection
    tuple    -> ordered, immutable collection
    set      -> unordered collection of unique values
    dict     -> key-value pairs
"""

# ============================================================
# 1. STRING (str)
# ============================================================

name = "Mridul"
message = 'Hello'

print(name)
print(type(name))       # <class 'str'>

# Strings can contain letters, numbers and symbols.
# Anything inside quotes is a string.

number = "17"           # This is a STRING, not an integer.


# ============================================================
# 2. INTEGER (int)
# ============================================================

age = 17
year = 2026
negative_number = -10

print(age)
print(type(age))        # <class 'int'>


# ============================================================
# 3. FLOAT (float)
# ============================================================

price = 99.99
temperature = 36.5

print(price)
print(type(price))      # <class 'float'>


# ============================================================
# 4. COMPLEX (complex)
# ============================================================

# Complex numbers have a real and imaginary part.
# Python uses 'j' for the imaginary part.

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

# Booleans are commonly used with conditions.

if is_student:
    print("Student account")
else:
    print("Not a student account")


# ============================================================
# 6. NONE (NoneType)
# ============================================================

# None represents the absence of a value.

result = None

print(result)
print(type(result))     # <class 'NoneType'>

if result is None:
    print("No result available.")


# ============================================================
# 7. LIST
# ============================================================

# Ordered and MUTABLE collection.
# Mutable = can be changed after creation.

subjects = ["Physics", "Chemistry", "Maths"]

print(subjects)
print(type(subjects))   # <class 'list'>

subjects.append("Computer Science")

print(subjects)


# ============================================================
# 8. TUPLE
# ============================================================

# Ordered and IMMUTABLE collection.
# Immutable = cannot be changed after creation.

coordinates = (28.45, 77.03)

print(coordinates)
print(type(coordinates))    # <class 'tuple'>


# ============================================================
# 9. SET
# ============================================================

# Unordered collection of UNIQUE values.

numbers = {1, 2, 3, 3, 4}

print(numbers)
print(type(numbers))        # <class 'set'>

# Duplicate values are automatically removed.


# ============================================================
# 10. DICTIONARY
# ============================================================

# Stores data as KEY : VALUE pairs.

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
# 11. CHECKING DATA TYPES
# ============================================================

x = 100

print(type(x))              # <class 'int'>

# isinstance() checks whether a value belongs to a type.

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
None     -> No value

list     -> [1, 2, 3]
tuple    -> (1, 2, 3)
set      -> {1, 2, 3}
dict     -> {"name": "Mridul", "age": 17}

Useful functions:

    type(x)
    isinstance(x, type)

Common conversions:

    int(x)
    float(x)
    str(x)
    bool(x)

Mutable:
    list
    set
    dict

Immutable:
    str
    int
    float
    bool
    tuple
"""