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
butter_surf = pygame.Surface((64, 64))
butter_surf.fill("yellow")
butter_pos = (100, 100)
butter_rect = butter_surf.get_rect(topleft=butter_pos)

# attempt to make grid for item slots
grid_totalsize = 96
grid_padding = 6
grid_x = [(x * grid_totalsize) + grid_padding for x in range(5)]
grid_y = [(y * grid_totalsize) + grid_padding + 64 for y in range(6)]
grid_pos = [(x, y) for y in grid_y for x in grid_x]

grid_surf_size = grid_totalsize - grid_padding
grid_surf = pygame.Surface((grid_surf_size, grid_surf_size))
grid_surf.fill("grey")

# when an item is clicked
selected = False

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if butter_rect.collidepoint(mouse_pos):
                selected = butter_rect

        if event.type == pygame.MOUSEBUTTONUP and selected:
            selected = False

        if event.type == pygame.MOUSEMOTION and selected:
            mouse_pos = event.pos
            selected.center = mouse_pos

    display_surface.fill("darkblue")

    for pos in grid_pos:
        display_surface.blit(grid_surf, pos)
    display_surface.blit(butter_surf, butter_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
