# Part 4: Functions

# Defining and Calling a Function
# Define a function named 'greet'
def greet():
    print("Hello from a function!")

# Call the function
greet()

# Arguments and Parameters
def greet_by_name(name):
    print("Hello, " + name + "!")

greet_by_name("Maria")
greet_by_name("David")

# Return Values
# This function calculates the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Call the function and store the result in a variable
rect_area = calculate_area(10, 5)
print("The area is " + str(rect_area))