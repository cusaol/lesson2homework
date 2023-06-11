"""
Scrieți un program care solicită utilizatorului să introducă trei numere și afișează cel mai mare număr dintre ele.
"""

nr1 = float(input("Introduceti numarul 1: "))
nr2 = float(input("Introduceti numarul 2: "))
nr3 = float(input("Introduceti numarul 3: "))

if nr1 == nr2 == nr3:
    print(f"Numere egale.")
else:
    if (nr1 >= nr2) and (nr1 >= nr3):
        maimare = nr1
    elif (nr2 >= nr1) and (nr2 >= nr3):
        maimare = nr2
    else:
        maimare = nr3
    print(f"Mai mare este {maimare}.")