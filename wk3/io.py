r = open("new.txt", "r")
f = open("reverse.txt", "w")
text = r.readlines()
text = text[::-1]
for item in text:
	f.write(item + "\n") 
f.close()
r.close()

