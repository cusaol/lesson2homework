# Scrie un program care preia numărul de minute ca intrare și îl convertește în ore și minute.
# Afișează orele și minutele convertite.

minute_init = input("Introduceti minutele: ")
ore = int(minute_init)//60
minute = int(minute_init) - ore * 60
print(f"Ore = {ore}; minute = {minute}")