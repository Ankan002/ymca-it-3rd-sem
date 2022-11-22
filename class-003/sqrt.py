from math import ceil, floor


def sqrt(num: int) -> int:
    if(num < 0): return -1
    if(num <= 1): return num
    
    num = floor(num)
    
    left = 1
    right = ceil(num / 2)
    
    square_root = -1
    
    while left <= right:
        mid = left + ((right - left) // 2)
        
        if (mid * mid) == num:
            square_root = mid
            break
        elif (mid * mid) < num:
            square_root = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return square_root

print(sqrt(64))