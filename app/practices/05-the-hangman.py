import sys
from pathlib import Path
from random import shuffle

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.color import color
from methods.printer import title

# Day 05 - The hangman

# Methods

title('Methods')

coffee_list = [
    ('Capuccino', 2.50),
    ('American', 3),
    ('Latte', 1.50),
]

def coffee_most_expensive(list):
    """
    This is my first method
    """
    max_name, max_price = [None, 0]
    for coffe_name, price in list:
        if price > max_price:
            max_name, max_price = coffe_name, price

    return (max_name, max_price)

expensive_coffe = coffee_most_expensive(coffee_list)

print(f"The most expensive coffee is {expensive_coffe[0]} and the price is {expensive_coffe[1]}")


# First play

title('First play')

# Initial list
tubes = ['-', '--', '---', '----']

# Mix tubes
def mix_list(list):
    shuffle(list)
    return list

# Ask user to choose
def ask_number():
    attempt = ''

    while attempt not in ['1', '2', '3', '4']:
        attempt = input('Choose a number between 1 and 4: ')

    return int(attempt)

# Verify the user's attempt
def verify_attempt(list, user_number):
    selection = list[user_number - 1]

    if selection == '-':
        print(color('You lost!', 'red'))
        pass
    else:
        print(color('You won!', 'cyan'))
        pass

    print(f'You got the "{selection}"')

mixed_tubes = mix_list(tubes)
user_number = ask_number()
verify_attempt(mixed_tubes, user_number)


# Variadic operator and argument unpacking

title('Variadic operator and argument unpacking')

print(color("""
Variadic operator:  func method(...$args) → def method(*args)
Argument unpacking: method(...$args)      → method(*args)

kwargs → def method(**dictionary)
       → method(k1=v1, k2=v2)
       → method(**dictionary)
""", 'magenta'))