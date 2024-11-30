import pygame
import globals
import player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            size=(globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT)
        )
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption(title="ChickenPy")
        self.player = player.Player()

    def run(self):
        while self.running:
            self.update()
            self.draw()
            self.blit_player()
            pygame.display.flip()
            self.clock.tick(60)
        self.quit()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pygame.display.update()

    def draw(self):
        self.screen.fill("lightblue")

    def blit_player(self):
        self.player.blit(self.screen)

    def quit(self):
        pygame.quit()
