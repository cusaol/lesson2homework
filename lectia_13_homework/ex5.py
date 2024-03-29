"""
Scrie un program care cere utilizatorului să introducă vârsta lor și gestionează eroarea AgeError dacă vârsta este
mai mică de 0 sau mai mare de 150. Defineste o clasă de excepție personalizată numită AgeError în acest scop.

Task:
Defineste o clasă de excepție personalizată numită AgeError care moștenește clasa de bază Exception.
Defineste o funcție care cere utilizatorului să introducă vârsta lor și returnează vârsta ca număr întreg.
Folosește un bloc try-except pentru a gestiona excepțiile potențiale.
În blocul try, converteste intrarea utilizatorului la un număr întreg și stochează rezultatul într-o variabilă.
Folosește o instrucțiune if pentru a verifica dacă vârsta este mai mică de 0 sau mai mare de 150.
Dacă vârsta este invalidă, generează o eroare AgeError cu un mesaj de eroare adecvat.
Dacă vârsta este validă, returnează-o.
"""
