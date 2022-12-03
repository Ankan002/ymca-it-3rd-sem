"""
    ? Problem Statement: Q1 of assignment 1.
"""

import math

def print_quadratic_roots(a: int, b: int, c: int) -> None:
    if a == 0: return

    D = (b**2) - (4 * a * c)

    if D >= 0:
        r1 = (-b + math.sqrt(D)) / (2*a)
        r2 = (-b - math.sqrt(D)) / (2*a)

        print("root one =", r1)
        print("root two =", r2)

    else:
        D = -D
        real = -b * (2*a)
        imaginary = math.sqrt(D) / (2*a)

        print("root one =", real, "+i", imaginary)
        print("root two =", real, "-i", imaginary)


co_one = int(input("Enter first coefficient one: "))
co_two = int(input("Enter first coefficient two: "))
co_three = int(input("Enter first coefficient three: "))

print_quadratic_roots(co_one, co_two, co_three)