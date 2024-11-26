import random

import pygame

# Initialize pygame
pygame.init()

# Set display window
WIDTH = 600
HEIGHT = 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake!')

# Set FPS and clock
FPS = 20
clock = pygame.time.Clock()

# Set game values
SNAKE_SIZE = 20

head_x = WIDTH // 2
head_y = HEIGHT // 2 + 100

snake_dx = 0
snake_dy = 0

score = 0

# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (211, 211, 211)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)

# Set text
title_text = font.render('~~Snake~~', True, DARKRED)
title_text_rect = title_text.get_rect()
title_text_rect.center = (WIDTH // 2, HEIGHT // 2)

score_text = font.render('Score: '+ str(score), True, DARKGREEN)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10, 10)

game_over_text = font.render('GAMEOVER', True, RED, DARKGREEN)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WIDTH // 2, HEIGHT // 2)

continue_text = font.render('Press any key to play again', True, RED, DARKGREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WIDTH // 2, HEIGHT // 2 + 64)

# Set sounds and music
pick_up_sound = pygame.mixer.Sound('assets/pick_up_sound.wav')
pick_up_sound.set_volume(.05)

# Set images ( in this case, use simple rects... so just create their coordinates )
# For a rectangle you need ( top-left x, top-left y, width, height )
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

body_coords = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1 * SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE


    # Update the x,y position of the snakes head and make a new coordinate
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    # Check for collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()

        # Move the apple randomly and update the coordinates
        apple_x = random.randint(0, WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

    # Update HUD
    score_text = font.render('Score: ' + str(score), True, DARKGREEN)

    # Fill the screen
    display_surface.fill(WHITE)

    # Blit HUD
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(score_text, score_text_rect)

    #Blit assets
    # Still need to do the body
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

    # Update the screen and clock
    pygame.display.flip()
    clock.tick(FPS)

# End game
pygame.quit()