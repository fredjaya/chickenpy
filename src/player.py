import pygame


class Player:
    def __init__(self, screen: pygame.surface):
        self.tileset = pygame.image.load("assets/Pawn_Purple.png")
        self.position = pygame.math.Vector2(96, 96)
        self.rectangle = pygame.Rect(0, 0, 128, 128)
        self.screen = screen

    def blit(self):
        self.screen.blit(self.tileset, self.position, self.rectangle)

    def input(self):
        keys = pygame.key.get_pressed()
        px_move = 5
        if keys[pygame.K_a]:
            self.position.x -= px_move
        if keys[pygame.K_d]:
            self.position.x += px_move
        if keys[pygame.K_w]:
            self.position.y -= px_move
        if keys[pygame.K_s]:
            self.position.y += px_move
