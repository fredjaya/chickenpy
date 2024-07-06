import pytest

from chickenpy.main import Inventory


def test_inventory_init_default():
    inv = Inventory()
    assert inv._items == []
    assert inv._size == 10


def test_inventory_init_items():
    inv = Inventory(items="x")
    assert inv._items == ["x"]


@pytest.mark.parametrize(
    "items,expect", [("x", ["x"]), (["x"], ["x"]), (["y", "z"], ["y", "z"])]
)
def test_inventory_store(items, expect):
    inv = Inventory()
    inv.store(items)
    got = inv._items
    assert got == expect
