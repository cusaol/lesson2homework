"""
Scrieţi un program care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""

# case sensitive
propozitie = input("Introduceti propozitia: ")
if len(propozitie) < 2:
    print(f"Acesta este un caracter!")
else:
    print(f"'a' este a doua litera a propozitiei: {'a' == propozitie[1]}")

# != case sensitive
# propozitieinit = input("Introduceti propozitia: ")
# propozitie = propozitieinit.lower()
# if len(propozitie) < 2:
#     print(f"Acesta este un caracter!")
# else:
#     print(f"'a' este a doua litera a propozitiei: {'a' == propozitie[1]}")
