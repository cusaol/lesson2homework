"""
Scrie un program care primește o listă de numere ca intrare. Programul ar trebui să calculeze produsul tuturor
numerelor din listă. Cu toate acestea, dacă produsul depășește 100, programul ar trebui să oprească calculul și
să afișeze un mesaj care indică că produsul este prea mare. Folosește o buclă for și instrucțiunea break pentru
a încheia bucla când este necesar.
"""

numere = input("Introduceti un sir de numere separate prin virgula: ").split(",")
list_numere = map(int, numere)

produs = 1
for el in list_numere:
    produs *= el
    if produs > 100:
        print("Produsul elementelor > 100!")
        break
else:
    print(f"Produsul elementelor este {produs}")
# if produs <= 100: