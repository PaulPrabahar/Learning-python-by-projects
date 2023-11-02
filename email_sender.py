from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'prabahar1080@gmail.com'
email_password = 'sxtk bgcu emgz ealc'

email_receiver = 'vijirani1512@gmail.com'

subject = "Don't forget to study"
body = '''
When you don't study you will suffer later
'''

em = EmailMessage()
em['from'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
