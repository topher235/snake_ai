# from keras.models import Sequential
# from keras.layers import Dense
import json
import os
import numpy as np

# get training data
training_data = []
for _, dirnames, filenames in os.walk('./training_data/'):
	for filename in filenames:
		with open('./training_data/' + filename, 'r') as f:
			array = json.load(f)
			for i in array:
				training_data.append(np.array(i))

# model = Sequential()

# model.add(Dense(units=4, activation='relu', input_dim=4))
# model.add(Dense(units=4, activation='softmax'))

# model.compile(loss='categorical_crossentropy',
# 				optimize='sgd')

