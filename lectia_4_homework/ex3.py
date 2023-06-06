"""
Citiţi de la tastatură un număr întreg.
Dacă numărul este negativ, afişaţi mesajul `"That number is less than 0!"`.
Dacă este pozitiv, afişaţi `"That number is greater than 0!"`.
Dacă nu este nici negativ nici pozitiv afişaţi mesajul `"You picked 0!"`.
"""

numar = int(input("Introduceti un numar intreg: "))
if numar < 0:
    print(f"That number is less than 0!")
elif numar > 0:
    print(f"That number is greater than 0!")
else:
    print(f"You picked 0!")