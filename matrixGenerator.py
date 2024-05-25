import numpy as np
import sys
import csv
from algorithm import *
from strassen_algorithm import *


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Proszę podać parametry w kolejnosci rowA colA row B colB plik1.csv plik2.csv")
        sys.exit(1)

    A = np.random.randint(-50, 50, size = (int(sys.argv[1]), int(sys.argv[2])))
    
    B = np.random.randint(-50, 50, size = (int(sys.argv[3]), int(sys.argv[4])))
    
    saveToFile(A, sys.argv[5])
    saveToFile(B, sys.argv[6])
    print("Pliki wygenerowane")