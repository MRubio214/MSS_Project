from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("Login.html")

@auth.route('/logout')
def logout():
    return render_template("HomePage.html")


@auth.route('/register')
def sign_up():
    return render_template("Register.html")


