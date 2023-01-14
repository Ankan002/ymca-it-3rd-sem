"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Program for roots of quadratic equation
"""  
import math
a=float(input('Enter the coeff. of x^2: \n'))
b=float(input('Enter the coeff. of x: \n'))
c=float(input('Enter constant term: \n'))
while (a==0):
    print('Not a valid input')
    a=input('Re-Enter the coeff. of x^2: \n')
disc=b**2-4*a*c
if (disc >= 0):
    r1=(-b+math.sqrt(disc))/(2*a)
    r2=(-b-math.sqrt(disc))/(2*a)
    print('root1=',r1)
    print('root2=',r2)
else:
    real=-b/(2*a)
    imag=math.sqrt(-disc)/(2*a)
    print('root1=',real,'+i',imag)
    print('root2=',real,'-i',imag)
    