"""
Scrie o listă comprehensivă care generează o listă a literelor majuscule dintr-un anumit șir de caractere.
De exemplu, dacă șirul de caractere este "Salut Lume", lista comprehensivă ar trebui să producă ['S', 'L'].
"""

sir = input("Sir de caractere: ")
list_caractere = list(sir)

lista_majuscule = [el for el in list_caractere if "A" <= el <= "Z"]
print(lista_majuscule)