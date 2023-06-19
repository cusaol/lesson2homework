"""
Dat fiind două dicționare care reprezintă notele elevilor:
math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}
Scrieți un program care calculeaza media notelor la fiecare elev din ambele dictionare si le stocheaza intr-un
dictionar nou.
"""

math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}

media = {}
for key in math_grades:
    media[key] = (math_grades[key] + science_grades[key])/2

print(f'{media}')