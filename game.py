import pygame
from pygame.locals import *
import time
import snake

def end_game(message):
    font = pygame.font.Font(None, 22)
    text = font.render("GAME OVER..." + message, 1, (250, 0, 0))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

def draw_snake():
    [pygame.draw.rect(background, snake.color, snake.get_rect(i), 0) for i,_ in enumerate(snake.body)]

def move_snake():
    # Clear screen, move the snake, re-draw the snake
    background.fill((0, 0, 0))
    snake.move()
    draw_snake()

def check_collision():
    # Check if snake has gone off screen, hit itself, or eaten food
    # Returns true if the collision would cause the game to end
    if snake.did_collide_with_wall(background.get_size()):
        end_game("You left the map!")
        return True
    elif snake.did_collide_with_body():
        end_game("You collided with your body!")
        return True
    elif snake.did_collide_with_food():
        snake.add_tail()
        ### update score
        return False
    return False

# Initialize pygame
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
draw_snake()

# Draw screen
screen.blit(background, (0, 0))
pygame.display.flip()

# Game loop
gameover = False
loop = True
while loop:
    if not gameover:
        # Listen for user input
        for event in pygame.event.get():
            if event.type == QUIT:
                condition = False
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    snake.move_right()
                if event.key == K_LEFT:
                    snake.move_left()
                if event.key == K_UP:
                    snake.move_up()
                if event.key == K_DOWN:
                    snake.move_down()
        move_snake();
        if check_collision():
            gameover = True

        # Draw screen
        screen.blit(background, (0, 0))
        pygame.display.flip()
        time.sleep(0.1)
    else:
        # Necessary to keep game from looping forever
        # and requiring a crash to exit
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False
