import pygame
import globals

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(globals.WINDOW_WIDTH,globals.WINDOW_HEIGHT))
        pygame.display.set_caption(title="ChickenPy")
        self.running = True
    
    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.quit()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pygame.display.update()

    def draw(self):
        self.screen.fill('lightblue')

    def quit(self):
        pygame.quit()
