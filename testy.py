import numpy as np
import random
import time

from algorithm import *
from strassen_algorithm import *
import matplotlib.pyplot as plt


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
    for iter in range(2, 12):
        print(iter)
        size.append(3**iter)

        rowA = random.randint(20, 50)
        colB = random.randint(20, 50)
        A = np.random.randint(-50, 50, size = (3**iter, 3**iter))
        B = np.random.randint(-50, 50, size = (3**iter, 3**iter))
        

        start_time = time.time()
        C_brutal = brutalAlgorithm(A, B)
        end_time = time.time()
        execution_time = end_time - start_time
        naive.append(execution_time)
        print("[Brutal] Czas wykonania: {:.6f} sekund".format(execution_time))
        
        start_time = time.time()
        C_strassen = multiplyMatrixStrassen(A, B)
        end_time = time.time()
        execution_time = end_time - start_time
        strassen.append(execution_time)
        print("[Strassen] Czas wykonania: {:.6f} sekund".format(execution_time))

        compare_matrices(C_brutal, C_strassen)
    
    plt.plot(size, strassen)
    plt.plot(size, naive)
    
    plt.title('Strassen wykres czasu od rozmiaru macierzy')
    plt.xlabel('Rozmiar obu macierzy [nxn]')
    plt.ylabel('Czas mnożenia [s]')
    plt.show()

