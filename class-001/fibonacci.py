def get_fibonacci(limit: int) -> list[int] :
    if limit < 2:
        return []
    
    if limit == 2:
        return [0, 1]
    
    current_series = [0, 1]
    
    for i in range(2, (limit + 1)):
        current_series.append(current_series[i - 1] + current_series[i-2])
        
    return current_series

print(get_fibonacci(5))