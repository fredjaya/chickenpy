import pygame
import globals
import player
import inventory


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            size=(globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT)
        )
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption(title="ChickenPy")
        self.play_bgm()
        self.player = player.Player(self.screen)
        self.inventory = inventory.Inventory(self.screen)

    def run(self):
        while self.running:
            self.update()
            self.draw()
            self.player.blit()
            self.player.input()
            self.inventory.draw()
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

    def play_bgm(self):
        pygame.mixer.init()
        pygame.mixer.music.load("assets/el_bosque_gris.mp3")
        pygame.mixer.music.play(1, 0.0, 3000)

    def quit(self):
        pygame.quit()
