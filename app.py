from flask import Flask, request, render_template, jsonify
from database import db, email_exists, add_email, get_emails
from verse_scheduler import send_emails
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

database_api = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = database_api
db.init_app(app)

@app.route('/')
def bible_bot():
    return render_template('index.html')

@app.route('/subscribe', methods = ['POST'])
def subscribe():
    
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No JSON data recieved"}), 400
    
    subscribed_message = "You're in! Expect a verse every morning."
    email_exists_message = "You're already subscribed."
    email = data.get('email')
    #print(email)
    exists = email_exists(email)
    if not exists:
        add_email(email)
        response = {
        'message': subscribed_message,
        'email': email
        }
        return jsonify(response)
    else:
        response = {
        'message': email_exists_message,
        'email': email
        }
        return jsonify(response)


def run_scheduler():
    with app.app_context():
        send_emails()


if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    #all_emails = send_emails()
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_scheduler, 'cron', hour=15, minute=0)
    scheduler.start()
    print('Scheduler started. Press Ctrl + C to exit.')

    app.run(debug=True, use_reloader=False) 