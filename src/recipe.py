from dataclasses import dataclass
from typing import Union


@dataclass  # Mainly for the free repr
class Recipe:
    name: Union[str, type]
    ingredients: list[Union[str | type]]


class RecipeBook:
    def __init__(self):
        self.recipes: dict[str, Recipe] = RECIPES

    def contents(self):
        print("\n".join(self.recipes.keys()))

    def show_recipe(self, recipe):
        print(self.__getitem__(recipe))

    def __getitem__(self, recipe: str) -> Recipe:
        return self.recipes[recipe]


RECIPES = {
    # aromatics
    "battuto": Recipe("battuto", ["onion", "carrot", "celery"]),
    "soffritto": Recipe("soffritto", ["butter", "battuto"]),
    "mirepoix": Recipe("mirepoix", ["oil", "battuto"]),
    # other
    "roux": Recipe("roux", ["butter", "flour"]),
    "veloute": Recipe("veloute", ["stock", "roux"]),
}
