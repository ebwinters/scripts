import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/los-angeles-ca/coffee-shops"
r = requests.get(url)
soup = BeautifulSoup(r.content)
# print (soup.prettify())

# for link in soup.find_all("a"):
# 	print (link.text)
g_data = soup.find_all("div", {"class":"info"})
for item in g_data:
	print (item.contents[0].find_all("a", {"class":"business-name"})[0].text)
	print (item.contents[1].find_all("p", {"class":"adr"})[0].text)
