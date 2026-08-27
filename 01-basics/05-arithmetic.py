"""
05 - Arithmetic

Basic math operators in Python.

Operators:
    +   addition
    -   subtraction
    *   multiplication
    /   division          (always returns float)
    //  floor division    (integer result)
    %   modulus           (remainder)
    **  exponentiation

Order of operations follows PEMDAS.
Parantheses → Exponents → Multiply/Divide → Add/Subtract
"""

# ============================================================
# 1. BASIC OPERATORS
# ============================================================

a = 10
b = 3

print(a + b)        # 13
print(a - b)        # 7
print(a * b)        # 30
print(a / b)        # 3.333...
print(a // b)       # 3
print(a % b)        # 1
print(a ** b)       # 1000


# ============================================================
# 2. ORDER OF OPERATIONS (PEMDAS)
# ============================================================

# Parentheses → Exponents → Multiply/Divide → Add/Subtract

result = 2 + 3 * 4
print(result)       # 14

result = (2 + 3) * 4
print(result)       # 20


# ============================================================
# 3. AUGMENTED ASSIGNMENT
# ============================================================

x = 10

x += 5              # x = x + 5
print(x)            # 15

x -= 3              # x = x - 3
print(x)            # 12

x *= 2
print(x)            # 24

x /= 4
print(x)            # 6.0

x //= 2
print(x)            # 3.0

x **= 2
print(x)            # 9.0


# ============================================================
# 4. USEFUL EXAMPLES
# ============================================================

# even / odd check
num = 17
print(num % 2)      # 1 → odd

# last digit
print(1234 % 10)    # 4

# power
print(2 ** 10)      # 1024


# ============================================================
# QUICK NOTES
# ============================================================

"""
+   add
-   subtract
*   multiply
/   true division (float)
//  floor division
%   remainder
**  power

PEMDAS applies.

Augmented:
    +=  -=  *=  /=  //=  %=  **=
"""