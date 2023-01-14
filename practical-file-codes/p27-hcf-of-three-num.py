"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Program for hcf of three numbers
"""
def hcf(a,b):
    if a > b:
        dvd=a
        dvsor=b
    else:
        dvd=b
        dvsor=a
    r=dvd % dvsor
    while (r !=0):
        dvd=dvsor
        dvsor=r
        r=dvd % dvsor
    hcf=dvsor
    return hcf
# main program
m=int(input('Enter first number: \n'))
n=int(input('Enter second number: \n'))
p=int(input('Enter third number: \n'))
while ( m<= 0 or n<= 0 or p <= 0):
    print('invalid data')
    m=int(input('Enter first number: \n'))
    n=int(input('Enter second number: \n'))
    p=int(input('Enter third number: \n'))
u=hcf(hcf(m,n),p)
print(u)