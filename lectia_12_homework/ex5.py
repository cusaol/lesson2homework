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
def is_valid_email(email):
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if "." not in domain:
        return False

    last_dot_index = domain.rindex(".")
    domain_name = domain[last_dot_index + 1:]

    if len(domain_name) < 2:
        return False

    return True


email = input("Enter an email address: ")

valid_email = is_valid_email(email)
print(f"Valid email address: {valid_email}")