# Scrie un program care preia numărul de secunde ca intrare și îl convertește în ore, minute și secunde.
# Afișează timpul convertit.

secunde_init = input("Introduceti secundele: ")
ore = int(secunde_init)//3600
minute = (int(secunde_init) - ore * 3600)//60
secunde = int(secunde_init) - ore * 3600 - minute * 60
print(f"Ore = {ore}; minute = {minute}; secunde = {secunde}")