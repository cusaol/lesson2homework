"""
De la consola se va introduce o bucata de text.
Calculati de cate ori fiecare cuvant a fost folosit.
Afisati informatia.
"""

import string
text = input('Introdu o bucata de text: ')
for punct in list(string.punctuation) + list(string.digits):
    text.replace(punct, '')

text = text.lower()

toate_cuvintele = text.split()

cuvinte_count = dict()

for cuvant in toate_cuvintele:
    if cuvant in cuvinte_count:
        cuvinte_count[cuvant] += 1
    else:
        cuvinte_count[cuvant] = 1

for cuvant, count in cuvinte_count.items():
    print(f"Cuvantul '{cuvant}' a fost gasit de {count} ori.")