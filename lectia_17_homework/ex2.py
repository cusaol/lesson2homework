"""
Creati un program care va numara timpul pana la un eveniment
Aplicatia trebuie sa permita utilizatorului sa introduca data si ora intr-un string conform urmatorului format:
31/12/2023 23:59 (dd/mm/YYYY HH:MM).
Programul va verifica daca data aleasa este cu mai putin de un an innainte. Daca data este cu mai mult de un an
innainte programul va arata o eroare si va ruga utilizatorul sa introduca din nou.
De asemenea, programul va intreba de la utilizator care este evenimentul care il asteapta: Exemlu Apare noul Iphone
Dupa ce datele au fost introduse si validate, programul va afisa fiecare secunda (cu ajutorul la time.sleep) timpul
ramas pan la eveniment. Exemplu: 23 zile, 19 minute si 34 secunde au ramas pan la Apare noul Iphone.
"""

import time
from datetime import timedelta, datetime

def get_event_date_and_name():
    while True:
        try:
            timpul = input("Introdu timpul pana la un eveniment in urmatorul format (dd/mm/YYYY HH:MM): ")
            name_event = input("Care este evenimentul pe care il astepti? ")
            event_datetime = datetime.strptime(timpul, "%d/%m/%Y %H:%M")
            current_datetime = datetime.now()
            one_year = timedelta(days=365)

            if event_datetime > current_datetime + one_year:
                raise ValueError("Data este cu mai mult de un an inainte.")

            return name_event, event_datetime
        except ValueError as e:
            print("Eroare:", str(e))
            print("Vă rugăm să introduceți o dată validă.\n")

def countdown_to_event(event_name: str, deadline: datetime):

    while datetime.now() < deadline:
        time_left = deadline - datetime.now()
        # calculam timp ramas
        days, seconds = time_left.days, time_left.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        print(f"Numarul de zile pana la {event_name}: {days} zile.")
        print(f"Timp ramas: {days} zile, {hours} ore, {minutes} minute, {seconds:.0f} secunde.")
        time.sleep(1)

    print(f'HURRAY! We reached {event_name}')

if __name__ == '__main__':
    name_event, event_datetime = get_event_date_and_name()
    countdown_to_event(name_event, event_datetime)