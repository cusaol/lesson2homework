# Scrie un program care preia raza unui cerc ca intrare și calculează aria acestuia.
# Afișează aria calculată.

PI = 3.14159265359
raza = input("Introduceti raza cercului: ")
aria = PI * pow(int(raza), 2)
print("Aria cercului = " + str(aria))