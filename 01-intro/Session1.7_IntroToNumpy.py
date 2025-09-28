import numpy as np
import pandas as pd

""" Creating Arrays"""
print(np.zeros(5))

print(np.ones(10))

print(np.full(10, 2.5))

# Convert list to array
a = np.array([1, 2, 3, 4, 5])
# Access 3rd element
print(a[2])

# Change value in array
a[2] = 10

print(a)

print(np.arange(10))

print(np.arange(3, 10))

print(np.linspace(0, 1, 11))

"""Multi-dimensional arrays"""

print(np.zeros((5, 2))) # Accepts a tuple

n = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(n[0, 1]) # Returns 2
#n[0, 1] = 20

print(n[1]) # Access entire row

print(n[:, 1]) # Access entire second column

"""Randomly Generated Arrays"""
print(np.random.seed(2))
print(100 * np.random.rand(5, 2))
print(np.random.randn(5, 2))
print(np.random.randint(low=0, high=100, size=(5, 2)))

"""Element-wise operations"""
a = np.arange(5)
print(a)
print(a + 1)
print(a * 2)

b = (10 + (a * 2)) ** 2 / 100
print(b)

print(a + b)

print(a / b + 10)
"""Comparison Operations"""

print(a >= 2)

print(a > b)

print(a[a > b]) # Returns elements from array a where condition is true

"""Summarizing operations"""

print(a.min())
print(a.max())
print(a.sum())
print(a.mean())
print(a.std())

print(n.sum())
print(n.min())





