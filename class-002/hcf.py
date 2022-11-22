def get_hcf(num1: int, num2: int) -> int:
    dividend = max(num1, num2)
    divisor = min(num1, num2)
    remainder: int or None = None

    while remainder != 0:
        if divisor == 0: return dividend

        remainder = dividend % divisor
        dividend = divisor
        if remainder != 0: divisor = remainder

    return divisor


number1 = int(input("Enter number one: "))
number2 = int(input("Enter number two: "))

print(f"HCF of {number1} and {number2} is {get_hcf(number1, number2)}")
