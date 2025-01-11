from chickenpy.inventory import Inventory
from chickenpy.recipe import RecipeBook


class Chef:
    def __init__(self, recipe_book: RecipeBook):
        self.recipe_book = recipe_book

    def cook(self, recipe: str, inventory: Inventory):
        r = self.recipe_book[recipe]
        # TODO: return list missing ingredients and quantities
        for i in r.ingredients:
            if not inventory._check_item(i):
                return f"There is not enough {i}."
            inventory.remove_item(i)
        inventory.add_item(recipe)
