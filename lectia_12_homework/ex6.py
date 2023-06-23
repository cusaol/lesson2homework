"""
Verificator de Palindrom
Scrieți o funcție Python numită is_palindrome care verifică dacă un șir de caractere dat este un palindrom. Funcția ar
trebui să primească un singur argument: text (șir de caractere) care reprezintă textul de verificat. Funcția ar trebui
să returneze o valoare booleană care indică dacă textul este un palindrom.
Sugestie: Un palindrom este un cuvânt, o frază, un număr sau o altă secvență de caractere care se citește la fel
înainte și înapoi, fără a ține cont de spații, semne de punctuație și capitalizare.

Scrieți un program care utilizează funcția is_palindrome pentru a face următoarele:
Solicitați utilizatorului să introducă un text.
Apelați funcția is_palindrome cu valoarea introdusă.
Afișați dacă textul este un palindrom sau nu.

Exemplu de rezultat:
Introduceți un text: radar
Palindrom: True

Introduceți un text: Hello
Palindrom: False
Notă: Verificatorul de palindrom poate fi personalizat pentru a ignora sau considera spații, semne de punctuație sau
capitalizare în funcție de preferințele dvs.
"""
import string

def is_palindrome(text: str):
    sir_invers = text[::-1]
    if text == sir_invers:
        return True
    else:
        return False

sir = input('Introduceti un text: ').lower().replace(' ', '')
for punct in list(string.punctuation) + list(string.digits):
    sir = sir.replace(punct, '')
rezultat = is_palindrome(sir)
print("Palindrom:", rezultat)