import math

import pygame

from chickenpy.drawable import Drawable


class Cell(Drawable):
    def __init__(self, surface, x=0, y=0, scale=1):
        super().__init__(surface, x, y, scale)
        self._occupied = False

    @property
    def occupied(self):
        return self._occupied

    @occupied.setter
    def occupied(self, occupation: bool):
        self._occupied = occupation


class CellGrid:
    def __init__(
        self,
        surface: pygame.Surface,
        nx: int,
        ny: int,
        padding_px,
        topleft_origin: tuple[int, int] = (0, 0),
    ):
        self.surface = surface
        self.nx = nx
        self.ny = ny
        self.padding_px = padding_px
        self.topleft_origin = topleft_origin  # start of very first cell
        self.cells = self._generate_cells()
        self.cell_centers = self._rect_centers()

    def _generate_toplefts(self) -> list[tuple[int, int]]:
        """
        Generate a list of (x, y) topleft coordinates for each Cell in the grid.

        Supports only square sprites.

        Returns:
            List of (x, y) tuples representing the topleft of each cell.
        """
        origin_x, origin_y = self.topleft_origin
        sprite_px = self.surface.get_width()
        step = sprite_px + self.padding_px

        return [
            (origin_x + x * step, origin_y + y * step)
            for y in range(self.ny)
            for x in range(self.nx)
        ]

    def _generate_cells(self):
        all_toplefts = self._generate_toplefts()
        return [Cell(surface=self.surface, x=x, y=y) for x, y in all_toplefts]

    def draw_cells(self, surface: pygame.Surface):
        for cell in self.cells:
            cell.draw(surface)

    def _all_rects(self) -> list:
        return [cell.rect for cell in self.cells]

    def _rect_centers(self) -> list:
        # To allow snapping to Cells
        rects = self._all_rects()
        return [rect.center for rect in rects]

    def closest_center(self, mouse_pos: tuple) -> int:
        # return the rect center of the Cell that is closest to the pos
        dists = [math.dist(mouse_pos, center_pos) for center_pos in self.cell_centers]
        idx = dists.index(min(dists))
        return self.cell_centers[idx]
