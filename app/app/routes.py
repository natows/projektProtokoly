from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signin')
def signin_page():
    return render_template('signin.html')
@app.route('/account')
def account_page():
    return render_template('account.html')