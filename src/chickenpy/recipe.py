from chickenpy.inventory import Inventory
from typing import Union

class Recipe:
    def __init__(self, name: Union[str,type], ingredients: list[Union[str|type]]):
        self.name = name
        self.ingredients = ingredients
    
    def cook(self, inventory: Inventory) -> Union[str,type]:
        for i in self.ingredients:
            if not inventory._check_item(i):
                return f"There is not enough of {i}."
            inventory.remove_item(i)
            inventory.add_item(self.name)
        

roux = Recipe("roux", ["butter", "flour"])