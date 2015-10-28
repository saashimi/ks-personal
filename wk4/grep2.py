import re

def run_grep(expression):
	res = []
	count = 0
	file_ = open("mbox.txt", "r")
	for line in file_:
		line = line.rstrip()
		if re.findall(expression, line):
			number = re.findall(expression, line) # number is a string in a list.
			for item in number:  
				new_num = int(item) # We need to convert these into ints in order 
									# to perform any calculations. 
				res.append(new_num)
				count += 1
	final = sum(res)
	final = final/count	

	print("Count of", expression, "is", count)
	print("Average is", final)

	file_.close()

if __name__ == "__main__":
	expression = 'New Revision: ([0-9.]+)'
	run_grep(expression)
