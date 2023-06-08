"""
Creaţi 2 liste: `elev1` şi `elev2`.

Pentru fiecare elev, cititi de la tastatură **numele**, **prenumele** şi **nota** obţinută la examen
şi salvaţi datele în listele `elev1` şi `elev2`.

După aceasta, afişaţi la ecran:
* care dintre cei 2 elevi are o notă mai mare la examen (afişaţi numele şi prenumele)
* care dintre cei 2 elevi are o notă mai mică la examen (afişaţi numele şi prenumele)
* pentru fiecare elev, transformaţi numele sa fie scris cu toate literele majuscule,
iar prenumele să înceapă cu literă mare. De exemplu, pentru elevul "Elon Musk", rezultatul afişat va fi "Elon MUSK"
*  afişaţi datele sub formă de tabel, folosind indexarea listelor, ca în exemplul de mai jos (Nu neaparat sa fie tabel):

| Elon | Musk | 9.5 |
|------|------|-----|
| Bill | Gates | 8.5|
"""

# ellevul 1
elev1 = []
nume1 = input("Introduceti numele elevului I: ")
prenume1 = input("Introduceti prenumele elevului I: ")
nota1 = float(input("Introduceti nota elevului I: "))
elev1 = [nume1, prenume1, nota1]

# elevul 2
elev2 = []
nume2 = input("Introduceti numele elevului II: ")
prenume2 = input("Introduceti prenumele elevului II: ")
nota2 = float(input("Introduceti nota elevului II: "))
elev2 = [nume2, prenume2, nota2]

# majuscule
nume1m = elev1[0].upper()
prenume1m = elev1[1][0].upper() + elev1[1][1:]

nume2m = elev2[0].upper()
prenume2m = elev2[1][0].upper() + elev2[1][1:]

# nota mai mare
if nota1 > nota2:
    print(f"Elevul {prenume1m} {nume1m} are o nota mai mare la examen.\nElevul {prenume2m} {nume2m} "
          f"are o nota mai mica la examen.")
elif nota1 < nota2:
    print(f"Elevul {prenume2m} {nume2m} are o nota mai mare la examen.\nElevul {prenume1m} {nume1m} "
          f"are o nota mai mica la examen.")
else:
    print(f" Elevii {prenume1m} {nume1m} si {prenume2m} {nume2m} au primit aceeasi nota la examen.")

# indexare
print(f"|  {elev1[0]}  |  {elev1[1]}  |  {elev1[2]}  |")
print(f"|  ---------  |  ---------  |  ----  |")
print(f"|  {elev2[0]}  |  {elev2[1]}  |  {elev2[2]}  |")