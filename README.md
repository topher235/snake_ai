# snake_ai
Learn AI development by creating a bot that plays Snake

[Snake wiki](http://gaming.wikia.com/wiki/Snake_(video_game))

## Rules of Snake:
1. A snake can move up, down, left, or right; and its tail will follow
2. A snake cannot go in reverse
3. A snake can eat food to make its tail grow longer
4. A snake will die if it goes off the borders of the screen
5. A snake will die if it collides with any part of its body

## Progress
*6/29/2018* : The snake is now being drawn on the screen and moving *almost* like it should. Currently, it can go in reverse but the tail follows the head as it should. The snake object is now comprised of a list of block objects. Food is populated at random places and the snake grows correctly when it eats food. Wall collision is detected and ends the game. Score keeping has been implemented.

## Future TODO:
1. Revisit the design of game.py -- Probably a better way of organizing logic. For example, take out game loop from Game class
2. Create a collision script to separate collision checking from snake class
3. Explore creating a food class? Maybe not necessary because a food object would simply be a block object with a specific color
4. Refactor duplicate code into methods
