from random import Random
from random import shuffle
import requests

def dice_roll(rolls):
	for n in range(rolls):
		rng = random.Random()
		dice = rng.randrange(1,7)
		print(dice)

def balls():
	lst = ["red_ball", "blue_ball"]
	print("The original list is:", lst)
	shuffle(lst)
	lst.pop()
	print(lst[0])
	# can also use a random number in order to pop an index value.

def coin_flip(flips):
	for n in range(flips):
		lst = ["heads", "tails"]
		shuffle(lst)
		lst.pop()
		print(lst[0])
	# bonus: see if you can count runs.

def request():
	f = requests.get("http://www.py4inf.com/code/romeo-full.txt")
	file_ = f.text
	file_ = file_.split("\n")
	for line in file_:
		if 'love' in line:
			print(line)