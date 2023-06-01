# Scrie un program care preia o temperatură în grade Celsius ca intrare și o convertește în grade Fahrenheit.
# Formula de conversie este: Fahrenheit = Celsius * 9/5 + 32. Afișează temperatura convertită.

celsius = input("Introduceti temperatura in grade Celsius: ")
fahrenheit = int(celsius)*9/5+32
print("Temperatura in grade Fahrenheit = " + str(fahrenheit))