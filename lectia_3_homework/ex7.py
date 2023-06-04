"""
Numărarea caracterelor
Scrieți un program care
 primește un șir de caractere ca intrare
 și numără de câte ori apare un caracter specific (introdus in consola).

 Numarul de caractere trebuie sa fie considerat indiferent daca e majuscula sau minuscula
"""

sir = input("Introduceți sirul de caractere: ")
caracter = input("Introduceți caracterul pe care doresti sa-l numeri: ")
uppersir = sir.upper()
uppercaracter = caracter.upper()
numar = uppersir.count(uppercaracter)
print(f"Sirul de caractere <{sir}> contine de {numar} ori caracterul <{caracter}>.")