import pygame


class Drawable:
    def __init__(self, surface: pygame.Surface, x: int = 0, y: int = 0):
        self.surface = surface
        self.rect = self.surface.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.surface, self.rect)


# roux = Recipe("roux", ["butter", "flour"])
# bechamel = Recipe("bechamel", ["roux", "milk"])
# mirepoix = Recipe("mirepoix", ["onion", "carrot", "celery"])
# stock = Recipe("stock", ["bones", "mirepoix"])
