"""
Scrie un program care primește o listă de șiruri de caractere ca intrare. Programul ar trebui să afișeze
fiecare șir de caractere pe o linie separată. Cu toate acestea, dacă un șir de caractere începe cu litera
'A', programul ar trebui să sara peste acel șir și să treacă la următorul folosind instrucțiunea continue.
"""

import string

caractere = input("Siruri de caractere separate prin virgula: ")
list_sir = caractere.split(",")

for el in list_sir:
    if el[0] == 'A':
        continue
    print(el)