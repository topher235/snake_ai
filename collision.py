import snake

def did_collide_with_wall(snake, screensize):
    screen_w = screensize[0]
    screen_h = screensize[1]
    head = snake.body[-1]
    # Check left side of screen
    if head.left+head.width <= 0:
        return True
    # Check top of screen
    if head.top+head.height <= 0:
        return True
    # Check right side of screen
    if head.left+head.width > screen_w:
        return True
    # Check bottom of screen
    if head.top+head.height > screen_h:
        return True
    # Snake is still in the play area
    return False

def did_collide_with_body(snake):
    head = snake.body[-1]
    head_x = head.left + (0.5 * head.width)
    head_y = head.top + (0.5 * head.height)
    for _,block in enumerate(snake.body[:-1]):
        if head_x >= block.left and head_x <= block.left+block.width and head_y >= block.top and head_y <= block.top+block.height:
            return True
    return False

def did_collide_with_food(snake, food):
    head = snake.body[-1]
    head_xpos = head.left + (0.5 * head.width)
    head_ypos = head.top + (0.5 * head.height)
    if head_xpos >= food.left and head_xpos <= food.left+food.width and head_ypos >= food.top and head_ypos <= food.top+food.height:
        return True
    return False
