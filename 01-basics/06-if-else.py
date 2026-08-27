"""
06 - If Else

Conditional statements let the program decide what to do.

Syntax:
    if condition:
        # code
    elif condition:
        # code
    else:
        # code

Comparison operators:
    ==  is equal
    !=  is not equal
    >   is greater
    <   is less
    >=  is greater than or equal to
    <=  is less than or equal to
"""

# ============================================================
# 1. BASIC IF
# ============================================================

age = 17

if age >= 18:
    print("Adult")
else:
    print("Not an adult")


# ============================================================
# 2. ELIF
# ============================================================

marks = 78

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")


# ============================================================
# 3. COMPARISON OPERATORS
# ============================================================

a = 10
b = 20

print(a == b)       # False
print(a != b)       # True
print(a > b)        # False
print(a < b)        # True
print(a >= 10)      # True
print(a <= 5)       # False


# ============================================================
# 4. NESTED IF
# ============================================================

age = 17
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("Need ID")
else:
    print("Too young")


# ============================================================
# 5. MULTIPLE CONDITIONS (preview)
# ============================================================

age = 17
is_student = True

if age < 18 and is_student:
    print("Student under 18")


# ============================================================
# 6. PRACTICAL EXAMPLES
# ============================================================

# even or odd
num = 15
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# positive / negative / zero
n = -5
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# ============================================================
# QUICK NOTES
# ============================================================

"""
if condition:
    ...
elif condition:
    ...
else:
    ...

Comparisons:
    ==  !=  >  <  >=  <=

Indentation is mandatory (usually 4 spaces).

Logical operators (and, or, not) → later file.
"""