import requests
from bs4 import BeautifulSoup
import sqlite3

exersizes = {'neck':6,'traps':11,'shoulders':12,'chest':1,'biceps':15,'forearms':2,'abdominals':13,
'quadriceps':7,'calves':9,'triceps':10,'lats':3,'middle-back':4,'lower-back':5,'glutes':14,'hamstrings':8}

conn = sqlite3.connect('data.db')

c = conn.cursor()
# def getExercizes(self):
for k,v in exersizes.iteritems():
	url = "http://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/{0}/muscle/{1}".format(v,k)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")

	data = soup.find_all("div", {"class":"exerciseName"})
	for item in data:
		exName = item.find_all("h3")[0].text
		exName.strip()
		c.execute("insert into names values(?)", (exName,))
conn.commit()
		#find other queries then insert
	








