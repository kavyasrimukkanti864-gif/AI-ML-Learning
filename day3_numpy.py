# a simple numpy array

import numpy as np
numbers = np.array([10,20,30,40,50])
print(numbers)

# array properties

import numpy as np
numbers = np.array([5,10,15,20,25])
print(numbers)
print(numbers.ndim) # no of dimensions
print(numbers.shape) # no of rows and columns
print(numbers.size) # total number of elements
print(numbers.dtype) # datatype of elements

# indexing and slicing

numbers = np.array([10,20,30,40,50])
print(numbers[0])  # Access the first element
print(numbers[-1])  # Access the last element
print(numbers[0:3])  # Access the first three elements
print(numbers[3:5])  # Access the last two elements

# mathematical and useful functions

arr = np.array([10,20,30])
print(arr+5) # Add 5 to each element
print(arr*2) # Multiply each element by 2
print(arr**2) # Square each element
print(np.mean(arr)) # Calculate the mean
print(np.max(arr)) # Find the maximum value
print(np.min(arr)) # Find the minimum value
print(np.sum(arr)) # Calculate the sum

#practice program

import numpy as np
marks = np.array([78,85,92,67,88])
print("Marks:", marks)
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))
print("Total:", np.sum(marks))

# final program 

import numpy as np
print("===== Day 3 - NumPy Basics =====\n")
numbers = np.array([10,20,30,40,50])
print("Array:")
print(numbers)
print("\nFirst Element:", numbers[0])
print("Last Element:", numbers[-1])
print("\nFirst Three Elements:")
print(numbers[:3])
print("\nArray + 5")
print(numbers + 5)
print("\nArray × 2")
print(numbers * 2)
print("\nSquare")
print(numbers ** 2)
print("\nMaximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Average:", np.mean(numbers))
print("Sum:", np.sum(numbers))
print("\n===== Day 3 Completed =====")
