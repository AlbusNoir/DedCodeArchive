'''
Tutorial at pygame.com
'''
import pygame, sys, random, time
from pygame.locals import *

pygame.init()

vec = pygame.math.Vector2                  # 2d object

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")


# player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.image.load("character.png")
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect()

        # movement
        # controls acc/vel along x and y axis
        self.pos = vec((10, 360))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.jumping = False
        self.score = 0

    def move(self):
        # Set acceleration to 0
        # check for key presses: if left, negative acc. If right, positive acc

        self.acc = vec(0, 0.5)             # control for gravity. 1st is horizontal 2nd is vertical
        '''
        The constant value of 0.5 is applied to the player, giving a constant 0.5 vertical acceleration, 
        thus gravity
        '''
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        # motion equation
        # takes into account friction to slow movement and allow deceleration
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # screen wrapping: go through left to pop out on right & vice versa
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # update pos
        self.rect.midbottom = self.pos

    def jump(self):
        # controls jump
        # the below will check to see if a platform collision happened, if yes, allow jump. else, don't
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15

    def cancel_jump(self):
        # cancel jump. allows control over jump height
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def update(self):
        # controls collisions and handles gravity rules
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:                   # ensures that velocity is not 0 unless there is some initial vel
            if hits:                         # basically avoids bug where jump is nullified due to update()
                if self.pos.y < hits[0].rect.bottom:  # checks for y pos at lowest rect.bottom
                    if hits[0].point == True:
                        hits[0].point = False
                        self.score += 1
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        '''
        Create a platform with random width between 50 and 100px
        '''
        self.surf = pygame.Surface((random.randint(50, 100), 12))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH-10),
                                                 random.randint(0, HEIGHT-30)))
        self.moving = True
        self.speed = random.randint(-1, 1)
        self.point = True

    def move(self):
        if self.moving == True:
            self.rect.move_ip(self.speed, 0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH


# fix platform gen
def check(platform, groupies):
    # check for any collisions
    if pygame.sprite.spritecollideany(platform, groupies):
        return True
    else:
        # further check for any near collisions with boundary of 50
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 50) and (abs(platform.rect.bottom - entity.rect.top) <
                                                                       50):
                return True
        C = False

# generate platforms off screen
def plat_gen():
    while len(platforms) < 6:
        width = random.randrange(50, 100)
        p = Platform()
        C = True

        while C:
            p = Platform()
            p.rect.center = (random.randrange(0, WIDTH - width),
                         random.randrange(-50, 0))
            C = check(p, platforms)
        platforms.add(p)
        all_sprites.add(p)


# out of loop set up
P1 = Player()
PT1 = Platform()
# set up PT1 (bottom of screen)
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255, 0, 0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
PT1.moving = False
PT1.point = False

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

# level stuff
for x in range(random.randint(4, 5)):
    C = True
    pl = Platform()
    while C:
        pl = Platform()
        C = check(pl, platforms)
    platforms.add(pl)
    all_sprites.add(pl)


while True:
    P1.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:    # press space - jump
                P1.jump()
        if event.type == pygame.KEYUP:         # release space - cancel jump
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()
                                               # max jump - hold space
    # infinite scrolling screen
    if P1.rect.top <= HEIGHT / 3:              # checks player height to decide when to scroll
        P1.pos.y += abs(P1.vel.y)              # each time player reaches HEIGHT/3 this executes
        for plat in platforms:                 # have to remove negative vel to keep player dynamic
            plat.rect.y += abs(P1.vel.y)       # have to also update everything else on screen
            if plat.rect.top >= HEIGHT:        # if a platform is off screen, kill it
                plat.kill()                    # at its core, this just moves everything down to give the scroll effect

    plat_gen()

    displaysurface.fill((0, 0, 0))
    f = pygame.font.SysFont("Verdana", 20)
    g = f.render(str(P1.score), True, (123, 255, 0))
    displaysurface.blit(g, (WIDTH/2, 10))

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()

    # game over
    if P1.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
            time.sleep(1)
            displaysurface.fill((255, 0, 0))
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
