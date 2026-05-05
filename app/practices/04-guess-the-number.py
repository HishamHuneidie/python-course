import sys
from pathlib import Path
from random import randint, uniform, random, choice, shuffle

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.color import color
from methods.printer import title

# Day 04 - Guess the number

# Control structures

title('Control structures (if else)')

cond1 = True
cond2 = False

if cond2:
    print('cond2 is true')
elif cond1:
    print('cond1 is true')
else:
    print('cond1 and cond2 are false')

print(color("var1 if condition else var2", 'magenta'), 'cond1 is true' if cond1 else 'cond1 is false')
print(color("var1 if condition else var2", 'magenta'), 'cond2 is true' if cond2 else 'cond2 is false')

title('Control structures (match)')

serie = 'ABC'
match serie:
    case 'ASD':
        print(color('match serie:', 'magenta'), 'ASD')
    case 'ABC':
        print(color('match serie:', 'magenta'), 'ABC')
    case _:
        print(color('match serie:', 'magenta'), 'Nada')

# Loops
title('Loops')

items = ["First item", "Second item", "Third item"]
print(color("""
for item in items:
    print(item)
""", 'magenta').strip())

for item in items:
    if item.startswith('S'):
        print("Don't show items that stats with S")
        continue
    print(item)

print(color("""
for (a, b, c) in matrix:
    print(a, b, c)
""", 'magenta'))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];
for (a, b, c) in matrix:
    print(a, b, c)

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
}

print(color("""
for (key, value) in dictionary.items():
    print(key, value)
""", 'magenta'))

for (key, value) in dictionary.items():
    print(key, value)

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0

for n in lista_numeros:
    if n % 2 == 0:
        suma_pares += n
    else:
        suma_impares += n

print(suma_pares, suma_impares)

# Ranges

title('Ranges')

r = range(5)

print(r)
print(type(r))

for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)

# Zip elements

title('Zip elements')

names = ['Hisham', 'Faisal', 'Sharif']
ages = [31, 65, 34]
cities = ['Madrid', 'Lima', 'Lima']

for name, age, city in zip(names, ages, cities):
    print(f"{name} lives in {city} and is {age} years old")

# Randoms

title('Randoms')

sorted_numbers = [1, 2, 3, 4, 5]
shuffle(sorted_numbers)
random_list = {
    'int': randint(1, 50),
    'float': uniform(1, 5),
    'random': random(),
    'choice': choice(names),
    'shuffle': sorted_numbers,
}

print(color('Random numbers:', 'magenta'))
for key, value in random_list.items():
    print(color(key, 'magenta'), value)

# Other loops

title('Other loops')

letters = 'MyLettersAreGood'
list = [L for L in letters]
print(color('list = [L for L in letters]', 'magenta'))
print(list)

print(color("list2 = [(n if (n*2 > 10) else 'no') for n in range(0, 22, 3)]", 'red'))
list2 = [(n if (n * 2 > 10) else 'no') for n in range(0, 22, 3)]
print(list2)

print(color('Convert inches into meters', ''))

inches = [10, 20, 30, 40, 50]
meters = [(inch * .0254) for inch in inches]

print(color('inches:', 'yellow'), inches)
print(color('meters:', 'yellow'), meters)
