from flask import Flask, request, render_template, jsonify
from verses import bible_verses
from database import db, email_exists, add_email, get_emails

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 