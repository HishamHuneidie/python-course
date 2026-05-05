import sys
from pathlib import Path
from random import randint

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.color import color
from methods.printer import title
from methods.table import to_table

name = input('What is your name? ')
tries = []
max_tries = 8
min_number = 1
max_number = 100
correct_answer = randint(1, max_number + 1)
isWinner = False
i = 0
cleaner = "\r\033[K"

print()
while len(tries) < max_tries:
    i += 1
    number = int(input(f"Tell me a number from {min_number} to {max_number} ({i}/{max_tries}): "))

    print("\033[A", end="")
    message = ''

    if number < min_number or number > max_number:
        print(f"{cleaner}{number} is out of range. Try again.")
        message = 'OUT OF RANGE'
    elif number == correct_answer:
        isWinner = True
        message = 'CORRECT'
    elif number > correct_answer:
        print(f"{cleaner}Incorrect answer. Try again with a smaller number.")
        message = 'TO HIGH'
    else:
        print(f"{cleaner}Incorrect answer. Try again with a higher number.")
        message = 'TO SMALL'

    result = color(message, 'green' if isWinner else 'red')
    tries.append({'Attempt': i, 'Answer': number, 'Result': result})

    if isWinner: break

print("\033[A", end="")
print()
if isWinner:
    print(color(f"{cleaner}Congratulations {name}! You won after {len(tries)} tries!", 'green'))
else:
    print(color(f"{cleaner}Oh no! You lost after {max_tries} tries.", 'yellow'))

print()
print('Here are your results:')
print(to_table(tries))
