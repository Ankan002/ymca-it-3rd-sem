from math import pi


def sin(angle: float) -> float:
    d = angle
    
    if d > 360:
        d = d % 360
    elif d <= 0:
        d = (d % 360) + 360
        
    x = d*pi / 180
    
    sum=x
    alt = -1
    fact = 1
    
    for i in range(1,5):
        fact = (2 * i) * ((2*i) + 1) * fact
        sum = sum + alt * (x ** (2 * i + 1)) / fact
        alt = -alt
        
    return sum

angle = float(input("Enter the angle: "))
print(sin(angle))