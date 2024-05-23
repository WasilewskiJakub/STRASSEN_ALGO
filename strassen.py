import numpy as np
import sys
import csv
from algorithm import *
from strassen_algorithm import *



if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Proszę podać 2 ścieżki do plików z macierzami i ścieżkę do pliku do zapisu")
        sys.exit(1)
    if len(sys.argv) > 4:
        print("Podano za dużo argumentów")
    csv_files = sys.argv[1:]
    
    # Odczytanie Macierzy:
    A = readFile(csv_files[0])
    B = readFile(csv_files[1])
    if len(A) != len(B):
        print("Macierze A oraz B są innych rozmiarów")
    path = csv_files[2]
    C = None
    if A != None and B != None:
        C = brutalAlgorithm(A,B)
    if C != None:
        print("Wynik mnożenia: C = ")
        printMatrix(C)
        saveToFile(C, path)


    print(strassen(np.array(A), np.array(B)))
    # print(strassen(np.array(tab)))