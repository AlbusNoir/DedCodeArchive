'''
Pygame Tutorial from freeCodeCamp.org
'''
import pygame
from pygame import mixer
import random
import math

# window
pygame.init()

screen = pygame.display.set_mode((800, 600))

# title icon bg
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Imgs/ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Imgs/background.png")

# sound
bg_music = mixer.music.load("sounds/background.wav")
mixer.music.play(-1)                            # -1 plays on loop
mixer.music.set_volume(0.1)


# player
player_icon = pygame.image.load("Imgs/player.png")
playerX = 370
playerY = 480
playerX_change = 0

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# game over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

# enemy
enemy_icon = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy_icon.append(pygame.image.load("Imgs/enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)


# bullet
# ready - not shown on screen
# fire = shown, changing Y
bullet_icon = pygame.image.load("Imgs/bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 7
bullet_state = "ready"


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(text, (200, 250))
    

def player(x, y):
    screen.blit(player_icon, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_icon[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_icon, (x + 16, y + 10))  # center bullet at center of ship


def is_collision(enemyX, enemyY, targetX, targetY):
    # d = sqrt((x1-x2)^2 + (y1-y2)^2)
    distance = math.sqrt((math.pow(enemyX - targetX, 2)) + (math.pow((enemyY - targetY), 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:    # only fire if ready
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("sounds/laser.wav")
                    bullet_sound.set_volume(0.1)
                    bullet_sound.play()
                    bulletX = playerX          # set initial x to playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0

    # update
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # boundaries
    playerX += playerX_change
    if playerX >= 736:                         # ship is 64x64, so 800-64=736
        playerX = 736
    if playerX < 0:
        playerX = 0

    # enemy movement
    for i in range(num_of_enemies):

        # game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000               # idk just put it off screen
            playerY = 2000                     # yeet
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]

        # collision checks
        collision_bullet = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision_bullet:
            collision_sound = mixer.Sound("sounds/explosion.wav")
            collision_sound.set_volume(0.1)
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

        collision_player = is_collision(enemyX[i], enemyY[i], playerX, playerY)
        if collision_player:
            collision_sound = mixer.Sound("sounds/explosion.wav")
            collision_sound.set_volume(0.1)
            collision_sound.play()
            playerY = 2000                      # yeet
            game_over_text()
            break

    # bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY < 0:
        bulletY = 480
        bullet_state = "ready"

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
