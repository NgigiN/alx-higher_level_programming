#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    mat_sqrd = []
    for i in range(len(matrix)):
        mat_sqrd.append([])
        for j in range(len(matrix[i])):
            mat_sqrd[i].append(matrix[i][j] ** 2)
    return (mat_sqrd)
