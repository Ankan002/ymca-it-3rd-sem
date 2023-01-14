"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Recursive function for sum of digits of a integer number
"""
def sod(n):     #sum of digits function   
    if (n==0):  
        return 0
    else:
        k=n // 10
        p=n % 10  # remainder or digits
        return p+sod(k)  
#return 2+sod(453),2+3+sod(45),2+3+5+sod(4), 2+3+4+5+sod(0),2+3+4+5+0
k=int(input('Enter the number: \n')) #4532  
t=sod(k)   
print('Number=',k,'Sum of digits=',t)