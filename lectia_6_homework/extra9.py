"""
Scrieți un program care afișează numerele de la 1 la 100. Pentru multiplii de 3, se va afișa "Fizz" în locul numărului.
Pentru multiplii de 5, se va afișa "Buzz". Pentru numerele care sunt multipli atât de 3, cât și de 5, se va afișa
" FizzBuzz".
"""

for x in range(101):
    if x % 3 == 0 and x % 5 == 0:
        print(" FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)