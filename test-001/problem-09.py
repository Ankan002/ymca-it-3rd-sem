"""
    ? Problem Statement: Write a program to read print the sum of the series 18+27+36+45+54+63+72+81
"""

def get_sum(max_base: int, max_power: int) -> int:
    current_base = 1
    current_power = max_power
    
    sum = 0
    
    while current_base <= max_base and current_power >= 1:
        sum += current_base ** current_power
        current_base += 1
        current_power -= 1
        
    return sum

max_base = int(input("Enter the max base: "))
max_power = int(input("Enter the max power: "))

if max_base != max_power:
    raise Exception("Max power and max base must be the same.")

print(get_sum(max_base, max_power))