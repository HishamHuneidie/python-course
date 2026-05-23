from .color import color
from typing import Callable


class MenuItem:
    def __init__(self, index: int, key: str, text: str, callback: Callable=None):
        self.index = index
        self.key = key
        self.text = text
        self.callback = callback

    def __str__(self):
        return color(f"[{self.index}]", 'magenta') + f" {self.text}"

    def execute(self, *args):
        if self.callback is None:
            return None

        return self.callback(*args)


class Menu:
    def __init__(self, items: list=[]):
        self.items = items
        self._update_indexes()

    def append(self, item: MenuItem):
        self.items.append(item)
        self._update_indexes()
        return self

    def remove(self, index: int):
        self.items = [item for item in self.items if item.index != index]
        self._update_indexes()
        return self

    def list(self):
        return self.items

    def get(self, index: int):
        if not self.has(index):
            raise IndexError

        return self.items[index]

    def has(self, index: int):
        for i, item in enumerate(self.items):
            if i == index: return True

        return False

    def execute(self, index: int, *args):
        if not self.has(index):
            raise IndexError

        return self.items[index].execute(*args)

    def _update_indexes(self):
        for i, item in enumerate(self.items):
            item.index = i
            self.items[i] = item

    def __str__(self):
        return "\n".join(str(item) for item in self.items)

    def __len__(self):
        return len(self.items)


