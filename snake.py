from pygame.locals import *
from block import Block

class Snake:
    def __init__(self):
        self.body = [Block(10, 20), Block(20, 20), Block(20, 30)]
        self.color = (0, 250, 0)
        self.dx = 10
        self.dy = 0

    def move(self):
        for i, _ in enumerate(self.body[:-1]):
            self.body[i].left = self.body[i+1].left
            self.body[i].top = self.body[i+1].top
        self.body[-1].left += self.dx
        self.body[-1].top += self.dy

    def get_rect(self, i):
        body = self.body
        return Rect(body[i].left, body[i].top, body[i].width, body[i].height)

    def add_block(self):
        lastblock = self.body[-1]
        self.body.insert(0, Block(lastblock.left, lastblock.top))
