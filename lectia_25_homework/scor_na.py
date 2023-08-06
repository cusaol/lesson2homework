"""
Creați un program care să ne permită să vedem rândurile în care scorul lipsește, adică este NaN (nedefinit).
"""
import pandas as pd

df = pd.read_excel('lectia_25.xlsx')

score_NaN = df[df['score'].isna()]
print(score_NaN)
