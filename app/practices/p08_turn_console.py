"""
This script is to practice this before the project
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from packages.colorizer import Colorizer
from packages.colorizer.Colorizer import color_class

print(Colorizer.colorize('Exito!!', color_class.RED))
print(Colorizer.colorize('Exito!!', color_class.BLUE))
print(Colorizer.colorize('Exito!!', color_class.YELLOW))
print(Colorizer.colorize('Exito!!', color_class.GREEN))
print(Colorizer.colorize('Exito!!', color_class.MAGENTA))
print(Colorizer.colorize('Exito!!', color_class.CYAN))

def my_method():
    return 'My method'

print('Test styles with ', Colorizer.colorize('pylint /path/filename -ry', color_class.BLUE))