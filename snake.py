from pygame.locals import *

class Snake:
    def __init__(self):
        self.left = 10
        self.top = 25
        self.width = 10
        self.height = 10
        self.color = (250, 0, 0)
        self.dx = 0
        self.dy = 0

    def move(self):
        self.left += self.dx
        self.top += self.dy

    def get_rect(self):
        return Rect(self.left, self.top, self.width, self.height)
