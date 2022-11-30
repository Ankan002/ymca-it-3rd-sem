"""
    ? problem Statement: Write a program to compute  using trapezoidal rule.
"""

f = lambda n: ((2 * n) + 4)

def integrate (lower_range, upper_range, n):
     
    # Grid spacing
    grid_space = (upper_range - lower_range) / n
     
    # Computing sum of first and last terms
    # in above formula
    s = (f(lower_range) + f(upper_range))
 
    # Adding middle terms in above formula
    i = 1
    while i < n:
        s += 2 * f(lower_range + i * grid_space)
        i += 1
         
    # h/2 indicates (b-a)/2n.
    # Multiplying h/2 with s.
    return ((grid_space / 2) * s)

print(integrate(5, 10, 10000))
