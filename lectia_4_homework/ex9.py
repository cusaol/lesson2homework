"""
Scrieți un program care cere utilizatorului să introducă o parolă.
Dacă parola conține cel puțin 8 caractere și include atât litere mari,
cât și litere mici, afișați mesajul „Parolă puternică”.
În caz contrar, afișați mesajul „Parolă slabă”.
"""

parola = input("Introduceti o parola: ")
contor = 0
for x in parola:
    for y in parola:
        if len(parola) >= 8 and x.isupper() and y.islower():
            contor += 1
        else:
            contor += 0
if contor > 0:
    print(f"Parola puternica.")
else:
    print(f"Parola slaba.")