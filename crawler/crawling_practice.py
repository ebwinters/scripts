import requests
from bs4 import BeautifulSoup


url = "http://hphs.dist113.org/Lists/EmployeeDirectory7/AllItems.aspx"
r = requests.get(url)

soup = BeautifulSoup(r.content)

data = soup.find_all("div", {"class": "ms-vb itx"})


teacher_list = []

for item in data:
	# listing = item.find_all('a')
	# print(item.get("href"))
	instance = item.a.string
	num = instance.find(',')
	new = instance[0:num]
	teacher_list.append(new)

teacher = input("What is the teacher's last name?: ")

if teacher in teacher_list:
	print("Y")
else:
	print("N")


