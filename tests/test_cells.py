import pytest

from chickenpy.cells import Cells


@pytest.fixture
def simple_cells():
    return Cells(size_px=96, padding_px=6, nx=5, ny=5)


def test_generate_positions(simple_cells):
    sc = simple_cells
    poss = sc.generate_positions()
    assert isinstance(poss, list)
    assert len(poss) == sc.nx * sc.ny


@pytest.mark.parametrize("nx", [2, 4, 6])
@pytest.mark.parametrize("ny", [2, 4, 6])
def test_occupied_get(nx, ny):
    sc = Cells(96, 6, nx, ny)
    # inits an empty list same size as n cells
    assert sc.occupied == [False] * nx * ny
    assert len(sc.occupied) == len(sc.positions)


# def test_occupied_set():
#    sc = Cells(96, 6, nx, ny)
#    # inits an empty list same size as n cells
#    assert sc.occupied == [0] * nx * ny
#    assert len(sc.occupied) == len(sc.positions)
