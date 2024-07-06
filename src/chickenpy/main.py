from functools import singledispatch
from typing import Optional

ItemTypes = list[str | type] | str


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

    def __repr__(self):
        return "WholeChicken"


def list_as_str(l: list) -> str:
    return ", ".join(l)


class Inventory:
    def __init__(self, size: int = 10) -> None:
        self._size = size
        self._items = []

    def store(self, items: ItemTypes) -> Optional[str]:
        if len(self) + len(items) == self._size:
            return "Not enough space in the inventory!"
        self._items += items
        print(f"Added {list_as_str(items)} to inventory.")

    def remove(self, item: str) -> Optional[str]:
        # Support item: list?
        if item not in self._items:
            return f"{item} does not exist!"
        self._items.remove(item)
        print(f"Removed {item} from inventory.")

    def use(self, item: str, method) -> None:
        if item not in self._items:
            return f"{item} does not exist!"

    @property
    def inspect(self) -> str:
        return list_as_str(self._items) if self._items else "Inventory is empty."

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return self.inspect
