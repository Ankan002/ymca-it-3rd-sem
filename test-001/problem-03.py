"""
    ? Problem Statement: Write a program to read a date and to print previous date.
"""

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

check_leap_year = lambda year : year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def previous_date(dateString: str) -> str:
    splitDateArray = dateString.split("/")
    
    if len(splitDateArray) != 3:
        raise Exception("Please provide date in the format DD/MM/YYYY")
    
    date = int(splitDateArray[0])
    month = int(splitDateArray[1])
    year = int(splitDateArray[2])
    
    if date == 1 and month == 1:
        year -= 1
        month = 12
        date = DAYS_IN_MONTH[(month - 1)]
        
    elif date == 1:
        month -= 1
        
        if month == 2 and check_leap_year(year): date = 29
        else: date = DAYS_IN_MONTH[(month - 1)]
        
    else: date -= 1
    
    return f"{date}/{month}/{year}"

print(previous_date("01/01/2000"))
        