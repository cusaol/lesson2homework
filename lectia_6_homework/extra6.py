"""
Scrieți un program care solicită utilizatorului să introducă o propoziție și numără numărul de vocale
din acea propoziție.
"""

propozitie = input("Introduceti propozitia: ")

vocala = 0

for x in propozitie:
    if x in "aeiou":
        vocala += 1
print(f"Propozitia contine {vocala} vocale.")