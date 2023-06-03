"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere

Note: Indiferent daca e majuscula sau minusucula litera

"""

sir = input("Introduceți sirul de caractere: ")
litere = len(sir)
vocale = 0
consoane = 0
for i in sir:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vocale=vocale+1;
    else:
        consoane=consoane+1;
print (f"Sirul de caractere {sir} are lungimea {litere}, compus din {vocale} vocale si {consoane} consoane.")