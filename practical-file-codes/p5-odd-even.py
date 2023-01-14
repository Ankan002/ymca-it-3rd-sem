"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Odd even number
"""

def isOddEven(num: int) -> str:
    if num % 2 == 0: return "even"
    return "odd"

print(f"4 is {isOddEven(4)} number")
print(f"3 is {isOddEven(3)} number")
