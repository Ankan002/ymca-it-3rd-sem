"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Enumerating subsets of a Set
"""
A= {"apple", "banana", "cherry","Chiku"}
print(A)
n=len(A) # cardinality or number of elements
print(n)
num=2**n # number of subsets
print(num)
A_list=list(A) #converting set to list
print(A_list)
for i in range(num):
    print('subset{',i,'}=',end='')
    t=i
    j=1
    print('{',end='') # subset printing begins
    while t!=0:
        m=t % 2  # take remainder
        if m==1 :
            print(A_list[n-j],',',end='')
        t=t//2  # get quotient
        j=j+1
    print('}')