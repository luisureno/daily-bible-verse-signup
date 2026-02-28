from flask import Flask, request, render_template, jsonify
from verses import bible_verses

app = Flask(__name__)

@app.route('/')
def bible_bot():
    return render_template('index.html')

@app.route('/subscribe', methods = ['POST'])
def subscribe():
    
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No JSON data recieved"}), 400
    
    message = "You're in! Expect a verse every morning."
    email = data.get('email')
    #print(email)

    response = {
        'message': message,
        'email': email
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True) 