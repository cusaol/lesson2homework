"""
Scrieți un program care cere utilizatorului să introducă o parolă.
Dacă parola conține cel puțin 8 caractere și include atât litere mari,
cât și litere mici, afișați mesajul „Parolă puternică”.
În caz contrar, afișați mesajul „Parolă slabă”.
"""

parola = input("Introduceti o parola: ")
if any(char.isupper() for char in parola) and any(char.islower() for char in parola) and len(parola) >= 8:
    print(f"Parola puternica.")
else:
    print(f"Parola slaba.")