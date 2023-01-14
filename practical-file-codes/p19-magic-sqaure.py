"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Generating a magic square
"""
n=int(input('Enter the dimension: \n'))
magicSquare = [[0 for x in range(n)]for y in range(n)]
i=0   # row index
j=n//2 # column index
num = 1
while num <= (n * n):
    if i == -1 and j < n:  
        i = n-1
    else:
        if j == n and i < n :
            j = 0
        if i < 0:
            i = n - 1
    if magicSquare[int(i)][int(j)]:  
        j = j - 2
        i = i + 1
        continue
    else:
        magicSquare[int(i)][int(j)] = num
        num = num + 1
        j = j + 1
        i = i - 1      
print("Magic Square for n =", n)
print("Sum of each row or column",n * (n * n + 1) / 2, "\n")
for i in range(n):
    for j in range(n):
            print('%2d ' % (magicSquare[i][j]),end='')
            if j == n - 1:
                print()