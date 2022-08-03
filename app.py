from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY DATABASE_URL'] = "mysql://root:'Sumedh@3009'@localhost/crud"
app.config['SQLALCHEMY TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    name = db.Column(db.String(100), primary_key = True)
    company_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    address = db.Column(db.String(100))
    extra_info = db.Column(db.String(100))

    def __init__(self,name,company_name,email,phone,address,extra_info):
        self.name = name
        self.company_name = company_name
        self.email = email
        self.phone = phone
        self.address = address
        self.extra_info = extra_info
    


@app.route('/')

def Index():
    return render_template("Index.html")


if __name__ == "__main__":
    app.run(debug=True)