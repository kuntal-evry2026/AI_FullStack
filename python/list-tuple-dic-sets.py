numbers = [1,2,3]
fruits = ["apple","bannana"]
mix = [1,"pomigranate",57.90]
fruits[0] = "orange"
print (fruits)
fruits.append("grape")
fruits.insert(1,"kiwi")
print(fruits)
del fruits[2]
print(fruits)
slice_fruits = fruits[1:5]
print (slice_fruits)

#tuples
colors = ("red","green","blue")
print (colors )

#dictionarirs
person  = {"name":"John","age":25,"city":"New York"}
print (person ["name"])

for key,value in person.items():
    print (key , ":" , value)
    
    
#sets
unique_number = {1,2,3,4} 
print (unique_number)   