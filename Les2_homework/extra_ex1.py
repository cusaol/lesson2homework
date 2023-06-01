# Scrie un program care atribuie valori celor două variabile, a și b, și apoi schimbă valorile lor.
# Afișează valorile lui a și b înainte și după schimbare.

a = input("Introduceti a: ")
b = input("Introduceti b: ")
print("a = " + a + "; b =  " + b)

temp = a
a = b
b = temp
print("a = " + a + "; b =  " + b)