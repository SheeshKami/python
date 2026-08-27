"""
03 - Type Casting

Converting a value from one data type to another.

Common functions:
    int()
    float()
    str()
    bool()
"""

# ============================================================
# 1. int() and float()
# ============================================================

age = 17
age_float = float(age)

print(age_float)            # 17.0
print(type(age_float))      # <class 'float'>

price = 9.99
price_int = int(price)

print(price_int)            # 9

# int() truncates (cuts off) the decimal — it does NOT round
print(int(9.99))            # 9


# ============================================================
# 2. str()
# ============================================================

age = 17
age_string = str(age)

print(age_string)           # "17"
print(type(age_string))     # <class 'str'>

# Needed when joining numbers with text
print("I am " + age_string + " years old.")


# ============================================================
# 3. Strings → numbers
# ============================================================

age = int("17")
price = float("99.99")

print(age)                  # 17
print(price)                # 99.99


# ============================================================
# 4. bool()
# ============================================================

# 0, 0.0, "" → False
# almost everything else → True

print(bool(0))              # False
print(bool(1))              # True
print(bool(""))             # False
print(bool("Hello"))        # True

# even the string "False" is True (not empty)
print(bool("False"))        # True


# ============================================================
# 5. Common mistake
# ============================================================

age = "17"

print(age + "1")            # 171  (concatenation)

age = int(age)
print(age + 1)              # 18


# ============================================================
# 6. Invalid conversions
# ============================================================

# int("hello")        → ValueError
# int("9.99")         → ValueError

# safe way for float strings:
number = int(float("9.99"))
print(number)               # 9


# ============================================================
# QUICK NOTES
# ============================================================

"""
int(9.99)   → 9        (truncates)
float(10)   → 10.0
str(10)     → "10"
bool(0)     → False
bool("")    → False

input() always returns str → cast when you need a number

Invalid casts raise ValueError
"""