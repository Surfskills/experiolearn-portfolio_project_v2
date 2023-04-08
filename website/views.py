from flask import Blueprint, render_template
from flask_login import current_user

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('home_page.html')

@views.route('/home_page')
def home_page():
    return render_template('home_page.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/services')
def services():
    return render_template('services.html')

@views.route('/hub')
def hub():
    return render_template('hub.html')

@views.route('/blog')
def contact():
    return render_template('blog.html')

@views.route('/userprofile')
def userprofile():
    return render_template('userprofile.html')