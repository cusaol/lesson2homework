"""
Creați un program cu următoarele operații:
* Adăugați un nou element (rezultat) în dataframe (valorile introduse de la consolă)
* Eliminați rezultatele din dataframe (după index)
* Salvați o listă cu toți studenții calificați, într-un fișier Excel separat numit qualified_students.xlsx.
* Doar coloanele name și score trebuie să fie vizibile acolo.
"""
import pandas as pd

df = pd.read_excel('lectia_25.xlsx')

# coloana rezultat
list_of_rez = []

for index, name in enumerate(df['name']):
    rez = int(input(f'Introdu rezultatul elevului {index}: '))
    list_of_rez.append(rez)
df['rezultat'] = list_of_rez

# sterge rand
delete_row = int(input('Introdu index de sters: '))

df1 = df.drop(delete_row)

# lista calificari
calificat = df[df['qualify'] == 'yes']
qual = calificat.drop(['attempts', 'qualify', 'rezultat'], axis=1)
qual.to_excel('qualified_students.xlsx')

