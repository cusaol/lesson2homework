"""
Scrieți un program care cere utilizatorului să introducă o propoziție.
Dacă propoziția se încheie cu un semn de întrebare ("?"),
afișați mesajul „Aceasta este o întrebare”.
În caz contrar, afișați mesajul „Aceasta nu este o întrebare”
"""

propozitie = input("Introduceti o propozitie: ")
if propozitie[-1] == "?":
    print(f"Aceasta este o întrebare.")
else:
    print(f"Aceasta nu este o întrebare.")