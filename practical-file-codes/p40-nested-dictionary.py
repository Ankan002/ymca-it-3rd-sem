"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: nested dictionaries
"""
#Nested dictionary is an unordered collection of dictionaries
#Slicing Nested Dictionary is not possible.
# We can shrink or grow nested dictionary as per need.
# Like Dictionary, it also has key and value.
# Dictionary are accessed using key.
people = {
        1: {'name': 'John', 'age': '27', 'sex': 'Male'},
        2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}
        }
print(people[1])
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
# Adding more elements to nested dictionary 
people[3] = {}  # null dictionary that does contain any key value pair
people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'
print(people)
# Removing elements from nested dictionary
# a particular key value pair will be removed
del people[3]['married']
print(people[3])
# adding dictionary directly to a nested dictionary
people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people)
# Iterating through nested dictionary
# A dictionary has two elements key and value
#key and value combination is known as item
for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)    
    for key in p_info:
        print(key + ':', p_info[key])