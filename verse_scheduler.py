from database import get_emails
from verses import bible_verses
import random
from dotenv import load_dotenv
import os 
#from app import app
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

load_dotenv()

today = date.today()
email_sender = os.getenv("EMAIL")
app_password = os.getenv("APP_PASSWORD")

def send_emails():
    bible_verse = random.choice(bible_verses)
    
    #with app.app_context():
    for user in get_emails():
        reciever = user.email
        print(reciever)

        message = MIMEMultipart()
        message["Subject"] = "Morning Manna: Scripture of the Day"
        message["From"] = email_sender
        message["To"] = reciever
        host = 'smtp.gmail.com'
        port = 587

        text = f"""
Good morning!

Today's date is: {today:%m/%d/%y}

Here is your verse for today:

{bible_verse}

Have a blessed day.
— Morning Manna
"""

        part1 = MIMEText(text, "plain")
        message.attach(part1)

        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(email_sender, app_password)
            server.sendmail(email_sender, reciever, message.as_string())



#send_emails()
