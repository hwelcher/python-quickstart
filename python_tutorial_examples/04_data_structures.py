# Part 3: Data Structures

# Lists
# A list of numbers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing list items by index
print(fruits[0])
print(fruits[2])

# Appending to a list
fruits.append("orange")
print(fruits)

# Looping through a list
for fruit in fruits:
    print("I like to eat " + fruit)

# A Quick Look at Dictionaries
# A dictionary representing a student
student = {
    "name": "Alex",
    "age": 16,
    "grade": "11th"
}

print(student["name"])
print(student["age"])