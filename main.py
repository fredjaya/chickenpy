import math

import pygame

from chickenpy.globals import PIXEL_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH
from chickenpy.grid import Grid

# basic setup and window
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

# Set up background grid of item slots
grid_totalsize = 96
grid_padding = 6

grid = Grid(grid_totalsize, grid_padding, 5, 5)

grid_surf_size = grid_totalsize - grid_padding
grid_surf = pygame.Surface((grid_surf_size, grid_surf_size))
grid_surf.fill("grey")
grid_rects = [grid_surf.get_rect(topleft=pos) for pos in grid.positions]
grid_centers = [rect.center for rect in grid_rects]

# yellow box as placeholder
butter_surf = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
butter_surf.fill("yellow")
butter_pos = (100, 100)
butter_rect = butter_surf.get_rect(topleft=butter_pos)

# when an item is clicked and dragged around
selected_item = False


def closest_center(main_rect: pygame.Rect, rects: list[pygame.Rect]) -> int:
    # return the index of the grid that's closest to a single (mouse) position
    dists = [math.dist(main_rect, center_pos) for center_pos in rects]
    return dists.index(min(dists))


# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if butter_rect.collidepoint(mouse_pos):
                selected_item = butter_rect

        if event.type == pygame.MOUSEBUTTONUP and selected_item:
            # when dropping, snap to closest grid
            mouse_pos = event.pos
            grid_idx = closest_center(mouse_pos, grid_centers)
            selected_item.center = grid_centers[grid_idx]
            selected_item = False

        if event.type == pygame.MOUSEMOTION and selected_item:
            mouse_pos = event.pos
            selected_item.center = mouse_pos

    display_surface.fill("darkblue")

    for rect in grid_rects:
        display_surface.blit(grid_surf, rect)

    display_surface.blit(butter_surf, butter_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()
