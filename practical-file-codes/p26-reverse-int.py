"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Reversing an integer number
"""
num=int(input('Enter the integer number: \n'))# 45802
n=num
s=1
if (num < 0):
    s=-1  # save the sign
    n=-num                                                    
d=0  # number of digits in n
i=n  # save a copy of n
while (i > 0):                    
    i=i//10   # i=4580,458,45,4,0  
    d=d+1     #d=1,2,3,4,5
#reversing the number
sum=0
i=n
j=d-1   # to create positional weights
while (i > 0):
    r=i % 10  #r=2,0,8,5 
    sum=sum+r*10**j # sum=20000,20000,20800,20850,20854 
    i=i//10 #i=4580,458,45,4,0
    j=j-1  #3,2,1,0,-1 
sum=s*sum
print('number=',num,'reverse of the number=',sum)