"""
Scrieți un program care primește două șiruri de caractere ca intrare și verifică dacă acestea sunt anagrame
(adică un cuvânt poate fi format prin rearanjarea literelor altui cuvânt).
"""

sir1 = input("Introduceti sirul de caractere I: ")
sir2 = input("Introduceti sirul de caractere II: ")

sir1 = sir1.replace(" ", "").lower()
sir2 = sir2.replace(" ", "").lower()

if(len(sir1) == len(sir2)):
    sortsir1 = sorted(sir1)
    sortsir2 = sorted(sir2)
    if(sortsir1 == sortsir2):
        print(f"Sirurile sunt anagrame.")
    else:
        print(f"Sirurile nu sunt anagrame.")
else:
    print(f"Sirurile nu sunt anagrame.")