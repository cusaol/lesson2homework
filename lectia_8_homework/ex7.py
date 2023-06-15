"""
Scrie o listă comprehensivă care generează o listă a primelor litere ale fiecărui cuvânt dintr-un anumit enunț.
De exemplu, dacă enunțul este "Python este minunat", lista comprehensivă ar trebui să producă ['P', 'e', 'm'].
"""
import string

enunt = input("Enuntul: ")
fara_punctuatie = enunt.translate(str.maketrans("", "", string.punctuation))
fara_cifre = fara_punctuatie.translate(str.maketrans("", "", string.digits))
enunt_list = fara_cifre.split(" ")

primul_carcater = [el[0] for el in enunt_list]
print(primul_carcater)