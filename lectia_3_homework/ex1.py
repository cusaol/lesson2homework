"""1.	Creați 2 variabile x şi y, a căror valoare este citită de la tastatură.

Folosiți funcţia int() pentru a transforma valorile citite în numere întregi.

* Definiţi după aceasta variabila suma care va fi egală cu suma lui x şi y.
* Definiţi variabila **diff** care va fi egală cu x - y (diferenţa lui x şi y).
* Definiţi variabila **rest_impart** care va fi egală cu restul împărţirii lui x la y.
* Definiţi variabila **mult** care va fi egală cu x înmulţit cu y.
* Definiţi variabila **power3** care va fi egală cu x la puterea 3.

Afișați toate rezultatele

"""

x = int(input("Introduceți x: "))
y = int(input("Introduceți y: "))
suma = x + y
diff = x - y
rest_impart = x % y
mult = x * y
power3 = x**3
print (f"Pentru numerele {x} si {y} suma este {suma}, diferenta este {diff}, restul impartirii este {rest_impart}, "
       f"produsul este {mult}, iar x la puterea a 3-a va fi egal cu {power3}.")