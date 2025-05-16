import pygame

from chickenpy.cells import CellGrid
from chickenpy.drawable import Drawable, Producer
from chickenpy.globals import SCALING_FACTOR, SPRITE_PX, WINDOW_HEIGHT, WINDOW_WIDTH

# basic setup and window
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

# New grids
s = pygame.Surface((SPRITE_PX, SPRITE_PX))
s.fill("grey")
cell_grid = CellGrid(s, nx=3, ny=2, padding_px=6, topleft_origin=(24, 64))


# Example Drawable. Consider creating in drawable.py
carrot = Drawable.load_sprite("assets/sprites/png/carrot.png", scale=SCALING_FACTOR)
drawables = [carrot]

# when an item is clicked and dragged around
selected_item = False

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            start_click = pygame.time.get_ticks()
            # TODO: refactor to drawable container class
            for d in drawables:
                if d.rect.collidepoint(mouse_pos):
                    selected_item = d.rect

        if selected_item and event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            selected_item.center = mouse_pos

        if selected_item and event.type == pygame.MOUSEBUTTONUP:
            # Determine whether you're clicking or moving object
            end_click = pygame.time.get_ticks()
            click_duration = end_click - start_click
            if click_duration < 200 and isinstance(selected_item, Producer):  # ms
                selected_item.activate()
            else:
                # when dropping, snap to closest grid
                mouse_pos = event.pos
                selected_item.center = cell_grid.closest_center(mouse_pos)
                selected_item = False

    display_surface.fill("darkblue")

    # DRAW
    cell_grid.draw_cells(display_surface)

    # TODO: refactor to drawable container class
    for d in drawables:
        d.draw(display_surface)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()
