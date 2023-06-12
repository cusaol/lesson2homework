"""
Convertor de timp V2
Scrie un program care preia timpul introdus de utilizator în următorul format:
"11:20 PM" sau "02:00 AM".
Și îl convertește în formatul de 24 de ore.
"23:20" sau "02:00"

Combină soluția cu soluția din lecția live
și permite utilizatorului să decidă ce conversie să facă.
De la 24 de ore la 12 ore, sau invers.
"""

alegere = input("Pentru a converti din format 12h in 24h tasteaza 1.\nPentru a converti din format 12h in 24h "
                "tasteaza 2. ")
if alegere == "1":
    ora = input("Introduceti ora in format 'HH:MM AM/PM': ")
    formatat = ""
    perioada = ora[-2:]
    if perioada == "PM":
        formatat = str(int(ora[:2]) + 12) + ora[2:5]
    else:
        formatat = str(int(ora[:2])) + ora[2:5]
    print(f"Ora formatata este: {formatat}")
elif alegere == "2":
    ora = input("Introduceti ora in format 'HH:MM': ")
    formatat = ""
    perioada = ""
    if ora[:2] > "12":
        perioada = "PM"
        formatat = str(int(ora[:2]) - 12) + ora[2:]
    else:
        perioada = "AM"
        formatat = str(int(ora[:2])) + ora[2:]
    print(f"Ora formatata este: {formatat} {perioada}")
else:
    print("Ai introdus un carcter gresit!")