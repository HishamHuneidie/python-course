import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.color import color
from methods.printer import title

filename = './fixtures/open-file.txt'
absolute_filename = '/app/fixtures/open-file.txt'
file = open(filename)
original_content = file.read()
file.close()


def finish():
    file = open(filename, 'w')
    file.write(original_content)
    file.close()


# Day 06 - Recipe book

# Read files

title('Read files')

file = open(filename)
print(color('open("my-file")', 'magenta'))
print(file)
print()
print(color('file.read()', 'magenta'))
print(file.read())
file.close()

file = open(filename)
print()
print(color('file.readline()', 'magenta'), file.readline().strip())
print(color('file.readline()', 'magenta'), file.readline().strip())
print(color('file.readline()', 'magenta'), file.readline().strip())
file.close()

file = open(filename)
print()
print(color("""
for line in file:
    print(line)
""".strip(), 'magenta'))
for line in file:
    print(line.strip())
file.close()

file = open(filename)
print()
print(color('file.readlines()', 'magenta'), file.readlines())
file.close()

print()
print(color('Opening methods:', 'magenta'))
print('- ', color('r:', 'magenta'), 'Just read the file. If not exists, then error.')
print('- ', color('w:', 'magenta'),
      'Just write the file. If not exists, then it is created. If exists, then its content is replaced.')
print('- ', color('a:', 'magenta'),
      'Add text to the file. If not exists, then it is created. If exists, then it adds more lines.')

file = open(filename, 'a')
file.write('New line')
file.writelines(['New line', 'Second line', 'third line'])
file.close()

file = open(absolute_filename, 'r')
print()
print(color('Open file with an absolute path', 'magenta'))
print(file.read())
file.close()

my_folder = Path('/app/fixtures')
file_path = my_folder / 'open-file.txt'
file = open(file_path, 'r')
print()
print(type(file_path))
print(color('open(Path(), "r")', 'magenta'), file.readline())
file.close()

print(color('system("clear")', 'magenta'), 'It cleans the terminal')

finish()
# file.close()
