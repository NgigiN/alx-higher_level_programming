#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda row: lit(map(lambda x: x * x), row))), matrix))
