from game_api import Game
import random
import json
import os

if not os.path.exists('./training_data/'):
	os.mkdir('./training_data/')

for i in range(100):
	game = Game()
	directions = ["left", "right", "up", "down"]
	obstacles = []
	while not game.gameover:
		direction = random.randrange(len(directions))
		game.play(directions[direction])
		if not game.gameover:
			obstacles.append(game.get_obstacles())
	
	if not os.path.exists('./training_data/' + str(i)):
		open('./training_data/' + str(i), 'w').close()

	with open('./training_data/' + str(i), 'w') as f:
		json.dump(obstacles, f)
