# Operators in Python

# Python divides the operators in the following groups:
#
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Addition
print(10 + 5) # 15

# Subtraction
print(10 - 5) # 5

# Multiplication
print(10 * 5) # 50

# Division
print(10 / 5) # 2.0

# Modulus
print(10 % 5) # 0

# Exponentiation
print(10 ** 5) # 100000

# Floor division
print(10 // 5) # 2

# Assignment operators
# Assignment operators are used to assign values to variables:

# =
x = 5
print(x) # 5

# +=
x += 5 # x = x + 5
print(x) # 10

# -=
x -= 5 # x = x - 5
print(x) # 5

# *=
x *= 5 # x = x * 5
print(x) # 25

# /=
x /= 5 # x = x / 5
print(x) # 5.0

# %=
x %= 5 # x = x % 5
print(x) # 0.0

# **=
x **= 5 # x = x ** 5
print(x) # 0.0

# //=
x //= 5 # x = x // 5

# Comparison operators
# Comparison operators are used to compare two values:

# ==
print(10 == 5) # False

# !=
print(10 != 5) # True

# >
print(10 > 5) # True

# <
print(10 < 5) # False

# >=
print(10 >= 5) # True

# <=
print(10 <= 5) # False

# Logical operators
# Logical operators are used to combine conditional statements:

# and
print(10 > 5 and 10 < 15) # True

# or
print(10 > 5 or 10 > 15) # True

# not
print(not(10 > 5 and 10 < 15)) # False

# Identity operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # True

# is not
print(x is not z) # False

# Membership operators
# Membership operators are used to test if a sequence is presented in an object:

# in
x = ["apple", "banana"]
print("banana" in x) # True

# not in
print("pineapple" not in x) # True

# Bitwise operators
# Bitwise operators are used to compare (binary) numbers:

# & (AND) Sets each bit to 1 if both bits are 1
print(10 & 5) # 0

# | (OR) Sets each bit to 1 if one of two bits is 1
print(10 | 5) # 15

# ^ (XOR) Sets each bit to 1 if only one of two bits is 1
print(10 ^ 5) # 15

# ~ (NOT) Inverts all the bits
print(~10) # -11

# << (Zero fill left shift) Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(10 << 5) # 320

# >> (Signed right shift) Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(10 >> 5) # 0

# Dry Run in bits

# 10 = 0000 1010
# 5 = 0000 0101
# 10 & 5 = 0000 0000
# 10 | 5 = 0000 1111
# 10 ^ 5 = 0000 1111
# ~10 = 1111 0101
# 10 << 5 = 0010 1000 0000
# 10 >> 5 = 0000 0000

