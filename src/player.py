import pygame


class Player:
    def __init__(self):
        self.tileset = pygame.image.load("assets/Pawn_Purple.png")
        self.position = pygame.math.Vector2(96, 96)
        self.rectangle = pygame.Rect(0, 0, 128, 128)

    def blit(self, surface: pygame.Surface):
        surface.blit(self.tileset, self.position, self.rectangle)
