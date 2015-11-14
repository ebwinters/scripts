import requests
from bs4 import BeautifulSoup
import mail



url = "http://hphs.dist113.org/Lists/EmployeeDirectory7/AllItems.aspx"
r = requests.get(url)

soup = BeautifulSoup(r.content)

data = soup.find_all("div", {"class": "ms-vb itx"})


teacher_list = []
teacher_email = ""
for item in data:
	# listing = item.find_all('a')
	# print(item.get("href"))
	instance = item.a.string
	num = instance.find(',')
	new = instance[0:num]
	teacher_list.append(new)


teacher = input("What is the teacher's last name?: ")
user_email = input("What is your email?: ")
user_pass = input("What is your password?: ")
message = input("What is the message you wish to send?: ")



for link in soup.find_all('a'):
	if teacher in str(link.get('href')):
		teacher_email = link.get("href")
		col = teacher_email.find(":") + 1
		teacher_email = teacher_email[col:len(teacher_email)]
		print(link.get("href"))
		print(teacher_email)
	
	# mail_list.append(link.get('@dist113'))


if teacher in teacher_list:
	print("Y")
else:
	print("N")




mail.send_email(user_email, user_pass, teacher_email, message)
print("Done")
