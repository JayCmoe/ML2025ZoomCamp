import numpy as np
import pandas as pd


"""Vector Operations"""

a = np.array([2, 4, 5, 6])
print(2 * a)

"""Multiplication"""
# Vector-vector multiplication (dot product)
v1 = np.array([2, 4, 5, 6])
v2 = np.array([1, 0, 0, 2])

print(v1 * v2)


def vector_vector_multiplication(u, v):
    # Multiply each vector against second vector and sum total
    assert u.shape[0] == v.shape[0]

    n = u.shape[0]
    result = 0.0
    for i in range(n):
        result = result + u[i] * v[i]

    return result


print(vector_vector_multiplication(v1, v2))
print(v1.dot(v2))

# Matrix-vector multiplication

v3 = np.array([[2, 4, 5, 6],
              [1, 2, 1, 2],
              [3, 1, 2, 1]])
v4 = np.array([[1, 1, 2],
              [0, 0.5, 1],
              [0, 2, 1],
              [2, 1, 0]])


def matrix_vector_multiplication(u, v):
    # Multiply each row in matrix against column vector and sum total
    assert u.shape[1] == v.shape[0]

    num_rows = u.shape[0]

    result = np.zeros(num_rows)

    for i in range(num_rows):
        result[i] = vector_vector_multiplication(u[i], v)

    return result

print(v3)
print(v2)
print(matrix_vector_multiplication(v3, v2))
print(v3.dot(v2))

# Matrix-matrix multiplication

def matrix_matrix_multiplication(u, v):
    assert u.shape[1] == v.shape[0]

    num_rows = u.shape[0]
    num_columns = v.shape[1]

    result = np.zeros((num_rows, num_columns))

    for i in range(num_columns):
        vi = v[:, i]
        uvi = matrix_vector_multiplication(u, vi)
        result[:, i] = uvi

    return result


print(matrix_matrix_multiplication(v3, v4))
print(v3.dot(v4))

"""Identity Matrix"""

I = np.eye(3)
V = v4.dot(I)

"""Matrix Inverse"""
Vs = V[[0, 1, 2]]
print(Vs)

Vs_inv = np.linalg.inv(Vs)
print(Vs_inv)

print(Vs_inv.dot(Vs))