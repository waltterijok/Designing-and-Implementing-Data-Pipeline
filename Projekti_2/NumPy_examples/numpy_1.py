import numpy as np

# 1D array

array1 = np.array([1, 2, 3, 4, 5])
print(f"\narray1:\n{array1}\n")

#2D array

array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"array 2:\n{array2}\n")

# Addition

array3 = array1 + 5
print(f"\nArray 3:\n{array3}")

# Multiplication
array4 = array1 * 2
print(f"\nArray 4:\n{array4}")

# Transpose ( turns the rows of data into columns)

array5 = array2.T
print(f"\nArray 5:\n{array5}")

# Matrix multiplication

array6 = np.dot(array2, array2.T)
print(f"\nArray 6:\n{array6}")