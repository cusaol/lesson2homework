"""
Scrie un program care cere utilizatorului să introducă două numere și calculează împărțirea lor.
Gestionează eroarea de tip ZeroDivisionError dacă al doilea număr este zero.

Task:
Cere utilizatorului să introducă primul număr și stochează-l într-o variabilă.
Cere utilizatorului să introducă al doilea număr și stochează-l într-o altă variabilă.
Convertiți ambele intrări în numere cu zecimale folosind funcția float().
Împarte primul număr la al doilea număr și stochează rezultatul într-o variabilă.
Folosește un bloc try-except pentru a gestiona eroarea ZeroDivisionError și afișează un mesaj de eroare adecvat dacă
al doilea număr este zero.
Dacă împărțirea este reușită, afișează rezultatul.
"""

numarul_unu = float(input('Tipăreste primul numar: '))
numarul_doi = float(input('Tipăreste al doilea numar: '))
impart = numarul_unu/numarul_doi
try:
    impart = numarul_unu / numarul_doi
    print("Catul este", impart)
except ZeroDivisionError as eroare:
    print('Impartirea la zero nu e posibila')