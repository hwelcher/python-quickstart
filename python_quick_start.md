# Python Quick Start for High School Students

Welcome to the world of Python! This tutorial is designed to give you a one-hour introduction to the basics of Python programming. No prior coding experience is needed. By the end of this tutorial, you'll be able to write simple Python programs and have a solid foundation for further learning.

## Table of Contents

*   [Introduction to Python](#introduction-to-python)
*   [Part 1: The Basics](#part-1-the-basics)
*   [Part 2: Control Flow](#part-2-control-flow)
*   [Part 3: Data Structures](#part-3-data-structures)
*   [Part 4: Functions](#part-4-functions)
*   [Wrap-up and Next Steps](#wrap-up-and-next-steps)

## Introduction to Python

**What is Python?**

Python is a high-level, versatile programming language known for its readability and simple syntax. It was created by Guido van Rossum and released in 1991. Think of it as a way to give instructions to a computer in a language that's much easier to understand than the computer's native binary code.

**Why Python?**

*   **Easy to Learn:** Python reads like plain English, which makes it one of the easiest programming languages to learn for beginners.
*   **Versatile:** You can use Python for a wide range of applications, including web development, data science, artificial intelligence, game development, and automation.
*   **Large Community:** Python has a massive and supportive community, which means you can easily find help and resources online.

**Getting Started: Online Python Interpreter**

To get started without the hassle of installing anything on your computer, you can use an online Python interpreter. These are websites that let you write and run Python code directly in your browser. Here are a couple of popular options:

*   **Replit:** [https://replit.com/languages/python3](https://replit.com/languages/python3)
*   **Google Colab:** [https://colab.research.google.com/](https://colab.research.google.com/)

For this tutorial, just open one of the links above, and you'll be ready to start coding!

## Part 1: The Basics (15 minutes)

Let's dive into the fundamental concepts of Python.

### Your First Python Program: "Hello, World!"

It's a tradition in programming to start with a program that prints "Hello, World!". In Python, it's just one line:

```python
print("Hello, World!")
```

Go ahead and type this into your online interpreter and run it. You should see `Hello, World!` displayed as the output.

### Variables and Data Types

A **variable** is like a container that stores a value. You can give it a name and use it to refer to the value later.

```python
# A variable named 'greeting' that stores a string
greeting = "Hello, students!"
print(greeting)

# A variable named 'age' that stores an integer
student_count = 25
print(student_count)

# A variable for pi, which is a float (a number with a decimal)
pi = 3.14159
print(pi)
```

Python has several built-in **data types**. Here are the most common ones:
*   **String (`str`)**: Text, enclosed in double (`"`) or single (`'`) quotes.
*   **Integer (`int`)**: Whole numbers, like `10`, `-5`, `1000`.
*   **Float (`float`)**: Numbers with decimal points, like `3.14`, `-0.5`.

### Getting User Input

You can make your programs interactive by asking the user for input. The `input()` function prompts the user for text and returns it as a string.

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```
**Note:** The `+` operator, when used with strings, combines them. This is called **concatenation**.

### Basic Operations

Python can be used as a powerful calculator.

```python
# Addition
sum = 10 + 5
print(sum)  # Output: 15

# Subtraction
difference = 20 - 8
print(difference) # Output: 12

# Multiplication
product = 7 * 6
print(product) # Output: 42

# Division
quotient = 50 / 10
print(quotient) # Output: 5.0
```

What if you want to do math with a user's input? Remember that `input()` gives you a string. You need to convert it to a number first using `int()` or `float()`.

```python
age_str = input("How old are you? ")
age = int(age_str)
next_year_age = age + 1
print("Next year, you will be " + str(next_year_age) + " years old.")
```
Here, we converted the age back to a string with `str()` to concatenate it with the other strings for printing.

> You can find all the code for this section in the file: `python_tutorial_examples/01_basics.py`

## Part 2: Control Flow (20 minutes)

**Control flow** refers to the order in which the statements in your program are executed. You can control this flow using conditional statements and loops.

### Conditional Statements: `if`, `elif`, `else`

Conditional statements allow you to execute certain blocks of code only if a specific condition is true.

```python
age = 17

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

You can also use `elif` (short for "else if") to check for multiple conditions.

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

### Loops: `while` and `for`

Loops are used to repeat a block of code multiple times.

A **`while` loop** continues as long as a certain condition is true.

```python
# A simple countdown
count = 5
while count > 0:
    print(count)
    count = count - 1 # or count -= 1
print("Blast off!")
```

A **`for` loop** iterates over a sequence (like a list of numbers or a string).

```python
# Loop through a range of numbers
for i in range(5):  # range(5) generates numbers from 0 to 4
    print("The current number is " + str(i))

# Loop through the letters of a string
for letter in "Python":
    print(letter)
```

> You can find all the code for this section in the file: `python_tutorial_examples/02_control_flow.py`

### Mini-Project: Number Guessing Game

Let's combine what we've learned to create a simple number guessing game.

```python
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess = 0

print("I'm thinking of a number between 1 and 100.")

while guess != secret_number:
    guess_str = input("What's your guess? ")
    guess = int(guess_str)

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("You got it! The number was " + str(secret_number))
```
This game uses a `while` loop to keep asking for guesses until the user gets it right. It also uses `if/elif/else` to provide hints.

> You can find the code for this game in the file: `python_tutorial_examples/03_number_guessing_game.py`

## Part 3: Data Structures (10 minutes)

Data structures allow you to store and organize data efficiently. Python has several built-in data structures, but we'll focus on the most common one: the list.

### Lists

A **list** is an ordered collection of items. You can create a list by placing items inside square brackets `[]`, separated by commas.

```python
# A list of numbers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

You can access individual items in a list using their **index**. The index is the item's position in the list, and it starts from 0.

```python
print(fruits[0]) # Output: apple
print(fruits[2]) # Output: cherry
```

You can also add items to a list with the `append()` method and loop through a list with a `for` loop.

```python
fruits.append("orange")
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange']

for fruit in fruits:
    print("I like to eat " + fruit)
```

### A Quick Look at Dictionaries

Another useful data structure is the **dictionary**. It stores data in **key-value pairs**.

```python
# A dictionary representing a student
student = {
    "name": "Alex",
    "age": 16,
    "grade": "11th"
}

print(student["name"]) # Output: Alex
print(student["age"])  # Output: 16
```
We won't go deep into dictionaries in this tutorial, but it's good to know they exist!

> You can find all the code for this section in the file: `python_tutorial_examples/04_data_structures.py`

## Part 4: Functions (10 minutes)

Functions are reusable blocks of code that perform a specific task. Using functions helps keep your code organized and avoids repetition.

### Defining and Calling a Function

You can define a function using the `def` keyword, followed by a function name, parentheses `()`, and a colon `:`.

```python
# Define a function named 'greet'
def greet():
    print("Hello from a function!")

# Call the function
greet() # Output: Hello from a function!
```

### Arguments and Parameters

You can pass information into functions through **arguments**. The variables that receive these arguments inside the function are called **parameters**.

```python
def greet_by_name(name):
    print("Hello, " + name + "!")

greet_by_name("Maria") # Output: Hello, Maria!
greet_by_name("David") # Output: Hello, David!
```

### Return Values

Functions can also send a value back to the code that called it. This is done using the `return` keyword.

```python
# This function calculates the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Call the function and store the result in a variable
rect_area = calculate_area(10, 5)
print("The area is " + str(rect_area)) # Output: The area is 50
```
Using functions to perform calculations and return results is a very common practice in programming.

> You can find all the code for this section in the file: `python_tutorial_examples/05_functions.py`

## Wrap-up and Next Steps (5 minutes)

Congratulations on taking your first step into the world of Python programming!

**What You've Learned**

In just one hour, you've learned the essentials of Python, including:
*   Writing and running your first program.
*   Storing data in variables with different data types.
*   Getting input from a user.
*   Controlling the flow of your program with `if` statements and `while`/`for` loops.
*   Organizing data in lists.
*   Creating reusable code with functions.

**Next Steps**

The journey of a programmer is one of continuous learning. Here are some ideas for what you can do next:

*   **Practice, Practice, Practice:** Try to modify the number guessing game. Can you add a limit to the number of guesses? Can you let the user choose the range of numbers?
*   **Build Small Projects:** Think of a simple idea and try to build it. A simple calculator, a to-do list app, or a text-based adventure game are all great starting points.
*   **Explore More Python:** There's so much more to Python! Look into other data structures like dictionaries and tuples, learn about file handling, and explore object-oriented programming.
*   **Check Out Online Resources:**
    *   **The Official Python Tutorial:** [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
    *   **freeCodeCamp:** [https://www.freecodecamp.org/learn/scientific-computing-with-python/](https://www.freecodecamp.org/learn/scientific-computing-with-python/)
    *   **Codecademy:** [https://www.codecademy.com/learn/learn-python-3](https://www.codecademy.com/learn/learn-python-3)

Keep coding, stay curious, and have fun!