from database import get_emails
from verses import bible_verses
import random
from dotenv import load_dotenv
import os 
#from app import app
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

email_sender = os.getenv("EMAIL")
app_password = os.getenv("APP_PASSWORD")

def send_emails():
    bible_verse = random.choice(bible_verses)
    
    #with app.app_context():
    for user in get_emails():
        reciever = user.email
        print(reciever)

        message = MIMEMultipart()
        message["Subject"] = "Morning Manna"
        message["From"] = email_sender
        message["To"] = reciever
        host = 'smtp.gmail.com'
        port = 587

        text = f"""
            Welcome to Morning Manna! 
            {bible_verse}
            
        """

        part1 = MIMEText(text, "plain")
        message.attach(part1)

        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(email_sender, app_password)
            server.sendmail(email_sender, reciever, message.as_string())



#send_emails()
