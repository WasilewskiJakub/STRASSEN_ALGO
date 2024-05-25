import numpy as np
import random
import time

from algorithm import *
from strassen_algorithm import *


def compare_matrices(M1, M2):
    row1, col1 = M1.shape
    row2, col2 = M2.shape
    if row1 != row2 or col1 != col2:
        raise Exception("inne wymiary")
    
    for i in range(row1):
        for j in range(col1):
            if M1[i][j] != M2[i][j]:
                raise Exception("inna wartosc")

if __name__ == "__main__":
    naive = []
    strassen = []
    size = []
    for iter in range(1, 20):

        rowA = random.randint(20, 50)
        colB = random.randint(20, 50)
        A = np.random.randint(-50, 50, size = (rowA, colB))
        B = np.random.randint(-50, 50, size = (colB, rowA))
        

        start_time = time.time()
        C_brutal = brutalAlgorithm(A, B)
        end_time = time.time()
        execution_time = end_time - start_time
        naive.append(execution_time)
        time_native = execution_time
        
        start_time = time.time()
        C_strassen = multiplyMatrixStrassen(A, B)
        end_time = time.time()
        execution_time = end_time - start_time
        strassen.append(execution_time)
        time_strassen = execution_time

        print("${} \\times {}$& {:.6f} s & {:.6f} s\\\\ \\hline".format(rowA, colB, time_native, time_strassen))

        compare_matrices(C_brutal, C_strassen)

