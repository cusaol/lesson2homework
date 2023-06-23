"""
Conversie de Temperatură
Scrieți o funcție Python numită convert_temperature care convertește valorile temperaturii între Celsius și Fahrenheit.
Funcția ar trebui să primească două argumente: temperature (float) și unit (șir de caractere) care indică unitatea
actuală a temperaturii ("C" pentru Celsius sau "F" pentru Fahrenheit). Funcția ar trebui să returneze valoarea
temperaturii convertite.
Sugestie: Pentru a converti Celsius în Fahrenheit, utilizați formula: F = (C * 9/5) + 32.
Pentru a converti Fahrenheit în Celsius, utilizați formula: C = (F - 32) * 5/9.

Scrieți un program care utilizează funcția convert_temperature pentru a face următoarele:
Solicitați utilizatorului să introducă o valoare a temperaturii.
Solicitați utilizatorului să introducă unitatea actuală a temperaturii ("C" sau "F").
Apelați funcția convert_temperature cu valorile introduse.
Afișați valoarea temperaturii convertite împreună cu unitatea corespunzătoare.

Exemplu de rezultat:
Introduceți temperatura: 25
Introduceți unitatea curentă (C/F): C
Temperatura convertită: 77.0 F

Introduceți temperatura: 98.6
Introduceți unitatea curentă (C/F): F
Temperatura convertită: 37.0 C
"""
def convert_temperature(temperature: float, unit: str):
    if unit == "C":
        return (temperature * 9 / 5) + 32
    elif unit == "F":
        return (temperature - 32) * 5 / 9

temp = float(input('Introduceți temperatura: '))
format = input('Introduceți unitatea curentă (C/F): ').upper()

rezultat = round(convert_temperature(temp, format), 2)
form = "F"
if format == "F":
    form = "C"
elif format == "C":
    form = "F"
print("Temperatura convertita: ", rezultat, form)