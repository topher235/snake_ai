from pygame.locals import *
from block import Block

class Snake:
    def __init__(self):
        # The tail is the first index, the head is the last index
        self.body = [Block(10, 20), Block(20, 20), Block(20, 30)]
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
        self.dx = -10
        self.dy = 0

    def move_up(self):
        self.dx = 0
        self.dy = -10

    def move_right(self):
        self.dx = 10
        self.dy = 0

    def move_down(self):
        self.dx = 0
        self.dy = 10

    def get_rect(self, i):
        # Return a rectangle of the desired body
        body = self.body
        return Rect(body[i].left, body[i].top, body[i].width, body[i].height)

    def add_tail(self):
        # Add a tail block to beginning of list / end of snake
        self.body.insert(0, self.next_tail)

    def did_collide_with_wall(self, screensize):
        screen_w = screensize[0]
        screen_h = screensize[1]
        head = self.body[-1]
        # Check left side of screen
        if head.left+head.width < 0:
            return True
        # Check top of screen
        if head.top+head.height < 0:
            return True
        # Check right side of screen
        if head.left+head.width > screen_w:
            return True
        # Check bottom of screen
        if head.top+head.height > screen_h:
            return True
        # Snake is still in the play area
        return False

    def did_collide_with_body(self):
        # Not yet implemented
        return False

    def did_collide_with_food(self, food):
        head = self.body[-1]
        head_xpos = head.left + (0.5 * head.width)
        head_ypos = head.top + (0.5 * head.height)
        if head_xpos >= food.left and head_xpos <= food.left+food.width and head_ypos >= food.top and head_ypos <= food.top+food.height:
            return True
        return False
