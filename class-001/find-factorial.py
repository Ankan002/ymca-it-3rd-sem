"""
    Time Complexity: O(n)
    Space Complexity: O(1)
"""


def get_factorial(numInput: int) -> int:
    if numInput < 0:
        return -1

    fact: int = 1

    for i in range(2, numInput + 1):
        fact *= i

    return fact


num: int = int(input("Enter the number for which you want to find factorial: "))

tries_remaining = 5

while tries_remaining > 0:
    factorial = get_factorial(num)

    if factorial < 1:
        print("Invalid Input")
        num = int(input("Re-enter the value: "))
        tries_remaining -= 1

    else:
        print(f"Factorial of {num} is {factorial}")
        break

if tries_remaining <= 0:
    print("You have exhausted all of your tries.")
