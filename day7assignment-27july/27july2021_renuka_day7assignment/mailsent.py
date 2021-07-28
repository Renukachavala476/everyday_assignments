import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = "Sample Content"

sender_address = 'chavala.sridhar476@gmail.com'
sender_pass = 'Sridhar123@'
receiver_address = 'chavala.renuka@gmail.com'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = '  attachment.'

message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'C:/Users/Lenovo/Downloads/atmega32.pdf'
attach_file = open(attach_file_name, 'rb')
# payload = MIMEBase('application', 'octate-stream')
payload = MIMEBase('application', 'pdf',Name=attach_file_name)
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) 

payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')