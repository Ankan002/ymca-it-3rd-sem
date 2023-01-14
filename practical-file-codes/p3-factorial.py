"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: program to find factorial of a number
"""
n=int(input('Enter the number: \n'))
k=1
Compute=True
while (n < 0 and k< 5):
    print('invalid number')
    n=int(input('Re-Enter the number: '))
    k=k+1
if (k >= 5 and n < 0):
    print('you have exceeded the valid number of attempts')
    Compute=False
if Compute is True:
    f=1
    for i in range (1,n+1):
        f=f*i
if Compute is True:
    print(n,'!=',f)