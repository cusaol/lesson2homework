"""
Validare Adresă de Email
Scrieți o funcție Python numită is_valid_email care validează formatul unei adrese de email date. Funcția ar trebui
să primească un singur argument: email (șir de caractere) care reprezintă adresa de email de validat. Funcția ar trebui
să returneze o valoare booleană care indică dacă adresa de email este validă.
Criteriile de validare ale adresei de email sunt următoarele:
Conține un singur simbol "@".
Conține cel puțin un punct (.) după simbolul "@".
Domeniul (după ultimul punct) are cel puțin două caractere.

Scrieți un program care utilizează funcția is_valid_email pentru a face următoarele:
Solicitați utilizatorului să introducă o adresă de email.
Apelați funcția is_valid_email cu valoarea introdusă.
Afișați dacă adresa de email este validă sau nu.

Exemplu de rezultat:
Introduceți o adresă de email: john@example.com
Adresă de email validă: True

Introduceți o adresă de email: johndoe@example
Adresă de email validă: False
"""
import string

def is_valid_email(email: str):
    for a in email:
        if a.count("@") == 1:
            return True
    else:
        return False

adresa = input("Introduceți o adresă de email: ")
rezultat = is_valid_email(adresa)
print("Adresă de email validă:", rezultat)