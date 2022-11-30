"""
    ? problem Statement: Write a program to compute  using trapezoidal rule.
"""

f = lambda n: ((2 * n) + 4)

def integrate (lower_range, upper_range, grid_divisions):
    grid_space = (upper_range - lower_range) / grid_divisions

    sum = (f(lower_range) + f(upper_range))
 
    i = 1
    while i < grid_divisions:
        s += 2 * f(lower_range + i * grid_space)
        i += 1
         
    
    return ((grid_space / 2) * sum)

print(integrate(5, 10, 10000))
