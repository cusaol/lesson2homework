"""
Avand lista de mai jos.

Adaugati in ea elementele **4**, **5** si **6**.

Afișați rezultatele
"""

list_1 = [1, 2, 3]
my_list = [4, 5, 6]
list_1.extend(my_list)
print(f"Lista obtinuta: {list_1}")

# alta metoda
# list_1 = [1,2,3]
# list_1.append(4)
# list_1.append(5)
# list_1.append(6)
# print(f"Lista obtinuta: {list_1}")