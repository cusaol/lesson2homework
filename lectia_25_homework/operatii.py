"""
Creați un program cu următoarele operații:
* Adăugați un nou element (rezultat) în dataframe (valorile introduse de la consolă)
* Eliminați rezultatele din dataframe (după index)
* Salvați o listă cu toți studenții calificați, într-un fișier Excel separat numit qualified_students.xlsx.
* Doar coloanele name și score trebuie să fie vizibile acolo.
"""
import pandas as pd

df = pd.read_excel('lectia_25.xlsx')