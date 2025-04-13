import time

from pygame import *
init()
clock = time.Clock()

DISPLAY_SIZE = (700, 500)

FPS = 60

mixer.init()
mixer.music.load("CAMOrOH.ogg")
mixer.music.play()

window = display.set_mode(DISPLAY_SIZE)
display.set_caption("Maze")

class Gamespite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
     window.blit(self.image, (self.rect.x, self.rect.y))

background = transform.scale(image.load("backgroundmaze.jpg"), DISPLAY_SIZE)
player = Gamespite(("ukraine.png"), 100, 350, 3)
monster = Gamespite(("russia.png"), 500, 70, 2)
final = Gamespite(("NATO.png"), DISPLAY_SIZE[0] - 250, DISPLAY_SIZE[1] - 200, 0)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
                game = False
    window.blit(background, (0, 0))
    player.reset()
    monster.reset()
    final.reset()
    display.update()
    clock.tick(FPS)