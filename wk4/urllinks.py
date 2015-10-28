import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
count = 0
tags = soup('a')
for tag in tags:
   count += 1
   print tag.get('href', None)
print count

