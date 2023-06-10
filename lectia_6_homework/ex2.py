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

"""
Write a program that takes a time in 24-hour format as input (e.g., 13:45)
and converts it to 12-hour format (e.g., 1:45 PM).

"""
time = input('Time in format HH:MM')
hours_and_minutes_list = time.split(':')
hours, minutes = hours_and_minutes_list[0], hours_and_minutes_list[1]

pm = 'AM'

if hours >= '12':
    if hours != '12':
        hours = str(int(hours) - 12)
    pm = 'PM'

print(f"{hours}:{minutes} {pm}")

# Harder acasa
time = input('time in format HH:MM AM/PM')
