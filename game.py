import pygame
from pygame.locals import *
import time
import snake

def draw_snake():
    pygame.draw.rect(background, snake.color, snake.get_rect(), 0)

def move_snake():
    background.fill((0, 0, 0))
    snake.move()
    pygame.draw.rect(background, snake.color, snake.get_rect(), 0)

pygame.init()

# Display
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Snake')

# Background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))

# Initialize snake
snake = snake.Snake()
pygame.draw.rect(background, snake.color, snake.get_rect(), 0)

# Draw screen
screen.blit(background, (0, 0))
pygame.display.flip()

condition = True
while condition:
    move_snake();
    # Listen for user input
    for event in pygame.event.get():
        if event.type == QUIT:
            condition = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                snake.dx = 10
                snake.dy = 0
            if event.key == K_LEFT:
                snake.dx = -10
                snake.dy = 0
            if event.key == K_UP:
                snake.dx = 0
                snake.dy = -10
            if event.key == K_DOWN:
                snake.dx = 0
                snake.dy = 10
    # Draw screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
    time.sleep(0.1)
