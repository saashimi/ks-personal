# Contains functions that take integer values of days of the week and return
# their string values, and vice versa.

def day_name(number):
	"""
	Takes an integer and returns its corresponding day of the week. 
	Note: Sunday is integer 0.

	Example:
	--------
	1 --> Monday
	"""
	if number > 6:
		return None
	elif type(day_name) is str:
		return None
	else:
		names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
					"Saturday"]
		named_day = names[number]
		return named_day

def day_num(name):
	"""Takes a named day and returns its corresponding integer number.
	Note: Sunday is integer 0.

	Example:
	--------
	Friday --> 5
	"""
	names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
			"Saturday"]
	if type(name) is int:
		return None
	elif name not in names:
		return None
	else:
		indexed = names.index(name)
		return indexed

def day_add(today, delta):
	"""Calculates what the day of the week will be, x days from now."""
	names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
			"Saturday"]	
	index_today = names.index(today)
	delt_calc = (delta % 7) + index_today
	indexed = names[delt_calc]
	return indexed

def day_name_tests():
	assert day_name(3) == "Wednesday"
	assert day_name(6) == "Saturday"
	assert day_name(42) == None

def day_num_tests():
	assert day_num("Friday") == 5
	assert day_num("Sunday") == 0
	assert day_num(day_name(3)) == 3
	assert day_name(day_num("Thursday")) == "Thursday"

def day_add_tests():
	assert day_add("Monday", 4) ==  "Friday"
	assert day_add("Tuesday", 0) == "Tuesday"

day_name_tests()
day_num_tests()
day_add_tests()