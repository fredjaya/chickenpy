import pygame as pg

# Assets
ground = pg.image.load("assets/Tilemap_Flat.png")

pg.init()

# Game window opts
window = pg.display.set_mode(size=(640, 480))
pg.display.set_caption(title="chickenpy")

window.blit(source=ground, dest=ground.get_rect())
pg.display.update()

# Main game loop
run_game_loop = True
while run_game_loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_game_loop = False

pg.quit()