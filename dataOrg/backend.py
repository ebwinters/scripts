import requests
from bs4 import BeautifulSoup

exersizes = {'neck':6,'traps':11,'shoulders':12,'chest':1,'biceps':15,'forearms':2,'abdominals':13,
'quadriceps':7,'calves':9,'triceps':10,'lats':3,'middle-back':4,'lower-back':5,'glutes':14,'hamstrings':8}

# def getExercizes(self):
for k,v in 
url = "http://money.cnn.com/data/hotstocks/index.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")





