import numpy as np
import csv
import math
from decimal import Decimal

class BadSizeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def printMatrix(M):
    for rows in M:
        print(rows)

def readFile(file):
    Matrix = []
    try:
        with open(file,'r',newline='') as stream:
            reader = csv.reader(stream)
            for row in reader:
                Matrix.append([Decimal(x) for x in row[0].split(";")])
        return np.array(Matrix)
    except FileNotFoundError:
        print("Can not read: " + file)
    except BadSizeException as e:
        print(str(e))
    return None

def saveToFile(C,path):
    with open(path,mode='w',newline='') as file:
        writer = csv.writer(file,delimiter=';')
        for row in C:
            writer.writerow(row)
    print("Macierz zapisana do pliku " + path)

def brutalAlgorithm(A, B):
    
    rowA, colA = A.shape
    rowB, colB = B.shape
    C = []
    for i in range(rowA):
        row = []
        for j in range(colB):
            row.append(0)
        C.append(row)

    for i in range(rowA):
        for j in range(colB):
            for k in range(rowB):
                C[i][j] += A[i][k] * B[k][j]
    return np.array(C)