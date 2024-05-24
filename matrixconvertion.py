import numpy as np
import csv
import math

def new_size(n):
        if math.log(n, 3).is_integer():
             return n
        power = 1
        while power < n:
            power *= 3
        return power

def padMatrix(matrix, size):
    padded_matrix = np.zeros((size, size))
    original_size = matrix.shape
    padded_matrix[:original_size[0], :original_size[1]] = matrix
    return padded_matrix

def matrixConvertion(A,B):
    rowA,colA = A.shape
    rowB,colB = B.shape
    max_dim = max(rowA, colA, rowB, colB)
    n_size = new_size(max_dim)
    A_padded = padMatrix(A, n_size)
    B_padded = padMatrix(B, n_size)

    return A_padded, B_padded

def validateMatrix(A,B):
    rowA, colA = A.shape
    rowB, colB = B.shape
    return colA == rowB
    
