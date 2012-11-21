#!/usr/bin/env python

def guess():
	from random import randint
	computer = randint(1,100)
	player = input("Enter a number (1-100): ")
	i = 0
	while i< 5:
		try:
			player = int(player)
		except:
			print("Error input.")
			break
		if computer == int(player):
			print("Good guess!")
			break
		elif computer < int(player):
			player = input("Too high, Try again: ")
			i += 1
		else:
			player = input("Too low, Try again: ")
			i += 1
	if i == 5:
		print("Game Over. ")

if __name__ == '__main__':
	guess()
