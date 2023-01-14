"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Generating a magic square of 4n Type
"""
n=int(input('Enter the dimension: \n'))
MS4n = [[0 for x in range(n)]for y in range(n)]
# store count in the cells
for i in range(n):
    for j in range(n):
        MS4n[i][j] = (n*i) + j + 1         
# Check for normal storage
for i in range(n):
    for j in range(n):
        print(MS4n[i][j],end=' ')
    print(" ")
print(" ")
# make replacements in red area
for i in range(n//4):
    for j in range(n//4):
            MS4n[i][j] = (n*n + 1) - MS4n[i][j]
for i in range(n//4):
    for j in range(3*(n//4),n):
        MS4n[i][j] = (n*n + 1) - MS4n[i][j]
for i in range(3* n//4, n):
    for j in range(n//4):
            MS4n[i][j] = (n*n + 1) - MS4n[i][j]
for i in range (3* n//4,n):
    for j in range(3* n//4,n):
            MS4n[i][j] = (n*n + 1) - MS4n[i][j]
for i in range(n//4, 3* n//4):
    for j in range(n//4,3* n//4):
            MS4n[i][j] = (n*n + 1) - MS4n[i][j]
# print magic square
for i in range(n):
    for j in range(n):
        print(MS4n[i][j],end='   ')
    print(" ")
# print using %3d to avoid misallignment 