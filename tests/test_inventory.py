import pytest

from chickenpy.main import Inventory


def test_inventory_init_default():
    inv = Inventory()
    assert inv._items == []
    assert inv._size == 10


@pytest.mark.parametrize(
    "items,expect", [("x", ["x"]), (["x"], ["x"]), (["y", "z"], ["y", "z"])]
)
def test_inventory_store(items, expect):
    inv = Inventory()
    inv.store(items)
    got = inv._items
    assert got == expect


def test_inventory_remove():
    inv = Inventory()
    inv.store(["x", "y"])
    inv.remove("x")
    assert inv._items == ["y"]


@pytest.mark.xfail(reason="Inventory.remove() only supports a single str")
def test_inventory_remove_list():
    inv = Inventory()
    inv.store(["x", "y"])
    inv.remove(["x"])
    assert inv._items == ["y"]


def test_inventory_store_full():
    inv = Inventory(size=10)
    assert inv.store(["x"] * 10) == "Not enough space in the inventory!"
