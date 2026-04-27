import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.color import color
from methods.printer import title

# Day 03 - Text analyzer

## Method index() to search characters

title('Method index() to search characters')

text1 = "This is a test"
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(text1[0])
print(type(text1[0]))
print(text1.index("i"))

print(f"Operación > abc[2] = {abc[2]}")
print(f"Operación > abc[2:] = {abc[2:]}")
print(f"Operación > abc[2:5] = {abc[2:5]}")
print(f"Operación > abc[:5] = {abc[:5]}")
print(f"Operación > abc[5] = {abc[5]}")
print(f"Operación > abc[2:15:2] = {abc[2:15:2]}")
print(f"Operación > abc[2:15:-2] = {abc[2:15:-2]}")
print(f"Operación > abc[::-2] = {abc[::-2]}")

frase = "Controlar contempla cosas"
print(f"First word in '{frase}' is: '{frase[:9]}'")

## Other string methods
title('Other string methods')

text2 = """
First line
Second line
Third line
""".strip()

print(text2)
print(text2.find('agua') >= 0)
print(len(text2))

## Working with lists
title('Working with lists')

list1 = ['A', 'K', 'U']
list2 = ['S', 'M', 'B']

print(list1[::-1])
list1.reverse()
print(list1)
print(list2)
list2.sort()

print(list2)

## Working with dictionaries
title('Working with dictionaries')

user1 = {
    'name': 'Carl Smith',
    'age': 31,
    'city': 'Madrid',
}

print(user1)
print(user1.keys())
print(user1.values())
print(user1.items())

## Working with tuples
title('Working with tuples')

my_tuple = (1, 2, 3)
t1 = (1, 2, 3)
l1 = [1, 2, 3]

print(my_tuple)
print(type(my_tuple))

my_tuple = list(my_tuple)
print(type(my_tuple))

a, b, c = t1
d, e, f = l1

print(a, b, c, d, e, f)
print('length', len(my_tuple))
print('count', my_tuple.count(2))

## Working with tuples
title('Working with tuples')

set1 = set(l1);
set2 = {4, 5, 6}
set3 = set1.union(set2, {3, 6, 7, 8})

print(type(set1))
print(type(set2))
print(color('set1:', 'magenta'), set1)
print(color('set2:', 'magenta'), set2)

print(color('2 in set1:', 'magenta'), 'Yes it is' if (2 in set1) else 'Nope')
print(color('2 in set2:', 'magenta'), 'Yes it is' if (2 in set2) else 'Nope')

print(color('set3:', 'magenta'), set3)
set3.add('Hola')
print(color('set3.add("String"):', 'magenta'), set3)

## Working with booleans
title('Working with booleans')

bool1 = True
bool2 = False
bool3 = 5 > 4
bool4 = 5 < 4
bool5 = 3 in [1, 2, 3, 4, 5, 6]

print(color('Booleans:', 'magenta'), bool1, bool2, bool3, bool4, bool5)