"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Classes and Objects
"""
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age =age 
        self.gender=gender
    def myfunc(self):
        print('Name is:',self.name)
        print('Age:',self.age)
        print('Gender:',self.gender)
        
p1 = Person("Chander",56,'M')
p1.myfunc()