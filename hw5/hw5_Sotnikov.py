#!/usr/bin/env python
# coding: utf-8

import numpy as np


# The three arrays (by A. Duma)
if __name__ == "__main__":
    array_atos = np.array([[1, 3], [5, 7], [9, 11]])
    array_portos = np.arange(1, 12, 2).reshape(3, 2)
    array_aramis = np.linspace(1, 11, 6, dtype="int").reshape(3, 2)

# Bonus
    array_dartanyan = np.random.random(4)



# Multiplication of matrices
def matrix_multiplication(matrix1, matrix2):
    return matrix1 @ matrix2


# Checking possibility of matrix multiplication and multiplication, if possible
def multiplication_list_of_matrices(list_of_matrices):
    flag = "first"
    flag2 = True
    multiplicated_matrix = None
    for matrix_number in range(1, len(list_of_matrices)):
        if flag == "first":
            flag = "not first"
            if list_of_matrices[matrix_number].shape[0] == list_of_matrices[matrix_number - 1].shape[1]:
                multiplicated_matrix = list_of_matrices[matrix_number - 1] @ list_of_matrices[matrix_number]
            else:
                flag2 = False
                break
        else:
            if list_of_matrices[matrix_number].shape[0] == multiplicated_matrix.shape[1]:
                multiplicated_matrix = multiplicated_matrix @ list_of_matrices[matrix_number]
            else:
                flag2 = False
                break
    result = [multiplicated_matrix, flag2]
    return result


# Checking of matrices multiplication possibility
def multiplication_check(list_of_matrices):
    return multiplication_list_of_matrices(list_of_matrices)[1]


# Matrices polymultiplication
def multiply_matrices(list_of_matrices):
    return multiplication_list_of_matrices(list_of_matrices)[0]



# Unfunny joke about movie with Keanu Reeves



# Computation of distance on the plane
def compute_2d_distance(coords1, coords2):
    diff = coords1 - coords2
    dist = np.sqrt(np.sum(diff**2))
    return dist

# Computation of distance in k-D space
def compute_multidimensional_distance(coords1, coords2):
    diff = coords1 - coords2
    dist = np.sqrt(np.sum(diff**2))
    return dist

# Computation of distance between matrices
def compute_pair_distances(d2_matrix):
    for i in range(np.shape(d2_matrix)[0]):
        diff = np.array(d2_matrix[i] - d2_matrix)
        dist = np.sqrt(np.sum(diff**2, axis=1))
        if i == 0:
            result = np.copy(dist)
        else:
            result = np.vstack([result, dist])
    return result

