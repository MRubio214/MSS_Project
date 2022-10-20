from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('views.requestingitems'))
    return render_template("Login.html", error=error)

@auth.route('/logout')
def logout():
    return render_template("HomePage.html")


@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    error = None
    if request.method == 'POST':
        if request.form['email'] == '' or request.form['psw'] == '' or request.form['psw-repeat'] == '':
            error = 'All values need to be filled. Please try again.'
        else:
            return redirect(url_for('views.requestingitems'))
    return render_template("Register.html", error=error)




