import re

# V2
orainit = input('Ora in format HH:MM PM/AM: ')
lista_ora = re.split(r': ', orainit)
print(lista_ora)
# ora, minute, perioada = lista_ora[0], lista_ora[1], lista_ora[2]