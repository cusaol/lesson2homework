'''
Creati un program python cu ajutorul careia vor fi gasite toate elementele dintr-o lista de string-uri care sunt palindroame.
Avand lista ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa'] rezultatul va fi ['php', 'aaa'].

Note: Puteti folosi functia filter pentru a filtra elementele unei colectii.
'''

lista_elemente = ['Python', 'abba', 'online', 'radar', 'Ion']

def epalindrom(valoare):
    return valoare == valoare[::-1]

b = list(filter(lambda el: el == el[::-1], lista_elemente))
print(b)