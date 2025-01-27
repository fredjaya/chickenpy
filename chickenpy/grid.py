from chickenpy.globals import PIXEL_SIZE


class Grid:
    """2D grid of positions that serves as the background and storage of item
    rects.

    The grid is initialised with cell size, padding, and dimensions (nx, ny).
    It then generates and stores the positions for each cell.

    TODO:
        - attribute to show occupied/empty cells
        - method to return first empty cell
        - create Cell class which inherits from Item class with surf/rect/pos
    """

    def __init__(self, size_px, padding_px, nx, ny):
        self.size_px = size_px
        self.padding_px = padding_px
        self.nx = nx
        self.ny = ny
        self.positions = self.generate_grids()

    def generate_grids(self):
        """Generate a list of cell positions.

        Creates a grid of 2D cell positions based on dimensions (nx, ny).

        """
        pos_x = [(x * self.size_px) + self.padding_px for x in range(self.nx)]
        pos_y = [
            (y * self.size_px) + self.padding_px + PIXEL_SIZE for y in range(self.ny)
        ]
        return [(x, y) for y in pos_y for x in pos_x]
