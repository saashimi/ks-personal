"""def binarySearch(list_, item):
	if len(list_) == 0:
    	return False
	else:
    	midpoint = len(alist) // 2
    	if alist[midpoint]==item:
      		return item
    	else:
      		if item < list_[midpoint]:
        		return binarySearch(list_[:midpoint], item)
      	else:
        	return binarySearch(list_[midpoint+1:], item)
"""
	

def search_list(list_, value):
	for item in list_:
		if item <= value:
			return search(list_, item)
		else:
			return item
		