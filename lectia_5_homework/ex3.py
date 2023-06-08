"""
Creaţi lista `date_personale`.

Citiţi după aceasta de la tastatură **numele**, **prenumele**, **vârsta**, **înălţimea** şi **ocupaţia** utilizatorului
şi adăugaţi aceste valori în lista creată.
"""

date_personale = list()
nume = input("Introduceti numele utilizatorului: ")
prenume = input("Introduceti prenumele utilizatorului: ")
varsta = input("Introduceti varsta utilizatorului: ")
inaltime = input("Introduceti inaltimea utilizatorului: ")
ocupatie = input("Introduceti ocupatia utilizatorului: ")
new_list = [nume, prenume, varsta, inaltime, ocupatie]
date_personale = date_personale.extend(new_list)
print(f"Lista obtinuta: {date_personale}")