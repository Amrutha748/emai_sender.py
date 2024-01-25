import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from']='Ammu M'
email['to']='123@gmail.com'
email['subject']='Birthday wishs'

email.set_content(" Advance Happy Birthday 🎂")

with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('am@gmail.com','asdcghhkggk')
    smtp.send_message(email)
    print("All the best for Future")
