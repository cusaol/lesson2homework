"""
Scrie un program care generează numere aleatorii între 1 și 10 folosind bucla while.
Programul ar trebui să continue generarea de numere până când generează un număr mai mare decât 8.
Odată ce numărul este mai mare decât 8, programul ar trebui să încheie bucla folosind instrucțiunea break.
"""

import random

x = 0
contor = 1
while contor:
    x = random.randint(1, 10)
    print(x)
    if x > 8:
        break
    contor += 1