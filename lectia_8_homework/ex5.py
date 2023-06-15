"""
Scrie o listă comprehensivă care generează o listă a lungimilor cuvintelor dintr-un anumit enunț.
De exemplu, dacă enunțul este "Salut lume, cum te simți?", lista comprehensivă ar trebui să producă [5, 5, 3, 3, 4].
"""

import string

enunt = input("Un enunt: ")
fara_semne = enunt.translate(str.maketrans("", "", string.punctuation))
list_caractere = fara_semne.split(" ")

lista_lungime = [len(el) for el in list_caractere]
print(lista_lungime)