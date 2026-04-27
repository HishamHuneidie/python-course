class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

    @staticmethod
    def get_color(color=None):
        if (color is None):
            return Color.RED

        switch = {
            'red': Color.RED,
            'green': Color.GREEN,
            'blue': Color.BLUE,
            'yellow': Color.YELLOW,
            'magenta': Color.MAGENTA,
            'cyan': Color.CYAN,
            'white': Color.WHITE,
        }

        return switch.get(color, Color.RED)

def color(text, color):
    return Color.get_color(color) + text + Color.RESET