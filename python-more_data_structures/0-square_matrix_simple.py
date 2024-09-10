#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    dup_matrix = []
    for row in matrix:
        new_row = [i * i for i in row]
        dup_matrix.append(new_row)
    return dup_matrix
