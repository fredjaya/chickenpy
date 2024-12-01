from typing import Union
import pygame
import globals


class Inventory:
    def __init__(self, screen: pygame.surface, slots: int = 8):
        self._items = {}
        self.screen = screen
        self.slots = slots

    def add_item(self, item: Union[str, type], quantity: int = 1):
        self._items[item] = self._items.get(item, 0) + quantity
        print(f"Added {quantity} {item} to inventory.")

    def _check_item(self, item: Union[str, type], quantity: int = 1) -> bool:
        return self._items.get(item, 0) >= quantity

    def remove_item(self, item: Union[str, type], quantity: int = 1):
        if not self._check_item(item, quantity):
            return f"There is not enough {item}."

        self._items[item] -= quantity
        if self._items[item] == 0:
            del self._items[item]

        print(f"Removed {quantity} {item} from inventory.")

    def __repr__(self):
        return f"Inventory({self._items})"

    def draw(self):
        height_px = 64 + 8 + 8
        width_px = (height_px * (self.slots - 1)) + 32
        x_offset = globals.WINDOW_WIDTH / 2 - width_px / 2
        y_offset = globals.WINDOW_HEIGHT - height_px - 16

        """background"""
        pygame.draw.rect(
            surface=self.screen,
            color="gray",
            rect=pygame.Rect(x_offset, y_offset, width_px, height_px),
        )

        """slots"""
        slot_img = pygame.image.load("assets/Carved_Regular.png")
        x_offset += 16
        y_offset += 8
        for _ in range(self.slots):
            pos = pygame.math.Vector2(x_offset, y_offset)
            rect = pygame.Rect(0, 0, 64, 64)
            self.screen.blit(slot_img, pos, rect)
            x_offset += 64 + 8
