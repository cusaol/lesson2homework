"""
 Extrageți un subșir de caractere
Scrieți un program care primește un șir de caractere ca intrare și extrage un subșir specific din acesta,
 bazat pe pozițiile de început și sfârșit definite de utilizator.
"""

sir = input("Introduceți sirul de caractere: ")
primele4 = sir[:4]
ultimele3 = sir[-3:]
print(f"Primele 4 caractere ale sirului sunt <{primele4}>, ultimele 3 caractere sunt <{ultimele3}>.")