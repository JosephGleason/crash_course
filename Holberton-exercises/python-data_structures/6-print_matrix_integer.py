#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted = []
        for num in row:
           formatted.append("{:d}".format(num))
        print(" ".join(formatted))
