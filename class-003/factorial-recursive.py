def factorialRecursive(num: int) -> int:
    if num < 0: return -1
    if num == 0: return 1
    if num <= 2: return num
    
    return num * factorialRecursive(num - 1)

print(factorialRecursive(5))