# Scrie un program care preia două numere ca intrare și efectuează următoarele operații:
#
# Adună cele două numere și afișează rezultatul.
# Scade al doilea număr din primul număr și afișează rezultatul.
# Înmulțește cele două numere și afișează rezultatul.
# Împarte primul număr la al doilea număr și afișează rezultatul.

x = input("Introduceti x: ")
y = input("Introduceti y: ")
suma = int(x) + int(y)
print(f"suma = {str(suma)}")
scadere = int(y) - int(x)
print(f"scaderea = {str(scadere)}")
produs = int(x) * int(y)
print(f"produs = {str(produs)}")
impartire = int(x) / int(y)
print(f"impartire = {str(impartire)}")