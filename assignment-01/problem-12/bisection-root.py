"""
    ? problem Statement: Q12 of assignment 1.
"""

def f(x: int) -> int:
    return 2*x**3 + 4*x**2 + x - 3

def bisection(a: int, b: int) -> int:
    if f(a) * f(b) >= 0:
        raise("Your both assumptuions are wrong....")
    
    c = a
    
    while b-a >= 0.01:
        c = (a+b) / 2
        
        if f(c) == 0.0: break
        
        if (f(c) * f(a)) < 0:
            b = c
        else:
            a = c
            
    return c

a = -200
b = 300

print(bisection(a,b))