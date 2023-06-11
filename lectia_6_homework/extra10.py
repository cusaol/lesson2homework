"""
Scrieți un program care solicită utilizatorului să introducă un număr întreg pozitiv și afișează un model de triunghi
utilizând asteriscuri. De exemplu, dacă utilizatorul introduce 5, programul ar trebui să afișeze:
*
**
***
****
*****
"""

numar = int(input("Introduceti un numar intreg pozitiv: "))
asterisc = "*"

for x in range(numar + 1):
    print(asterisc * x)
