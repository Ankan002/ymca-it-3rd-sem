"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Python Dictionary
"""
# stores data in the form of key value pair
# my dictionary is about my car
my_car = {
  "brand": "Huandai",
  "model": "i20",
  "year": 2010,
  "fuel":"Petrol"
  }
print(my_car)
print(my_car["fuel"])
your_car = {
  "brand": "Suzuki",
  "model": "ciaz",
  "year": 2015,
  "fuel":"Petrol"
  }
x=your_car.get("model")
print(x)
# keys of the dictionary
x=your_car.keys()
print(x)
# adding more keys
my_car["color"]="white"  
x=my_car.keys()
print(x)
print(my_car)
print(my_car.keys())
# removing a key
my_car.pop("year")
print(my_car)
# iterating over the dictionary, all values will be printed
for x in my_car:
    print(x)
    print(my_car[x])

