#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    dup_matrix = []
    for row in matrix:
        for i in row:
            dup_matrix.append(i * i)
    return dup_matrix
