"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Program to compute hcf and lcm of 2 numbers
"""  
a=int(input('Enter first number : \n'))
b=int(input('Enter second number : \n'))
while (a <= 0 or b <=0):
    print('Not a valid input')
    a=int(input('Enter first number :'))
    b=int(input('Enter second number :'))
if ( a > b):
    dvd=a
    dvsor=b
else:
    dvd=b
    dvsor=a
remd=dvd % dvsor
while (remd !=0):
    dvd=dvsor
    dvsor=remd
    remd=dvd % dvsor
hcf=dvsor
print ('hcf=',hcf)
lcm=a*b/hcf
print('lcm=',lcm)
