"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: To compute cosine of x
"""
import math
a=float(input('Enter the angle in degrees: \n'))
x=3.14159*a/180
sum=1
term=-1
d=1
for i in range (1,9):
    d=d*(2*i)*(2*i-1)
    sum=sum+term*(x**(2*i))/d
    term=-term
print('cos(',a,')=',sum)
s=math.cos(x)
print(s)