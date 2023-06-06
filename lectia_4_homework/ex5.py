"""
Nota trecătoare la un test.
Presupunem că pentru a avea o notă trecătoare la un test,
elevii trebuie să obţină minim 15 puncte.
Scrieţi un program care citeşte de la tastatură punctajul obţinut de un elev şi
afişează dacă elevul are o notă trecătoare sau va trebui să mai susţină încă o dată testul.
"""

punctaj = float(input("Introduceti punctajul acumulat: "))
if punctaj >= 15:
    print(f"Elevul are o notă trecătoare.")
else:
    print(f"Elevul va trebui să mai susţină încă o dată testul.")