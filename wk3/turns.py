def turn_clockwise(direction):
	"""
	Inputs a cardinal direction and outputs the next clockwise direction.
	"""
	if direction == "N":
		return("E")
	elif direction == "E":
		return("S")
	elif direction == "S":
		return("W")
	elif direction == "W":
		return("N")
	elif type(direction) is int:
		return(None)
	else:
		return(None)

"""Tests"""
def turn_clockwise_tests():
	assert turn_clockwise("N") == "E"
	assert turn_clockwise("W") == "N"
	assert turn_clockwise(42) == None
	assert turn_clockwise("rubbish") == None 

turn_clockwise_tests()