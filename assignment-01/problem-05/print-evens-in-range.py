"""
    ? Problem Statement: Q5 of assignment 1.
"""

def print_evens_in_range(num1: int, num2: int) -> None:
    if num1 % 2 != 0: num1 += 1
    else: num1 += 2
    
    while num1 < num2:
        print(num1)
        num1 += 2
        

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

if num1 < 0 or num2 < 0:
    print("Please provide positive numbers only....")
else:
    print_evens_in_range(num1, num2)