"""
Creati doua liste care vor reprezenta numele participantilor la doua evenimente.
Transformati-le apoi in seturi.

Utilizati operatiile cu seturi si afisati rezultatele:
* cati participanti au fost prezenti la ambele evenimente;
* cati participanti au fost prezenti doar la primul eveniment;
* cati participanti au fost prezenti doar la al doilea eveniment.
"""

eveniment1 = set(input("Introdu lista participantilor la primul eveniment separat prin spatiu: "). split(" "))
eveniment2 = set(input("Introdu lista participantilor la al doilea eveniment separat prin spatiu: ").split(" "))

print(f"Au participat la ambele evenimente: {eveniment1 & eveniment2}")
print(f"Au participat doar la primul eveniment: {eveniment1 - eveniment2}")
print(f"Au participat doar la al doilea eveniment: {eveniment2 - eveniment1}")