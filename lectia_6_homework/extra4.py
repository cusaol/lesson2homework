"""
Scrieți un program care solicită utilizatorului să introducă un număr și afișează toate numerele pare
de la 1 la acel număr.
"""

numar = int(input('Introduceti un numar: '))
for x in range(numar + 1):
    if x == 0: # deoarece se cere de la 1
        continue
    elif x % 2 == 0:
        print(x)