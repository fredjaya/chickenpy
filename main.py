import pygame

# globals
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

# basic setup and window
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

# orange box as placeholder
carrot_surf = pygame.Surface((32, 32))
carrot_surf.fill("orange")
carrot_pos = (100, 100)
carrot_rect = carrot_surf.get_rect(topleft=carrot_pos)

# when an item is clicked
selected = False

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if carrot_rect.collidepoint(mouse_pos):
                selected = carrot_rect

        if event.type == pygame.MOUSEBUTTONUP and selected:
            selected = False

        if event.type == pygame.MOUSEMOTION and selected:
            mouse_pos = event.pos
            print(selected)
            print(selected.center)
            print(mouse_pos)
            selected.center = mouse_pos

    display_surface.fill("darkblue")
    display_surface.blit(carrot_surf, carrot_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
