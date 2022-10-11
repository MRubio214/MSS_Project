from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("HomePage.html")

@views.route('/about')
def about():
    return render_template("About.html")

@views.route('/requestingitems')
def requestingitems():
    return render_template("RequestingItems.html")

@views.route('/donate')
def donate():
    return render_template("Donate.html")


