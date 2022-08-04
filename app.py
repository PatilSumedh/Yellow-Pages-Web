from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Sumedh123@localhost/yellow_pages'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    name = db.Column(db.String(100), primary_key = True)
    company_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
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

    all_data = Data.query.all()


    return render_template("Index.html",record = all_data)

@app.route('/insert',methods = ['POST'])

def insert():

    if request.method == 'POST':
        
        name = request.form['name']
        company_name = request.form['company_name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        extra_info = request.form['extra_info']

        my_data = Data(name,company_name,email,phone,address,extra_info)
        db.session.add(my_data)
        db.session.commit()

        flash("Details added successfully")


        return redirect(url_for('Index'))


@app.route('/update',methods = ['GET','POST'])

def update():

    if request.method == 'POST':
        
        my_data = Data.query.get(request.form.get('name'))

        my_data.company_name = request.form['company_name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        my_data.address = request.form['address']
        my_data.extra_info = request.form['extra_info']

        db.session.commit()

        flash("Details updated successfully")

        return redirect(url_for('Index'))


@app.route('/delete/<name>/', methods = ['GET','POST'])

def delete(name):
    my_data = Data.query.get(name)
    db.session.delete(my_data)
    db.session.commit()
    flash("Record deleted successfully")

    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
