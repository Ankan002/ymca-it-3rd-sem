"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Hcf by recusion
"""
def hcf(m1,m2):
    if m1 % m2 ==0:    # terminal condition
        return m2 
    else:
        return hcf(m2,m1 % m2)  # recursive condition
n1=int(input('Enter first number: \n'))
n2=int(input('Enter second number: \n' ))
if (n1 <= 0 or n2<= 0 ):
    print('invalid numbers')
    n1=int(input('Re-Enter first number:'))
    n2=int(input('Re-Enter second number:' ))
if (n1 < n2):    # swap, exchanging the values
    temp=n1
    n1=n2
    n2=temp
u=hcf(n1,n2)
print('hcf(',n1,',',n2,')=',u)