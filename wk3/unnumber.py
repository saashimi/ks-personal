"""
Strips line numbers from the file.
"""

f_r = open("numbered_snake.txt", "r")
f_w = open("unnumbered_snake.txt", "w")


for line in f_r:
	line = line[4::]
	f_w.write(line)
	
print("Wrote stuff!")

f_r.close()
f_w.close()