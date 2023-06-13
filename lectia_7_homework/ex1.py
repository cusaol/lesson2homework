"""
Cu while toate exercitiile, dar fara break.
Scrieți un program care utilizează o buclă while pentru a calcula factorialul unui număr întreg pozitiv dat n.
Factorialul unui număr este produsul tuturor numerelor întregi pozitive de la 1 la n.
"""

n = int(input("Scrie un numar intreg pozitiv: "))

factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print(f"Factorialul lui {n} este {factorial}.")