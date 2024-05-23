import numpy as np
import csv
import math



def makeSubmatrix(matrix):
    row, col = matrix.shape
    row3, col3 = row // 3, col // 3
    return matrix[:row3, :col3], matrix[:row3, col3:2*col3], matrix[:row3, 2*col3:], matrix[row3:2*row3, :col3], matrix[row3:2*row3, col3:2*col3], matrix[row3:2*row3, 2*col3:], matrix[2*row3:, :col3], matrix[2*row3:, col3:2*col3], matrix[2*row3:, 2*col3:]

def strassen(A,B):
    if len(A) == 1:
        return A * B
    
    A11, A12, A13, A21, A22, A23, A31, A32, A33 = makeSubmatrix(A)
    B11, B12, B13, B21, B22, B23, B31, B32, B33 = makeSubmatrix(B)

    M1 = strassen(A11 + A12 + A13 - A21 - A22 - A32 - A33, B22)
    M2 = strassen(A11 - A21, -B12 + B22)
    M3 = strassen(A22, -B11 + B12 + B21 - B22 - B23 - B31 + B33)
    M4 = strassen(-A11 + A21 + A22, B11 - B12 + B22)
    M5 = strassen(A21 + A22, -B11 + B12)
    M6 = strassen(A11, B11)
    M7 = strassen(-A11 + A31 + A32, B11 - B13 + B23)
    M8 = strassen(-A11 + A31, B13 - B23)
    M9 = strassen(A31 + A32, -B11 + B13)
    M10 = strassen(A11 + A12 + A13 - A22 - A23 - A31 - A32, B23)
    M11= strassen(A32, -B11 + B13 + B21 - B22 - B23 - B31 + B32)
    M12 = strassen(-A13 + A32 + A33, B22 + B31 - B32)
    M13 = strassen(A13 - A33, B22 - B32)
    M14 = strassen(A13, B31)
    M15 = strassen(A32 + A33, -B31 + B32)
    M16 = strassen(-A13 + A22 + A23, B23 + B31 - B33)
    M17 = strassen(A13 - A23, B23 - B33)
    M18 = strassen(A22 + A23, -B31 + B33)
    M19 = strassen(A12, B21)
    M20 = strassen(A23, B32)
    M21 = strassen(A21, B13)
    M22 = strassen(A31, B12)
    M23 = strassen(A33, B33)

    C11 = M6 + M14 + M19
    C12 = M1 + M4 + M5 + M6 + M12 + M14 + M15
    C13 = M6 + M7 + M9 + M10 + M14 + M16 + M18
    C21 = M2 + M3 + M4 + M6 + M14 + M16 + M17
    C22 = M2 + M4 + M5 + M6 + M20
    C23 = M14 + M16 + M17 + M18 + M21
    C31 = M6 + M7 + M8 + M11 + M12 + M13 + M14
    C32 = M12 + M13 + M14 + M15 + M22
    C33 = M6 + M7 + M8 + M9 + M23

    C = np.vstack((np.hstack((C11, C12, C13)), np.hstack((C21, C22, C23)),np.hstack((C31, C32, C33))))
    return C 


