import pygame
import pytest

from chickenpy.cells import CellGrid


@pytest.mark.parametrize(
    "topleft_origin, expect",
    [
        ((0, 0), [(0, 0), (22, 0), (44, 0), (0, 22), (22, 22), (44, 22)]),
        ((6, 6), [(6, 6), (28, 6), (50, 6), (6, 28), (28, 28), (50, 28)]),
    ],
    ids=[
        "origin_0_0",
        "origin_6_6",
    ],
)
def test_generate_toplefts_origins(topleft_origin, expect):
    # Create surface
    sprite_px = 16
    s = pygame.Surface((sprite_px, sprite_px))
    # Create CellGrid
    grid = CellGrid(s, nx=3, ny=2, padding_px=6, topleft_origin=topleft_origin)
    get = grid._generate_toplefts()
    assert get == expect
