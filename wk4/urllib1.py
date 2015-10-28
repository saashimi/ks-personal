import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
"""
tags = soup('a')
for tag in tags:
    print tag.get('href', None)
"""
#print(soup.get_text())

count = 0
for char in soup:
	while count < 1:
		count += 1
		print char
print count
		
