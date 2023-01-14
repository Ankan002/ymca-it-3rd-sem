"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Performing matrix operations in python
"""
# you need import numpy for performing matrix operations
from numpy import array, add, subtract, divide, multiply, dot, sqrt, sum
# Two matrices are initialized by value
x = array([[1, 2], [4, 5]])
y = array([[7, 8], [9, 10]])
print(x)
print(y)
#  add()is used to add matrices
print ("Addition of two matrices: ")
print (add(x,y))
# subtract()is used to subtract matrices
print ("Subtraction of two matrices : ")
print (subtract(x,y))
# divide()is used to divide matrices
print ("Matrix Division : ")
print (divide(x,y)) #elementwise division
print ("Multiplication of two matrices elementwise: ")
print (multiply(x,y)) #elementwise multiply
print ("Product of two matrices : ")
print (dot(x,y)) #normal matrix multiplication
print ("square root is : ")
print (sqrt(x)) # all elements are square rooted
print ("The summation of elements : ")
print (sum(y)) # sum all elements of matrix
print ("The column wise summation  : ")
print (sum(y,axis=0))
print ("The row wise summation: ")
print (sum(y,axis=1))
# using "T" to transpose the matrix
print ("Matrix transpose: ")
print (x.T)