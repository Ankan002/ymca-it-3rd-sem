"""
    Time Complexity: O(1)
    Space Complexity: O(1)
"""


def print_table(numInput: int) -> None:
    for i in range(1, 11):
        print(f"{numInput} * {i} = {numInput * i}")


num: int = int(input("Enter the number for which you want to find the table: "))

print_table(num)
