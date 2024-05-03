# STRASSEN 3

## Wywołanie programu
program przyjmuje na wejściu 3 argumenty (ścieżki do plików .csv):
1. A - macierz nr 1
2. B - macierz nr 2
3. C - ścieżka do zapisu wyniku mnożenia macierzy C = A*B

## Informacje
Zaimplementowane zostały funkcje do czytania oraz zapisu macierzy do pliku csv. Program sprawdza czy podane na wejściu macierze są macierzami kwadratowymi oraz czy ich rozmiar jest potęgą liczby 3. Zaimplementowany został również algorytm naiwny do obliczania iloczynu macierzy.

## Przykładowe wywołanie
```console
$ python strassen.py A.csv B.csv wynik.csv
```
Powyższy przykład zaczyta macierze A oraz B z folderu roboczego, a następnie wynik zapisze do pliku wynik.csv