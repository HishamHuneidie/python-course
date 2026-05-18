import sys
from pathlib import Path
from random import choice

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.color import color

def is_letter(text):
    return len(text) == 1 and text.isalpha()

def show_match(secret_letters, mask_letters, letter):
    for i, l in enumerate(secret_letters):
        if l == letter.upper():
            mask_letters[i] = l.upper()

    selected_letters.add(letter.upper())
    return mask_letters

def result_to_string(mask_letters):
    return f"[{''.join([l for l in mask_letters])}]"

def has_won(mask_letters):
    return not '_' in mask_letters

is_winner = False
max_lives = 10
lives = max_lives
allowed_words = [
    'I LOVE PYTHON',
    'PYTHON IS A GOOD LANGUAGE',
    'PROGRAMMERS ARE THE BEST'
]
secret_word = choice(allowed_words)
secret_letters = [l for l in secret_word]
mask_letters = ['_' for l in secret_letters]
selected_letters = set()
heart = color('♡', 'red')

mask_letters = show_match(secret_letters, mask_letters, ' ')
mask_letters = show_match(secret_letters, mask_letters, choice(secret_letters))
mask_letters = show_match(secret_letters, mask_letters, choice(secret_letters))

print(f"You have this word: {result_to_string(mask_letters)}")

while not is_winner and lives > 0:
    letter = input('\rTell me a letter: ')
    print()

    if not is_letter(letter):
        continue

    letter = letter.upper()

    if letter in selected_letters:
        print('This letter is already selected')
        selected_letters.add(letter)
        continue

    if not letter in secret_letters:
        lives -= 1
        print(f'Your letter is invalid. You have {lives}/{max_lives} {heart}')
        pass

    mask_letters = show_match(secret_letters, mask_letters, letter)
    print(f"Result: {result_to_string(mask_letters)}")

    if has_won(mask_letters):
        print(color('✔ You won!', 'cyan'))
        is_winner = True
    elif lives == 0:
        print(color('✘ You lost!', 'red'))

