"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: A tuple is an ordered and unchangable collection repetition is allowed, index begins with 0
"""
my_tuple = ("apple", "banana", "cherry","apple")
print(my_tuple)
new_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(new_tuple[2:5])
print(new_tuple[:4])
print(new_tuple[2:])
print(new_tuple[-4:-1])
# checking an item in the tuple
if "cherry" in new_tuple:
    print("yes")
else:
    print("No")
# normally a tuple is immutable, if you want to make any changes then
# convert it to list, apply changes, convert back to tuple
my_list=list(new_tuple)
print(my_list)
print(new_tuple)
my_list.append("watermelon")
new_tuple=tuple(my_list)
print(new_tuple)
# delete a tuple
#del new_tuple #delete the tuple completely
#print(new_tuple)
#unpacking a tuple
fruits=new_tuple
(fruit1,fruit2,fruit3,*fruit4)=fruits  # asterik means rest
print(fruit1)
print(fruit2)
print(fruit3)
print(*fruit4)
#iterate in tuple
for x in fruits:
    print(x)
# join tuple
x=("1","2")
y=("3","4")
z=x+y
print(z)
# multiply tuples
z=x*2
print(z)