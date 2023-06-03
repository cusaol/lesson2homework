"""Declaraţi o variabilă price, de tip int, care va reţine preţul unui produs citit de la tastatură.

* Calculaţi cât va reprezenta 30% din preţul iniţial şi salvaţi valoarea în variabila reducere
*	Scădeţi din preţul iniţial valoarea reducerii, calculate la pasul precedent. Salvaţi valoarea în variabila preţ_final
* Creaţi o variabilă nouă pret_100_lei, şi salvaţi în această variabilă cât va fi preţul iniţial minus 100 lei
* Afişaţi la final ambele preturi.

"""

price = int(input("Introduceți pretul produsului: "))
reducere = price * 30 / 100
pret_final = price - reducere
pret_100_lei = price - 100
print (f"Pentru pretul produslui de {price} lei, reducerea de 30% va fi de {reducere} lei, cu pretul final de"
       f" {pret_final} lei, iar cu reducerea de 100 lei, pretul final va fi de {pret_100_lei} lei.")