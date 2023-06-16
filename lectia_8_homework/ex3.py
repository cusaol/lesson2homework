"""
Scrie un program care primește o listă de numere ca intrare. Programul ar trebui să calculeze produsul
tuturor numerelor din listă. Cu toate acestea, dacă produsul depășește 100, programul ar trebui să oprească
calculul și să afișeze un mesaj care indică că produsul este prea mare. Folosește o buclă while și instrucțiunea
break pentru a încheia bucla când este necesar.
"""

numere = input("Introduceti un sir de numere separate prin virgula: ").split(",")
list_numere = list(map(int, numere))
# list_numere = [int(a) for a in numere]

produs = 1
ind = 0
while ind < len(list_numere):
    produs *= list_numere[ind]
    if produs > 100:
        print("Produsul elementelor > 100!")
        break
    ind += 1
if produs <= 100:
    print(f"Produsul elementelor este {produs}")