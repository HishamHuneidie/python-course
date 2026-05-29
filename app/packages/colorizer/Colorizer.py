
class Color:
    def __init__(self):
        self.RED = '\033[31m'
        self.GREEN = '\033[32m'
        self.BLUE = '\033[34m'
        self.YELLOW = '\033[33m'
        self.MAGENTA = '\033[35m'
        self.CYAN = '\033[36m'
        self.WHITE = '\033[37m'
        self.RESET = '\033[0m'

    def get_color(self, color=None):
        if color is None:
            return self.RED

        switch = {
            'red': self.RED,
            'green': self.GREEN,
            'blue': self.BLUE,
            'yellow': self.YELLOW,
            'magenta': self.MAGENTA,
            'cyan': self.CYAN,
            'white': self.WHITE,
        }

        return switch.get(color, self.RED)

    def reset(self):
        return self.RESET

color_class = Color()

def colorize (text: str, color: str):
    return color + text + color_class.reset()