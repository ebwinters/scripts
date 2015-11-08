import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA"
r = requests.get(url)

# print(r.content)

soup = BeautifulSoup(r.content)
#print html
# print(soup.prettify())
#find all a tags
soup.find_all("a")
#loop through link tags and print links
# for link in soup.find_all("a"):
# 	print (link.get("href"))
# 	#prints everything with link tag
# 	print (link.text)

#find all div tags with class info
g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
	#print all headers for restaraunts, since h3 is first child of info class
	print (item.contents[0].find_all("a", {"class": "business-name"})[0].text)
	print (item.contents[1].find_all("p", {"class": "adr"})[0].text)
	try:
		print (item.contents[1].find_all("div", {"class": "phones"})[0].text)
	except:
		pass
