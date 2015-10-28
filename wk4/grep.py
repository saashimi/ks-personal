import re

def run_grep(expression):
	count = 0
	file_ = open("mbox.txt", "r")
	for line in file_:
		line = line.rstrip()
		if re.search(expression, line):
			count += 1
	print("Count of", expression, "is", count)

	file_.close()

if __name__ == "__main__":
	expression = input("Enter a regular expression: ")
	run_grep(expression)
