"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Python Classes
"""
class Complex:
    def __init__(self, real, image):
        self.real = 0
        self.imag= 0
    def display(self):
        print(self.real,'+i',self.imag)        
c1 = Complex(2,3)
c1.display()