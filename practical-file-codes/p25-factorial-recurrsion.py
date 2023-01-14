"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Factorial by recursion
"""
def f(x):
    if (x==0):   
        return 1
    else:
        return x*f(x-1)
n=int(input('Enter the number:'))
k=f(n)
print(n,'!=',k)