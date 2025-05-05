import pygame


class Drawable:
    """
    Class that can be drawn on a pygame.surface at a specified position.
    Use Drawable.load_sprite() to use an e.g. .png
    """

    def __init__(self, surface: pygame.Surface, x: int = 0, y: int = 0, scale: int = 1):
        if scale == 1:
            self.surface = surface

        else:
            width, height = surface.get_size()
            scaled_size = (width * scale, height * scale)
            self.surface = pygame.transform.scale(surface, scaled_size)
        self.rect = self.surface.get_rect(topleft=(x, y))

    @classmethod
    def load_sprite(cls, path: str, x: int = 0, y: int = 0, scale: int = 1):
        surface = pygame.image.load(path).convert_alpha()
        return cls(surface, x, y, scale)

    def draw(self, surface):
        surface.blit(self.surface, self.rect)


# roux = Recipe("roux", ["butter", "flour"])
# bechamel = Recipe("bechamel", ["roux", "milk"])
# mirepoix = Recipe("mirepoix", ["onion", "carrot", "celery"])
# stock = Recipe("stock", ["bones", "mirepoix"])
