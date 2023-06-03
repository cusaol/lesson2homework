"""Eliminați spațiile
Scrieți un program care primește o propoziție ca intrare și elimină toate caracterele de spațiu din ea."""

sir = input("Introduceți sirul de caractere: ")
sir_fara_spatii = sir.replace(" ", "")
print(f"Sirul de caractere fara spatii este: {sir_fara_spatii}.")