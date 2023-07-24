"""
Scrie o funcție care primește o listă ca intrare și returnează suma elementelor sale.
Gestionează eroarea de tip TypeError dacă intrarea nu este o listă.

Task:
Definește o funcție care acceptă un singur parametru.
Verifică dacă parametrul este de tip listă folosind o instrucțiune if.
Dacă parametrul este o listă, calculează suma elementelor sale folosind funcția sum() și returnează rezultatul.
Dacă parametrul nu este o listă, generează o eroare de tip TypeError cu un mesaj de eroare adecvat.
"""

def sum_of_numbers(numbers):
    if not isinstance(numbers, list):  # type(numbers) == list
        raise TypeError('Parameter is not list')
    return sum(numbers)
def sum_of_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Parameter is not list')
    return sum(numbers)

if __name__ == '__main__':
    from input_utils import input_list_of_numbers_safe
    print(sum_of_numbers(input_list_of_numbers_safe()))