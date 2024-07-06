from typing import Optional


class WholeChicken:

    def butcher(self) -> list[str]:
        return [
            "breast",
            "breast",
            "thigh",
            "thigh",
            "drumstick",
            "drumstick",
            "wing",
            "wing",
            "carcass",
        ]

    def roast(self) -> str:
        return "roast_chicken"


class Inventory:
    def __init__(self, items: Optional[list[str] | str] = None, size: int = 10):
        self._items = [] if not items else [items]
        self._size = size

    def store(self, items: str | list[str]):
        if len(self) == self._size:
            print(f"{self.__name__} is full!")
        else:
            self._items += items

    def remove(self, items):
        pass

    @property
    def inspect(self):
        return self._items if self._items else print(f"{self.__name__} is empty!")

    def __len__(self):
        return len(self._items)
