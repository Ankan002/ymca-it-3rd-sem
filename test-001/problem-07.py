"""
    ? Problem Statement: Write a program to read an integer number and to print: 
                            ? - Product of its digits if it is odd.
                            ? - Sum of its digits if it is even
"""

def get_sum_or_product(num: int) -> int:
    num = abs(num)
    if num % 2 == 0:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
            
        return sum
    
    product = 1
    
    while num > 0:
        product *= num % 10
        num //= 10
        
    return product

num = int(input("Enter the number: "))
print(get_sum_or_product(num))
