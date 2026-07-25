# Day 2 - Python Basics
# Codomax AI & ML Internship

print("----- Day 2: Python Basics -----\n")

# Variables
name = "Kavyasri"
age = 19
cgpa = 8.7

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print()

# Data Types
print("Data Types")
print(type(name))
print(type(age))
print(type(cgpa))
print()

# Operators
a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)
print()

# If-Else
marks = 85

if marks >= 75:
    print("Good job! You scored Grade A.")
else:
    print("Keep practicing!")
print()

# For Loop
print("Numbers from 1 to 5")

for i in range(1, 6):
    print(i)

print()

# While Loop
print("Counting using while loop")

count = 1

while count <= 3:
    print(count)
    count += 1

print()

# Functions

def greet(name):
    print("Hello,", name + "! Welcome to Python.")

greet(name)

print()

def add(num1, num2):
    return num1 + num2

answer = add(12, 8)

print("Sum =", answer)

print()

# Mini Program
number = 9

if number % 2 == 0:
    print(number, "is an Even number")
else:
    print(number, "is an Odd number")

print("\nDay 2 task completed successfully!")