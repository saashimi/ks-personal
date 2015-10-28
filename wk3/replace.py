def myreplace(old, new, s):
	"""Replace all occurrences of old with new in s."""
	s.split(old)
	a = new.join(s.split(old))
	return a

def my_replace_tests():
	assert myreplace(",", ";", "this, that, and some other thing") == "this; that; and some other thing"
	assert myreplace(" ", "**", "Words will now be separated by stars.") == "Words**will**now**be**separated**by**stars."

my_replace_tests()
