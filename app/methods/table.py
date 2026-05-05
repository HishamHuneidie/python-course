import re

types = {
    'list': 'list',
    'tuple': 'tuple',
    'dictionary': 'dictionary',
    'set': 'set',
}


def to_table(matrix):
    if not isinstance(matrix, list) or len(matrix) == 0:
        return None

    type = verify_type(matrix)
    if type == 'list':
        return list_to_table(matrix)
    elif type == 'tuple':
        return tuple_to_table(matrix)
    elif type == 'dictionary':
        return dictionary_to_table(matrix)
    elif type == 'set':
        return set_to_table(matrix)

    return None


def list_to_table(matrix):
    return format_table(matrix)


def tuple_to_table(matrix):
    rows = [list(row) for row in matrix]
    return format_table(rows)


def dictionary_to_table(matrix):
    headers = []
    for row in matrix:
        for key in row.keys():
            if key not in headers:
                headers.append(key)

    rows = [headers]
    for row in matrix:
        rows.append([row.get(header, '') for header in headers])

    return format_table(rows)


def set_to_table(matrix):
    rows = [sorted(list(row), key=str) for row in matrix]
    return format_table(rows)


def format_table(matrix):
    rows = [[str(cell) for cell in row] for row in matrix]
    columns = max(len(row) for row in rows)
    lengths = [0] * columns

    for row in rows:
        for i, cell in enumerate(row):
            clean_length = len(clear_text(cell))
            if clean_length > lengths[i]:
                lengths[i] = clean_length

    table = []
    for row in rows:
        formatted_row = []
        for i in range(columns):
            cell = row[i] if i < len(row) else ''
            formatted_row.append(format_cell(cell, lengths[i]))
        table.append(formatted_row)

    table_rows = ["|" + "|".join(row) + "|" for row in table]
    return "\n".join(table_rows)


def verify_type(matrix):
    if len(matrix) == 0: return None

    if isinstance(matrix[0], list):
        return types['list']
    elif isinstance(matrix[0], tuple):
        return types['tuple']
    elif isinstance(matrix[0], dict):
        return types['dictionary']
    elif isinstance(matrix[0], set):
        return types['set']

    return None


def clear_text(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)


def format_cell(text, width):
    visible_length = len(clear_text(text))
    padding = ' ' * max(0, width - visible_length)
    return f" {text}{padding} "


my_list_matrix = [
    ['uno', 'dos', 'tres'],
    ['cuatro', 'cinco', 'seis'],
    ['siete', 'ocho', 'nueve'],
]
my_tuple_matrix = [
    ('uno', 'dos', 'tres'),
    ('cuatro', 'cinco', 'seis'),
    ('siete', 'ocho', 'nueve'),
]
my_dict_matrix = [
    {'First': 'uno', 'Second': 'dos', 'Third': 'tres'},
    {'First': 'cuatro', 'Second': 'cinco', 'Third': 'seis'},
    {'First': 'siete', 'Second': 'ocho', 'Third': 'nueve'},
]
my_set_matrix = [
    {'uno', 'dos', 'tres'},
    {'cuatro', 'cinco', 'seis'},
    {'siete', 'ocho', 'nueve'},
]
