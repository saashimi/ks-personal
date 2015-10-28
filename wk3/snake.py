# Writes files if the word "snake" is in the line.

f_r = open("snake.txt", "r")
f_w = open("new_snake.txt", "w")
for line in f_r:
	if "snake" in line:
		f_w.write(line)

print("wrote stuff!")
f_w.close()
f_r.close()


