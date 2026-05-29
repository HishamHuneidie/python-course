import shutil
import sys
from os import system, name
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from fixtures.f08_turn_console.numbers import generate_ticket
from methods.color import color
from methods.Menu import Menu, MenuItem

cls_command = 'cls' if name == 'nt' else 'clear'

# Declare generators
pharmacy_ticket_generator = generate_ticket('Pharmacy')
cosmetics_ticket_generator = generate_ticket('Cosmetics')
perfumes_ticket_generator = generate_ticket('Perfumes')


# Individual ticket generator callback
def generate_pharmacy_ticket():
    return next(pharmacy_ticket_generator)


# Individual ticket generator callback
def generate_cosmetics_ticket():
    return next(cosmetics_ticket_generator)


# Individual ticket generator callback
def generate_perfumes_ticket():
    return next(perfumes_ticket_generator)


menu = Menu([
    MenuItem(0, 'F', 'Pharmacy', generate_pharmacy_ticket),
    MenuItem(1, 'C', 'Cosmetics', generate_cosmetics_ticket),
    MenuItem(2, 'P', 'Perfumes', generate_perfumes_ticket),
    MenuItem(3, 'EXIT', 'Exit', None),
])


def execute_menu(menu: Menu, question: str, last_message: str=None):
    while True:
        show_parts = []
        if last_message is not None:
            show_parts.append(last_message)
            last_message = None

        if question is not None and question != '':
            show_parts.append(question)

        show_parts.append(str(menu))

        show = '\n'.join(show_parts) + '\n'
        answer = input(show)

        try:
            selected: MenuItem = menu.get(int(answer))
        except IndexError:
            last_message = color('Select a valid option', 'red')
            continue

        if selected.key == 'EXIT':
            break

        selected.execute()

execute_menu(menu, 'Which type would you like? ')


# Fin
