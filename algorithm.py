import numpy as np
import csv
import math

class BadSizeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def ifpow3(number):
    if number <= 0:
        return False
    log = math.log(number,3)
    return log.is_integer()

def printMatrix(M):
    for rows in M:
        print(rows)

def readFile(file):
    Matrix = []
    try:
        with open(file,'r',newline='') as stream:
            reader = csv.reader(stream)
            for row in reader:
                Matrix.append([int(x) for x in row[0].split(";")])
        height = len(Matrix)
        
        if ifpow3(height) == False:
            raise BadSizeException("Rozmiar nie jest potęga liczby 3")
        for row in Matrix:
            if len(row) != height:
                raise BadSizeException("Macierz nie jest kwadratowa")
        return Matrix
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
    def calculate(A,B,i,j):
        sum = 0
        for r in range(len(A[0])):
            sum += A[i][r] * B[r][j]
        return sum

    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(calculate(A,B,i,j))
        C.append(row)
    return C