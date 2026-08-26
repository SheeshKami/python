"""
03 - Type Casting

Type casting means converting a value from one data type to another.

Common functions:
    int()
    float()
    str()
    bool()

Python lets us explicitly convert values when needed.
"""

# ============================================================
# 1. int() and float()
# ============================================================

age = 17
age_float = float(age)

print(age_float)            # 17.0
print(type(age_float))      # float

price = 9.99
price_int = int(price)

print(price_int)            # 9

# int() removes the decimal part. It does NOT round off.
print(int(9.99))            # 9


# ============================================================
# 2. str()
# ============================================================

age = 17
age_string = str(age)

print(age_string)           # "17"
print(type(age_string))     # str

# Useful when combining numbers with strings.
print("I am " + age_string + " years old.")


# ============================================================
# 3. Converting strings to numbers
# ============================================================

age = int("17")
price = float("99.99")

print(age)                  # 17
print(price)                # 99.99


# ============================================================
# 4. bool()
# ============================================================

# 0, 0.0 and "" are False.
# Most other values are True.

print(bool(0))              # False
print(bool(1))              # True
print(bool(""))             # False
print(bool("Hello"))        # True

# Even the string "False" is True because it is not empty.
print(bool("False"))        # True


# ============================================================
# 5. input() + type casting
# ============================================================

# input() ALWAYS returns a string.

age = input("Enter your age: ")
print(type(age))            # str

# Convert it before doing numerical calculations.
age = int(age)

print(f"Next year you will be {age + 1}.")


# ============================================================
# 6. Common mistake
# ============================================================

age = "17"

print(age + "1")            # 171
# Strings are joined together instead of being added.

age = int(age)

print(age + 1)              # 18


# ============================================================
# 7. Invalid conversions
# ============================================================

# This causes ValueError because "hello" isn't a number.

# number = int("hello")

# "9.99" is a valid float string, but not a valid int string.

# number = int("9.99")      # ValueError

number = int(float("9.99"))

print(number)               # 9


# ============================================================
# QUICK NOTES
# ============================================================

"""
int(9.99)       -> 9
float(10)       -> 10.0
str(10)         -> "10"
bool(0)         -> False
bool(1)         -> True

Important:
    input() always returns str.

    int() removes decimals; it doesn't round.

    Invalid conversions can raise ValueError.
"""