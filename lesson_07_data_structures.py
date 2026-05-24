"""
Data Structures - Lists, Tuples, Dicts, Sets

WHEN TO USE:
- List: Ordered, changes, can have duplicates []
- Tuple: Ordered, NEVER changes, protection()
- Dict: Key-value pairs, labeled data{}
- Set: Unique values, no order, no duplicates{}
"""

#List (shopping lists that can change)
shopping_list = ["Milk", "Eggs", "bread"]
shopping_list.append("butter")
shopping_list[0] = "almond milk" 
print("Shopping List : ", shopping_list)

#Tuple (coordinates can never change)
gps_location = (12.937582, 77.627483)
print("GPS Location : ", gps_location)
print("Latitude", gps_location[0])

#dictionary (user profile can change)
user = {
    "name": "Darshan",
    "age": 15,
    "email": "123@gmail.com",
    "city": "Banglore"
}
print("User :" , user)
print("user's name:", user["name"])
user["age"] = 20 # updating user age
print("updated user : ", user)

#set(unique , no duplicates)
tags = {"python", "backend", "learning", "python", "python"}
print("Tags : ",tags)

#example : set opertaions
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print("Union (all):", set1 | set2)
print("Intersection (common):", set1 & set2)

# List Comprehension (elegant way to create lists)
# Old way (verbose)
numbers = [1,2,3,4,5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print("Squared (old way):", squared)

#new way (list comprehension)
numbers = [1,2,3,4,5]
squared = [num ** 2 for num in numbers]
print("Squared (comprehension):", squared)

#filter with comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
evens = [num for num in numbers if num % 2 == 0]
print("Even numbers : ",  evens)

#dictionary comprehension
names = ["Darshan", "Dars", "Dar"]
ages = [15, 16, 17]
user_dict = {name: age for name, age in zip(names, ages)}
print("User Dict:", user_dict)