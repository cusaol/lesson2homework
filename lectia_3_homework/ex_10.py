"""
Înlocuiți un subșir de caractere
Scrieți un program care primește o propoziție, un subșir de caractere țintă
și un subșir de caractere de înlocuire ca intrare (din consola)
și înlocuiește toate aparițiile subșirului de caractere țintă cu subșirul de caractere de înlocuire.
"""

propozitie = input("Introduceți propozitia initiala: ")
sir_de_inlocuit = input("Introduceți sirul ce urmeaza inlocuit: ")
sir_inlocuire = input("Introduceți sirul de inlocuire: ")
propozitie_new = propozitie.replace(sir_de_inlocuit, sir_inlocuire)
print(f"Propozitia noua este: {propozitie_new}.")