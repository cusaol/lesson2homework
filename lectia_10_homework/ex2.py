"""
Creaza un program care va inregistra o lista de oaspeti si comenzile lor la un restaurant.
Utilizatorul va introduce la consola cati oaspeti vor fi inregistrati.
Pentru fiecare oaspete, utilizatorul va introduce Numele Oaspetelui si 2 feluri de mancare.
La sfarsit, programul va trebui sa afiseze lista cu oaspeti, ce au comandat, si cat in total va trebui restaurantul
sa pregateasca. (*Folositi dict)
"""

date = ['Nume', 'Mancare1', 'Mancare2']
nr_oaspeti = int(input('Introdu numarul de oaspeti in restaurant: '))
oaspeti = []
for a in range(nr_oaspeti):
    dictionar = dict()
    for info in date:
        detalii = input(info)
        dictionar[info] = detalii
    oaspeti.append(dictionar)

produse = 0
for client in oaspeti:
    print(f"{client['Nume']} a comandat {client['Mancare1']} si {client['Mancare2']}.")
    produse += 2

print(f"Au fost comandate {produse} feluri de mancare.")