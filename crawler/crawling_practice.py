import requests
from bs4 import BeautifulSoup


url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA"
r = requests.get(url)

soup = BeautifulSoup(r.content)
#gets title
print(soup.title.string)