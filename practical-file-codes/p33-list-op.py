"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Python List
"""
# to be written in straight brackets []
# repetition of elements is allowed
my_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(my_list)
k=len(my_list) # length of the list, number of elements
print(k)
# List is ordered and is numbered from 0 to n
for i in range(k):
    print(my_list[i],end='  ') # iteration with index
print(' ')
for x in my_list:
    print(x) # iteration without index
print(' ')
print(my_list[1:3])
print(my_list[-3:-1])
print(my_list[:3])
print(my_list[3:])
# List can contain all sort of elements
# List can contain heterogeneous elements
new_list=["apple",1,2,3.76,'a',True]
print(new_list)
#list concatenation
x_list=my_list+new_list
print(x_list)
my_list.append(new_list)
print(my_list)  # it is same as my_list=my_list+new_list
#checking an element in the list
if "cherry" in my_list:
    print('Yes, cherry is there in the list')
else:
    print('No, cherry is not there in the list')
#replacing an item in the list
my_list[0]="papaya"
print(my_list)
#inserting an element in the list
my_list.insert(2,"watermelon")
print(my_list)
#removing an element from the list
my_list.pop()  # removes last item of the list
print(my_list)
#removing an element from the list
my_list.pop(2)  # removes item from specified location
print(my_list)
# adding an element
my_list.extend(new_list) #my_list=my_list+new_list
#this is same as my_list=my_list+new_list
print(my_list)
my_list.pop()
print (my_list)
#appending an item
my_list.append("malta")
print(my_list)
#sorting the list
y_list=["MSn","Tfgr","Tfg1e","CKn","YSR","ckn"]
y_list.sort() # It will be sorted in the ascending order
print(y_list)
#sorting the list in descending order
y_list.sort(reverse=True)
print(y_list)
#reversing the list
y_list.reverse()
print(y_list)
# copying a list
x_list=y_list
print(x_list)
#a_list=['a','b']
#b_tuple=('c','d')
#c_list=list(b_tuple)
#a_list.append(c_list)
#print(a_list)