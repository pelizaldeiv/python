#!/bin/bash
import random
guess = input("Pick a number between 1 and 10: ")
rando = random.randrange(1,10,1)
if guess == rando:
	print("You guessed {}, and the number was {}".format(guess,rando))
	print("Success")
else:
	print("You guessed {}, but the number was {}".format(guess,rando))

