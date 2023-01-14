"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Python Sets
"""
#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*
# and unindexed.Set items are unchangeable, but can be
# removed or added
my_set = {"apple", "banana", "cherry"}
print(my_set)
# duplicate items are ignored
my_set = {"apple", "banana", "cherry", "banana"}
print(my_set)
# geeting the length or cardinality of the set
k=len(my_set) # cardinality or number of elements
print(k)
# iteration or iterate between the set elements
for x in my_set:
   print(x)
if "chiku" in my_set:
    print("yes, chiku is there in my set")
else:
    print("no, chiku is not there in my set")
# adding more items  to set
my_set.add("papaya")
print (my_set)
# creating a union or updation
your_set={"watermelon","cherry","banana","chiku"}
my_set.update(your_set)
print(my_set)
u_set=my_set.union(your_set)# another way to create union
print(u_set)
# even a list can be added
my_list=["1","2","3","chiku"]
my_set.update(my_list)
print(my_set)
# removing all the elements of the set
#making it a null set
#my_set.clear()
#print(my_set)
# delete the set
#del my_set   # set is deleted its existance is lost
#print(my_set)
#creating the intersection
your_set={"4","1","2","chiku"}
my_set.intersection_update(your_set)
print(my_set)
# another method
common_set=my_set.intersection(your_set)
print(common_set)
# symmetric difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)








