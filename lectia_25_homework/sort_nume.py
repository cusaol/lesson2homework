"""
Creați un program care să ne permită să vedem rândurile sortate după nume.

"""
import pandas as pd

df = pd.read_excel('lectia_25.xlsx')

nume_sorted = df.sort_values(by=['name'])
print(nume_sorted)
