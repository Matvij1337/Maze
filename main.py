import time as t


from pygame import *
init()
clock = time.Clock()

DISPLAY_SIZE = (700, 500)

FPS = 60

mixer.init()
#mixer.music.load("CAMOrOH.ogg")
#mixer.music.play()

slap = mixer.Sound("slap.ogg")

window = display.set_mode(DISPLAY_SIZE)
display.set_caption("Maze")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (45, 45))
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
        if self.rect.x < DISPLAY_SIZE[0] - 550:
            self.direction = "right"
        if self.rect.x > DISPLAY_SIZE[0] - 65:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, x, y, width, heigth, color):
        super().__init__()
        self.heigth = heigth
        self.width = width
        self.image = Surface((self.width, self.heigth))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.color = color
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

walls = []
walls.append(Wall(30, 20, 650, 20, (144, 198, 124)))
walls.append(Wall(670, 20, 20, 450, (144, 198, 124)))
walls.append(Wall(30, 470, 660, 20, (144, 198, 124)))
walls.append(Wall(30, 20, 20, 450, (144, 198, 124)))
walls.append(Wall(130, 100, 20, 375, (144, 198, 124)))
walls.append(Wall(150, 160, 340, 20, (144, 198, 124)))
walls.append(Wall(240, 100, 150, 70, (144, 198, 124)))
walls.append(Wall(490, 100, 20, 90, (144, 198, 124)))
walls.append(Wall(490, 100, 100, 20, (144, 198, 124)))
walls.append(Wall(580, 100, 20, 100, (144, 198, 124)))
secret_wall = Wall(510, 180, 70, 20, (144, 198, 124))
walls.append(Wall(220, 280, 450, 20, (144, 198, 124)))
walls.append(Wall(220, 370, 380, 20, (144, 198, 124)))
walls.append(Wall(530, 370, 20, 110, (144, 198, 124)))


background = transform.scale(image.load("backgroundmaze.jpg"), DISPLAY_SIZE)
player = Player("ukraine.png", 50, 400, 3)
monster = Enemy(("russia.png"), 450, 50, 2)
secret = GameSprite(("NATO.png"), DISPLAY_SIZE[0] - 175, DISPLAY_SIZE[1] - 375, 0)
final = GameSprite(("EU_union.png"), DISPLAY_SIZE[0] - 150, DISPLAY_SIZE[1] - 100, 0)

score_point = 0
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
                game = False
    if not finish:
        for wall in walls:
            if sprite.collide_rect(player, wall):
                slap.play()
                player.rect.x = 50
                player.rect.y = 400
                score_point += 1

        if sprite.collide_rect(player, monster):
            slap.play()
            player.rect.x = 50
            player.rect.y = 400
            score_point += 1

        window.blit(background, (0, 0))
        player.reset()
        player.update()
        monster.reset()
        monster.update()
        secret.reset()
        final.reset()

        secret_wall.draw()

        for wall in walls:
            wall.draw()

        if score_point == 3:
            break

        if sprite.collide_rect(player, final):
            mixer.music.load("Hymn_Ukraine.ogg")
            mixer.music.play()
            finish = True

        if sprite.collide_rect(player, secret):
            mixer.music.load("Hymn_Ukraine.ogg")
            mixer.music.play()
            finish = True

    display.update()
    clock.tick(FPS)

