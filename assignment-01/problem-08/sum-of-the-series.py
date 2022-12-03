def get_sum_of_the_series(max_base: int, max_power: int) -> int:
    sum = 0
    
    base = 1
    power = 2
    
    while base <= max_base and power <= max_power:
        sum += (base ** power)
        base += 1
        power += 1
        
    return sum

print(get_sum_of_the_series(7, 8))
        