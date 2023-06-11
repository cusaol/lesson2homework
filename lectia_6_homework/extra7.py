"""
Scrieți un program care primește un număr întreg pozitiv ca intrare și afișează suma tuturor numerelor
de la 1 până la acel număr.
"""

numar = int(input("Introduceti un numar intreg pozitiv: "))

suma = 0

for x in range(numar + 1):
    suma += x
print(f"Suma numerelor este {suma}.")