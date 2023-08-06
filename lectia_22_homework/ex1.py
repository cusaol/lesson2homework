"""
Creați clasele enumerate mai jos. Utilizați moștenirea.
Pentru toate proprietățile, utilizați sublinieri în interiorul clasei pentru a ascunde proprietățile
(exemplu self._inner_color) și declarați metode get și set (exemplu set_inner_color).
Creați o clasă care descrie o Formă (Shape).
Clasa Formă ar trebui să aibă următoarele proprietăți:
* culoarea interioară (inner color)
* culoarea marginii (border color)
Creați o altă clasă Cerc (Circle) care extinde clasa Formă (Shape).
Clasa cerc ar trebui să aibă următoarele proprietăți suplimentare:
* rază (radius)
Creați o altă clasă Dreptunghi (Rectangle) care, de asemenea, extinde clasa Formă (Shape)
Clasa dreptunghi ar trebui să aibă următoarele proprietăți suplimentare:
* lățime (width)
* lungime (length)
Creați o altă clasă Pătrat (Square) care extinde clasa Dreptunghi (Rectangle)
Clasa Pătrat ar trebui să se asigure că lățimea și lungimea sunt egale atunci când una dintre ele este setată.
De exemplu, dacă setez square.set_length(4), square.get_width() ar trebui să fie și el 4.
"""

class Forma:

    def __init__(self, _intercolor, _margcolor):
        self._intercolor = _intercolor
        self._margcolor = _margcolor

    def set_color(self):
        print(f'{self.species} {self.name} mănâncă')

    def get_color(self):
        print(f'{self.species} {self.name} doarme')

class Cerc(Forma):

    def __init__(self, raza):
        self.raza = raza
        self.species = 'câine'

    def raza(self):
        print(f'{self.species} {self.name} mănâncă')

class Dreptunghi(Forma):

    def __init__(self, latime, lungime):
        self.latime = latime
        self.lungime = lungime

    def raza(self):
        print(f'{self.species} {self.name} mănâncă')

class Patrat(Dreptunghi):

    def __init__(self, latime, lungime):
        self.latime = latime
        self.lungime = lungime

    def raza(self):
        print(f'{self.species} {self.name} mănâncă')