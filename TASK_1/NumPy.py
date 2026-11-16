import numpy as np
#1D Array
arr1 = np.array([12,24,36,48,60])
print("1D Array:", arr1)

# 2D Array
arr2 = np.array([[2, 4,6], [3,6,9], [4,8,12]])
print("\n2D Array:")
print(arr2)

# 2. Array Indexing
print("\nArray Indexing:")
print("First Element:", arr1[0])
print("Third Element:", arr1[2])

# 3. Array Slicing
print("\nArray Slicing:")
print("Elements from index 1 to 3:", arr1[1:4])
print("First Two Rows of 2D Array:")
print(arr2[:2])

# 4. Shape and Dimensions
print("\nShape and Dimensions:")
print("1D Array Shape:", arr1.shape)
print("1D Array Dimensions:", arr1.ndim)
print("2D Array Shape:", arr2.shape)
print("2D Array Dimensions:", arr2.ndim)

# 5. Basic Mathematical Operations
print("\nMathematical Operations:")
a = np.array([12, 24, 36])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# 6. Statistical Functions
print("\nStatistical Functions:")
numbers = np.array([12, 24, 36, 48, 60])
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Sum:", np.sum(numbers))
