lst = [1,1,0,0,0,0,1,1,1,1,1]


current_run = 1
max_run = 1
for item in range(len(lst)-1):
	if lst[item] == lst[item + 1]:
		current_run += 1
	else:
		current_run = 0
	if current_run > max_run:
		max_run = current_run	 

print(current_run)
print(max_run)


"""
current_run = 0
max_run = 0
for item in lst:
	if item == item +1:
		current_run += 1
	else:
		current_run = 0

if current_run > max_run:
	max_run = current_run	 

print(current_run)
print(max_run)
"""