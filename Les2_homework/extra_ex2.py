# Scrie un program care preia două numere ca intrare și efectuează următoarele operații:
#
# Adună cele două numere și afișează rezultatul.
# Scade al doilea număr din primul număr și afișează rezultatul.
# Înmulțește cele două numere și afișează rezultatul.
# Împarte primul număr la al doilea număr și afișează rezultatul.

x = input("Introduceti x: ")
y = input("Introduceti y: ")
suma = int(x) + int(y)
print("suma = " + str(suma))
scadere = int(y) - int(x)
print("scaderea = " + str(scadere))
produs = int(x) * int(y)
print("produs = " + str(produs))
impartire = int(x) / int(y)
print("impartire = " + str(impartire))