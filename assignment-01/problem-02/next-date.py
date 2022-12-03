"""
    ? Problem Statement: Q2 of assignment 1.
"""

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

check_leap_year = lambda year: year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def getNextDate(dateString: str) -> str:
    splitDateArray = dateString.split("/")
    
    if len(splitDateArray) != 3:
        raise Exception("Please provide date in the format DD/MM/YYYY")
    
    date = int(splitDateArray[0])
    month = int(splitDateArray[1])
    year = int(splitDateArray[2])
    
    if date == 31 and month == 12:
        year += 1
        month = 1
        date = 1
        
    elif check_leap_year(year) and month == 2 and date == 29:
        month += 1
        date = 1
        
    elif date == DAYS_IN_MONTH[month - 1]:
        month += 1
        date += 1
        
    else:
        date += 1
        
    return f"{date}/{month}/{year}"

print(getNextDate("31/12/2020"))
