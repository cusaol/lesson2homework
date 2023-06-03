"""
Eliminați semnele de punctuație
Scrieți un program care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea.
"""

sir = input("Introduceți sirul de caractere: ")
sir_fara_semne = sir.replace(".", "")
sir_fara_semne = sir_fara_semne.replace(",", "").replace("!", "").replace("?", "").replace(":", "")
sir_fara_semne = sir_fara_semne.replace(";", "").replace("@", "").replace("#", "").replace("%", "")
print(f"Sirul de caractere fara spatii este: {sir_fara_semne}.")