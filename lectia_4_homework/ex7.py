"""
Scrieți un program pentru a citi temperatura de la utilizator și pentru a afișa un mesaj adecvat în funcție de starea temperaturii de mai jos.
Temp -40-(-10) atunci 'Vremea extrem de rece'
Temp -10-0 atunci 'Vremea foarte rece'
Temp 0-10 atunci 'Vreme rece'
Temp 10-20 atunci 'Vreme normala'
Temp 20-30 atunci 'Vreme calda'
Temp 30-40 atunci 'Este foarte cald'
Temp >=40 atunci 'Este extrem de cald'
"""

temp = float(input("Introduceti temperatura: "))
if temp >= -40 and temp < -10:
    print(f"Vremea extrem de rece.")
elif temp >= -10 and temp < 0:
    print(f"Vremea foarte rece.")
elif temp >= 0 and temp < 10:
    print(f"Vreme rece.")
elif temp >= 10 and temp < 20:
    print(f"Vreme normala.")
elif temp >= 20 and temp < 30:
    print(f"Vreme calda.")
elif temp >= 30 and temp < 40:
    print(f"Este foarte cald.")
elif  temp >= 40:
    print(f"Este extrem de cald.")