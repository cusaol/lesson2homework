"""
De la consola se va introduce o bucata de text.
Calculati de cate ori fiecare cuvant a fost folosit.
Afisati informatia.
"""

import string
text = input('Introdu o bucata de text: ')
for punct in list(string.punctuation) + list(string.digits):
    text = text.replace(punct, '')

toate_cuvintele = text.split(" ")

dictionar_cuvinte = dict()
print(dictionar_cuvinte)