from typing import Union

from chickenpy.inventory import Inventory


class Recipe:
    def __init__(self, name: Union[str, type], ingredients: list[Union[str | type]]):
        self.name = name
        self.ingredients = ingredients


roux = Recipe("roux", ["butter", "flour"])
mirepoix = Recipe("mirepoix", ["onion", "carrot", "celery"])
