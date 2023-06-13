"""
Scrieți un program care utilizează o buclă while pentru a genera secvența Fibonacci până la un număr dat de termeni.
Secvența Fibonacci este o serie de numere în care fiecare număr este suma celor două numere precedente.
Secvența începe cu 0 și 1.
"""

nr_termeni = int(input("Urmeaza sa se scrie o secventa Fibonacci.\nIntroduceti numarul dorit de termeni (> 2): "))

nr1, nr2 = 0, 1
contor = 0
if nr_termeni < 2:
    print("Introdu un numar mai mare decat 2: ")
print("Secventa Fibonacci:")
while contor < nr_termeni:
    print(nr1)
    numar_nou = nr1 + nr2
    nr1 = nr2
    nr2 = numar_nou
    contor += 1