from typing import Union

class Inventory:
    def __init__(self):
        self._items = {}

    def add_item(self, item: Union[str, type], quantity: int = 1):
        self._items[item] = self._items.get(item, 0) + quantity
        print(f"Added {quantity} {item} to inventory.")

    def _check_item(self, item: Union[str, type], quantity: int = 1) -> bool:
        return self._items.get(item, 0) >= quantity
    
    def remove_item(self, item: Union[str ,type], quantity: int = 1):
        if not self._check_item(item, quantity):
            return f"There is not enough {item}."
        
        self._items[item] -= quantity
        if self._items[item] == 0:
            del self._items[item]

        print(f"Removed {quantity} {item} from inventory.")

    def __repr__(self):
        return f"Inventory({self._items})"
