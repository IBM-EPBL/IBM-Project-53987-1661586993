from flask import Flask, render_template, request, redirect, url_for 
from database import Database

app = Flask(__name__, static_url_path='')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/validateRegister', methods=['GET', 'POST'])
def validateRegister():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    db = Database()
    db.creeateUser(name, email, password)
    return render_template('login.html')


@app.route('/validateLogin', methods=['GET', 'POST'])
def validateLogin():
    email = request.form['email']
    password = request.form['password']
    db = Database()
    if password == db.loginUser(email)[0]:
        return redirect(url_for('customercare'))
    else:
        return "Invalid Credentials"


@app.route('/customercare')
def customercare():
    return render_template('customercare.html')

if __name__ == "__main__":
    app.run()