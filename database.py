from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.String(100))


def email_exists(email_address):
    #It always returns as an object or None, meaning its an object if email
    #exists and None if it doesnt. So wrapping it in boolean, says if its 
    #an object its true, or if its None its false
    return bool(User.query.filter_by(email=email_address).first())

def add_email(email_address):
    usr = User(email=email_address)
    db.session.add(usr)
    #always use commit when making changes to db
    db.session.commit()
    
def get_emails():
    all_emails = db.session.query(User.email).all()
    return all_emails