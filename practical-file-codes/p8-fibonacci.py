"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: program to check if a year is leap or not
"""
  
year=int(input('Enter the year: \n'))
while (year <= 0):
    print('Not a valid input')
    year=int(input('Re-Enter the year:'))
a=year % 4
b=year % 100
c=year % 400
if (a==0 and b!=0 or b==0 and c==0):
    print('year is leap')
else:
    print('year is not leap')
    