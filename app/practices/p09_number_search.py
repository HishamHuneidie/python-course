"""
This script is to practice this before the project
"""

import zipfile
import re
import os
import sys
import shutil
from pathlib import Path
from collections import Counter, defaultdict, namedtuple
import datetime as dt
import time
import timeit
from typing import Callable

sys.path.append(str(Path(__file__).resolve().parent.parent))

from packages.colorizer import Colorizer
from packages.colorizer.Colorizer import color_class

def print_title(text):
    print()
    print(Colorizer.colorize(text+':', color_class.GREEN))
    print()

print_title('Collections')

my_dict = {'uno': 111, 'dos': 222}
my_named_tuple = namedtuple('Person', ['name', 'age', 'eyes_color'])

objects = [
    Counter(['abc', 'def', 'abc', 'ghi', 'jkl']),
    defaultdict(lambda: 999, my_dict),
    my_named_tuple('Hisham', 31, 'brown'),
]

print('[')
for item in objects:
    print('\t'+ str(item))
print(']')

print(objects[0].most_common(1))
print(objects[1]['tres'])
print(objects[1]['cuatro'])
print(objects[1])
print(objects[2])
print(objects[2].name)


print_title('OS and Shutil')

filename_1 = '../fixtures/f09_number_search/file_1.py'
filename_2 = '../fixtures/f09_number_search/file_2.py'

try:
    shutil.move(filename_1, filename_2)
    print(f'Your file "{filename_1}" was moved to "{filename_2}"')
except:
    shutil.move(filename_2, filename_1)
    print(f'Your file "{filename_2}" was moved to "{filename_1}"')


print_title('List dir')

folder = '../'

for directory, subdir, files in os.walk(folder):
    print('-------')
    print(type(directory), directory)
    print(type(subdir), subdir)
    print(type(files), files)
    print('-------')



print_title('Dates and times')


birth = dt.datetime(1994, 10, 6, 20, 0, 0, 0)
today = dt.datetime.today()

age = today - birth

print(birth)
print(today)
print(type(birth))
print(type(age))
print(age.days)

print(type(dt.time()), dt.time())
print(type(time.time()), time.time())

limit = 10000000

def time_decorator(method: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        method(*args, **kwargs)

        duration = time.time() - start
        print(f'{method.__name__} took {duration} seconds')

    return wrapper


@time_decorator
def my_while():
    i = 0
    my_list = []
    while i < limit:
        my_list.append(i)
        i += 1

    return my_list


@time_decorator
def my_for():
    i = 0
    my_list = []
    for n in range(limit + 1):
        my_list.append(n)

    return my_list


setup_my_clean_while = """
def my_clean_while():
    i = 0
    my_list = []
    while i < limit:
        my_list.append(i)
        i += 1

    return my_list
"""


statement_my_clean_while = """
my_clean_while()
"""


setup_my_clean_for = """
def my_clean_for():
    i = 0
    my_list = []
    for n in range(limit + 1):
        my_list.append(n)

    return my_list
"""


statement_my_clean_for = """
my_clean_for()
"""


print_title('time')
my_while()
my_for()

duration_while = timeit.timeit(statement_my_clean_while, setup_my_clean_while, number=3, globals={'limit': limit})
duration_for = timeit.timeit(statement_my_clean_for, setup_my_clean_for, number=3, globals={'limit': limit})

print_title('timeit')
print(f'Duration while: {duration_while} seconds')
print(f'Duration for: {duration_for} seconds')


print_title('Regular expressions')


text = 'Si necesitas ayuda llama al (453)-342-7845 las 24 horas al servicio de ayuda online'

pattern = 'ayuda'
match = re.search(pattern, text)

print()
print(type(match), match)
print(match.span())
print(match.start())
print(match.end())


print()
print(Colorizer.colorize('re.finditer(pattern, text)', color_class.MAGENTA))
for found in re.finditer(pattern, text):
    print(found.span())


phone_pattern = r'\(\d{3}\)-\d{3}-\d{4}'
grouped_phone_pattern = re.compile(r'\((\d{3})\)-(\d{3})-(\d{4})')
phone_match = re.search(phone_pattern, text)
grouped_phone_match = re.search(grouped_phone_pattern, text)
print(phone_match.group())
print(grouped_phone_match.group())
print('Full match:', grouped_phone_match.group(0))
print('First group:', grouped_phone_match.group(1))
print('Second group:', grouped_phone_match.group(2))
print('Third group:', grouped_phone_match.group(3))

text_pattern = re.compile(r'necesitas(.*)llama')
text_match = re.search(text_pattern, text)
print()
print(text_match)
print(text_match.group(1))


print_title('Compress files')


zip_folder = '../fixtures/f09_number_search/zip/'
my_zip = zipfile.ZipFile(zip_folder + 'my_zip.zip', 'w')
my_zip.write(zip_folder + 'file_1.txt', arcname='file_1.txt')
my_zip.close()

my_zip.extract()















