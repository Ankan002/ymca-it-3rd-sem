"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505

    Question: Program for fibonacci sequence
"""  
n=int(input('Enter the required number of terms: \n'))
while(n<=3):
    print('Number of terms should be 3 or more')
    n=int(input('Enter the required number of terms: \n'))    
i=0
j=1
print(i,end=' ')
print(j,end=' ')
count=2
while (count <=n):
    count+=1
    k=i+j
    print(k,end=' ')
    i=j
    j=k