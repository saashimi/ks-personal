"""
Inserts line numbers with the format "0001" into the file
"""
f_r = open("snake.txt", "r")
f_w = open("numbered_snake.txt", "w")


linum = 1 # line number
for line in f_r:
	f_w.write(str(linum).zfill(4) + " " + line) # Adds leading zeroes
	linum += 1 # Adds one to the line number

print("Wrote stuff!")

f_r.close()
f_w.close()