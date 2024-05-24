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
        sys.exit(1)
    
    csv_files = sys.argv[1:]
    path = csv_files[2]

    # Odczytanie Macierzy:
    A = readFile(csv_files[0])
    B = readFile(csv_files[1])
    
    if validateMatrix(A, B) == False:
        print("Liczba kolumn macierzy A jest inna niż liczba wierszy macierzy B")
        sys.exit(1)
    
    C = multiplyMatrixStrassen(A, B)
    
    saveToFile(C,path)
    
