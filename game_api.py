import pygame
from pygame.locals import *
import time
import snake
import random
import collision
from block import Block

class Game:
    def __init__(self):
        self.score = 0
        # Initialize pygame
        pygame.init()
        self.init_screen()
        self.init_snake()
        self.init_food()
        self.gameover = False

    def init_screen(self):
        # Display
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption('Snake')
        # Background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        # Score
        self.draw_score()
        # Draw screen
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def init_snake(self):
        # Initialize snake
        self.snake = snake.Snake()
        self.draw_snake()

    def init_food(self):
        # Initialize food
        self.create_food()
        self.draw_food_to_screen()

    def draw_score(self):
        font = pygame.font.Font(None, 22)
        text = font.render("Score: " + str(self.score), 1, (0, 0, 250))
        textpos = text.get_rect()
        self.background.blit(text, textpos)

    def end_game(self, message):
        font = pygame.font.Font(None, 22)
        text = font.render("GAME OVER..." + message, 1, (250, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        textpos.centery = self.background.get_rect().centery
        self.background.blit(text, textpos)

    def draw_snake(self):
        # Draws snake onto the background
        self.background.fill((0, 0, 0))
        [pygame.draw.rect(self.background, self.snake.color, self.snake.get_rect(i), 0) for i,_ in enumerate(self.snake.body)]

    def draw_screen():
        return 0

    def check_collision(self):
        # Check if snake has gone off screen, hit itself, or eaten food
        # Returns true if the collision would cause the game to end
        if collision.did_collide_with_wall(self.snake, self.background.get_size()):
            self.end_game("You left the map!")
            return True
        elif collision.did_collide_with_body(self.snake):
            self.end_game("You collided with your body!")
            return True
        elif collision.did_collide_with_food(self.snake, self.food):
            self.snake.add_tail()
            self.create_food()
            self.draw_food_to_screen()
            self.score += 10
            return False
        return False

    def create_food(self):
        f = Block(0, 0)
        left = random.randrange(0, self.background.get_size()[0] - f.width, 10)
        top = random.randrange(0, self.background.get_size()[1] - f.height, 10)
        f.left = left
        f.top = top
        f.color = (250, 0, 0)
        self.food = f

    def draw_food_to_screen(self):
        rect = Rect(self.food.left, self.food.top, self.food.width, self.food.height)
        pygame.draw.rect(self.background, self.food.color, rect, 0)

    def play(self, direction):
    	if direction == "left":
    		self.snake.move_left()
    	elif direction == "right":
    		self.snake.move_right()
    	elif direction == "up":
    		self.snake.move_up()
    	elif direction == "down":
    		self.snake.move_down()

    	self.snake.move()
    	self.draw_snake()
    	self.draw_food_to_screen()
    	self.draw_score()
    	if self.check_collision():
    		self.gameover = True

    	# Draw background onto the screen
    	self.screen.blit(self.background, (0, 0))
    	pygame.display.flip()
    	# time.sleep(0.05)

    def get_obstacles(self):
        obstacles = []
        # check to left
        self.fake_move_left()
        if self.check_collision():
            obstacles.append(1)
        else:
            obstacles.append(0)
        self.fake_move_right()
        # check above
        self.fake_move_up()
        if self.check_collision():
            obstacles.append(1)
        else:
            obstacles.append(0)
        self.fake_move_down()
        # check to right
        self.fake_move_right()
        if self.check_collision():
            obstacles.append(1)
        else:
            obstacles.append(0)
        self.fake_move_left()
        # check to bottom
        self.fake_move_down()
        if self.check_collision():
            obstacles.append(1)
        else:
            obstacles.append(0)
        self.fake_move_up()
        return obstacles

    def fake_move_left(self):
        self.snake.move_left()
        self.snake.move()

    def fake_move_up(self):
        self.snake.move_up()
        self.snake.move()

    def fake_move_right(self):
        self.snake.move_right()
        self.snake.move()

    def fake_move_down(self):
        self.snake.move_down()
        self.snake.move()
