from pygame.locals import *
from block import Block

class Snake:
    def __init__(self):
        # The tail is the first index, the head is the last index
        self.body = [Block(10, 20)]
        self.size = 1
        # Keep track of where the next tail will appear
        self.next_tail = Block(0, 0)
        self.color = (0, 250, 0)
        self.dx = 10
        self.dy = 0

    def move(self):
        # Next tail will appear behind the current tail
        self.next_tail = Block(self.body[0].left, self.body[0].top)
        # Set body position to the next body block to "follow" the head
        for i, _ in enumerate(self.body[:-1]):
            self.body[i].left = self.body[i+1].left
            self.body[i].top = self.body[i+1].top
        # Move the head in the direction of user input
        self.body[-1].left += self.dx
        self.body[-1].top += self.dy

    def move_left(self):
        # Snakes can't go in reverse if longer than 1 block
        if not self.dx == 10 or self.size < 2:
            self.dx = -10
            self.dy = 0

    def move_up(self):
        # Snakes can't go in reverse if longer than 1 block
        if not self.dy == 10 or self.size < 2:
            self.dx = 0
            self.dy = -10

    def move_right(self):
        # Snakes can't go in reverse if longer than 1 block
        if not self.dx == -10 or self.size < 2:
            self.dx = 10
            self.dy = 0

    def move_down(self):
        # Snakes can't go in reverse if longer than 1 block
        if not self.dy == -10 or self.size < 2:
            self.dx = 0
            self.dy = 10

    def get_rect(self, i):
        # Return a rectangle of the desired body part
        body = self.body
        return Rect(body[i].left, body[i].top, body[i].width, body[i].height)

    def add_tail(self):
        # Add a tail block to beginning of list / end of snake
        self.body.insert(0, self.next_tail)
        self.size += 1
