"""
Creează o funcție care primește o șir de caractere ca intrare și verifică dacă este un palindrom.
Gestionează eroarea de tip ValueError dacă se furnizează un șir de caractere gol.

Task:
Definește o funcție care acceptă un singur parametru.
Verifică dacă șirul de caractere de intrare este gol folosind o instrucțiune if.
Dacă șirul este gol, generează o eroare de tip ValueError cu un mesaj de eroare adecvat.
Dacă șirul nu este gol, compară-l cu oglinditul său și returnează True dacă sunt egale (un palindrom) sau False în
caz contrar.
"""

import string

def check_palindrome(string_):
    if not string_:
        raise ValueError('String can not be empty for palindrom check')
    return string_ == string_[::-1]


print(check_palindrome('radar'))
print(check_palindrome('sanda'))
try:
    print(check_palindrome(''))
except ValueError as ex:
    print(ex)