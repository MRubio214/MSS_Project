from flask import Blueprint, render_template, request

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

@views.route('/submitted_donation', methods=['GET', 'POST'])
def submitted_donation():
    if request.method == 'POST':
        return render_template('Submitted_Donation.html', shortcode=request.form.get('shortcode'))
    elif request.method == 'GET':
        return 'A GET request was made'
    else:
        return 'Not a valid request method for this route'