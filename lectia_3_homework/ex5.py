"""
Verificarea unui palindrom
Scrieți un program care primește un șir de caractere ca intrare
și verifică dacă acesta este un palindrom (se citește la fel în ambele sensuri).
"""

sir = input("Introduceți sirul de caractere: ")
sirinvers = sir[::-1]
if sir == sirinvers:
	print("Sirul este palindrom.")
else:
	print("Sirul nu este palindrom.")
