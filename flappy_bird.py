from pygame import *
from random import *
font.init()
window = display.set_mode((1230, 600))
display.set_caption("Flappi bird")
blackground = transform.scale(image.load("background.png"), (1230, 600))
font1 = font.Font(None, 36)

clock = time.Clock()
FPS = 60





class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_image_x, player_image_y, player_speed_down):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_image_x, player_image_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        self.image_x = player_image_x
        self.image_y = player_image_y
        self.speed_y = player_speed_down
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        self.speed_y += 0.3
        self.rect.y += self.speed_y
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE] and self.rect.y > 0:     
            self.rect.y -= self.speed
            self.speed_y = 2
            

class Pillar_Sprite(GameSprite):
    def update(self):
        self.rect.x -= self.speed


birds = sprite.Group()
bird1 = Player("bird1.png", 80, 350, 20, 80, 60, 2)

birds.add(bird1)




Shag_x = 1230
Shag_x2 = 1230
pillars = sprite.Group()
pillars2 = sprite.Group()
for i in range(100):
    Shag_plus_x= randint(200, 400)
    Shag_x += Shag_plus_x
    Shag_y = randint(350,550)
    pillar = Pillar_Sprite("pillar.png", Shag_x, Shag_y, 2, 140, 280, 2)
    pillars.add(pillar)
for i in range(100):
    Shag_plus_x2= randint(400, 600)
    Shag_x2 += Shag_plus_x2
    Shag_y2 = randint(-200, -50)
    pillar2 = Pillar_Sprite("pillar3.png", Shag_x2, Shag_y2, 2, 140, 280, 2)
    pillars2.add(pillar2)
finish = False
bg_x = 0
km = 0
game = True
while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    if finish != True:
        window.blit(blackground, (bg_x, 0))
        window.blit(blackground,(bg_x +1230, 0))
        bg_x -= 2
        if bg_x == -1230:
            bg_x = 0

        birds.draw(window)
        birds.update()
        pillars.update()
        pillars.draw(window)
        pillars2.update()
        pillars2.draw(window)
        km += 0.1
        x = round(km)
        sh= font1.render("счёт: "+ str(x), True, (255, 255, 255))
        window.blit(sh, (80, 40))  
        if sprite.groupcollide(birds, pillars, False, False) or sprite.groupcollide(birds, pillars2, False, False):
            
            finish = True
        
            

        

        display.update()
        clock.tick(FPS)