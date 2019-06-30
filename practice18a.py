import numpy as np

# List Creation
print()
print("List")
print()

numbers = [10, 20, 30, 40, 50]
print(numbers, type(numbers))

array = np.array([10, 20, 30, 40, 50])
print(array, type(array))

print()
print("Tuple")
print()

numbers = (10, 20, 30, 40, 50)
print(numbers, type(numbers))

array = np.array((10, 20, 30, 40, 50))
print(array, type(array))

print()
print("Set")
print()

numbers = {10, 20, 30, 40, 50}
print(numbers, type(numbers))

array = np.array({10, 20, 30, 40, 50})
print(array, type(array))

print()
print("Dictionary")
print()

numbers = (10, 20, 30, 40, 50)
print(numbers, type(numbers))

array = np.array({10:1, 20:2, 30:3, 40:4, 50:5})
print(array, type(array))