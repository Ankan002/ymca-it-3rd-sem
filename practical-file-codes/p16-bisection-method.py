"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Finding root by bisection method
"""
import math
def f(x):
    return x**3-18*x**2+24
i=-26
t1=50 # to enter into the while loop
# Searching the unit interval
while (t1 > 0 and i<=25):
    i=i+1
    t1=f(i)*f(i+1)
    print(i,i+1,f(i),f(i+1),t1)
if (t1 > 0):
    print('No real root between -25 and 25')
else:
    print('root lies between',i,'and',i+1)
# Apply Bisection
a=i
b=i+1
print(f(a),f(b))
mid=(a+b)/2
k=1
m=math.fabs(f(mid))
while (m > 0.00000000001 and k <=25):
    if (f(a)*f(mid) < 0):
        b=mid
        mid=(a+b)/2
    else:
        a=mid
        mid=(a+b)/2
    m=math.fabs(f(mid))
    k=k+1           
print('root=',mid,'f(root=)',m)
