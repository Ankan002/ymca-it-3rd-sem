"""
    ? Problem Statement: Q4 of assignment 1.
"""

def print_odds_in_range(start: int, end: int) -> None:
    if start % 2 == 0:
        start += 1
        
    while start <= end:
        print(start)
        start += 2
        
        
        
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

if num1 < 0 or num2 < 0:
    print("Please provide positive numbers only....")
else:
    print_odds_in_range(num1, num2)