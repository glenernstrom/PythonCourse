"""
Implementation of Euclid's algorithm.
"""

a = int(input("Enter a positive integer, a: "))
b = int(input("Enter a positive integer, b: "))

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(f"The GCD is {a}.")