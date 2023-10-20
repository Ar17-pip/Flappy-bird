from pygame import *

window = display.set_mode((1230, 600))
display.set_caption("Flappi bird")
blackground = transform.scale(image.load("background.png"), (1230, 600))

clock = time.Clock()
FPS = 60





class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_image_x, player_image_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_image_x, player_image_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        self.image_x = player_image_x
        self.image_y = player_image_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:     
            self.rect.y -= self.speed
            

class Pillar_Sprite(GameSprite):
    def update(self):
        self.rect.x -= self.speed




bird = Player("bird2.png", 80, 350, 10, 100, 50)

game = True
while game:
    window.blit(blackground, (0,0))
    bird.reset()
    bird.update()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)