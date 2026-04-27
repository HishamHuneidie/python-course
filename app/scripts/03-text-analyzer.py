import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.color import color
from methods.printer import title

originalText = input('Write a text that you like: ')
letters = [
    str(input('Write a letter (1/2): ')).lower()[0],
    str(input('Write a letter (2/3): ')).lower()[0],
    str(input('Write a letter (3/3): ')).lower()[0],
]
words = originalText.split(' ')
text = originalText.lower()

# TODO: Count how many times appears a letter

title('Count how many times appears a letter')

print(color(f'Letter "{letters[0].upper()}" appears:', 'magenta'), text.count(letters[0]))
print(color(f'Letter "{letters[1].upper()}" appears:', 'magenta'), text.count(letters[1]))
print(color(f'Letter "{letters[2].upper()}" appears:', 'magenta'), text.count(letters[2]))

# TODO: Count how many words there are in total

title('Count how many words there are in total')

print(color(f'Words in text:', 'magenta'), len(words))

# TODO: Show first and last letters

title('Show first and last letters')

print(color(f'First letter:', 'magenta'), originalText[0])
print(color(f'Last letter:', 'magenta'), originalText[-1])

# TODO: Reverse words in text

title('Reverse words in text')

print(color(f'Reversed words:', 'magenta'), ' '.join(words[::-1]))

# TODO: Does 'python' appear in the text

title('Does "python" appear in the text')

print(color('Appears?:', 'magenta'), 'Yes' if 'python' in text else 'No')