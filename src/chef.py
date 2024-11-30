from typing import Union

from chickenpy.inventory import Inventory
from chickenpy.recipe import Recipe


class Chef:
    def cook(self, recipe: Recipe, inventory: Inventory) -> Union[str, type]:
        for i in recipe.ingredients:
            if not inventory._check_item(i):
                return f"There is not enough {i}."
            inventory.remove_item(i)
        inventory.add_item(recipe.name)
