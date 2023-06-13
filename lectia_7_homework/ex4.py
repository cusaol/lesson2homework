"""
Scrieți un program care utilizează o buclă while pentru a verifica dacă un număr întreg pozitiv dat n este
un număr prim. Un număr prim este un număr întreg pozitiv mai mare decât 1 care nu are divizori pozitivi
în afară de 1 și el însuși. Programul ar trebui să afișeze dacă numărul este prim sau nu.
"""

n = int(input("Introduceti un numar intreg pozitiv: "))

i = 2
flag = 0
while i < n:
    if n % i == 0:
        flag = 1
    i += 1
if flag == 0:
    print(f"{n} este numar prim.")
else:
    print(f"{n} nu este numar prim.")