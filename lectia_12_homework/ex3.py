"""
Verificator de Putere a Parolei
Scrieți o funcție Python numită check_password_strength care verifică puterea unei parole date. Funcția ar trebui să
primească un singur argument: password (șir de caractere) care reprezintă parola de verificat. Funcția ar trebui să
returneze o valoare booleană care indică dacă parola respectă criteriile de putere specificate.
Criteriile de putere ale parolei sunt următoarele:
Cel puțin 8 caractere lungime
Conține cel puțin o literă majusculă
Conține cel puțin o literă minusculă
Conține cel puțin o cifră
Conține cel puțin un caracter special (de exemplu, !@#$%^&*)

Scrieți un program care utilizează funcția check_password_strength pentru a face următoarele:
Solicitați utilizatorului să introducă o parolă.
Apelați funcția check_password_strength cu valoarea introdusă.
Afișați dacă parola respectă criteriile de putere sau nu.

Exemplu de rezultat:
Introduceți o parolă: MyPass123
Puterea parolei: True (respectă criteriile)

Introduceți o parolă: abcdefg
Puterea parolei: False (nu respectă criteriile)
Notă: Puteți îmbunătăți verificatorul de putere a parolei prin adăugarea de criterii suplimentare sau personalizarea
cerințelor în funcție de preferințele dvs.
"""
import string

def check_password_strength(password: str):
    for a in password:
        if a in list(string.punctuation) + list(string.digits) and any(char.isupper() for char in password) and \
                any(char.islower() for char in password) and len(password) >= 8:
            return True
    else:
        return False

parola = input("Introduceți o parolă: ")
rezultat = check_password_strength(parola)
comentariu = "(respectă criteriile)"
if rezultat is True:
    comentariu = comentariu
else:
    comentariu = "(nu respectă criteriile)"
print("Puterea parolei:", rezultat, comentariu)