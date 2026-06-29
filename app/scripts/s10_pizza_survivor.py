import shutil
import sys
from os import system, name
import os
import re
from pathlib import Path
import datetime
import time
import math

sys.path.append(str(Path(__file__).resolve().parent.parent))

from fixtures.f08_turn_console.numbers import generate_ticket
from methods.color import color
from methods.Menu import Menu, MenuItem

cls_command = 'cls' if name == 'nt' else 'clear'


def content(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()

    return content


def get_serial(text):
    pattern = r'N\w{3}-\d{5}'
    match = re.search(pattern, text)

    if match is None:
        return None

    return match.group()




# TODO:
#     os re para iterar y buscar nums
#     buscar num de serie (solo un num por archivo)

start = time.time()




walked_files = os.walk('../fixtures/f09_number_search/zip/Mi_Gran_Directorio')

serials = []

for folder, subfolder, files in walked_files:
    for file in files:
        filename = folder + '/' + file
        text = content(filename)
        serial = get_serial(text)

        if serial is None: continue

        serials.append((file, serial))


duration = time.time() - start



print('----------------------------------------------------')
print('Search date: ', datetime.datetime.today().strftime('%d/%m/%y'))
print()
print('FILE\tSERIAL')
for t in serials:
    print(f'{t[0]}\t{t[1]}')
print()
print('Serials count: ', len(serials))
print('Search duration: ', math.ceil(duration), 'seconds')
print('----------------------------------------------------')
