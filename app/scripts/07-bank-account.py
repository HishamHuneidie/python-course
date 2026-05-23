import shutil
import sys
from os import system, name
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.color import color
from methods.Menu import Menu, MenuItem

cls_command = 'cls' if name == 'nt' else 'clear'

def deposit():
    amount = float(input('Enter your deposit amount: '))

    customer1.balance += amount

def withdraw():

    amount = 0.0
    is_valid = False
    while not is_valid:
        amount = float(input('Enter your withdraw amount: '))

        if amount > customer1.balance:
            print(f'You have just {customer1.balance}€')
            continue

        break

    customer1.balance -= amount

menu = Menu([
    MenuItem(0, 'DEPOSIT', 'Deposit money', deposit),
    MenuItem(0, 'WITHDRAW', 'Withdraw money', withdraw),
    MenuItem(0, 'EXIT', 'Exit'),
])

class Person:
    def __init__(self, name: str, lastname: str):
        self.name = name
        self.lastname = lastname

class Client(Person):
    def __init__(self, name: str, lastname: str, account_number: str, balance: float):
        super().__init__(name, lastname)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        fullname = self.name + ' ' + self.lastname
        return f"{fullname} has {self.balance}€ in your account with the number {self.account_number}"

customer1 = Client('Hisham', 'Huneidie', '2121 5421', 1200.50)

def execute_men(menu: Menu, question=None, last_message=None):
    is_valid_answer = False
    while not is_valid_answer:

        menu_parts = []

        if last_message is not None:
            menu_parts.append(last_message)

        if question is not None:
            menu_parts.append(question)

        if len(menu_parts) > 0:
            menu_parts.append('')

        menu_parts.append(str(menu))
        menu_parts.append('\n')

        last_message = None





        system(cls_command)

        text_to_show = ''
        if last_message is not None:
            text_to_show = last_message + '\n'
        text_to_show = text_to_show + '\n'.join(menu_parts)

        answer = input(text_to_show)

        selected: MenuItem = menu.get(int(answer))

        if selected.key == 'EXIT':
            last_message = 'Bye bye!'
            break

        if selected.key == 'DEPOSIT':
            selected.callback()
            status = str(customer1)
            last_message = f'{status}\nYou want to deposit money!'

        if selected.key == 'WITHDRAW':
            selected.callback()
            status = str(customer1)
            last_message = f'{status}\nYou want to withdraw money!'

    if last_message is not None and last_message != '':
        system(cls_command)
        print(str(customer1))
        print(last_message)




execute_men(menu, 'What do you want to do today?', str(customer1))