"""
    ? Problem Statement: Q6 of assignment 1.
"""

def reverse_num(num: int) -> int:
    reversed_num = 0
    
    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10
        
    return reversed_num


num = int(input("Enter a number: "))

if num < 0:
    print("Please provide a positive integer")
else:       
    print(reverse_num(num))