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

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < DISPLAY_SIZE[1] - 65:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < DISPLAY_SIZE[0] - 65:
            self.rect.x += self.speed
        
class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x < DISPLAY_SIZE[0] - 500:
            self.direction = "right"
        if self.rect.x > DISPLAY_SIZE[0] - 65:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed

background = transform.scale(image.load("backgroundmaze.jpg"), DISPLAY_SIZE)
player = Player("ukraine.png", 100, 350, 3)
monster = Enemy(("russia.png"), 500, 70, 2)
final = GameSprite(("NATO.png"), DISPLAY_SIZE[0] - 250, DISPLAY_SIZE[1] - 200, 0)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
                game = False

    window.blit(background, (0, 0))
    player.reset()
    player.update()
    monster.reset()
    monster.update()
    final.reset()

    display.update()
    clock.tick(FPS)