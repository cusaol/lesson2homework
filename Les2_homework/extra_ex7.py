# Scrie un program care preia suma principală, rata dobânzii și timpul (în ani) ca intrare.
# Calculează și afișează dobânda simplă folosind formula: dobândă = (suma principală * rată dobândă * timp) / 100.

suma = input("Introduceti suma principala: ")
rata = input("Introduceti rata dobanzii: ")
timp = input("Introduceti timpul in ani: ")
dobanda = (int(suma) * int(rata) * int(timp)) / 100
print(f"Dobanda simpla = {dobanda}")