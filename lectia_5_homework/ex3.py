"""
Creaţi lista `date_personale`.

Citiţi după aceasta de la tastatură **numele**, **prenumele**, **vârsta**, **înălţimea** şi **ocupaţia** utilizatorului
şi adăugaţi aceste valori în lista creată.
"""

date_personale = []
nume = input("Introduceti numele utilizatorului: ")
prenume = input("Introduceti prenumele utilizatorului: ")
varsta = int(input("Introduceti varsta utilizatorului: "))
inaltime = int(input("Introduceti inaltimea utilizatorului: "))
ocupatie = input("Introduceti ocupatia utilizatorului: ")
date_personale = [nume, prenume, varsta, inaltime, ocupatie]
print(f"Datele personale: {date_personale}")