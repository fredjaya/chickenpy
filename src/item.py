import pygame


class Item:
    """
    For tilesets only, assumes sprites are squares
    """

    def __init__(
        self,
        name: str,
        image: str,
        sprite_size_px: float,
        tileset_column: int,
        tileset_row: int,
    ):
        self.name = name
        self.tileset = pygame.image.load(image)
        self.sprite_size_px = sprite_size_px
        self.tileset_column = tileset_column
        self.tileset_row = tileset_row

    def get_left_top(self):
        return (
            self.sprite_size_px * (self.tileset_column - 1),
            self.sprite_size_px * (self.tileset_row - 1),
        )


# carrot - 7x24, 16x16 px
