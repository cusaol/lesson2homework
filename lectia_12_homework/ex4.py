"""
Verificator de Număr Prim
Scrieți o funcție Python numită is_prime care verifică dacă un număr dat este prim sau nu. Funcția ar trebui să
primească un singur argument: number (integer) care reprezintă numărul de verificat. Funcția ar trebui să returneze
o valoare booleană care indică dacă numărul este prim.
Sugestie: Un număr prim este un număr mai mare decât 1 și care nu are divizori în afară de 1 și el însuși.

Scrieți un program care utilizează funcția is_prime pentru a face următoarele:
Solicitați utilizatorului să introducă un număr.
Apelați funcția is_prime cu valoarea introdusă.
Afișați dacă numărul este prim sau nu.

Exemplu de rezultat:
Introduceți un număr: 17
Număr prim: True

Introduceți un număr: 8
Număr prim: False
"""
def is_prime(number: int):
    i = 2
    flag = 0
    while i < n:
        if n % i == 0:
            flag = 1
        i += 1
    if flag == 0:
        return True
    else:
        return False


n = int(input("Introduceti un numar: "))
rezultat = is_prime(n)
print("Număr prim:", rezultat)