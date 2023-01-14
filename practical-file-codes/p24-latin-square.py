"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Program for latin square
"""
n=int(input('Enter the dimension of the square:'))
while n <= 0:  #input validation procedure
    print('invalid dimension')
    n=int(input('Re-Enter the dimension of the square:'))    
for i in range(1,n+1):
    for j in range(1,n+1):
        k=(i+j-2) % n +1
        print(k,end=' ')
    print("")