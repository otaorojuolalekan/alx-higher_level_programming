#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)


print("-------------------")
print("div = 0")
matrix = [
    [15, 16, 17],
    [18, 19]
    ]
print(matrix_divided(matrix, 7))
print(matrix)
