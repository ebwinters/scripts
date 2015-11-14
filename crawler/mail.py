import smtplib


def send_email(sender_email, sender_password, receiver_email, message):

	mail = smtplib.SMTP('smtp.gmail.com', 587)

	mail.ehlo()

	mail.starttls()

	mail.login(sender_email, sender_password)

	option = input("Press 1 to send the email ")
	if option == 1:
		mail.sendmail(sender_email, receiver_email, message)

	mail.close()