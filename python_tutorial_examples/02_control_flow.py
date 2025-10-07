# Part 2: Control Flow

# Conditional Statements: if, elif, else
age = 17

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Loops: while and for
# A simple countdown
count = 5
while count > 0:
    print(count)
    count = count - 1 # or count -= 1
print("Blast off!")

# Loop through a range of numbers
for i in range(5):  # range(5) generates numbers from 0 to 4
    print("The current number is " + str(i))

# Loop through the letters of a string
for letter in "Python":
    print(letter)