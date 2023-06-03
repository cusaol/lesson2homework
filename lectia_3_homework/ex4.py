"""Scrieţi un program care citeşte de la tastatură de 3 ori timpul în care un sportiv aleargă proba de 100 metri (numărul de secunde).
Apoi afişaţi la ecran timpul mediu (media aritmetică a celor 3 încercări) în secunde."""

timp1 = int(input("Introduceți numarul de secunde pentru prima proba de 100 metri: "))
timp2 = int(input("Introduceți numarul de secunde pentru a IIa proba de 100 metri: "))
timp3 = int(input("Introduceți numarul de secunde pentru a IIIa proba de 100 metri: "))
media = round((timp1 + timp2 + timp3) / 3, 2)
print (f"Timpul mediu de alergare, in secunde, este de {media} secunde.")