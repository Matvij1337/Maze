import time

from pygame import *
init()
clock = time.Clock()

DISPLAY_SIZE = (700, 500)

FPS = 60

window = display.set_mode(DISPLAY_SIZE)
display.set_caption("Maze")
background = transform.scale(image.load("backgroundmaze.jpg"), DISPLAY_SIZE)
#sprite1 = transform.scale(image.load("ukraine.png"))


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
                game = False
    window.blit(background, (0, 0))


    display.update()
    clock.tick(FPS)