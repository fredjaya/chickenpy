class Item:
    def __init__(self, name, image, start_topleft):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect(start_topleft)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# roux = Recipe("roux", ["butter", "flour"])
# mirepoix = Recipe("mirepoix", ["onion", "carrot", "celery"])
