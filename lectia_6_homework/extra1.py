"""
Scrieți un program care solicită utilizatorului să introducă un șir de caractere și numără numărul de caractere din șir
(excluzând spațiile).
"""

sir = input("Introduceti un sir de caractere: ")
print(f"Sunt {len(sir) - sir.count(' ')} caractere, excluzand spatiile.")