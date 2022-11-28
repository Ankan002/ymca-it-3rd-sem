def check_leap_year(year: int):
    if year < 0: return False

    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def getDay(date: str) -> str:
    """
    Arguments:
    
    - date: string -> It must be in the format dd|mm|yyyy
    """
    
    waste_day_list = [0, 3, 3, 6, 8, 11, 13, 16, 19, 21, 24, 26]
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    date_array = date.split("|")
    
    date = int(date_array[0])
    month = int(date_array[1])
    year = int(date_array[2])
    
    y = year - 1
    month = month - 1
    
    y = y % 400
    
    excess_days = ((y // 100) * 5) + (y % 100) + ((y % 100) // 4) + waste_day_list[month] + date
    
    if(check_leap_year(year)) and month >= 2:
        excess_days += 1
        
        
    return day_list[(excess_days % 7) - 1]
    

print(getDay("06|08|2002"))