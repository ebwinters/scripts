import requests
from bs4 import BeautifulSoup

# def getHotStocks(self):
url = "http://money.cnn.com/data/hotstocks/index.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# g_data = soup.find_all("tr")

# for item in g_data:
# 	link_data = item.find_all("span")
# 	print (link_data)
# 	print ("\n\n")

g_data = soup.find_all("table", {"class":"wsod_dataTable wsod_dataTableBigAlt"})
#gets only the most active hotstocks
print (g_data[0])