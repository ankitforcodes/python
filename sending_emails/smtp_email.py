import smtplib
from email.message import EmailMessage 

email_dict = {'dare2talk2ankit@gmail.com': 'Ankit'}

for items in email_dict:
	print(items, email_dict[items])
	print('Hi ' + email_dict[items] + ' Welcome to opinions.com! ' + '\n' + 'This is a system generated email.')

	email = EmailMessage()
	email['subject'] = 'Opinions Automated System Email Test'
	email['from'] = 'ankitforcodes@gmail.com'
	email['to'] = items
	email_content = 'Hi ' + email_dict[items] + 'Welcome to opinions.com! ' + '\n' + 'This is a system generated email.' 

	email.set_content(email_content)

	smtp_connector = smtplib.SMTP('smtp.gmail.com', 587)
	smtp_connector.starttls()
	smtp_connector.login('ankitforcodes@gmail.com', 'idlfumqaatnohlvi')

	smtp_connector.send_message(email)
	smtp_connector.quit() 
