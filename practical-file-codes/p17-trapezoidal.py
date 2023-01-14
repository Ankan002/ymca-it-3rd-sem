"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Integration using trapezoidal rule
"""
def f(x):
    return x**2  #function to be integrated
a=float(input('Enter lower limit: \n'))
b=float(input('Enter upper limit: \n'))
n=10000 # number of intervals
h=(b-a)/n
sum=0 #initialise integral value
for i in range (n+1):
    sum=sum+f(a+i*h)
sum=h*(sum-(f(a)+f(b))/2)    
print(sum)