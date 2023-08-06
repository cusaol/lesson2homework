"""
Creați un program care să ne permită să vedem rândurile în care scorul este între a și b,
unde a și b sunt valori introduse de la consolă.
"""
import pandas as pd

df = pd.read_excel('lectia_25.xlsx')

a = int(input('Introduce a: '))
b = int(input('Introduce b: '))
score_ab = df[df['score'].between(a, b)]
print(score_ab)