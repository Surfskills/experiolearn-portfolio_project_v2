from flask import Blueprint, render_template
from flask_login import current_user
from flask import session

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('home_page.html')

@views.route('/home_page')
def home_page():
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        return render_template('home_age.html', logged_in=True, username=user.name)
    else:
        return render_template('home_page.html', logged_in=False)

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

@views.route('/my_dashboard')
def my_dashboard():
    return render_template('my_dashboard.html')

@views.route('/profile')
def profile():
    return render_template('profile.html')