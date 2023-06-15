"""
Scrieți un program care generează un număr aleatoriu între 1 și 100 și permite utilizatorului
să ghicească numărul. Programul ar trebui să furnizeze feedback ("mai mare" sau "mai mic")
până când utilizatorul ghicește numărul corect. Programul ar trebui, de asemenea, să țină
evidența numărului de încercări necesare pentru ca utilizatorul să ghicească corect.
"""

import random

x = random.randint(1, 101)
nr_incercari = 10
print("Urmeaza sa ghicesti un numar de la 1 la 100.\nAi 10 incercari.")

contor = 0
cast                                                                      = True
while contor < nr_incercari and cast:
    contor += 1
    incercare = int(input(f"Incercarea {contor: }: "))
    if x == incercare:
        print("Felicitari! Ai castigat!")
        cast = False
    elif x > incercare:
        print("mai mare")
    elif x < incercare:
        print("mai mic")

if contor >= nr_incercari:
    print("Mai incearca.")