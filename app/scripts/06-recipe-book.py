import shutil
import sys
from os import system, name
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.color import color

# Definitions

cls_command = 'cls' if name == 'nt' else 'clear'
main_question = color('What would you like to order?', 'blue')


def beautify_title(file_path):
    filename = file_path.stem
    filename = filename.replace('-', ' ')
    return filename[0].upper() + filename[1:].lower()


def get_category(file_path):
    folder = str(file_path.parent)
    folders = folder.split('/')
    return folders[-1]


def menu_line(index, item):
    if isinstance(item, Path):
        file = item
        key = color(f"[{index}]", 'magenta')
        recipe_name = beautify_title(file)
        category = get_category(file)

        return f"{key} {recipe_name} ({category})"

    if isinstance(item, str):
        return color(f'[{index}]', 'magenta') + f' {item}'

    return None


def menu_to_string(menu_list, question=None, last_console_message=None):
    result = ''

    if last_console_message is not None:
        result += last_console_message + '\n'

    if question is not None:
        result += color(question, 'blue') + '\n'

    for index, item in enumerate(menu_list):
        result = result + '\n' + menu_line(index, item)

    return result.strip() + '\n'


def execute_menu(menu, question=None, last_console_message=None):
    menu = list(menu)
    system(cls_command)

    term_question = menu_to_string(menu, question, last_console_message)

    answer = None
    while answer is None:
        try:
            user_answer = int(input(term_question))

            if user_answer == -1:
                system(cls_command)
                print(color('Select a valid numeric option', 'red'))
                continue

            if user_answer not in range(0, len(menu)):
                system(cls_command)
                print(color('Select a valid numeric option', 'red'))
                continue

            answer = user_answer
        except ValueError:
            system(cls_command)
            print(color('Select a valid numeric option', 'red'))

    return {
        'menu': menu,
        'selection': answer,
    }


def find_recipes():
    return list(Path().glob('./fixtures/06-recipe-book/**/*.txt'))


def find_categories():
    return list(Path().glob('./fixtures/06-recipe-book/*'))


def get_answer_title(menu_execution):
    return menu_execution['menu'][menu_execution['selection']]


def show_recipe(filename):
    filename_title = color(beautify_title(filename), 'blue')
    content = filename.read_text()
    print(f"{filename_title}: {content}")
    return


def escape_title(text):
    return text.lower().replace(' ', '-')


def create_recipe():
    try:
        system(cls_command)
        recipe_name = escape_title(input(color('Write a name for your recipe: ', 'blue'))) + '.txt'

        system(cls_command)
        recipe_description = input(color('Write a description for your recipe: ', 'blue'))

        menu_categories = find_categories()
        recipe_category = get_answer_title(execute_menu(menu_categories, 'Select a category'))

        recipe = {
            'name': recipe_name,
            'description': recipe_description,
            'category': recipe_category,
        }

        filename = recipe['category'] / recipe['name']
        file = Path(filename)
        file.write_text(recipe['description'])

        return True
    except:
        return False


def create_category():
    try:
        system(cls_command)
        category_name = escape_title(input(color('Write a name for your category: ', 'blue')))

        Path(f"./fixtures/06-recipe-book/{category_name}").mkdir()

        return True
    except:
        return False


def remove(file):
    if not file.exists():
        return False

    if file.is_file():
        file.unlink()
        return True

    if file.is_dir():
        shutil.rmtree(str(file.resolve()))
        return True

    return False


def remove_entity(menu, entity_type):
    entity_answer = execute_menu(menu, f'Select a {entity_type} to remove:')
    entity_answer_filename = get_answer_title(entity_answer)
    entity_name = color(beautify_title(entity_answer_filename), 'red')

    system(cls_command)

    is_sure = input(f'Are you sure you want to remove recipe "{entity_name}"? (y/n) ')
    if is_sure == 'y' or is_sure == 'Y':
        file = Path(entity_answer_filename)
        return remove(file)

    return False


main_options = [
    'Read recipe',
    'Add recipe',
    'Remove recipe',
    'Add category',
    'Remove category',
    'Exit',
]
last_console_message = None

while True:
    main_answer = execute_menu(main_options, 'Select an option:', last_console_message)

    # Exit program
    if main_answer['selection'] == 5:
        print(color('Bye bye', 'red'))
        break

    # Read recipe
    if main_answer['selection'] == 0:
        recipes_menu = find_recipes()
        recipes_answer = execute_menu(recipes_menu, 'Select recipe:')
        recipes_answer_filename = get_answer_title(recipes_answer)
        system(cls_command)

        show_recipe(recipes_answer_filename)
        break

    # Add recipe
    if main_answer['selection'] == 1:
        is_recipe_created = create_recipe()

        if is_recipe_created:
            last_console_message = color('Recipe was added', 'green')
            continue

        print(color('Error adding recipe', 'red'))
        break

    # Remove recipe
    if main_answer['selection'] == 2:
        recipes_menu = find_recipes()
        is_removed = remove_entity(recipes_menu, 'recipe')

        if is_removed:
            last_console_message = color('Recipe was removed', 'green')
            continue

        last_console_message = color('Recipe was not removed', 'red')

    # Add category
    if main_answer['selection'] == 3:
        is_category_created = create_category()

        if is_category_created:
            last_console_message = color('Category was added', 'green')
            continue

        last_console_message = color('Category was not added', 'red')

    # Remove category
    if main_answer['selection'] == 4:
        menu_categories = find_categories()
        is_removed = remove_entity(menu_categories, 'category')

        if is_removed:
            last_console_message = color('Category was removed', 'green')
            continue

        last_console_message = color('Category was not removed', 'red')
