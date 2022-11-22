"""
    !Time Complexity: O(1)
    !Space Complexity: O(1)
"""


def check_leap_year(year: int):
    if year < 0: return False

    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


input_year = int(input("Enter the year: "))

if check_leap_year(input_year): print(f"{input_year} is Leap Year")
else: print(f"{input_year} is not a Leap Year")
