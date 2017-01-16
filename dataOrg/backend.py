# File to fill database
import collections
import requests
from bs4 import BeautifulSoup
import sqlite3

exersizes = collections.OrderedDict()
exersizes['neck'] = 6
exersizes['traps'] = 11
exersizes['shoulders'] = 12
exersizes['chest'] = 1
exersizes['biceps'] = 15
exersizes['forearms'] = 2
exersizes['abdominals'] = 13
exersizes['quadriceps'] = 7
exersizes['calves'] = 9
exersizes['triceps'] = 10
exersizes['lats'] = 3
exersizes['middle-back'] = 4
exersizes['lower-back'] = 5
exersizes['glutes'] = 14
exersizes['hamstrings'] = 8


conn = sqlite3.connect('data.db')

c = conn.cursor()

# # -----loop to fill rates list-----
# for key,val in exersizes.iteritems():
# 	url = "http://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/{0}/muscle/{1}".format(val,key)
# 	r = requests.get(url)
# 	soup = BeautifulSoup(r.content, "html.parser")

# 	ratings = soup.find_all("span", {"class":"rating"})
# 	for rating in ratings:
# 		if (rating.text == 'N/A'):
# 			rates.append(0.0)
		
# 		else:
# 			rates.append(rating.text)

for k,v in exersizes.iteritems():
	url = "http://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/{0}/muscle/{1}".format(v,k)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")


	data = soup.find_all("div", {"class":"exerciseName"})
	for item in data:
		exName = item.find_all("h3")[0].text
		exName.strip() 

		muscleName = item.find_all("a")[1].text
		muscleName.strip() 

		equipName = item.find_all("a")[2].text
		equipName.strip()

		
		c.execute("insert into exercises values(?,?,?)", (exName,muscleName,equipName))
			
		
conn.commit()

	








