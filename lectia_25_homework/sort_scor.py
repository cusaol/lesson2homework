"""
Creați un program care să ne permită să vedem rândurile sortate după scor.

"""
import pandas as pd

df = pd.read_excel('lectia_25.xlsx')

scor_sorted = df.sort_values(by=['score'])
print(scor_sorted)