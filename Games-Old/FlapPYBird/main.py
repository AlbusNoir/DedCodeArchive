# From a tutorial
import pygame
import sys
import random

pygame.init()
pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
screen = pygame.display.set_mode((576, 1024))

# vars
GAME_ACTIVE = True
FPS = 120
GRAV = 0.25
BIRD_MOVEMENT = 0
SCORE = 0
HIGH_SCORE = 0

clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.TTF", 40)


def score_display(game_state):
    if game_state == "main_game":
        score_surface = game_font.render(f'Score: {int(SCORE)}', True, (255, 255, 255))  # case to str then to int
        score_rect = score_surface.get_rect(center = (288, 100))
        screen.blit(score_surface, score_rect)
    if game_state == "game_over":
        score_surface = game_font.render(f'Score: {int(SCORE)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (288, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {int(HIGH_SCORE)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center = (288, 850))
        screen.blit(high_score_surface, high_score_rect)


def update_score(SCORE, HIGH_SCORE):
    if SCORE > HIGH_SCORE:
        HIGH_SCORE = SCORE
    return HIGH_SCORE


# scale image to fit screen, convert makes load a bit faster
bg_surface = pygame.transform.scale2x(pygame.image.load("imgs/background-day.png").convert())

floor_surface = pygame.transform.scale2x(pygame.image.load("imgs/base.png").convert())
floor_x_pos = 0


def draw_floor():
    # Create two floors, move 2nd off screen, move both left, move first to right after reaches off screen
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))


# No flap
# bird_surface = pygame.transform.scale2x(pygame.image.load("imgs/bluebird-midflap.png").convert_alpha())
# bird_rect = bird_surface.get_rect(center = (100, 512))


# flap
bird_downflap = pygame.transform.scale2x(pygame.image.load("imgs/bluebird-downflap.png").convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load("imgs/bluebird-midflap.png").convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load("imgs/bluebird-upflap.png").convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100, 512))
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -BIRD_MOVEMENT * 3, 1)
    return new_bird


pipe_surface = pygame.transform.scale2x(pygame.image.load("imgs/pipe-green.png").convert())
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)  # 1.2sec
pipe_height = [400, 600, 800]


def create_pipe():
    random_pipe_height = random.choice(pipe_height)
    bot_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_height))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_height - 300))
    return bot_pipe, top_pipe


def move_pipes(pipes):
    # Take list of pipes, move left, return
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:                   # if pipe bottom is off screen, it's bottom
            screen.blit(pipe_surface, pipe)
        else:                                     # else it's top, so flip it
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    # If bird hits pipe, GO. If bird hits top or bottom, GO.
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        death_sound.play()
        return False

    return True


game_over_surface = pygame.transform.scale2x(pygame.image.load("imgs/message.png").convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288, 512))


flap_sound = pygame.mixer.Sound("sounds/sfx_wing.wav")
flap_sound.set_volume(0.1)
death_sound = pygame.mixer.Sound("sounds/sfx_hit.wav")
death_sound.set_volume(0.1)
score_sound = pygame.mixer.Sound("sounds/sfx_point.wav")
score_sound.set_volume(0.1)
score_sound_countdown = 100

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and GAME_ACTIVE:
                flap_sound.play()
                BIRD_MOVEMENT = 0    # counter GRAV
                BIRD_MOVEMENT -= 12  # allow up move
            if event.key == pygame.K_SPACE and not GAME_ACTIVE:    # game over, reset bird, pipes
                GAME_ACTIVE = True
                pipe_list.clear()
                bird_rect.center = (100, 512)
                BIRD_MOVEMENT = 0
                SCORE = 0

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface, (0, 0))

    # GAME ACTIVE
    if GAME_ACTIVE:
        # bird
        BIRD_MOVEMENT += GRAV  # slowly increment gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += BIRD_MOVEMENT
        screen.blit(rotated_bird, bird_rect)

        # pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        GAME_ACTIVE = check_collision(pipe_list)

        SCORE += 0.01
        score_display("main_game")
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    # END GAME ACTIVE
    else:
        screen.blit(game_over_surface, game_over_rect)
        HIGH_SCORE = update_score(SCORE, HIGH_SCORE)
        score_display("game_over")

    # floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= - 576:
        floor_x_pos = 0
    
    pygame.display.update()
    clock.tick(FPS)  # set fps
